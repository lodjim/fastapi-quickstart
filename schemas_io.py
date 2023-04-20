from pydantic import BaseModel




class HearbitResponse(BaseModel):
    status:str = "state"
