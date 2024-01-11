from observable.observers.visions.subscriber \
    import VisionSubscriber


class TargetingSubscriber(
    VisionSubscriber
):
    def __init__(self):
        super().__init__()

    def subscribe(
        self,
        results: list[dict]
    ) -> None:
        pass