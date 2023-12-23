from cv2 import (
    cvtColor,
    COLOR_BGR2RGB,
    COLOR_BGR2GRAY
)


class StreamOrder:
    def __init__(
        self
    ):
        self.ordering: int = 1

    def pipeline(
        self,
        frame
    ):
        if self.flag_convert_to_rgb():
            frame = cvtColor(
                frame,
                COLOR_BGR2RGB
            )

        if self.flag_convert_to_gray():
            frame = cvtColor(
                frame,
                COLOR_BGR2GRAY
            )

        return frame

    def flag_convert_to_rgb(self):
        return self.get_ordering() == 1

    def flag_convert_to_gray(self):
        return self.get_ordering() == 10

    def flag_convert_to_g(self):
        return self

    def get_ordering(
        self
    ) -> int:
        return self.ordering

    def set_ordering(
        self,
        value: int
    ) -> None:
        self.ordering = value
