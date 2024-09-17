import os

from alembic import context
from dotenv import load_dotenv
from sqlalchemy import engine_from_config
from sqlalchemy import pool

from models import Base


load_dotenv()
target_metadata = Base.metadata

config = context.config
config.set_main_option('sqlalchemy.url', os.getenv('DATABASE_URL'))


def run_migrations() -> None:
    """
        'Online' migrations mode
    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )
        with context.begin_transaction():
            context.run_migrations()


run_migrations()
