import locust.events
from locust import HttpLocust, TaskSet


class LocustUser(HttpLocust):
    task_set = TaskSet
    min_wait = 1000
    max_wait = 1000

    request_success_stats = [list()]
    request_fail_stats = [list()]

    def __init__(self):
        locust.events.request_success += self.hook_request_success
        locust.events.request_failure += self.hook_request_fail
        locust.events.quitting += self.hook_locust_quit

    def hook_request_success(self, request_type, name, response_time, response_length):
        self.request_success_stats.append([name, request_type, response_time])

    def hook_request_fail(self, request_type, name, response_time, exception):
        self.request_fail_stats.append([name, request_type, response_time, exception])

    def hook_locust_quit(self):
        self.save_success_stats()

    def save_success_stats(self):
        import csv
        with open('success_req_stats.csv', 'wb') as csv_file:
            writer = csv.writer(csv_file)
            for value in self.request_success_stats:
                writer.writerow(value)