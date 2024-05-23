import logging
import strawberry
import uvicorn
from dotenv import dotenv_values
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from src.main.graphql.queries import Query

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)
logger = logging.getLogger(__name__)

schema = strawberry.Schema(query=Query)
graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")


def main():
    required_environment_vars = [
        'MONGO_USERNAME',
        'MONGO_PASSWORD',
        'MONGO_HOST'
    ]
    env_vars = dotenv_values(".env")
    for var in required_environment_vars:
        if var not in env_vars:
            logger.warning(f"Environment variable {var} is not set")
    logger.info('Logger configured')
    logger.info('Starting FastAPI application')
    uvicorn.run(app, port=8081, host='0.0.0.0', access_log=False)


@app.get('/test/logging')
def log_check():
    logger.info('Logger is working')
    return 'Logger is working'


@app.get('/health')
def health_check():
    return {'STATUS": "UP'}


if __name__ == '__main__':
    main()
