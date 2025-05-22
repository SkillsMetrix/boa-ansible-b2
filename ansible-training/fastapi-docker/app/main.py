
from fastapi import FastAPI

app= FastAPI()
@app.get("/")
def loadData():
    return {"message":"welcome to FastAPI Apps"}
