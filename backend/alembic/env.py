import asyncio
from logging.config import fileConfig

from alembic import context
from sqlalchemy.ext.asyncio import create_async_engine

# 1. Импортируем настройки и Base из твоего проекта
from app.core.config import settings
from app.core.database import Base

# 2. Импортируем сами модели (или весь пакет models), чтобы Alembic видел таблицы
import app.models  # noqa

config = context.config

if config.config_file_name is not None:
  fileConfig(config.config_file_name)

target_metadata = Base.metadata

# 3. Динамически подставляем строку подключения из твоего config.py
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL_asyncpg)


def run_migrations_offline() -> None:
  url = config.get_main_option("sqlalchemy.url")
  context.configure(
      url=url,
      target_metadata=target_metadata,
      literal_binds=True,
      dialect_opts={"paramstyle": "named"},
  )

  with context.begin_transaction():
    context.run_migrations()


def do_run_migrations(connection):
  context.configure(connection=connection, target_metadata=target_metadata)

  with context.begin_transaction():
    context.run_migrations()


async def run_async_migrations() -> None:
  connectable = create_async_engine(
      config.get_main_option("sqlalchemy.url"), future=True
  )

  async with connectable.connect() as connection:
    await connection.run_sync(do_run_migrations)

  await connectable.dispose()


def run_migrations_online() -> None:
  asyncio.run(run_async_migrations())


if context.is_offline_mode():
  run_migrations_offline()
else:
  run_migrations_online()