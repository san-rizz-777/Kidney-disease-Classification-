from dataclasses import dataclass
from pathlib import Path

# Contains all the data ingestion directories and storing zip and unzip file paths.
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path