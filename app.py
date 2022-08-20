import app_logger
from app_logger_formatter import CustomFormatter
from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()
formatter = CustomFormatter('%(asctime)s')
logger = app_logger.get_logger(__name__, formatter)


def get_extra_info(request):
    return {'req': {
        'url': request.url.path,
        'headers': {'host': request.headers['host'],
                    'user-agent': request.headers['user-agent'],
                    'accept': request.headers['accept']},
        'method': request.method,
        'httpVersion': request.scope['http_version'],
        'originalUrl': request.url.path,
        'query': {}
        },
        'res': {'statusCode': 200, 'body': {'statusCode': 200,
                   'status': 'OK'}}}


@app.get("/foo")
def foo(request: Request):
    logger.info('GET ' + request.url.path, extra={'extra_info': get_extra_info(request)})
    return "success"

