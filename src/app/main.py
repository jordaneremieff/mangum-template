from fastapi import FastAPI, Request

from app.conf import DEBUG, LIB_PATH


app = FastAPI(debug=DEBUG)


@app.get("/")
def get_lambda_info(request: Request):
    payload = {
        "event": request.scope.get("aws.event", {}),
        "dependencies": sorted([item.name for item in LIB_PATH.iterdir()]),
    }

    return payload
