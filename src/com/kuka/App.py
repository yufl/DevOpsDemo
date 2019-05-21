#!/usr/bin/python
# -*- coding: UTF-8 -*-

from win32com import client
import os
import sys
from docxtpl import Document

def update_doc_toc(doc_path):
    word = client.DispatchEx("Word.Application")
    doc = word.Documents.Open(doc_path)
    doc.TablesOfContents(1).Update()
    doc.Close(SaveChanges=True)
    word.Quit()
    return

def get_template_dir():
    cur_dir = os.path.realpath(sys.argv[0])
    temp_dir = cur_dir
    dirs = cur_dir.split('\\')
    src_index = 0
    for i in range(len(dirs) - 1, -1, -1):
        if dirs[i] == 'src':
            src_index = i
            break
    if src_index == 0:
        print('Wrong package.')
    for i in range(src_index, len(dirs)):
        temp_dir = temp_dir.replace(os.path.sep + dirs[i], '')
    return temp_dir

if __name__ == "__main__":
    template_dir = os.path.join(get_template_dir(), 'templates')
    template_path = os.path.join(template_dir, "debug.docx")
    object_path = os.path.join(template_dir, "c:\\debugDemo.docx")
    doc = Document(template_path)
    doc.save(object_path)
    update_doc_toc(object_path)