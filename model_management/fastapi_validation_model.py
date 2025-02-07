from pydantic import BaseModel

class HouseInfo(BaseModel):
    city_location: int
    block_sector: int
    bedroom: int
    bathroom: int
    sqrtFeet: int
