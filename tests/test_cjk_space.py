#!/usr/bin/python3
# -*- coding: utf-8 -*-
# vi:ts=4 sw=4 sts=4 tw=78 et:
# -----------------------------------------------------------------------------
import os
import markdown
import unittest

EXTENSIONS = ['markdown_cjk_spacing.cjk_spacing']
TEST_FILES = (
    ('test01.md', 'output01.html'),
    ('test02.md', 'output02.html'),
    ('test03.md', 'output03.html'),
)

class CjkSpaceTest(unittest.TestCase):
    def test01_simple(self):
        md_source = '中文Chinese西文English字符Character自动Auto空格Spacing'
        expected = '<p>中文 Chinese 西文 English 字符 Character 自动 Auto' + \
            ' 空格 Spacing</p>'
        html_string = markdown.markdown(md_source, extensions=EXTENSIONS)
        self.assertEqual(html_string, expected)

    def test02_fromFile(self):
        for i, (infile, outfile) in enumerate(TEST_FILES):
            with self.subTest(i=i):
                with open(os.path.join(os.path.dirname(__file__), infile),
                          'r', encoding='utf-8') as f:
                    html_string = markdown.markdown(
                        f.read(), extensions=EXTENSIONS).replace('\n', '')
                with open(os.path.join(os.path.dirname(__file__), outfile),
                          'r', encoding='utf-8') as f:
                    expected = f.read().replace('\n', '')
                self.assertEqual(html_string, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
