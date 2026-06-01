import os
import ensure
from box import ConfigBox
from box.exceptions import BoxValueError
import yaml
from ensure import ensure_annotations
from pathlib import Path
from cnnClassifier import logger
import json



@ensure_annotations
def read_yaml(yaml_filepath: str) -> ConfigBox:
    """
    Reads a yaml file and returns a ConfigBox

    Args:
        yaml_filepath: path to yaml file
    RETURNS:
        ConfigBox: ConfigBox
    """
    try:
        with open(yaml_filepath) as f:
            config = yaml.safe_load(f)
            logger.info(f"Loaded config from {yaml_filepath} successfully!!!!")
            return ConfigBox(config)
    except BoxValueError:
        raise ValueError("yaml file is empty!!!!")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Creates directories given a list of paths

    Args:
        path_to_directories: list of paths,
        verbose : bool(amount of logging
    """
    for path in path_to_directories:
        os.makdirs(path,exist_ok=True)
        if verbose:
            logger.info(f"Created directory at :{path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Saves data to a json files

     Args:
         path: path to json file,
         data: data to save
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data

      Args:
          path (Path): path to json file

      Returns:
          ConfigBox: data as class attributes instead of dict
      """
    with open(path, "r") as f:
        data = json.load(f)
    logger.info(f"loaded json file from {path}")
    return ConfigBox(data)

