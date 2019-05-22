from win32com import client
import os
import sys

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
        src_index = len(dirs) - 1
    for i in range(src_index, len(dirs)):
        temp_dir = temp_dir.replace(os.path.sep + dirs[i], '')
    return temp_dir