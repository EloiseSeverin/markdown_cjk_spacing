#!/usr/bin/python3
# -*- coding: utf-8 -*-
# vi:ts=4 sw=4 sts=4 tw=78 et:
# -----------------------------------------------------------------------------
import os
import shutil
import invoke

@invoke.task()
def clean(context):
    work_dirs = (
        'markdown_cjk_spacing.egg-info',
        'build', 'dist',)
    for path in work_dirs:
        if os.path.exists(path):
            shutil.rmtree(path)

@invoke.task()
def test(context):
    cmd = 'py -m unittest discover tests -v'
    context.run(cmd)

@invoke.task(test)
def build(context):
    cmd = 'setup.py sdist bdist_wheel'
    context.run(cmd)

@invoke.task(build)
def upload(context):
    cmd = 'twine upload dist/*'
    context.run(cmd)
