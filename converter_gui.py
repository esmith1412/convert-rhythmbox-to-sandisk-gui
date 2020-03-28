import PySimpleGUI as sg
import re
from playlist_functions import (
    get_rhythmbox_song_paths,
    get_playlist_name,
    create_sandisk_playlist,
    PLAYLIST_REGEX
)


sg.theme('Reddit')

layout = [
    [sg.Text('Please select the Rhythmbox playlist file to add:')],
    [sg.Input(key='PLAYLIST_FILE'), sg.FileBrowse()],
    [
        sg.Button( 'Create Playlist', button_color=('white', '#008000') ),
        sg.Cancel( button_color=('black', '#ff4040') )
    ]
]

window = sg.Window('SanDisk Sansa Playlist Creator', layout)

while True:
    event, values = window.read()

    if event in (None, 'Cancel'):
        break
    else:
        chosen_file = values['PLAYLIST_FILE']

        if not chosen_file:
            sg.popup('You must choose a file.', title='Error Message')
            continue
        elif not PLAYLIST_REGEX.search(chosen_file):
            sg.popup(
                'You must select a valid playlist file.',
                title='Error Message'
            )
            continue
        else:
            song_paths = get_rhythmbox_song_paths(chosen_file)
            playlist_name = get_playlist_name(chosen_file)
            #create_sandisk_playlist(playlist_name, song_paths)
            #delete_songs_from_sandisk(playlist_name, song_paths)
            #copy_songs_to_sandisk(playlist_name, song_paths)

window.close()
