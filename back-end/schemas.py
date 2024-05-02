from pydantic import BaseModel
from typing import List

class queryAI(BaseModel):
    query: str
    messages: List[str]
    system: str