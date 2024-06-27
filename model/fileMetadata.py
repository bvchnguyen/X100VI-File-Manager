from dataclasses import dataclass
from typing import Optional
from PIL import Image
from datetime import datetime

@dataclass
class ImageMetadata:
    file_name: str
    file_path: str
    date_time: Optional[datetime] = None
    camera_model: Optional[str] = None