from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml, create_directories
from cnnClassifier.entity.config_entity import DataIngestionConfig

class ConfigManager:
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
            unzip_dir=config_obj.unzip_file
        )

        return data_ingestion_config
