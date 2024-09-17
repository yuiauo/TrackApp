import os

import dotenv
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


dotenv.load_dotenv()
url = os.getenv("DATABASE_URL")
bind = create_async_engine(url=url, future=True, echo=True)
AsyncSession = async_sessionmaker(bind=bind, expire_on_commit=False)
