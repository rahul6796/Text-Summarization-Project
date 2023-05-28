

from textSummarizer.config.configuration import  ConfigurationManager
from textSummarizer.components.model_trainer import ModelTrainer


class ModelTrainingPipeline:

    def __init__(self):
        pass

    @staticmethod
    def main():
        config = ConfigurationManager()
        model_training_config = config.get_model_training_config()
        model_training = ModelTrainer(config=model_training_config)
        model_training.train()
