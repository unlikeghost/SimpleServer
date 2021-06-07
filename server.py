"""Servidor basico con metodos post y get
    by.- Unlikeghost"""

from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler

class Metodos(BaseHTTPRequestHandler):
    """Clase para majerar metodos"""

    def html(self, texto):
        """Genera un html"""

        content = f"<html><body><h1>{texto}</h1></body></html>"
        return content.encode("utf8")

    def do_GET(self):
        """Metodo GET"""

        self.send_response(200)
        self.end_headers()
        self.wfile.write(self.html("HOLAAAAA"))



    def do_POST(self):
        """Metodo POST"""

        #Respuesta
        content = bytes("OK", "UTF-8")
        
        self.send_response(200)
        
        #tipo de contenido a manejar
        self.send_header("Content-type","text/plain")
        
        self.send_header("Content-Length", len(content))
        
        self.end_headers()
        
        data = self.rfile.read(int(self.headers['Content-Length'])).decode("UTF-8")
        
        #imprimimos la informacion
        print(data)

        self.wfile.write(content)


def runserver(ip="127.0.0.1",puerto=80):
    """Funcion principal"""

    print(f"El servidor esta corriendo en {ip}:{80}")
    address = (ip,puerto)
    httpd = HTTPServer(address, Metodos)
    httpd.serve_forever()

if __name__ == "__main__":
    runserver()
