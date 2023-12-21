from observable.observers.visions.streams.streamable \
    import Streamable

from cv2 \
    import (VideoCapture)

from PIL \
    import Image


class VideoStream(
    Streamable
):
    def __init__(
        self,
        device: str | int = 0
    ):
        super().__init__()

        self.device = device
        self.capture: VideoCapture | None = None

    def get_capture(
        self
    ) -> VideoCapture:
        if self.is_capture_empty():
            self.set_capture(
                VideoCapture(
                    self.get_device()
                )
            )

        return self.capture

    def set_capture(
        self,
        capture: VideoCapture
    ) -> None:
        self.capture = capture

    def is_capture_available(
        self
    ) -> bool:
        return self.get_capture().isOpened()

    def is_capture_empty(
        self
    ) -> bool:
        return self.capture is None

    def get_device(
        self
    ) -> str | int:
        return self.device

    def set_device(
        self,
        value: str | int
    ) -> None:
        self.capture = value

    def build(
        self
    ):
        pass

    def skip(
        self
    ):
        if self.is_done():
            self.call_finish_event()

        if self.is_capture_available():
            returnable, frame = self.get_capture().read()

            if not returnable:
                self.flag_is_done()

        return None

    def fetch(
        self
    ):
        if self.is_done():
            self.call_finish_event()

        if self.is_capture_available():
            returnable, frame = self.get_capture().read()

            if returnable:
                frame = self.get_order().pipeline(
                    frame
                )
                
                frame = Image.fromarray(
                    frame
                )
            else:
                self.flag_is_done()

            return frame
        return None

    def cleanup(
        self
    ):
        self.get_capture().release()
