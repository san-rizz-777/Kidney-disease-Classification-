from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.component.training import Training
from cnnClassifier import logger


STAGE_NAME = "Training Model"

class TrainingModelPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        training_model_config = config.get_training_config()
        training = Training(training_model_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()


if __name__ == "__main__":
    try:
        logger.info(f"######### Stage {STAGE_NAME} started!!!!##########")
        training = TrainingModelPipeline()
        training.main()
        logger.info(f"######### Stage {STAGE_NAME} completed!!!!##########")
    except Exception as e:
        logger.exception(e)
        raise e

