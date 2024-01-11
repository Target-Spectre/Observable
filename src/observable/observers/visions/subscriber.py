from abc \
    import (
        abstractmethod,
        ABC
    )


class VisionSubscriber(
    ABC
):
    def __init__(
        self
    ):
        super().__init__()

    @abstractmethod
    def subscribe(
        self,
        results: list[dict]
    ) -> None:
        raise NotImplemented(
            'Subscribe method is not implemented.'
        )

