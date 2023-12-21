from observers.visions \
    import VisionStream


class Observer:
    def __init__(
        self
    ):
        self.vision = VisionStream()

    def __del__(
        self
    ):
        pass

