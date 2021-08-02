from flask import Blueprint, request, redirect
from .tinyurls import tiny_url

bp = Blueprint('', __name__, url_prefix='/')


@bp.route('/', methods=['GET'])
def get_all_codes():
    executor = tiny_url()
    return executor.get_all_urls()

@bp.route('/<string:short_url>', methods=['GET', 'POST'])
def get_code(short_url):
    executor = tiny_url()

    if request.method == 'GET':
        url = executor.lookup_key(short_url)
        if url:
            return redirect(url)
        else:
            return 404
    else:
        return executor.insert_url(short_url)
