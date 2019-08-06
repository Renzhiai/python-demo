#!/usr/bin/env python
# coding=utf-8
import arrow
from xmindConvert.cfg import *
from flask import g

def insert_record(xmind_name, note=''):
    '''
    插入记录
    :param xmind_name:
    :param note:
    :return:
    '''
    c = g.db.cursor()
    now = str(arrow.now())
    sql = "INSERT INTO records (name,create_on,note) VALUES (?,?,?)"
    c.execute(sql, (xmind_name, now, str(note)))
    g.db.commit()

def delete_record(filename, record_id):
    xmind_file = os.path.join(UPLOAD_FOLDER, filename)
    testlink_file = os.path.join(UPLOAD_FOLDER, filename[:-5] + 'xml')
    zentao_file = os.path.join(UPLOAD_FOLDER, filename[:-5] + 'csv')

    for f in [xmind_file, testlink_file, zentao_file]:
        if os.path.exists(f):
            os.remove(f)

    c = g.db.cursor()
    sql = 'UPDATE records SET is_deleted=1 WHERE id = ?'
    c.execute(sql, (record_id,))
    g.db.commit()

def get_latest_record():
    found = list(get_records(1))
    if found:
        return found[0]

def get_records(limit=8):
    short_name_length = 120
    c = g.db.cursor()
    sql = "select * from records where is_deleted<>1 order by id desc limit {}".format(int(limit))
    c.execute(sql)
    rows = c.fetchall()

    for row in rows:
        name, short_name, create_on, note, record_id = row[1], row[1], row[2], row[3], row[0]

        # shorten the name for display
        if len(name) > short_name_length:
            short_name = name[:short_name_length] + '...'

        # more readable time format
        create_on = arrow.get(create_on).humanize()
        yield short_name, name, create_on, note, record_id

def save_file(file):
    if file and file.filename:
        filename = file.filename
        upload_to = os.path.join(UPLOAD_FOLDER, filename)

        if os.path.exists(upload_to):
            filename = '{}_{}.xmind'.format(filename[:-6], arrow.now().strftime('%Y%m%d_%H%M%S'))
            upload_to = os.path.join(UPLOAD_FOLDER, filename)

        file.save(upload_to)
        insert_record(filename)
        g.is_success = True
        return filename

    elif file.filename == '':
        g.is_success = False
        g.error = "Please select a file!"

    else:
        g.is_success = False
        g.invalid_files.append(file.filename)


def delete_records(keep=20):
    """Clean up files on server and mark the record as deleted"""
    sql = "SELECT * from records where is_deleted<>1 ORDER BY id desc LIMIT -1 offset {}".format(keep)
    c = g.db.cursor()
    c.execute(sql)
    rows = c.fetchall()
    for row in rows:
        name = row[1]
        xmind_file = os.path.join(UPLOAD_FOLDER, name)
        testlink_file = os.path.join(UPLOAD_FOLDER, name[:-5] + 'xml')
        zentao_file = os.path.join(UPLOAD_FOLDER, name[:-5] + 'csv')

        for f in [xmind_file, testlink_file, zentao_file]:
            if os.path.exists(f):
                os.remove(f)

        sql = 'UPDATE records SET is_deleted=1 WHERE id = ?'
        c.execute(sql, (row[0],))
        g.db.commit()

def verify_uploaded_files(files):
    # download the xml directly if only 1 file uploaded
    if len(files) == 1 and getattr(g, 'is_success', False):
        g.download_xml = get_latest_record()[1]

    if g.invalid_files:
        g.error = "Invalid file: {}".format(','.join(g.invalid_files))