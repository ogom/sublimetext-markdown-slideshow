#!/usr/bin/env python
""" mcider - main
Copyright(c) 2012-2014 ogom

Mcider is to convert markdown into slideshow.
"""
from __future__ import print_function
import os
import webbrowser
from . import cli_helper
from . import converter
from . import util


def main():
    """ entry points """
    args = cli_helper.parser.parse_args()

    # path of the output file
    output_path = os.path.abspath(os.path.dirname(args.file.name))
    output_file = os.path.join(output_path, os.path.splitext(os.path.basename(args.file.name))[0] + '.html')
    if args.output:
        output_path = os.path.abspath(os.path.dirname(args.output.name))
        output_file = os.path.abspath(args.output.name)

    _contents = args.file.read().decode('utf-8') if util.py2k else args.file.read()
    # slide options
    opts = {
        'themes': args.themes,
        'theme': args.theme,
        'contents': _contents,
        'extensions': args.extensions,
        'clean': args.clean
    }

    # custom themes or default themes
    if opts['themes'] is None or not os.path.isdir(opts['themes']):
        opts['themes'] = os.path.abspath(os.path.join(os.path.dirname(__file__), 'themes'))

    try:
        # slide maker
        slide = converter.Slide(opts)
        html = slide.maker(output_path)
        util.fs_writer(output_file, html)
        if args.browser:
            url = 'file://' + output_file
            if slide.options['theme'] == 'io2012':
                url += '?presentme='
                url += 'true' if args.presenter else 'false'
            webbrowser.open_new_tab(url)
    except KeyError as e:
        print("KeyError: %s" % e)
    else:
        print("Output file is %s" % output_file)
    finally:
        print('Mcider is finished!')

if __name__ == '__main__':
    main()
