from pydantic import BaseModel
from pydantic import Field

class MediaPlatform(BaseModel):
    identity: str = Field(alias='UserName')
    nick_name: str = Field(alias='NickName')
    signature: str = Field(alias='Signature')
    province: str = Field(alias='Province')
    city: str = Field(alias='City')

    def __repr__(self):
        return f'<MediaPlatform {self.nick_name}>'

    def __str__(self):
        return f'<MediaPlatform {self.nick_name}>'
