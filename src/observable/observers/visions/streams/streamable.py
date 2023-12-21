from abc \
    import (
        ABC,
        abstractmethod
)

from observable.observers.visions.streams.streamorder \
    import StreamOrder


class Streamable(
    ABC
):
    def __init__(
        self
    ):
        self.done: bool = False
        self.build()
        self.order: StreamOrder = StreamOrder()

    def __del__(
        self
    ):
        self.cleanup()

    def get_order(
        self
    ) -> StreamOrder:
        return self.order

    def set_order(
        self,
        value: StreamOrder
    ) -> None:
        self.order = value

    def is_done(
        self
    ) -> bool:
        return self.done

    def set_done(
        self,
        value: bool
    ) -> None:
        self.done = value

    def flag_is_done(
        self
    ) -> None:
        self.set_done(
            True
        )

    @abstractmethod
    def build(
        self
    ):
        raise NotImplemented(
            "Please implement me in class"
        )

    @abstractmethod
    def fetch(
        self
    ):
        raise NotImplemented(
            "Please implement me in class"
        )

    @abstractmethod
    def skip(self):
        raise NotImplemented(
            "Please implement me in class"
        )

    @abstractmethod
    def cleanup(
        self
    ):
        raise NotImplemented(
            "Please implement me in class"
        )

    def call_finish_event(
        self
    ) -> None:
        raise IOError(
            'Stream is finished'
        )
    