### Welcome to soundcard
Publish your songs on github!

#### Simple Example:
```python
import soundcard as sc
soundcard1 = sc.soundcard(
  name="mysound",
  description="Short sound description.",
  author="Author/Band Name",
  filetype=".mp4/.ogg/.etc",
  sound="song_file_name_without_file_type",
  package=["directory_to_song_file","song_file_name"],
  build=True                                                           # To build the sound card so you can play the song.
)
soundcard.play("mysound")                                              # Plays the sound file.  Without file type.
```
