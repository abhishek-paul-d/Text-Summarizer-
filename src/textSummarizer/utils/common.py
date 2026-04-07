import os 
from box.exceptions import BoxValueError
import yaml
from src.textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path)-> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded sucessfully")
            return ConfigBox(content)
    except BoxValueError as e:
        raise BoxValueError(f"Error while parsing yaml file")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_dictories: list ,verbose = True):
    for path in path_to_dictories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created Directory at : {path}")





