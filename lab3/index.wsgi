import sae
from booksystem import wsgi

application = sae.create_wsgi_app(wsgi.application)

ADD C4

