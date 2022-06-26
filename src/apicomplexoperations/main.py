from fastapi import FastAPI, HTTPException
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
async def complex_string(text: str, number: int = 0):
    return {"message": stringop.operate(text, number)}


@app.get("/health")
async def health_check():
    if mathop is not None and stringop is not None:
        return {"message": "Healthy"}
    else:
        msg = "We have problem! Complex Operation are None"
        HTTPException(status_code=500, detail=msg)
