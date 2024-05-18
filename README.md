# Intelligent Radiologist Assistant - A web application for classifying tears in knee MRI images


## Overview

MRNet is a web application designed to analyze MRI scans for the detection of tears using deep learning models. Developed as an internship project at iNeuron Intelligence Pvt. Ltd., MRNet utilizes PyTorch, specifically leveraging the capabilities of AlexNet and ResNet18 architectures, to process MRI images from axial, sagittal, and coronal planes. The application generates detailed reports with visualizations and probability metrics, aiding in the diagnosis and understanding of tears.

## Key Features

- **User Authentication**: 
  - **Login**: Existing users can securely access their dashboard.
  - **Registration**: New users can sign up to create an account.

- **File Upload**: 
  - Users can upload MRI images from axial, coronal, and sagittal planes.
  - A blank CSV file must also be uploaded for analysis.

- **Report Generation**: 
  - Detailed reports are generated after processing the uploaded images and CSV data.
  - Visualizations such as bar plots, line plots, stacked bar plots, and pie charts are included.
  - Probability metrics for different types of tears are calculated and displayed.

- **Analysis**:
  - In-depth analysis of tear types, providing insights into their severity and probability.
 
## Workflow of this web application
![workflow_diagram](https://github.com/ArupSankarRoy/INTELLIGENT-RADIOLOGIST-ASSISTANT/assets/115450599/a2067030-2178-4fc8-9030-daecb4feb40b)


## Installation

To install and run the MRNet web application locally, follow these steps:

1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/mrnet-webapp.git
   cd mrnet-webapp
   ```

2. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```sh
   python app.py
   ```

## Model Description

MRNet utilizes two main models:

- **MRNet**: A model for analyzing single MRI planes based on AlexNet architecture.
- **TripleMRNet**: An extended model that handles MRI scans from three different planes, using either AlexNet or ResNet18 as the backbone.

## Usage

1. **Upload MRI Images**: Navigate to the upload section and upload the required files.
2. **Generate Report**: After uploading, click on the "Generate Report" button to process the images and view the results.
3. **View Analysis**: The report page will display detailed analysis through various visualizations and probability metrics.

## Contributing

Contributions to the MRNet project are welcome. Please create a pull request or open an issue if you have suggestions or find any bugs.

---

For more information, refer to the [project documentation](https://github.com/yourusername/mrnet-webapp/wiki). Developed as an internship project at iNeuron Intelligence Pvt. Ltd.
