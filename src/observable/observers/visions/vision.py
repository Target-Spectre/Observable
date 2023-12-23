from observable.observers.visions.streams.streamable \
    import Streamable

from observable.observers.visions.visionModel \
    import VisionModel

from observable.observers.visions.subscriber \
    import VisionSubscriber


class Vision:
    def __init__(
        self,
        stream: Streamable | None = None,
        model: VisionModel | None = None
    ) -> None:
        self.stream: None | Streamable = stream
        self.model: VisionModel | None = model

        self.subscribers: list[VisionSubscriber] = []

    def update(
        self
    ) -> None:
        frame = self.get_stream().fetch()

    def get_stream(
        self
    ) -> Streamable | None:
        if self.is_stream_empty():
            raise IOError(
                'stream not found.'
            )

        return self.stream

    def set_stream(
        self,
        stream: Streamable | None = None
    ) -> None:
        self.stream = stream

    def is_stream_empty(
        self
    ) -> bool:
        return self.stream is None

    def is_subscribers_none(
        self
    ):
        return self.subscribers is None

    def get_subscribers(
        self
    ) -> list[VisionSubscriber]:
        if self.is_subscribers_none():
            self.set_subscribers(
                []
            )

        return self.subscribers

    def set_subscribers(
        self,
        value: list[VisionSubscriber]
    ):
        self.subscribers = value

    def get_model(
        self
    ) -> VisionModel:
        if self.is_model_empty():
            self.set_model(
                VisionModel()
            )

        return self.model

    def set_model(
        self,
        value: VisionModel
    ) -> None:
        self.model = value

    def is_model_empty(
        self
    ):
        return self.model is None
