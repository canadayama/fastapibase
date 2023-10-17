"""
    main.py
"""
# Third Party Imports
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
# Built-in Imports
import logging
# Relative Imports


logger = logging.getLogger(__name__)

def get_name() -> str:
    """"""
    return "Jane Doe"

try:
    app = FastAPI()

    # Add middleware
    # app.add_middleware(SessionMiddleware, secret_key=settings.sec_secret_key)
    origins = ["*"]
    app.add_middleware(CORSMiddleware,
                       allow_origins=origins,
                       allow_credentials=True,
                       allow_methods=["*"],
                       allow_headers=["*"])
    
    @app.get("/", tags=['index'])
    async def root(name: str=Depends(get_name)):
        return {"server": "alive", "name": name}
    
    # Setup routes

    @app.on_event('startup')
    def in_startup():
        """Handles on startup event."""
        logger.info("Starting...")
    @app.on_event('shutdown')
    def on_shutdown():
        """Handles on shutdown event."""
        logger.info("Shutting down...")
except Exception as ex:
    logger.exception(ex)