from pydantic import BaseModel
from pydantic import Field

class Chatroom(BaseModel):
    identity: str = Field(alias='UserName')
    nick_name: str = Field(alias='NickName')

    def __repr__(self):
        return f'<Chatroom {self.nick_name}>'

    def __str__(self):
        return f'<Chatroom {self.nick_name}>'
