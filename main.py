import io


import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException,UploadFile,File
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field

app = FastAPI()

# 1st step is model load 
model = joblib.load("house_model.joblib")
features = joblib.load("house_features.joblib")

# Input schema
class HouseFeatures(BaseModel):
    Medinc: float = Field(gt=0, description="media income of Neighbourhood")
    HouseAge: float = Field(gt=0, description="averge house of house in the block")
    AveRooms: float = Field(gt=0, description="averge number of roomsin house")
    AveBedrms: float = Field(gt=0, description="averge number of bedrms in room")
    Population: float = Field(gt=0, description="Total Population")
    AveOccup: float = Field(gt=0, description="averge number of Occup")
    Latitude: float = Field(gt=32, le=42, description="Latitude")
    Longitude: float = Field(gt=-125, le=-114, description="Longitude") # USA California Longitude negative hote hain (-)

# Home endpoint
@app.get("/")
def home():
    return {
        "message": "california predection api",
        "status": "running",
        "endpoint": "send POST request to /predict"
    }

# Health endpoint
@app.get("/health")
def health():
    return {
        "status": "running",
        "model": "RandomForestRegressor",
        "features": features,
        "avg_error": "$39,000"
    }
    
# Prediction endpoint
@app.post("/predict")
def predict(house: HouseFeatures):
    try:
        # Columns ke naam bilkul model ki training ke mutabiq set kiye hain
        input_data = pd.DataFrame([{
            "MedInc": house.Medinc,        # 'Medinc' ko badal kar 'MedInc' kiya (capital I)
            "HouseAge": house.HouseAge,
            "AveRooms": house.AveRooms,
            "AveBedrms": house.AveBedrms,
            "Population": house.Population,
            "AveOccup": house.AveOccup,
            "Latitude": house.Latitude,
            "Longitude": house.Longitude
        }])
        
        # DataFrame ke columns ka order model ke features ke mutabiq arrange karne ke liye
        input_data = input_data[features]
        
        predicted = model.predict(input_data)
        
        # Kyunke predicted value ek array (numpy array) ho sakti hy, 
        # is liye uski pehli value nikalne ke liye [0] lagaya hy
        predicted_val = float(predicted[0])
        price_usd = predicted_val * 100000
        
        return {
            "predicted_price": f"${price_usd:,.0f}",
            "predicted_price_short": f"${predicted_val:.2f} hundred thousands",
            "confidence_range": f"${price_usd-39000:,.0f} to ${price_usd+39000:,.0f}"
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"prediction failed {str(e)}"
        )
@app.post("/predict_file")
async def predict_file(file:UploadFile=File(...)):
        if not file.filename.endswith(".csv"):
            raise HTTPException(
                status_code=400,
                detail= "please upload a csv file only"
            )
            
        contents = await file.read()
        df = pd.DataFrame(io.BytesIO(contents))
        required_columns= [
            "MedInc","HouseAge","AveRooms","AveBedrms"
            "Population","AveOccup", "Latitude"
            "Longitude"
        ]
        
        missing_columns=[
            col for col in required_columns
            if col not in df.columns
                
        ]
        
        if missing_columns:
            raise HTTPException(
                status_code =400,
                details = f"this coloumns missing from your file {missing_columns} "
            )
        if len(df)==0:
            raise HTTPException(
                status_code=400,
                detail= "the upload file has no data rows"
            )
        try:
            predictions= model.predict(df[required_columns])
            df["predicted_columns_usd"]= df["predicted_columns_usd"].apply(lambda x:f"${x:.0f}")
            output = df.to_csv(index=False)
            return StreamingResponse(
                io.StringIO(output),
                media_type="text/csv",
                headers = {
                    "Content_Disposition":"attachment;filename = predictions.csv"
                }
            )
        except Exception as e:
            raise HTTPException(
                status_code=500,
                details= "f prediction failed :{str(e)}"
                
            )
                 
        