from pydantic import BaseModel 

class StudentIn(BaseModel):
    name: str
    age: int    

    # class Config:
    #     orm_mode = True
  
class StudentOut(BaseModel): 
    id: int
    name: str
    age: int    

    class Config:
        orm_mode = True

