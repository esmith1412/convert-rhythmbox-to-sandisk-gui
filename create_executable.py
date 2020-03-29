import os
import PySimpleGUI as sg
import platform
import click
import pkg_resources
import PyInstaller.__main__


# To get the correct separator for the license file
os_name = platform.system()

if os_name == 'Windows':
    SEPARATOR = ';'
# Debian 10 (Buster)
else:
    SEPARATOR = ':'

# To add the version number to the executable file name
VERSION_NUM = pkg_resources.get_distribution(
    'convert-rhythmbox-to-sandisk-gui'
).version

# To get the correct paths for each required file
DIST_PATH = os.path.join(os.path.abspath('.'), 'dist')
SPEC_PATH = os.path.join(os.path.abspath('.'), 'specs')
LICENSE_PATH = os.path.join(os.path.abspath('.'), f'LICENSE{SEPARATOR}.')


# To create an executable with no external console
def create_gui():
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
    create_gui()
