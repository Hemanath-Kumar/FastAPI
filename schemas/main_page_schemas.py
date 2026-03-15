from pydantic import BaseModel


#request Body schema for main page
class MainPageRequestBodySchema(BaseModel):
    
    Name: str


#Response Body schema for main page
class MainPageResponseBodySchema(BaseModel):
    Name: str
