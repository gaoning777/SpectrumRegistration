from gevent import wsgi 
from flask_service import app

http_server = wsgi.WSGIServer(('0.0.0.0', 5000), app)
http_server.serve_forever()
