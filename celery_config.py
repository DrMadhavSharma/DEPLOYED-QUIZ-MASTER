import os

broker_url = os.getenv("REDIS_URL")
result_backend = broker_url
broker_connection_retry_on_startup = True
