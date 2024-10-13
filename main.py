import logfire
from dotenv import load_dotenv
from fastapi import FastAPI

from routers import manage_accounts, manage_backtesting, manage_broker_messages, manage_docker, manage_files, \
    manage_market_data, manage_databases, manage_performance

load_dotenv()

app = FastAPI()
logfire.configure()
logfire.instrument_fastapi(app)

app.include_router(manage_docker.router)
app.include_router(manage_broker_messages.router)
app.include_router(manage_files.router)
app.include_router(manage_market_data.router)
app.include_router(manage_backtesting.router)
app.include_router(manage_accounts.router)
app.include_router(manage_performance.router)
app.include_router(manage_databases.router)
