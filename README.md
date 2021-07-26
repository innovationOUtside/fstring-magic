# fstring-magic
Simple magic to interpret code cell content as a simple formatted string or as an f-string:

![image](https://user-images.githubusercontent.com/82988/126971355-984c5aba-b78e-4943-b6be-d6bf44eedb53.png)

This might be useful where a notebook or markdown file is being used to author a Jupyter Book generated HTML site and inline code outputs are required in text without having to use [`glue`](https://jupyterbook.org/content/executable/output-insert.html). The code cell input should also be removed using a `remove-input` tag so that only the output formatted markdown is displayed. 
