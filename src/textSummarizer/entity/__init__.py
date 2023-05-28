from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path


@dataclass
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: list


@dataclass
class DataTransformConfig:
    root_dir: Path
    data_path: Path
    tokenizer_name: Path


