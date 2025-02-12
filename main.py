from fastapi import FastAPI, HTTPException
from pydantic import ValidationError
import uvicorn
import pandas as pd
import numpy as np
from model_management.fastapi_validation_model import HouseInfo
from model_management.aws_s3 import load_model_from_s3


app = FastAPI()

house_model = load_model_from_s3('s3_model_from_trainStage/housePrice.pkl')
rent_model = load_model_from_s3('s3_model_from_trainStage/houseRent.pkl')


@app.get("/")
def root():
    return {"message": "Hello, Thanks for using my API"}


@app.post("/predict-house-price")
def predict_house_price(house_info: HouseInfo):

    try:
        data = pd.DataFrame([house_info.dict()])
        pred = house_model.predict(data)
        estimate_house_price = round(float(np.expm1(pred[0])))
        return {"Estimated House Price": str(estimate_house_price)+"৳"}
    
    except ValidationError as e:
        # Handle validation errors explicitly
        raise HTTPException(
            status_code=422,  # Unprocessable Entity
            detail={
                "message": "Invalid input data",
                "errors": e.errors()  # Detailed validation errors
            }
        )
    except Exception as e:
        # Handle any unexpected errors
        raise HTTPException(
            status_code=500,  # Internal Server Error
            detail=f"An error occurred while processing your request: {str(e)}"
        )
    
@app.post("/predict-rent-price")
def predict_rent_price(house_info: HouseInfo):
    try:
        house_info_dict = dict(house_info)
        data = pd.DataFrame([house_info_dict])
        pred = rent_model.predict(data)
        estimate_house_rent = round(float(pred[0]))
        return {"Estimated House Rent Amount": str(estimate_house_rent)+"৳"}

    except ValidationError as e:
        # Handle validation errors explicitly
        raise HTTPException(
            status_code=422,  # Unprocessable Entity
            detail={
                "message": "Invalid input data",
                "errors": e.errors()  # Detailed validation errors
            }
        )
    except Exception as e:
        # Handle any unexpected errors
        raise HTTPException(
            status_code=500,  # Internal Server Error
            detail=f"An error occurred while processing your request: {str(e)}"
        )
    
if __name__=="__main__":
    uvicorn.run(app="main:app", port=8501, reload=True, host="0.0.0.0")
