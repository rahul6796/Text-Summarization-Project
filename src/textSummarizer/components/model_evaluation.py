from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_dataset, load_from_disk, load_metric
import torch
import pandas as pd
from tqdm import tqdm
from textSummarizer.entity import ModelEvaluationConfig


class ModelEvalution:

    def __init__(self,
                 config: ModelEvaluationConfig):
        self.config = config

    def get_batch_sized_chunks(self,
                               list_of_elements,
                               batch_size):

        """
        split the dataset into smaller batches that we can process simultaneously
        yield successive batch-size chunk from list_to_elements:
        """
        for i in range(0, len(list_of_elements), batch_size):
            yield list_of_elements[i: i+batch_size]

    def calculate_metric_on_test_ds(self,
                                    dataset,
                                    metric,
                                    model,
                                    tokenizer,
                                    batch_size = 16, device="cuda" if torch.cuda.is_available() else "cpu",
                                    column_text= "article",
                                    column_summary="highlights"):

        article_batches = list(
            self.get_batch_sized_chunks(dataset[column_text], batch_size)
        )
        target_batch = list(
            self.get_batch_sized_chunks(dataset[column_text], batch_size)
        )




