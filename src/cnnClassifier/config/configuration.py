from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml, create_directories
from cnnClassifier.entity.config_entity import DataIngestionConfig
from cnnClassifier.entity.config_entity import PrepareBaseModelConfig
from cnnClassifier.entity.config_entity import TrainingConfig
from cnnClassifier.entity.config_entity import EvalConfig
import os

class ConfigurationManager:
    def __init__(self, config_file_path=str(CONFIG_FILE_PATH), params_file_path=str(PARAMS_FILE_PATH)):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """
            To get the DataIngestionConfig object containing the essential directories and files
        """
        config_obj = self.config.data_ingestion
        create_directories([config_obj.root_dir])  # created the root directory

        data_ingestion_config = DataIngestionConfig(  # Passing the essential params
            root_dir=config_obj.root_dir,
            source_url=config_obj.source_url,
            local_data_file=config_obj.local_data_file,
            unzip_dir=config_obj.unzip_dir
        )

        return data_ingestion_config

    def get_prepared_model_config(self) -> PrepareBaseModelConfig:
        config_base_model = self.config.prepare_base_model

        # Create the root dir now
        create_directories([config_base_model.root_dir])

        # Create the prepare_basemodel_config object
        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=Path(config_base_model.root_dir),
            base_model_path=Path(config_base_model.base_model_path),
            updated_base_model_path=Path(config_base_model.updated_base_model_path),
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weights=self.params.WEIGHTS,
            params_classes=self.params.CLASSES
        )

        return prepare_base_model_config

     # From the config and params set the data members of TrainigConfig
    def get_training_config(self) -> TrainingConfig:
        training = self.config.training
        prepare_base_model = self.config.prepare_base_model
        params = self.params
        training_data = os.path.join(self.config.data_ingestion.unzip_dir,
                                     "kidney_ct_scan_dataset/kidney_ct_scan_dataset")
        create_directories([Path(training.root_dir)])

        training_config = TrainingConfig(root_dir=Path(training.root_dir),
                                         trained_model_path=Path(training.trained_model_path),
                                         updated_base_model_path=Path(prepare_base_model.updated_base_model_path),
                                         training_data=Path(training_data),
                                         params_epochs=params.EPOCHS,
                                         params_batch_size=params.BATCH_SIZE,
                                         params_is_augumentation=params.AUGUMENTATION,
                                         params_image_size=params.IMAGE_SIZE,
                                         params_learning_rate=params.LEARNING_RATE)

        return training_config


    def get_eval_config(self) -> EvalConfig:
        eval_config = EvalConfig(
            path_of_model="artifacts/training/model.h5",
            training_data="artifacts/data_ingestion/kidney_ct_scan_dataset/kidney_ct_scan_dataset",
            mlflow_uri="https://dagshub.com/gundesanskar71/Kidney-disease-Classification-.mlflow",
            all_params=self.params,
            params_image_size=self.params.IMAGE_SIZE,
            params_batch_size=self.params.BATCH_SIZE
        )

        return eval_config