import pygame
import numpy as np

def song_list():
    mp3_files = []
    pygame.mixer.init() # Initialize the Pygame mixer module for audio playback
    while len(mp3_files) <= 20:
        num = np.random.randint(1, 20)
        if num not in mp3_files:
            mp3_files.append(num)
            num_str = str(num)
            pygame.mixer.music.load('songs/' + num_str + '.mp3') # Load the specified MP3 file for playback
            pygame.mixer.music.play() # Start playing the loaded MP3 file
            while pygame.mixer.music.get_busy(): # Check if any sound is still playing
                user_input = input("Press 's' to move to next song, or 'q' to quit and repeat the playlist: ")#Also press q on the 20th song to repeat the playlist
                if user_input.lower() == 's':
                    pygame.mixer.music.stop() # Stop the currently playing MP3 file
                    break
                elif user_input.lower() == 'q':
                    pygame.mixer.music.stop() # Stop the currently playing MP3 file
                    return  # Exit the song_list() function if 'q' is entered

while True:
    song_list()
