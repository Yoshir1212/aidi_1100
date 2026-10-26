#this file is titled main.py on my machine
from fastapi import FastAPI

app = FastAPI()


@app.post("/add")
def add_numbers(a: int, b: int):    #make sure we are passing an integer 
    return {"sum": a + b}


