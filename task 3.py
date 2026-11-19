"""
Build a small snippet that creates three variables representing a 
Spotify playlist: playlist_title, number_of_songs, and is_public. 
Use the id() function to print the memory address of each variable."""

playlist_title = "mann mera"
number_of_songs = 7
is_public = True

print("Memory address of playlist title:", id(playlist_title))
print("Memory address of number of songs:", id(number_of_songs))
print("Memory address of is public:", id(is_public))