from fastapi import FastAPI
from settings import app_settings
from helpers.logger import get_logger


app = FastAPI()

logger = get_logger("main")


@app.get("/healthcheck", status_code=200)
async def healthcheck():
    logger.info("Healthcheck endpoint called")
    return {"status": "ok", "app_name": app_settings.app_name}


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
