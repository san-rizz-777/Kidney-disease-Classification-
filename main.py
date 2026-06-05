from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion_pipeline import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_training_model import TrainingModelPipeline
from cnnClassifier.pipeline.stage_04_model_evaluation import EvaluationModelPipeline

STAGE_NAME = "DataIngestion Stage"
try:
    logger.info(f"Stage started!!!! >> {STAGE_NAME}!!!!")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"Stage completed!!!! >> {STAGE_NAME}!!!!")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare Base Model Stage"
try:
    logger.info(f"Stage started!!!! >> {STAGE_NAME}!!!!")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f"Stage completed!!!! >> {STAGE_NAME}!!!!")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Training Model"
try:
    logger.info(f"######### Stage {STAGE_NAME} started!!!!##########")
    training = TrainingModelPipeline()
    training.main()
    logger.info(f"######### Stage {STAGE_NAME} completed!!!!##########")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Evaluation stage"
try:
    logger.info(f"######### Stage {STAGE_NAME} started!!!!##########")
    training = EvaluationModelPipeline()
    training.main()
    logger.info(f"######### Stage {STAGE_NAME} completed!!!!##########")
except Exception as e:
    logger.exception(e)
    raise e