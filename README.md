![ineuron](https://user-images.githubusercontent.com/57321948/196933065-4b16c235-f3b9-4391-9cfe-4affcec87c35.png)
# INTELLIGENT RADIOLOGIST ASSISTANT- A web application for classifying tears in knee MRI images


## Overview

This a web application designed to analyze knee MRI scans for the detection of tears using deep learning models. Developed as an internship project at iNeuron Intelligence Pvt. Ltd., MRNet utilizes PyTorch, specifically leveraging the capabilities of AlexNet and ResNet18 architectures, to process MRI images from axial, sagittal, and coronal planes. The application generates detailed reports with visualizations and probability metrics, aiding in the diagnosis and understanding of tears.

## Key Features

- **User Authentication**: 
  - **Login**: Existing users can securely access their dashboard.
  - **Registration**: New users can sign up to create an account.

- **File Upload**: 
  - Users can upload MRI images from axial, coronal, and sagittal planes.
  - A blank CSV file must also be uploaded for analysis.

- **Report Generation**: 
  - Detailed reports are generated after processing the uploaded images and blank CSV file.
  - Visualizations such as bar plots, line plots, stacked bar plots, and pie charts are included.
  - Probability metrics for different types of tears are calculated and displayed.

- **Analysis**:
  - In-depth analysis of tear types, providing insights into their severity and probability.
 
## Workflow of this web application
![workflow_diagram](https://github.com/ArupSankarRoy/INTELLIGENT-RADIOLOGIST-ASSISTANT/assets/115450599/a2067030-2178-4fc8-9030-daecb4feb40b)


## Installation

To install and run the this web app locally, follow these steps:
1. **Create a database**:
    ```sh
    -- I'm using MySQL database here
    USE `patient-details-system`; -- It's my database name

    -- I'm creating a table named "user," but you can use your own table name.
    CREATE TABLE `user` (
      -- Don't change anything here
      `userid` int(11) AUTO_INCREMENT PRIMARY KEY,
      `name` varchar(100) NOT NULL,
      `phone` varchar(20) NOT NULL,
      `address` varchar(400) NOT NULL,
      `password` varchar(255) NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

    -- Inserting a row into the table for testing purposes.(optional)
    INSERT INTO `user` (`name`, `phone`, `address`, `password`) VALUES
    ('John', '9874563214', 'Jalpaiguri', '123');
    ```

2. **Clone the repository**:
   ```sh
   git clone https://github.com/ArupSankarRoy/INTELLIGENT-RADIOLOGIST-ASSISTANT.git
   cd INTELLIGENT-RADIOLOGIST-ASSISTANT
   ```

3. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```
4. **Update `app.py` if you make any changes to the database; otherwise, skip this step.**:
   ```sh
   app.config['MYSQL_DB'] = 'patient-details-system' # Replace with your MySQL database name
   app.config['MYSQL_PORT'] = 3308  # Replace with your MySQL port
   table_name = 'user' # Change this according to your database table name
   ```
5. **Run the application**:
   ```sh
   python app.py
   ```
### Note: These steps will only run if your Python version is <=3.11.0. To check your Python version, use `$ python --version`.

## Here's how the app looks.
![MRNET_GIF](https://github.com/ArupSankarRoy/INTELLIGENT-RADIOLOGIST-ASSISTANT/assets/115450599/372e4f44-fb65-4231-98b5-f788b13e2144)


## Model Description
MRNet utilizes two main models:

- **MRNet**: A model for analyzing single MRI planes based on AlexNet architecture.
- **TripleMRNet**: An extended model that handles MRI scans from three different planes, using either AlexNet or ResNet18 as the backbone.
- For more details, check this [paper](https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1002699) 


## Usage

1. **Upload MRI Images**: Navigate to the upload section and upload the required files.
2. **Generate Report**: After uploading, click on the "Generate Report" button to process the images and view the results.
3. **View Analysis**: The report page will display detailed analysis through various visualizations and probability metrics.

## Contributing

Contributions to the MRNet project are welcome. Please create a pull request or open an issue if you have suggestions or find any bugs.

