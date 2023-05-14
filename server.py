from http.server import BaseHTTPRequestHandler, HTTPServer
from io import BytesIO

class ServerHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        Dir = "myserver/"+self.path[1:]
        try:
            htmlResponse = open(Dir).read()
            self.send_response(200)
        except:
            htmlResponse = open("myserver/error.html").read()
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(htmlResponse, 'utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        f = open("C:\\pass.txt", "w")
        f.write(str(response.getvalue()))
        f.close()
        response.write(b'Saved :')
        response.write(body)
        self.wfile.write(response.getvalue())


HOST = '127.0.0.1'
PORT = 80
ServerAddress = (HOST, PORT)
httpd = HTTPServer(ServerAddress, ServerHandler)
httpd.serve_forever()