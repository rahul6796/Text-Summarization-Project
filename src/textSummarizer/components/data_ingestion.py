import os
import urllib.request as request
import zipfile
from textSummarizer.logging import logger
from textSummarizer.utils.common import get_size
from textSummarizer.config.configuration import DataIngestionConfig
from pathlib import Path


class DataIngestion:

    def __init__(self,
                 config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, header = request.urlretrieve(
                url=self.config.source_url,
                filename=self.config.local_data_file
            )

            logger.info(f"{filename} downloaded! with follwing info: \n{header}")
        else:
            logger.info(f'file already exists of size : {get_size(Path(self.config.local_data_file))}')

    def extract_zip_file(self):
        """
        :arg
            zip_file_path: str
            Extracts the zip file to the data directory
        :return:
            None
        """
        unzip_file_path = self.config.unzip_dir
        os.makedirs(unzip_file_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_file:
            zip_file.extractall(unzip_file_path)

