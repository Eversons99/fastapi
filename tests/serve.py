from fastapi import FastAPI

app = FastAPI()


@app.get("/test")
async def testing():
    return {"message": "Hello World"}