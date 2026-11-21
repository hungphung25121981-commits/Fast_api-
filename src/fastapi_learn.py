from fastapi import FastAPI 
app=FastAPI()


@app.get("/")
async def greeting():
    print("siêu đep trai\n")
    return {"message": "Hello World! fastapi "}