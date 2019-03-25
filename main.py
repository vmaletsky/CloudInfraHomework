
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

from multiprocessing import Pool
from multiprocessing import cpu_count

hostName = ""
hostPort = 81


def fibonacci(n):
    fib = lambda n: n if n < 2 else fib(n - 1) + fib(n - 2)
    result = fib(40)
    return result


def run_task():
    processes = cpu_count()
    pool = Pool(processes)
    data = pool.map(fibonacci, range(processes))
    return data


class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.end_headers()
        if self.path == "/ready":
            self.send_response(200)
            self.end_headers()
        elif self.path == "/":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(bytes("Starting calculation of fibonacci numbers on %d cores\n " % cpu_count(), 'utf-8'))
            result = str(run_task())
            self.wfile.write(bytes(result, 'utf-8'))


myServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

myServer.serve_forever()
