# python3

from collections import namedtuple
from re import S

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []

    def process(self, request):
        # write your code here
        if len(self.finish_time) < self.size :
            start = request[0]
            if len(self.finish_time) > 0 :
                start = max(request[0], self.finish_time[0])
            self.finish_time.append(start + request[1])
            return Response(False, start)
        elif min(self.finish_time) <= request[0] :
            for item in self.finish_time :
                if item <= request[0] :
                    self.finish_time.remove(item)
                    start = item - request[0]
                    if start < 0 :
                        start = 0
                    self.finish_time.append(start + request[1])
                    break
            return Response(False, request[0])
        else:
            return Response(True, -1)


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
