from http.server import HTTPServer, SimpleHTTPRequestHandler

class Handler(SimpleHTTPRequestHandler):
    # The only POST request we get is the one we send when we're saving the `exName.log` file
    def do_POST(self):
        # The path we get is an absolute path on the server (which is not an absolute path on our local filesystem)
        # Remove the leading slash so that its a relative path
        path = self.path.lstrip("/")

        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)

        with open(path, "wb") as f:
            content = f.write(body)

        self.send_response(200) # Indicate success (HTTP response code: 200)
        self.end_headers()

with HTTPServer(("", 38080), Handler) as httpd:
    httpd.serve_forever()
