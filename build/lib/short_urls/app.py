from fastapi import FastAPI

from short_urls.api.url import url_router

app = FastAPI()
app.include_router(url_router)
