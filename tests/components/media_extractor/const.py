"""The tests for Media Extractor integration."""

AUDIO_QUERY = "bestaudio[ext]/bestaudio[ext]/bestaudio"

YOUTUBE_VIDEO = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
YOUTUBE_PLAYLIST = (
    "https://www.youtube.com/playlist?list=PLZ4DbyIWUwCq4V8bIEa8jm2ozHZVuREJP"
)
YOUTUBE_EMPTY_PLAYLIST = (
    "https://www.youtube.com/playlist?list=PLZ4DbyIWUwCq4V8bIEa8jm2ozHZVuREJO"
)

SOUNDCLOUD_TRACK = "https://soundcloud.com/bruttoband/brutto-11"

# The ytdlp code indicates formats can be none.
# This acts as temporary fixtures until a real situation is found.
NO_FORMATS_RESPONSE = "https://test.com/abc"
