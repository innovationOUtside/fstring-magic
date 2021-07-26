from setuptools import setup

from os import path

def get_long_description():
    with open(
        path.join(path.dirname(path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(name='fstring_magic',
      author='Tony Hirst',
      author_email='tony.hirst@open.ac.uk',
      install_requires=[],
      description='IPython fstring magic.',
      long_description=get_long_description(),
      long_description_content_type="text/markdown",
      license='MIT License',
      packages=['fstring_magic']
)
