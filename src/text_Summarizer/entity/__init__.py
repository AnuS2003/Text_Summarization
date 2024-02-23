from dataclasses import dataclass
from pathlib import Path

# Modify the DataIngestionConfig class definition
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    root_dir: str
    source_URL: str
    local_data_file: str
    unzip_dir: str
