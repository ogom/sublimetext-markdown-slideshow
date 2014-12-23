""" mcider - util
Copyright(c) 2012-2014 ogom

"""
import codecs
import sys


def fs_reader(path):
    return codecs.open(path, mode='r', encoding='utf8').read()


def fs_writer(path, raw):
    codecs.open(path, mode='w', encoding='utf8').write(raw)


def is_v3():
    return sys.version_info >= (3, 0)
