import PIL.Image

from observable.observers.visions.subscriber \
    import VisionSubscriber

from PIL.Image \
    import fromarray

from PIL.Image import Image
from PIL import ImageDraw

from os.path import join


def normalise_value_to_below_zero_edge(
    input_number: float
):
    output_value: float = input_number

    if input_number < 0.0:
        output_value = 0.0
    else:
        output_value = input_number

    return output_value


class LoggingSubscriber(
    VisionSubscriber
):
    def __init__(self):
        super().__init__()

        self.counter: int = 0
        self.save_at: str = "/opt/mjoelner/log"
        self.outline_predictions: bool = True

    def get_outline_predictions(
        self
    ) -> bool:
        return self.outline_predictions

    def set_outline_predictions(
        self,
        value: bool
    ) -> None:
        self.outline_predictions = value

    def increment(self) -> int:
        self.set_counter(
            self.get_counter()
            +
            1
        )

        return self.get_counter()

    def get_counter(self) -> int:
        return self.counter

    def set_counter(
        self,
        value: int
    ) -> None:
        self.counter = value

    def outline(
        self,
        image,
        prediction_boxes
    ) -> Image:
        drawing = ImageDraw.Draw(image)
        number_of_boxes = len(prediction_boxes)

        for idx in range(
            number_of_boxes
        ):
            left, top, right, bottom = prediction_boxes[idx]

            left = normalise_value_to_below_zero_edge(
                left
            )

            top = normalise_value_to_below_zero_edge(
                top
            )

            right = normalise_value_to_below_zero_edge(
                right
            )

            bottom = normalise_value_to_below_zero_edge(
                bottom
            )

            draw_shape = (left, top, right, bottom)
            drawing.rectangle(
                draw_shape,
                outline='#FFFFFF'
            )

        return image

    def subscribe(
        self,
        results: list[dict]
    ) -> None:
        size_of_results = len(
            results
        )

        for index in range(
            size_of_results
        ):
            identity = self.increment()
            selected = results[index]

            if not(
                selected['number_of_detections'] == 0
            ):
                image = selected[
                    'image'
                ]

                image = fromarray(
                    image
                )

                image = self.outline(
                    image,
                    selected['boxes']
                )

                filename = str(
                    str(identity)
                    +
                    '.jpg'
                )

                image.save(
                    str(
                        join(
                            self.save_at,
                            filename
                        )
                    )
                )


