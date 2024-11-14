from fastapi import FastAPI, Request
from schemas import UserInfoModel
from fastapi import APIRouter
from routers import main_router 
import uvicorn

app = FastAPI(
    title = "SeSAC Dobong AI - FastAPI Application",
    description="SeSAC Dobong AI",
    version = "0.0.1"
)
app.include_router(main_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port = 8080, reload = False)    

