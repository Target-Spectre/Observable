from observable.observers.visions.vision \
    import Vision

from observable.observers.visions.streams.videostream \
    import VideoStream


def test_observable():
    vision = Vision()

    vision.set_stream(
        VideoStream('/opt/predict_on/2.mp4')
    )

    while True:
        if vision.get_stream_is_done():
            break

        vision.update()

    assert True
