"""
Nanobot Local Development Server
Starts a local HTTP server and automatically opens the catalog in your browser.
"""

import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8080

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Prevent caching during testing
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Try preferred port or next available
    port = PORT
    for _ in range(10):
        try:
            with socketserver.TCPServer(("", port), Handler) as httpd:
                url = f"http://localhost:{port}"
                print("="*60)
                print(f"  ✨ NANOBOT BOTTLE CATALOG & QUOTATION PORTAL ✨")
                print("="*60)
                print(f"  Local URL: {url}")
                print(f"  Serving directory: {os.getcwd()}")
                print(f"  Press Ctrl+C to stop the server.")
                print("="*60)
                webbrowser.open(url)
                httpd.serve_forever()
                break
        except OSError:
            port += 1

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        sys.exit(0)
