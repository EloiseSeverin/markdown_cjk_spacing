<!-- -*- coding: utf-8 -*- -->
<!-- ----*---------*---------*---------*---------*---------*---------*---- -->
# markdown_cjk_spacing

Markdownドキュメント中の中国語/日本語/韓国語と英単語との間にスペースを挿入
して、美しく表示する [Python-Markdown][] 拡張です。

`中文Chinese西文English` は `中文 Chinese 西文 English`
に変換されます。

![build](https://travis-ci.org/EloiseSeverin/markdown_cjk_spacing.svg?branch=master)

### インストール

pipでインストールします。

```
$ pip install markdown-cjk-spacing
```

### 利用方法

[Python-Markdown][] の拡張として使用します。

```.python
import markdown

md = markdown.Markdown(extensions=["markdown_cjk_spacing.cjk_spacing"])
md.convert("markdown text")
```

または、[Pelican][] から、Markdown拡張として使用します。

```.python
# pelicanconf.py
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown_cjk_spacing.cjk_spacing': {},
    },
    'output_format': 'html5',
}
```

### セグメント分割変換

中国語/日本語文中で改行を行うと半角空白になりますが、
このスペースを削除することができます。

```.python
import markdown

md = markdown.Markdown(extensions=["markdown_cjk_spacing.cjk_spacing"],
    extension_configs={'markdown_cjk_spacing.cjk_spacing':
            {'segment_break': True}})
md.convert("markdown text")
```

[Python-Markdown]: https://github.com/Python-Markdown/markdown "Python-Markdown"
[Pelican]: https://blog.getpelican.com/ "Pelican Static Site Generator"
