from flask import Blueprint, jsonify
fomula = Blueprint('f1', __name__, url_prefix='/f1')
from ..dbconnect import dbconnect


@fomula.route('/')
def f1_constructor():
  cur = dbconnect().cursor()
  sql = "SELECT * FROM items"
  cur.execute(sql)
  rows = cur.fetchall()
  return jsonify(rows)
  # return 'this is db'
  