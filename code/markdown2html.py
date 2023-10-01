###########################################################################
# markdown2html
# A piece of code to convert written Markdown to HTML for publishing
# Author: Rodrigo Nobrega
# 20231001
###########################################################################
__title__ = "markdown2html"
__version__ = 0.03


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
        self.split_markdown = self.split_md_contents()

    def read_markdown(self, markdown_file):
        with open(markdown_file, "r") as f:
            input_markdown = f.read()
        return input_markdown

    def write_html(self, output_file):
        with open(output_file, "w+") as f:
            f.write(self.wrap_html_with_div(self.convert_md_html()))

    def split_md_contents(self):
        positions = []
        parts = []
        position = -1  # start position
        # start marker
        while True:
            position = self.markdown.find("\n\n|", position + 1)  # find next occurrence
            if position == -1:  # if no more occurrences found, break
                break
            positions.append(position + 2)
            # position += 2
        # end marker
        while True:
            position = self.markdown.find("|\n\n", position + 1)  # find next occurrence
            if position == -1:  # if no more occurrences found, break
                break
            positions.append(position + 1)
            # position += 1
        # split them
        from_position = 0
        positions.sort()
        for marker in positions:
            parts.append(self.markdown[from_position: marker])
            from_position =  marker
        parts.append(self.markdown[marker:])
        return parts
        # return positions

    def convert_md_html(self):
        html_final = ""
        for part in self.split_markdown:
            if part[0] == "|":
                html = markdown.markdown(part, extensions=['tables'])
            else:
                html = markdown.markdown(part)
            html_final += html
        return html_final

    def wrap_html_with_div(self, html):
        wrapping = """<section id="main_content" class="inner">\n<h6>{0}</h6>\n{1}\n</section>\n"""
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
