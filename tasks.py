#!/usr/bin/python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
import os
import glob
import re
import shutil
import logging
import invoke

logging.basicConfig(level=logging.INFO, format='%(levelname)s %(message)s')
logger = logging.getLogger(name=__name__)


@invoke.task()
def config(context):
    """Setup config."""
    c = context.config
    c.curdir = os.path.dirname(__file__)
    # c.logfile = os.path.join(c.curdir, 'tasks.log')
    # c.dist_dir = os.path.join(c.curdir, 'dist')


@invoke.task(config)
def autopep8(context):
    """Automatically formats Python code."""
    c = context.config
    context.run(f'autopep8 -r -i {c.curdir}')


@invoke.task(config)
def beautify(context):
    """Automatically formats html/css code"""
    c = context.config
    for fname in glob.glob('**/*.css') + glob.glob('**/*.html') + glob.glob('**/*.js'):
        if re.match(r'tests\\output\d+.html', fname):
            continue
        context.run(f'js-beautify --editorconfig -r {fname}')


@invoke.task(config, autopep8, beautify)
def clean(context):
    """Clean work folders."""
    c = context.config
    if 'logfile' in c.keys() and os.path.exists(c.logfile):
        os.unlink(c.logfile)
    for p in glob.glob('**/__pycache__'):
        shutil.rmtree(p, ignore_errors=True)
    workdirs = (
        'markdown_cjk_spacing.egg-info', 'build', 'dist',)
    for path in workdirs:
        if os.path.exists(path):
            shutil.rmtree(path)


@invoke.task()
def test(context):
    """Unit test"""
    c = context.config
    logfile = ""
    if 'logfile' in c.keys():
        logfile = f'>{c.logfile} 2>&1'
    cmd = f'py -m unittest discover tests -v {logfile}'
    context.run(cmd)


@invoke.task(test)
def build(context):
    cmd = 'setup.py sdist bdist_wheel'
    context.run(cmd)


@invoke.task(build)
def upload(context):
    cmd = 'twine upload dist/*'
    context.run(cmd)


if __name__ == '__main__':
    invoke.run('invoke -l')
