from textSummarizer.config.configuration import *
from textSummarizer.components.data_validation import DataValidation


class DataValidationTrainingPipeline:

    def __init__(self):
        pass

    @staticmethod
    def main():
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(data_validation_config)
        data_validation.validate_all_file_exists()


