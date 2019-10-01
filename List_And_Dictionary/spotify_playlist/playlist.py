playlist = {
    'title': 'Patagonia Bus',
    'author': 'colt steele',
    'songs': [
        {'title': 'song1', 'artist': ['blue'], 'duration': 2.5},
        {'title': 'song2', 'artist': ['blue', 'dj'], 'duration': 5.5},
        {'title': 'song3', 'artist': ['blue', 'dj'], 'duration': 3.2},
    ]
}

totalDuration = 0
for song in playlist['songs']:
    totalDuration += song['duration']

print(totalDuration)