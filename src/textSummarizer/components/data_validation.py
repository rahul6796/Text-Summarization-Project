import os
import urllib.request as request
import zipfile
from textSummarizer.logging import logger
from textSummarizer.utils.common import get_size
from textSummarizer.config.configuration import DataValidationConfig
from pathlib import Path
validation_status = None


class DataValidation:

    def __init__(self,
                 config: DataValidationConfig):
        self.config = config

    def validate_all_file_exists(self) -> bool:
        try:
            global validation_status
            all_files = os.listdir(os.path.join("artifacts", "data_ingestion", "samsum_dataset"))
            for file in all_files:
                if file not in self.config.ALL_REQUIRED_FILES:
                    validation_status = False
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"validation_status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"validation_status :: {validation_status}")
            logger.info("successfully validate all files exists")
        except Exception as ex:
            logger.error(f"failed to validation all file exists ::{ex}")





