import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    read yaml file and returns
    :arg
        path_to_yaml (str): path like input
    :exception
        ValueError: if yaml file is empty
        e: empty file
    :return
        ConfigBox: ConfigBox type
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as ex:
        logger.error(f'utils.py failed to read_yaml files due  :: {ex}')


@ensure_annotations
def create_directory(path_to_directories: list, verbose=True):
    """
    :arg

        path_to_directories: list of path of directories

        ignore_log (bool, options): ignore if multiple dirs is to  create. Defaults to False.

    :return:

        None
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def get_size(path: Path) -> str:
    """
    :arg
        path (Path): path of file
    :return:
        str: size in kb
    """

    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} kb"
