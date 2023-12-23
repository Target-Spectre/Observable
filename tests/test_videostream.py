from observable.observers.visions.streams.videostream \
    import VideoStream

from tests.static_paths \
    import device_path_to_file

from os import path

import tempfile

location_to_save_frame: str = tempfile.mkdtemp()
print(location_to_save_frame)

def test_videostream():
    global location_to_save_frame
    stream = VideoStream(
        device=device_path_to_file
    )

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

