from cnnClassifier import logger
from cnnClassifier.config.configuration import PrepareBaseModelConfig, ConfigurationManager
from cnnClassifier.component.prepare_base_model import PrepareBaseModel

STAGE_NAME = "Prepare Base Model"

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        base_model_config = config.get_prepared_model_config()
        base_model = PrepareBaseModel(base_model_config)
        base_model.get_base_model()
        base_model.update_base_model()



if __name__ == "__main__":
    try:
        logger.info(f"#### Stage {STAGE_NAME} started.......####")
        config = ConfigurationManager()
        base_model_config = config.get_prepared_model_config()
        base_model = PrepareBaseModel(base_model_config)
        base_model.get_base_model()
        base_model.update_base_model()
        logger.info(f"#### Stage {STAGE_NAME} completed successfully......####")
    except Exception as e:
        logger.exception(e)
        raise e

###