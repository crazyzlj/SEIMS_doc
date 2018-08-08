#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Replace the relative links by global paths for Doxygen.
    @author   : Liang-Jun Zhu
    @changelog: 2018-08-08 - lj - Initial implementation.
"""
import os


def current_path(local_function):
    """Get current path
    Reference: https://stackoverflow.com/questions/2632199/how-do-i-get-the-path-of-the-current-executed-file-in-python/18489147#18489147
    Examples:
        curpath = current_path(lambda: 0)
    """
    from inspect import getsourcefile
    fpath = getsourcefile(local_function)
    if fpath is None:
        return None
    return os.path.dirname(os.path.abspath(fpath))

def replace_relative_paths(filepath, relative_path):
    print('Replace relative paths of %s' % filepath)
    lines = list()
    with open(filepath, 'r') as f:
        for line in f.readlines():
            lines.append(line.strip())
    rewrite = false
    for line in lines:
        
    if rewrite:
        with open(filepath, 'w') as f:
            for line in lines:
                f.write(line + os.linesep)

def main(fpath, relative_path):
    entries = os.listdir(fpath)
    for entry in entries:
        tmppath = fpath + os.sep + entry
        if os.path.isdir(tmppath):
            relative_path += os.sep + entry
            main(tmppath, relative_path)
        else:
            name, ext = os.path.splitext(entry)
            if not ext.upper() == 'MD':
                continue
            replace_relative_paths(tmppath, relative_path)

if __name__ == '__main__':
    cpath = current_path(lambda: 0)
    topname = os.path.split(cpath)[-1]  # By default this should be 'doc'
    langs = ['en', 'zh-cn']
    for lang in langs:
        nextdir = cpath + os.sep + lang
        if not os.path.exists(nextdir):
            print('%s is not existed!' % nextdir)
            continue
        topname += os.sep + lang
        main(nextdir, topname)
