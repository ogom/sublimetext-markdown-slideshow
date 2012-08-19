""" mcider - cli helper
Copyright(c) 2012 ogom

Parser for command line options.
"""
import argparse

parser = argparse.ArgumentParser(description='Mcider is to convert markdown into slideshow.')

parser.add_argument(
    'file', metavar='FILE', type=argparse.FileType('r'),
    help='Contents of the markdown.'
)

parser.add_argument(
    '--theme', '-t', default='io2012',
    help='Theme of the slide. (io2012, io2011, ...)'
)

parser.add_argument(
    '--output', '-o', metavar='FILE', type=argparse.FileType('w+'),
    help='File to output slide.'
)

parser.add_argument(
    '--extensions', '-e', metavar='EXTENSION', nargs='*',
    help='''
      Provided to expand the base syntax.
      (extra, fenced_code, tables, ...)
    '''
)

parser.add_argument(
    '--browser', '-b', action='store_true', default=False,
    help='View in Web Browser.'
)

parser.add_argument(
    '--clean', '-c', action='store_true', default=False,
    help='Theme was to clean the output.'
)

parser.add_argument(
    '--themes', metavar='PATH',
    help='Path of the custom themes'
)
