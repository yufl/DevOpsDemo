#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Desc: Main program
'''

from src.com.kuka.util import utils
import os
from docxtpl import Document

if __name__ == "__main__":
    template_dir = os.path.join(utils.get_template_dir(), 'templates')
    template_path = os.path.join(template_dir, "debug.docx")
    object_path = os.path.join(template_dir, "c:\\debugDemo.docx")
    doc = Document(template_path)
    doc.save(object_path)
    #utils.update_doc_toc(object_path)