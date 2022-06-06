from __future__ import annotations
from typing import Dict
from pydantic import BaseModel
from pydantic import Field

class Friend(BaseModel):
    identity: str = Field(alias='UserName')
    city: str = Field(alias='City')
    province: str = Field(alias='Province')
    signature: str = Field(alias='Signature')
    nick_name: str = Field(alias='NickName')
    remark_name: str = Field(alias='RemarkName')

    def __repr__(self):
        return f'<Friend {self.remark_name or self.nick_name}>'

    def __str__(self):
        return f'<Friend {self.remark_name or self.nick_name}>'
