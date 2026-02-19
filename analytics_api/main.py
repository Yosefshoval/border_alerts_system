from fastapi import FastAPI
import uvicorn
from routes import router

app = FastAPI()

@app.get('/')
def home():
    return {"message": "server is running"}

app.include_router(router)



if __name__ == "__main__":
    uvicorn.run(
        app='main:app',
        host='0.0.0.0',
        port=8080
    )