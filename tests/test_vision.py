import tempfile

from observable.observers.visions.vision \
    import Vision

from observable.observers.visions.streams.videostream \
    import VideoStream


location_to_save_frame: str = tempfile.mkdtemp()
location_to_video: str = 'E:\\Gambithollow\\videos\\games\\Counter-Strike\\GO\\Counter-strike  Global Offensive 2023.04.06 - 22.23.42.31.mp4'


def test_vision() -> None:
    global location_to_video
    stream = VideoStream(
        device=location_to_video
    )

    vision = Vision(
        stream=stream
    )

    assert True
