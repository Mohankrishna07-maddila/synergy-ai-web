import http.server
import socketserver

PORT = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Serve web.html when someone visits the root URL (/)
        if self.path == '/':
            self.path = '/index.html'
        return super().do_GET()

try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"✅ Python web server is running on port {PORT}")
        print(f"🌐 Open http://localhost:{PORT} in your browser to view your website")
        print("Press Ctrl+C to stop the server.")
        httpd.serve_forever()
except OSError as e:
    if e.errno == 98 or e.errno == 10048: # Port already in use
        print(f"❌ Port {PORT} is already in use. Try a different port or kill the process using it.")
    else:
        raise
