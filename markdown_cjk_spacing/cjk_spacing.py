#!/usr/bin/python3
# -*- coding: utf-8 -*-
# vi:ts=4 sw=4 sts=4 tw=78 et:
# -----------------------------------------------------------------------------
"""
CJK Spacing Extension for Python-Markdown

Python markdown extension for insert a space between Chinese / Japanese /
Korean and English words, to display beautifully.
"""
import markdown

INSIDE_ELEMENTS = (
    'p', 'div', 'span', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
    'li', 'a', 'th', 'td', 'dt', 'dd'
)
SPACE = ' '
RANGE_CJK = (
    ('\u2460', '\u24ff'),           # Enclosed Alphanumerics
    ('\u3040', '\u309f'),           # Japanese Hiragana
    ('\u30a0', '\u30ff'),           # Japanese Katakana
    ('\u3400', '\u4db5'),           # CJK Unified Ideographs Extension A
    ('\u4e00', '\u9fef'),           # CJK Unified Ideographs
    ('\uf900', '\ufaff'),           # CJK Compatibility Ideographs
    ('\uff00', '\uffee'),           # Halfwidth and Fullwidth Forms
    ('\U00020000', '\U0002a6d6'),   # CJK Unified Ideographs Extension B
    ('\U0002a700', '\U0002b734'),   # CJK Unified Ideographs Extension C
    ('\U0002b740', '\U0002b81d'),   # CJK Unified Ideographs Extension D
    ('\U0002b820', '\U0002cea1'),   # CJK Unified Ideographs Extension E
    ('\U0002ceb0', '\U0002ebe0'),   # CJK Unified Ideographs Extension F
    ('\U0002f800', '\U0002fa1f'),   # CJK Compatibility Ideographs Supplement
    ('\u2700', '\u27bf'),           # Dingbats
    ('\U0001f650', '\U0001f67f'),   # Ornamental Dingbats
    ('\U0001f600', '\U0001f64f'),   # Emoticons
    ('\u2600', '\u26ff'),           # Miscellaneous Symbols
    ('\U0001f300', '\U0001f5ff'),   # Miscellaneous Symbols and Pictographs
    ('\U0001f900', '\U0001f9ff'),   # Supplemental Symbols and Pictographs
    ('\U0001f680', '\U0001f6ff'),   # Transport and Map Symbols
)
RANGE_SYMBOL = (
    ('\u0000', '\u002f'),           # space and ASCII symbols
    ('\u003a', '\u003f'),
    ('\u007b', '\u007e'),
    ('\u2010', '\u205e'),           # General Punctuation
    ('\u3000', '\u303f'),           # CJK Symbols and Punctuation
    ('\uff5b', '\uff65'),           # Halfwidth and Fullwidth Forms
    ('\u200d', '\u200d'),           # ZERO WIDTH JOINER
    ('\ufe0e', '\ufe0f'),           # VARIATION SELECTOR-15/16
)

class CjkSpaceExtension(markdown.Extension):
    """CJK Space Extension for Python-Markdown."""

    def extendMarkdown(self, md, md_globals=None):
        # Register instance with a priority.
        md.treeprocessors.register(
            CjkSpaceTreeProcessor(md), 'cjk_spacing', 5)

class CjkSpaceTreeProcessor(markdown.treeprocessors.Treeprocessor):
    """CJK Space Extension Processor."""

    def run(self, root):
        def _check_range(char, c_range):
            for start, end in c_range:
                if len(start) >= 2:     # Not supported unicode RANGE
                    next
                if start <= char <= end:
                    return True
            return False

        def _auto_spacing(text):
            prev = None
            result_text = ''
            for char in text:
                curr_cjk = _check_range(char, RANGE_CJK)
                curr_sym = _check_range(char, RANGE_SYMBOL)
                if prev:
                    prev_cjk, prev_sym = prev
                    if curr_sym or prev_sym:
                        result_text += char
                    elif prev_cjk != curr_cjk:
                        result_text += SPACE + char
                    else:
                        result_text += char
                else:
                    result_text = char
                prev = (curr_cjk, curr_sym)
            return result_text

        for e in root.iter():
            if e.text and e.tag in INSIDE_ELEMENTS:
                e.text = _auto_spacing(e.text)
            if e.tail:
                e.tail = _auto_spacing(e.tail)
        return(root)


def makeExtension(**kwargs):    # pragma: no cover
    return CjkSpaceExtension(**kwargs)
