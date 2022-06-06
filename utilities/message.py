from pydantic import BaseModel
from pydantic import Field
from pydantic import validator
from datetime import datetime

from utilities.friend import Friend

class Message(BaseModel):
    identity: str = Field(alias='MsgId')
    sender: Friend = Field(alias='FromUserName')
    receiver: Friend = Field(alias='ToUserName')
    create_time: datetime = Field(alias='CreateTime')

    @validator('identity')
    def _identity(self, value):
        pass
