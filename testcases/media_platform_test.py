from utilities.media_platform import MediaPlatform

def test_media_platform(core):
    for item in core.get_mps():
        media_platform = MediaPlatform(**item)
        print(media_platform)
