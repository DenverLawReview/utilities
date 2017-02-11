#!/usr/bin/env python3

import re
import clipboard

def clean_article(article):
    # Format footnote links so they will actually work.
    article = re.sub(r"href=\"#_ftn(\d+)\"", r'name="_ftnref\1" href="#_ftn\1"', article)
    article = re.sub(r"href=\"#_ftnref(\d+)\"", r'name="_ftn\1" href="#_ftnref\1"', article)
    # Fix quotation marks to dumb quotes
    article = re.sub(r"&lsquo;|&rsquo;", r"'", article)
    article = re.sub(r"&ldquo;|&rdquo;", r'"', article)
    # Remove sequences of two or more non-breaking spaces
    article = re.sub(r"(&nbsp;){2,}", r"", article)
    # Remove whitespace at beginnings of paragraphs
    article = re.sub(r"<p>\s+", r"<p>", article)
    # Replace <h1> tags with formatted <p> tags.
    article = re.sub(r"<h1>(.+?)</h1>", r'<p style="font-weight:bold;text-decoration:underline;text-align:center">\1</p>', article)
    # Replace <h2> tags with formatted <p> tags.
    article = re.sub(r"<h2>(.+?)</h2>", r'<p style="font-weight:bold;font-style:italic;">\1</p>', article)
    return article


if __name__ == '__main__':
    article = clipboard.paste()
    clipboard.copy(clean_article(article))
