from os.path import join, dirname, abspath

from bottle import static_file, Bottle, run, post, get, request

import json

import subprocess

app = Bottle()

appPath =  dirname(abspath(__file__))

@app.route('/')
# add route to static files
@app.route('/static/<filepath:path>')
def static_route(filepath=None):
    if filepath is None:
        return static_file("index.html", root=join(appPath, 'static'))
    return static_file(filepath, root=join(appPath, 'static'))


@app.route('/get_thumbnail', name='get_thumbnail')
def get_thumbnail():
    py2output = subprocess.Popen([join(appPath,'./extractThumbnail.sh'), request.query.url], stdout=subprocess.PIPE)
    image_name = py2output.stdout.read()
    result = json.dumps({'image_name': image_name})
    return result


if __name__ == "__main__":
    run(app, host='localhost', port=8080)