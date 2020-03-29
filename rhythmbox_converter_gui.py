"""This module creates a GUI to enter the absolute path to the Rhythmbox
playlist folder, and then the program will create the playlist, delete all
songs missing from the playlist, and copy all new songs to the SanDisk Sansa
playlist folder.
"""

import PySimpleGUI as sg
from playlist_functions import (
    PLAYLIST_REGEX,
    get_rhythmbox_song_paths,
    get_playlist_name,
    create_sandisk_playlist,
    delete_songs_from_sandisk,
    copy_songs_to_sandisk
)


def get_rhythmbox_converter_layout():
    """To create the PySimpleGUI layout needed for the Rhythmbox playlist
    converter GUI
    """
    sg.theme('Reddit')

    return [
        [sg.Text('Please select the Rhythmbox playlist file to use:')],
        [sg.Input(key='PLAYLIST_FILE'), sg.FileBrowse()],
        [
            sg.Button(
                'Create SanDisk Sansa Playlist',
                button_color=('white', '#008000')
            ),
            sg.Cancel( button_color=('black', '#ff4040') )
        ]
    ]


def create_rhythmbox_converter_window(layout):
    """To create a PySimpleGUI window for the Rhythmbox playlist converter GUI,
    get its data, and then process it
    """
    window = sg.Window('SanDisk Sansa Playlist Creator', layout)

    while True:
        event, values = window.read()

        if event in (None, 'Cancel'):
            break

        chosen_file = values['PLAYLIST_FILE']

        if not chosen_file:
            sg.popup('You must choose a file.', title='Error Message')
        elif not PLAYLIST_REGEX.search(chosen_file):
            sg.popup(
                'You must select a valid playlist file.',
                title='Error Message'
            )
        else:
            # To create a progress bar for the program
            progress_layout = [
                [sg.Text('Creating the SanDisk Sansa playlist...')],
                [
                    sg.ProgressBar(
                        5, orientation='h', size=(20, 20), key='progbar'
                    )
                ],
                [sg.Cancel()]
            ]

            progress_window = sg.Window(
                'SanDisk Sansa Playlist Creation', progress_layout
            )

            event, values = progress_window.read(timeout=0)

            if event in ('Cancel', None):
                progress_window.close()

            song_paths = get_rhythmbox_song_paths(chosen_file)
            progress_window['progbar'].update_bar(1)

            playlist_name = get_playlist_name(chosen_file)
            progress_window['progbar'].update_bar(2)

            create_sandisk_playlist(playlist_name, song_paths)
            progress_window['progbar'].update_bar(3)

            delete_songs_from_sandisk(playlist_name, song_paths)
            progress_window['progbar'].update_bar(4)

            copy_songs_to_sandisk(playlist_name, song_paths)
            progress_window['progbar'].update_bar(5)

            # To close the window, after new playlist has been created
            progress_window.close()

            sg.popup(
                'New playlist has been created, new songs copied, and old songs deleted!',
                title='Success Message'
            )

    window.close()


# To get the layout and create the window
LAYOUT = get_rhythmbox_converter_layout()
create_rhythmbox_converter_window(LAYOUT)
