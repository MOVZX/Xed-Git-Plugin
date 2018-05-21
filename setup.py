#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
xed-git-plugin
Copyright 2013 Yan-ren Tsai <elleryq@gmail.com>

This file is part of xed-git-plugin.

xed-git-plugin is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

xed-git-plugin is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with xed-plugin-ipython.  If not, see <http://www.gnu.org/licenses/>.
"""

from distutils.core import setup

setup(name='xed-git-plugin',
      version='0.1',
      description='xed plugin to show git difference',
      author='Yan-ren Tsai',
      author_email='elleryq@gmail.com',
      url='https://github.com/elleryq/xed-git-plugin',
      scripts=[],
      data_files=[
          ('lib/xed/plugins', ['git.plugin']),
          ('lib/xed/plugins/git', ['git/diffrenderer.py',
           'git/__init__.py', 'git/viewactivatable.py']),
      ]
      )
