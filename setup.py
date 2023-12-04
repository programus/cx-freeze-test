#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import sys
import os
from cx_Freeze import setup, Executable


script_path = os.path.abspath(os.path.dirname(__file__))
# start for mac
plist_items = [
    ('CFBundleExecutable', 'cx-freeze-test'),
    ('CFBundleIdentifier', 'org.programus.test.cx-freeze'),
    ('CFBundleName', 'cx-freeze-test'),
    ('CFBundleDisplayName', 'cx-Freeze Test'),
    ('CFBundleShortVersionString', '1.0.0'),
    ('NSHighResolutionCapable', 'True'),
]

bdist_mac_options = {
    'bundle_name': 'cx-freeze test',
    'plist_items': plist_items,
    # 'codesign_identity': 'Mac Developer: Yuan Wang (A2ND4G7HSM)',
}

bdist_dmg_options = {
    'volume_label': f'cx-freeze-test-1.0.0',
    'applications_shortcut': True,
}
# end for mac

build_exe_options = {
    'no_compress': True,
    'include_files': [
        'res',
    ],
    'excludes': [
    ],
    "include_msvcr": True,
}

options = {
    'bdist_mac': bdist_mac_options,
    'bdist_dmg': bdist_dmg_options,
}

base = 'Win32GUI' if sys.platform == 'win32' else None

setup(
    name='cx-freeze-test',
    version='1.0.0',
    description='',
    long_description='A tool allow you get information of multiple people from IBM BluePages',
    author='programus',
    options=options,
    py_modules=[],
    executables=[
        Executable(
            'main.py',
            base=base,
            copyright='',
            shortcut_name='cx-freeze-test',
            shortcut_dir='ProgramMenuFolder',
        )
    ]
)
