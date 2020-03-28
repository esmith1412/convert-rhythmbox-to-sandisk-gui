import os
import re
import shutil
import pprint
import PySimpleGUI as sg


# To get the path from inside the SanDisk Sansa player itself
SANDISK_ROOT_PATH = '/<microSD1>/SD CARD MUSIC/'
# To get the path from the laptop
SANDISK_PC_PATH = '/media/elijah/16GB Rockbo/SD CARD MUSIC/'
MUSIC_PATH = '/home/elijah/Music/'
# To get the playlist name from its file path
PLAYLIST_REGEX = re.compile('Favorites|Anime|Instrumentals_Soundtrack|Rap')


# To get the absolute paths for all the songs in a given playlist, in order
def get_rhythmbox_song_paths(playlist_file_path):
    song_paths = []

    with open(playlist_file_path) as playlist_file:
        for line in playlist_file.readlines():

            if not line.startswith('#EXTINF') \
            and not line.startswith('#EXTM3U'):
                song_paths.append(
                    os.path.join(
                        os.path.dirname(playlist_file_path), line.strip()
                    )
                )
            else:
                continue

    return song_paths


def get_playlist_name(playlist_file_path):
    return PLAYLIST_REGEX.search(
        'Favorites|Anime|Instrumentals_Soundtrack|Rap', playlist_file_path
    ).group()


def create_sandisk_playlist(playlist_name, song_paths):
    playlist_file_name = f'{playlist_name}_sandisk.m3u'
    playlist_folder_path = os.path.join(SANDISK_ROOT_PATH, playlist_name)

    # TODO: Put the actual path on the SanDisk player where playlist
    # is currently saved
    with open(playlist_file_name, 'w') as sandisk_playlist_file:
        for song_path in song_paths:
            song_file_name = os.path.basename(song_path)

            sandisk_playlist_file.write(
                f'{os.path.join(playlist_folder_path, song_file_name)}\n'
            )


# To delete any songs that are not in the playlist, but in its folder
def delete_songs_from_sandisk(playlist_name, song_paths):
    song_files = [os.path.basename(song_path) for song_path in song_paths]

    sandisk_playlist_folder = os.path.join(SANDISK_PC_PATH, playlist_name)

    try:
        for song in os.listdir(sandisk_playlist_folder):
            sandisk_song_path = os.path.join(sandisk_playlist_folder, song)

            if song not in song_files:
                #os.remove(sandisk_song_path)
                print(sandisk_song_path)
            else:
                continue
    except FileNotFoundError:
        sg.popup(
            'SanDisk Sansa Player is not available. Please try again.',
            title='Error Message'
        )


# To copy any songs that are in the playlist, but not the folder
def copy_songs_to_sandisk(playlist_name, song_paths):
    sandisk_playlist_folder = os.path.join(SANDISK_PC_PATH, playlist_name)

    for song_path in song_paths:
        sandisk_song_path = os.path.join(
            sandisk_playlist_folder, os.path.basename(song_path)
        )

        # To copy any songs that are not in the playlist folder
        try:
            if not os.path.isfile(sandisk_song_path):
                #shutil.copy(song_path, sandisk_playlist_folder)
                print(song_path, sandisk_playlist_folder)
            else:
                continue
        except FileNotFoundError:
            sg.popup(
                'SanDisk Sansa Player is not available. Please try again.',
                title='Error Message'
            )


#song_paths = get_rhythmbox_song_paths('/home/elijah/Music/Anime_rhythmbox.m3u')
#playlist_name = get_playlist_name('/home/elijah/Music/Anime_rhythmbox.m3u')
#create_sandisk_playlist(playlist_name, song_paths)
#delete_songs_from_sandisk(playlist_name, song_paths)
#copy_songs_to_sandisk(playlist_name, song_paths)
