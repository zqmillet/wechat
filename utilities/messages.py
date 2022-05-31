from pydantic import BaseModel
from datetime import datetime

class Message(BaseModel):
    id: int
    create_time: datetime
    receive_time: datetime
    text: str
    type: str
    sender: str
    receiver: str
