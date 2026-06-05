import os
from cnnClassifier.__init__ import logger
import zipfile
import gdown
from cnnClassifier.config.configuration import DataIngestionConfig


# Create a class for data ingestion from downloadintg the zip file from gdrive to unzipping it int right directory
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self) -> str:
        # get the source url
        # path of file to store zip in
        # create the artifacts dir
        try:
            src_url = self.config.source_url
            zip_data_file_path = self.config.local_data_file

            os.makedirs("../artifacts/data_ingestion", exist_ok=True)
            logger.info(f"Downloading zip file from {src_url} into local file:- {zip_data_file_path}")  # Log the info

            file_id = src_url.split('/')[-2]
            src_file_path = f"https://drive.google.com/uc?/export=download&id={file_id}"
            gdown.download(src_file_path, zip_data_file_path)
            logger.info(f"Downloaded the data set from {src_file_path} into the file:- {zip_data_file_path}")
        except Exception as e:
            raise e

        return zip_data_file_path

    def extract_zip_file(self):
        """
        Takes the zip file path: str , and unzip it into the data directory
        """
        unzip_data_dir = self.config.unzip_dir
        os.makedirs(unzip_data_dir, exist_ok=True)

        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_data_dir)

        # Rename the extracted folder to the desired name
        extracted_folder = os.path.join(self.config.unzip_dir, "CT-KIDNEY-DATASET-Normal-Cyst-Tumor-Stone/CT-KIDNEY-DATASET-Normal-Cyst-Tumor-Stone")
        desired_folder = os.path.join(self.config.unzip_dir, "kidney_ct_scan_dataset/kidney_ct_scan_dataset")

        if os.path.exists(extracted_folder):
            os.rename(extracted_folder, desired_folder)
