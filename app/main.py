import json
import logging

from app.utils.log_generator import generate_logs
from app.utils.log_parser import parse_log_line
from app.services.log_service import save_log
from fastapi import FastAPI
import time
from fastapi import Request
from app.api.log_routes import router as log_router

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)

# Create FastAPI application instance
app = FastAPI()

# Register API routes
app.include_router(log_router)

LOG_FILE = "logs/app.log"
JSON_FILE = "data/logs.json"


@app.middleware("http")
async def log_requests(request: Request, call_next):
    """
    Middleware that logs every API request.
    """
    start_time = time.time()

    response = await call_next(request)

    process_time = (time.time() - start_time) * 1000 # converts to ms

    log_message = (
        f"INFO | {request.method} {request.url.path} | "
        f"Status: {response.status_code} | "
        f"Time: {process_time:.2f}ms"
    )

    print(log_message)

    return response


@app.get("/")
def root():
    """
    Root endpoint.

    Used to check if the API server is running.
    """
    return {"message": "Log API server is running"}


@app.get("/health")
async def health_check():
    """
    Simple health check endpoint
    Used by monitoring systems and load balancers
    to verify the API is running
    """
    return {"status": "Ok"}



def process_logs():

    parsed_logs = []

    with open(LOG_FILE) as file:

        for line in file:

            log = parse_log_line(line)

            inserted_id = save_log(log)

            log["_id"] = str(inserted_id)

            parsed_logs.append(log)

            # save_log(log)

            print("SSaved to MongoDB:", log)

    with open(JSON_FILE, "w") as json_file:

        json.dump(parsed_logs, json_file, indent=4)


if __name__ == "__main__":

    generate_logs()

    process_logs()