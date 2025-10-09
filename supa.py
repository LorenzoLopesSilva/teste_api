@app.get("/")
async def read_root():
    return {"hello": "jaaj"}