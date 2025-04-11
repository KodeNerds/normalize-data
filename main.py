from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import tempfile, shutil, os
from pathlib import Path
from normalize_jewelry_data import normalize_file

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/normalize")
async def normalize(files: list[UploadFile] = File(...)):
    with tempfile.TemporaryDirectory() as tmpdir:
        dataframes = []
        for file in files:
            file_path = os.path.join(tmpdir, file.filename)
            with open(file_path, "wb") as f:
                shutil.copyfileobj(file.file, f)
            vendor = Path(file.filename).stem.split("_")[0]
            df = normalize_file(file_path, vendor)
            dataframes.append(df)

        combined = pd.concat(dataframes, ignore_index=True)
        output_path = os.path.join(tmpdir, "normalized_products.csv")
        combined.to_csv(output_path, index=False)

        static_path = "./static/normalized_products.csv"
        shutil.copy(output_path, static_path)

        return JSONResponse({"downloadUrl": "/static/normalized_products.csv"})
    
@app.get("/")
def health_check():
    return {"status": "ok"}

