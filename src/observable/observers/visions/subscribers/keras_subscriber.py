from PIL.Image \
    import Image

from observable.observers.visions.subscriber \
    import VisionSubscriber

from keras.models \
    import load_model


class KerasSubscriber(
    VisionSubscriber
):
    def __init__(
        self,
        path_to_model: str
    ):
        super().__init__()

        self.model = load_model(
            path_to_model,
            compile = False
        )

    def subscribe(
        self,
        frame: Image,
        objects: list
    ) -> None:
        pass

