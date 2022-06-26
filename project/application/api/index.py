from flask import Blueprint, Response
import time
import json

index = Blueprint('index', __name__)
index.url_prefix = '/index'

@index.route('/')
def get_name():
    return Response(json.dumps("Index API"))

@index.route('/time')
def get_time():
    return str(time.time())