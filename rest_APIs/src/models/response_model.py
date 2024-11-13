from pydantic import BaseModel
from typing import Dict, Any

class Response(BaseModel):
    status_code: int
    message: Dict[str, Any]