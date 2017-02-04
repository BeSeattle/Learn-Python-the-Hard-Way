# -*- coding: utf-8 -*-
from __future__ import unicode_literals
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description': 'my project',
        'author': 'BeSeattle',
        'url': 'uphlk.com',
        'download_url':'Where to download it.',
        'author_email':'My email',
        'version':'0.1',
        'install_requires':['nose'],
        'packages':['NAME'],
        'scripts':[],
        'name':'projectname'
}
# 'description':关于该模块的单行描述
# 'author':模块作者
# 'url':模块主页
# 'download_url':模块下载链接
# 'author_email':作者电邮
# 'version':模块版本号
# 'install_requires':此模块依赖的模块,
# 'packages':告诉distutils需要处理的包
# 'scripts':指定源码文件，可从命令行执行
# 'name':模块名
setup(**config)
