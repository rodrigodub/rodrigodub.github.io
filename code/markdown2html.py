###########################################################################
# markdown2html
# A piece of code to convert written Markdown to HTML for publishing
# Author: Rodrigo Nobrega
# 20231001
###########################################################################
__title__ = "markdown2html"
__version__ = 0.02


# import libraries
import datetime
import markdown


# global variables
MARKDOWN_FILE = "input_markdown.md"
HTML_FILE = "output_html.html"


# Class name
class Markdown(object):
    """
    Documentation
    """
    def __init__(self, markdown_file):
        self.markdown = self.read_markdown(markdown_file)

    def read_markdown(self, markdown_file):
        with open(markdown_file, "r") as f:
            input_markdown = f.read()
        return input_markdown

    def write_html(self, output_file):
        with open(output_file, "w+") as f:
            f.write(self.wrap_html_with_div(self.convert_md_html()))

    def convert_md_html(self):
        html = markdown.markdown(self.markdown)
        return html

    def wrap_html_with_div(self, html):
        wrapping = """
        <section id="main_content" class="inner">
            <h6>{0}</h6>
            {1}
        </section>
        """
        return wrapping.format(datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S"),
                               html)


# main loop
def main():
    # header --------------------------------------------------------------
    print(f'\n{75 * "="}')
    print(f'{f"{__title__} v.{__version__}":^75}')
    print(f'{75 * "="}\n')
    # ---------------------------------------------------------------------
    # main code goes here
    print("Reading MarkDown")
    md = Markdown(MARKDOWN_FILE)
    print("Writing HTML")
    md.write_html(HTML_FILE)
    print("OK")
    #
    # footer --------------------------------------------------------------
    print(f'\n{34 * "="}  OK  {35 * "="}\n')


# test loop
def test():
    # header --------------------------------------------------------------
    print(f'\n{75 * "="}')
    print(f'{"TEST":^75}')
    print(f'{f"{__title__} v.{__version__}":^75}')
    print(f'{75 * "="}\n')
    # ---------------------------------------------------------------------
    # test code goes here
    #
    # footer --------------------------------------------------------------
    print(f'\n{34 * "="}  OK  {35 * "="}\n')


# main, calling main loop
if __name__ == '__main__':
    main()
    # test()
