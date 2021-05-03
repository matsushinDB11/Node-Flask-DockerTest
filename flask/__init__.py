from flask import Flask
from .view.hello import hello
from .view.index import index
from .view.fomula import fomula

app = Flask(__name__)

app.register_blueprint(hello)
app.register_blueprint(index)
app.register_blueprint(fomula)
