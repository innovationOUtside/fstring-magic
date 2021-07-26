from IPython.core.magic import magics_class, line_cell_magic, Magics
from IPython.core.magic import needs_local_scope
from IPython.display import display, Markdown

@magics_class
class fstringMagic(Magics):
    def __init__(self, shell, cache_display_data=False):
        super(fstringMagic, self).__init__(shell)

    @line_cell_magic
    def stringformat(self, line, cell):
        """Treat code cell content as f-string."""
        return display(Markdown(cell.format(**self.shell.user_ns)))

    @line_cell_magic
    @needs_local_scope
    def fstring(self, line, cell, local_ns):
        """Treat code cell content as f-string."""
        return display(Markdown(eval("f'''" + cell + "'''", local_ns)))
