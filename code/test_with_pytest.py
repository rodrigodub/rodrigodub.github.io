###########################################################################
# Testing
# A piece of code to convert written Markdown to HTML for publishing
# Author: Rodrigo Nobrega
# 20231001
###########################################################################

# import sys
# sys.path.extend(["./code/"])
from pathlib import Path
from code.markdown2html import *
# from markdown2html import *

##### markdown file
def test_existing_md_file():
    assert (Path("code") / MARKDOWN_FILE).exists()

def test_md_contents_ok():
    md = Markdown(Path("code") / MARKDOWN_FILE)
    assert md.markdown

##### html file
def test_existing_html_file():
    assert (Path("code") / HTML_FILE).exists()