"""
Creates an executable version of the Rhythmbox playlist converter GUI,
on either Debian 10 (Buster) GNU/Linux or Windows.
"""

import os
import platform
import click
import pkg_resources
import PyInstaller.__main__


# To get the correct separator for the license file
OS_NAME = platform.system()

if OS_NAME == 'Windows':
    SEPARATOR = ';'
else:
    SEPARATOR = ':'

# To add the program's version number to the executable file name
VERSION_NUM = pkg_resources.get_distribution(
    'convert-rhythmbox-to-sandisk-gui'
).version

# To get the correct paths for each required file/folder
DIST_PATH = os.path.join(os.path.abspath('.'), 'dist')
SPEC_PATH = os.path.join(os.path.abspath('.'), 'specs')
LICENSE_PATH = os.path.join(os.path.abspath('.'), f'LICENSE{SEPARATOR}.')


# To create an executable with no external console
def create_gui():
    """To make sure that the Rhythmbox playlist conveter executable is created
    with a file name that includes the program version, and has the license file
    """
    package_name = f'create_sandisk_sansa_m3u_gui_{VERSION_NUM}_no_console'

    PyInstaller.__main__.run([
        '--name=%s' % package_name,
        '--onefile',
        '--noconsole',
        '--distpath=%s' % DIST_PATH,
        '--specpath=%s' % SPEC_PATH,
        '--add-data=%s' % LICENSE_PATH,
        'rhythmbox_converter_gui.py',
    ])


# The command-line options for the script
@click.command()
def create_executable():
    """The Click script used to create the executable"""
    create_gui()
