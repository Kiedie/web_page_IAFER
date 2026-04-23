#!/usr/bin/env python3
"""
Servidor web que bloquea el acceso directo a archivos PDF
pero permite imágenes PNG (previews) y otros recursos estáticos.
"""

import http.server
import socketserver
import os

PORT = 8080

class SecureHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

    def do_GET(self):
        # Bloquear acceso a archivos .pdf
        if self.path.lower().endswith('.pdf'):
            self.send_response(403)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<h1>403 Forbidden</h1><p>Access to PDF files is restricted.</p>')
            return

        # Bloquear listado de directorios que contengan PDFs
        if 'paper_pdfs' in self.path and not self.path.endswith('.png'):
            self.send_response(403)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<h1>403 Forbidden</h1>')
            return

        # Servir normalmente el resto de archivos
        super().do_GET()

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    with socketserver.TCPServer(("", PORT), SecureHTTPRequestHandler) as httpd:
        print(f"Serving at http://localhost:{PORT}")
        print("PDF files are blocked, PNG previews are allowed.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")
