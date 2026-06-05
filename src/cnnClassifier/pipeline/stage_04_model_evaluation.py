from cnnClassifier.component.evaluation import Evaluation
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier import logger
import dagshub



STAGE_NAME = "Evaluation stage"

class EvaluationModelPipeline:
    def __init__(self):
        pass

    def main(self):
        dagshub.init(repo_owner='gundesanskar71', repo_name='Kidney-disease-Classification-', mlflow=True)
        config = ConfigurationManager()
        eval_config = config.get_eval_config()
        eval_ = Evaluation(eval_config)
        eval_.evaluate()
        eval_.log_into_mlflow()



if __name__ == "__main__":
    try:
        logger.info(f"######### Stage {STAGE_NAME} started!!!!##########")
        training = EvaluationModelPipeline()
        training.main()
        logger.info(f"######### Stage {STAGE_NAME} completed!!!!##########")
    except Exception as e:
        logger.exception(e)
        raise e