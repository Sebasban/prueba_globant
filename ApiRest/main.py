# main.py
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def root():
 return {"greeting":"Hello world"}

@app.get("/other_endpoint")
async def root():
 return {"greeting":"this is an another endpoint"}