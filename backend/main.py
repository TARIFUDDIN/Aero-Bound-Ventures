from fastapi import FastAPI


app = FastAPI()
@app.get("/")
def hello():
    return {"message":"flight booking"}

class Person():
    ...
    
john=Person()