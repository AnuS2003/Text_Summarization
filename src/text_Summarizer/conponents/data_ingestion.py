import os
import urllib.request as request
import zipfile
from text_Summarizer.logging import logger
from text_Summarizer.utils.common import get_size
from pathlib import Path
from text_Summarizer.entity import DataIngestionConfig

class DataIngestionConfig:
    def __init__(self, root_dir, source_URL, local_data_file, unzip_dir):
        # Initialize DataIngestionConfig with provided arguments
        self.root_dir = root_dir
        self.source_URL = source_URL
        self.local_data_file = local_data_file
        self.unzip_dir = unzip_dir


class DataIngestion:
    def __init__(self, config):
        # Initialize DataIngestion with configuration
        self.config = config

    def download_file(self):
        # Implement download logic using self.config.source_URL and self.config.local_data_file
        pass

    def extract_zip_file(self):
        # Implement extraction logic using self.config.local_data_file and self.config.unzip_dir
        pass