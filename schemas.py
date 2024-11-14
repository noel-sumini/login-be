from pydantic import BaseModel, Field

class UserInfoModel(BaseModel): 
    userid:str = Field()
    password:str = Field()
