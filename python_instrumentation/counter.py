import http.server
import random
from prometheus_client import start_http_server, Counter
#defines a counter with metric name and it's description, the 3rd argument is for adding labels name, 
REQUEST_COUNT = Counter('app_requests_count', 'total app http request count',['app_name', 'endpoint'])
RANDOM_COUNT = Counter('app_random_count','increment counter by random value')

# port of python app
APP_PORT = 8000
# port of metric server
METRICS_PORT = 8001

class HandleRequests(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        # labels of app_name and endpoint
        REQUEST_COUNT.labels('prom_python_app', self.path).inc()
        random_val = random.random()*10
        RANDOM_COUNT.inc(random_val)
        
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>First Application</title></head><body style='color: #333; margin-top: 30px;'><center><h2>Welcome to our first Prometheus-Python application.</center></h2></body></html>", "utf-8"))
        self.wfile.close()

if __name__ == "__main__":
    # start the metric server on port 8001
    start_http_server(METRICS_PORT)
    server = http.server.HTTPServer(('localhost', APP_PORT), HandleRequests)
    server.serve_forever()