# coding:utf-8
# _author_:Junjie
# date:2018/11/6
from distutils.core import setup
from Cython.Build import cythonize

setup(name='command_node',ext_modules=cythonize("./command_node.py"))