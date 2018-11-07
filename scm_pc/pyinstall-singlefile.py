# -*- coding: utf-8 -*-

import os

if __name__ == '__main__':
    from PyInstaller.__main__ import run
    opts = ['-F', '-w', '--paths=E:\\Python\\Lib\\site-packages\\PyQt5\\Qt\\bin',
            '--paths=E:\\Python\\Lib\\site-packages\PyQt5\\Qt\\plugins',
            '--paths=E:\\PythonWork\\IChenfan_GUI\\scm_pc',
            'ScmGui.py']
    run(opts)

