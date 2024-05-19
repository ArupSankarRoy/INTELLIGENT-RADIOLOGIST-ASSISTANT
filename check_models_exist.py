import os

def model_exist_count(folder_path=None):
    count = 0
    if os.path.exists(folder_path) and len(os.listdir(os.path.join(os.getcwd(),"MODELS"))) > 0:
        for dir_name in os.listdir(folder_path):
            subdirectory = os.path.join(os.path.join(folder_path , dir_name))
            if os.path.isdir(subdirectory):
                count += 1 if len(os.listdir(subdirectory)) == 1 else 0

    return count




