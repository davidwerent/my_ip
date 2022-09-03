from fastapi import Request, FastAPI

app = FastAPI()


@app.get('/ip')
async def ip(request: Request):
    return request.client.host
