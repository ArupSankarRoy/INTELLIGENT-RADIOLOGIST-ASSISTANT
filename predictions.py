import os
import numpy as np
import torch
from torch.autograd import Variable
from model import TripleMRNet 
import shutil

INPUT_DIM = 224
MAX_PIXEL_VAL = 255
MEAN = 58.09
STDDEV = 49.73

device = 'cuda:0' if torch.cuda.is_available() else 'cpu'

def get_study(axial_path=None, coron_path=None, sagit_path=None):
    vol_axial = np.load(axial_path)
    vol_sagit = np.load(sagit_path)
    vol_coron = np.load(coron_path)

    def process_volume(volume):
        pad = int((volume.shape[2] - INPUT_DIM) / 2)
        volume = volume[:, pad:-pad, pad:-pad]
        volume = (volume - np.min(volume)) / (np.max(volume) - np.min(volume)) * MAX_PIXEL_VAL
        volume = (volume - MEAN) / STDDEV
        volume = np.stack((volume,) * 3, axis=1)
        return volume

    vol_axial = process_volume(vol_axial)
    vol_sagit = process_volume(vol_sagit)
    vol_coron = process_volume(vol_coron)

    return {
        "axial": torch.FloatTensor(vol_axial),
        "sagit": torch.FloatTensor(vol_sagit),
        "coron": torch.FloatTensor(vol_coron)
    }


def get_prediction(model, tensors, abnormality_prior=None):
    with torch.no_grad():
        vol_axial = tensors["axial"].to(device)
        vol_sagit = tensors["sagit"].to(device)
        vol_coron = tensors["coron"].to(device)

        logit = model.forward(vol_axial, vol_sagit, vol_coron)
        pred = torch.sigmoid(logit)
        pred_npy = pred.cpu().numpy()[0][0]

        if abnormality_prior:
            pred_npy = pred_npy * abnormality_prior

        return pred_npy


def save_predictions_csv():
    root = os.getcwd()
    pred_folder = os.path.join(root, 'Pred')
    if os.path.exists(pred_folder):
        shutil.rmtree(pred_folder)
    os.makedirs(pred_folder, exist_ok=True)
    axial_path = os.path.join(root, 'uploads', 'axial_numpy.npy')
    coron_path = os.path.join(root, 'uploads', 'coronal_numpy.npy')
    sagit_path = os.path.join(root, 'uploads', 'sagittal_numpy.npy')

    abnormal_model_path = os.path.join(root, 'MODELS', 'Abnormal_model', 'val0.1019_train0.0882_epoch9.pth')
    acl_model_path = os.path.join(root, 'MODELS', 'Acl_model', 'val0.1677_train0.0959_epoch9.pth')
    meniscal_model_path = os.path.join(root, 'MODELS', 'Meniscal_model', 'val0.2556_train0.1862_epoch6.pth')

    # Get study from input paths
    study = get_study(axial_path, coron_path, sagit_path)

    # Load models
    def load_model(model_path):
        model = TripleMRNet(backbone="alexnet", training=False)
        state_dict = torch.load(model_path, map_location=torch.device('cpu'))
        model.load_state_dict(state_dict)
        model.to(device)
        model.eval()
        return model

    abnormal_model = load_model(abnormal_model_path)
    acl_model = load_model(acl_model_path)
    meniscal_model = load_model(meniscal_model_path)

    # Get predictions
    abnormality = get_prediction(abnormal_model, study)
    acl_tear = get_prediction(acl_model, study)
    meniscal_tear = get_prediction(meniscal_model, study)

    # Output predictions with headers
    with open(os.path.join(pred_folder, 'predictions.csv'), 'w') as f:
        f.write("Abnormalities,ACL_Tear,Meniscal_Tear\n")
        f.write(f"{abnormality},{acl_tear},{meniscal_tear}\n")


