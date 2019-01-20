<!-- -*- coding: utf-8 -*- -->
<!-- ----*---------*---------*---------*---------*---------*---------*---- -->
# markdown_cjk_spacing

Markdownドキュメント中の中国語/日本語/韓国語と英単語との間にスペースを挿入
して、美しく表示する [Python-Markup][] 拡張です。

### インストール

pipでインストールします。

```
$ pip install markdown_cjk_spacing
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

[Python-Markdown]: https://github.com/Python-Markdown/markdown "Python-Markdown"
[Pelican]: https://blog.getpelican.com/ "Pelican Static Site Generator"
