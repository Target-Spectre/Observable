from observable.observers.visions.streams.videostream \
    import VideoStream

from os import path


def test_videostream():
    device_path_to_file: str = 'E:\\Gambithollow\\videos\\games\\Counter-Strike\\GO\\Artifacts\\Counter-strike  Global Offensive 2023.09.24 - 02.12.13.13.mp4'

    stream = VideoStream(
        device=device_path_to_file
    )

    location_to_save_frame: str = 'D:\\Outputs'
    counter: int = 0

    while stream.is_capture_available():
        counter = counter + 1

        frame = stream.fetch()

        frame.save(
            path.join(
                location_to_save_frame,
                str(str(counter) + '.jpg'))
        )

        if counter >= 100:
            break

    assert True

