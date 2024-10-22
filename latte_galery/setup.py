from fastapi import FastAPI
from latte_galery.routers import status_router, account_router
from fastapi.middleware.cors import CORSMiddleware

def create_app():
    app = FastAPI(title="LatteGalery")

    app.include_router(status_router)
    app.include_router(account_router)
    
    app.add_middleware(CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_credentials=True,
    )
    return app