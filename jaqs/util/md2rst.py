# encoding: utf-8

import os
from os.path import join
from jaqs.util import fileio
import subprocess


def md2rst():
    input_dir = fileio.join_relative_path('../doc')
    output_dir = fileio.join_relative_path('../doc/source')

    for dir_path, dir_names, file_names in os.walk(input_dir):
        for fn in file_names:
            if fn.endswith('.md'):
                print "Converting {:s}...".format(fn)
                
                fn_pure = fn[:-2]
                fn_md = join(input_dir, fn)
                fn_html = join(input_dir, fn_pure+'html')
                fn_rst = join(output_dir, fn_pure+'rst')
                
                subprocess.check_output(['pandoc', fn_md,
                                         '-f', 'markdown_github',
                                         '-t', 'html', '-s', '-o', fn_html])
                subprocess.check_output(['pandoc', fn_html,
                                         '-f', 'html',
                                         '-t', 'rst', '-s', '-o', fn_rst])
                os.remove(fn_html)


if __name__ == "__main__":
    md2rst()