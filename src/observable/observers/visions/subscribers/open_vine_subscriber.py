from PIL.Image \
    import Image

from observable.observers.visions.subscriber \
    import VisionSubscriber


class OpenVineSubscriber(
    VisionSubscriber
):
    def __init__(
        self
    ):
        super().__init__()

    def subscribe(
        self,
        frame: Image,
        objects: list
    ) -> None:
        pass
