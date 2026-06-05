from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.component.data_ingestion import DataIngestion
from cnnClassifier import logger


STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass


    #run the entire pipline
    def main(self):
        config = ConfigurationManager()        # Reads yaml files and create the ConfigBox object
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)             # Creates the data ingestion object to download and unzip file.
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


# For debugging purposes
if __name__ == '__main__':
    try:
        logger.info(f"Stage started!!!! >> {STAGE_NAME}!!!!")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f"Stage completed!!!! >> {STAGE_NAME}!!!!")
    except Exception as e:
        logger.exception(e)
        raise e


    ###