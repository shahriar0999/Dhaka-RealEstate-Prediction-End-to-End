from pydantic import BaseModel

class HouseInfo(BaseModel):
    city_location: str
    block_sector: str
    bedroom: int
    bathroom: int
    sqrtFeet: int
