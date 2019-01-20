#!/usr/bin/python3
# -*- coding: utf-8 -*-
# vi:ts=4 sw=4 sts=4 tw=78 et:
# -----------------------------------------------------------------------------
import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='markdown_cjk_spacing',
    version='0.1.0',
    author='Eloise Severin',
    author_email='Eloise.severin @ gmail.com',
    description='Python markdown extension for insert a space between Chinese / Japanese / Korean and English words',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/EloiseSeverin/markdown_cjk_spacing/',
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    install_requires=['Markdown>=3.0.0'],
    test_suite='tests',
    packages=['markdown_cjk_spacing'],
    keywords=['Markdown', 'extension', 'plugin', 'CJK'],
    entry_points={
        'markdown.extensions': [
            'cjk_spacing = markdown_cjk_spacing.cjk_spacing:CjkSpaceExtension']
    },
)
