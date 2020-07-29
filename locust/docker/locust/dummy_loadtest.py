import uuid
import time
import logging
from locust import HttpLocust, TaskSet, task

logger = logging.getLogger(__name__)

class MetricsTaskSet(TaskSet):
    _deviceid = None

    def on_start(self):
        self._deviceid = str(uuid.uuid4())

    @task(1)
    def login(self):
        time_start = time.time()
        response = self.client.get("/datetime")
        time_end = time.time()
        logger.info("Response - URL: {url}. Status code: {status}. "
                    "Latency: {duration}".format(url=response.url,
                                                 status=response.status_code,
                                                 duration=round(time_end - time_start, 3)))


class MetricsLocust(HttpLocust):
    task_set = MetricsTaskSet
