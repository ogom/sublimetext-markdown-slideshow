""" mcider - util
Copyright(c) 2012 ogom

file reader or writer
"""
import codecs

def fs_reader(path):
    return codecs.open(path, mode='r', encoding='utf8').read()

def fs_writer(path, raw):
    codecs.open(path, mode='w', encoding='utf8').write(raw)
