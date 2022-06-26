from fastapi import FastAPI
from complexoperations import JustSomeMath, JustSomeString

app = FastAPI()
mathop = JustSomeMath.JustSomeMath()
stringop = JustSomeString.JustSomeString()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/math/{number}")
async def complex_math(number: int = 0):
    return {"message": mathop.operate(number)}


@app.get("/string")
async def complex_string(text: str, number: int = 1):
    return {"message": stringop.operate(text, number)}
