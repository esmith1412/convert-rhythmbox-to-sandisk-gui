from setuptools import setup, find_packages

setup(
    name='convert-rhythmbox-to-sandisk-gui',
    version='1.0.0.dev1',
    description='A GUI application that takes an M3U playlist exported from Rhythmbox, and converts it to a format that can be read by the SanDisk Sansa music player, running Rockbox firmware',
    url='https://github.com/esmith1412/convert-rhythmbox-to-sandisk-gui',
    author='Elijah Smith',
    license='GNU GPLv3',
    packages=find_packages(),
    entry_points='''
        [console_scripts]
        create_executable=create_executable:create_executable
    ''',
    classifiers=[
        "Programming Language :: Python :: 3.7",
        'Development Status :: 3 - Alpha',
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows :: Windows 10"
    ],
    python_requires='~=3.7.3'
)
