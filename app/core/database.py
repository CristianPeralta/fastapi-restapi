import motor.motor_asyncio
from beanie import init_beanie
from app.config.settings import get_settings
import logging

# We import the models that will be initialized with Beanie
from app.models.user import User

logger = logging.getLogger("uvicorn")

settings = get_settings()


async def init_db():
    """
    Initialize the MongoDB database connection and register the Beanie models
    """
    # MongoDB client using Motor
    client = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGODB_URL)
    try:
      # Initialize Beanie with the database and models
      await init_beanie(
          database=client[settings.MONGODB_DB_NAME],
          document_models=[
              User
              # Add more models here when needed
          ]
      )
      logger.info(f"MongoDB connected: {settings.MONGODB_URL}/{settings.MONGODB_DB_NAME}")
    except Exception as e:
      logger.error(f"❌ Failed to connect to MongoDB: {e}")

