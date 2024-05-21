![ineuron](https://user-images.githubusercontent.com/57321948/196933065-4b16c235-f3b9-4391-9cfe-4affcec87c35.png)
# INTELLIGENT RADIOLOGIST ASSISTANT- An optimized web application designed specifically for classifying tears in knee MRI images.


## Overview

It is a web application designed to analyze knee MRI scans for tear classification using deep learning models. Developed as an internship project at iNeuron Intelligence Pvt. Ltd., This application uses TripleMRNet to utilize the capabilities of AlexNet and ResNet18 architectures, to process MRI images from axial, sagittal, and coronal planes.It generates detailed reports with visualizations and probability metrics, aiding in the diagnosis and understanding of tears.

## Key Features

- **User Authentication**: 
  - **Login**: Existing users can securely access their dashboard.
  - **Registration**: New users can sign up to create an account.

- **File Upload**: 
  - Users can upload MRI planes like axial, coronal, and sagittal (Note:Files must have a .npy extension).
  - A blank CSV file must be uploaded to write the probabilities of classifying a specific knee tear.

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
   cd "INTELLIGENT-RADIOLOGIST-ASSISTANT"
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
**After completing the previous steps, enter "http://127.0.0.1:5000/" in Chrome's address bar or click this site address in cmd to redirect to the site.**
### Note: These steps will only run if your Python version is <=3.11.0. To check your Python version, use `$ python --version`.

## Here's how the app looks.
![MRNET_GIF](https://github.com/ArupSankarRoy/INTELLIGENT-RADIOLOGIST-ASSISTANT/assets/115450599/372e4f44-fb65-4231-98b5-f788b13e2144)


## Model Description
This project utilizes mainly two models:

- **MRNet**: A model for analyzing single MRI planes based on AlexNet architecture.
- **TripleMRNet**: An extended model that handles MRI scans from three different planes, using either AlexNet or ResNet18 as the backbone.
- For more details, check this [paper](https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1002699) 


## Usage

1. **Upload MRI Planes and a blank csv file**: Navigate to the upload section and upload the required files.
2. **Generate Report**: After uploading, click on the "predict" button to process the planes and csv file and view the results.
3. **View Analysis**: The report page will display detailed analysis through various visualizations and probability metrics.

**Check out this [demo video.](https://drive.google.com/file/d/1QHb9iWCWlgbeszTZhjt41UYnS5MiUH-F/view?usp=sharing)**
## Contributing

I appreciate contributions! Feel free to create a pull request or open an issue if you have suggestions or encounter any bugs.

