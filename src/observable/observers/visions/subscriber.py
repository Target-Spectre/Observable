from abc \
    import (
        abstractmethod,
        ABC
    )

from PIL.Image \
    import Image


class VisionSubscriber(
    ABC
):
    def __init__(self):
        pass

    @abstractmethod
    def subscribe(
        self,
        frame: Image,
        objects: list
    ) -> None:
        raise NotImplemented(
            'Subscribe method is not implemented.'
        )

