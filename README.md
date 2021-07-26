# fstring-magic
Simple magic to interpret code cell content as a simple formatted string or as an f-string and then display formatted markdown output.

Installation:

`pip install git+https://github.com/innovationOUtside/fstring-magic.git`

To load the magic: `load_ext fstring_magic`

Two *%%block* magics are currently supported:

`%%stringformat`: pass the content of the code cell to a string formatter running in the local scope (essentially `cell.format(**shell.user_ns) )`)

`%%fstring`: treat the content of the code cell as an f-string (note this uses and `eval()` so treat with caution... Essentially runs `eval("f'''" + cell + "'''", local_ns)` 



![image](images/fstring_magic.png)

This might be useful where a notebook or markdown file is being used to author a Jupyter Book generated HTML site and inline code outputs are required in text without having to use [`glue`](https://jupyterbook.org/content/executable/output-insert.html). The code cell input should also be removed using a `remove-input` tag so that only the output formatted markdown is displayed. 

See also: [`nbextensions/python-markdown`](https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/nbextensions/python-markdown/readme.html) — _"displaying output produced by the current kernel in markdown cells"_.


TO DO: make a simple notebook pipleine processor to weave this into a Jupyter Book workflow ([related issue](https://github.com/innovationOUtside/ou-jupyter-book-tools/issues/4)). For example:

```
if cell.type=='md' and 'f-string` in tags:
  #convert cell type to 'code'
  # tag cell as `remove-input`
  # prefix code cell body with appropriate magic
```
