from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion_pipeline import DataIngestionTrainingPipeline

STAGE_NAME = "DataIngestion Stage"

if __name__ == '__main__':
    try:
        logger.info(f"Stage started!!!! >> {STAGE_NAME}!!!!")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f"Stage completed!!!! >> {STAGE_NAME}!!!!")
    except Exception as e:
        logger.exception(e)
        raise e