#!/usr/bin/env python
# coding=utf-8
import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(filename)s - %(levelname)s : %(message)s')

import os,sys
here = os.path.abspath(os.path.dirname(__file__))
logging.info(here)
rootPath = os.path.split(here)[0]
logging.info(rootPath)
# sys.path.append(rootPath)

from xmindConvert.initDb import *
from xmindConvert.control import *
from xmindConvert.utils import *
from flask import Flask, request, send_from_directory, render_template, abort, redirect, url_for

# flask app
app = Flask(__name__)
app.config.from_object(__name__)
DEBUG = True
HOST = '0.0.0.0'


# 在请求收到之前绑定一个函数做一些事情
@app.before_request
def before_request():
    g.db = connect_db()


# 每一个请求之后绑定一个函数，即使遇到了异常
@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

# 处理错误的页面
@app.errorhandler(Exception)
def app_error(e):
    return str(e)

@app.route('/', methods=['GET', 'POST'])
def index(download_xml=None):
    g.invalid_files = []
    g.error = None
    g.download_xml = download_xml
    g.filename = None

    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        g.filename = save_file(file)
        verify_uploaded_files([file])
        delete_records()
    else:
        g.upload_form = True
    if g.filename:
        return redirect(url_for('preview_file', filename=g.filename))
    else:
        return render_template('index.html', records=list(get_records()))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route('/<filename>/to/testlink')
def download_testlink_file(filename):
    full_path = os.path.join(UPLOAD_FOLDER, filename)
    if not os.path.exists(full_path):
        abort(404)
    mode = request.args.get('mode')
    xmlPath = xmind_to_testlink_xml_file(full_path, mode)
    filename = os.path.basename(xmlPath) if xmlPath else abort(404)
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)

@app.route('/<filename>/to/robot')
def download_robot_file(filename):
    full_path = os.path.join(UPLOAD_FOLDER, filename)
    if not os.path.exists(full_path):
        abort(404)
    mode = request.args.get('mode')
    tarPath = xmind_to_robot_tar_file(full_path, mode)
    filename = os.path.basename(tarPath) if tarPath else abort(404)
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)

@app.route('/preview/<filename>')
def preview_file(filename):
    full_path = os.path.join(UPLOAD_FOLDER, filename)
    if not os.path.exists(full_path):
        abort(404)
    nodes, maxLevel = convertToDisplay(full_path)
    return render_template('preview.html', name=filename, nodes=nodes, maxLevel=maxLevel)

@app.route('/delete/<filename>/<int:record_id>')
def delete_file(filename, record_id):
    full_path = os.path.join(UPLOAD_FOLDER, filename)
    if not os.path.exists(full_path):
        abort(404)
    else:
        delete_record(filename, record_id)
    return redirect('/')

init()  # initializing the database

if __name__ == '__main__':
    app.run(HOST, debug=DEBUG, port=8001)
