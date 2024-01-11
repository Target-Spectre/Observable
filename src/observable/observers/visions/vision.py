from PIL.Image \
    import Image

from observable.observers.visions.streams.streamable \
    import Streamable

from observable.observers.visions.visionModel \
    import VisionModel

from observable.observers.visions.subscriber \
    import VisionSubscriber

import numpy

from math \
    import (
        ceil
)


class Vision:
    def __init__(
        self,
        stream: Streamable | None = None,
        model: VisionModel | None = None
    ) -> None:
        self.stream: None | Streamable = stream
        self.stream_is_done: bool = False

        self.width: int = 960
        self.height: int = 540

        self.model: VisionModel | None = model
        self.subscribers: list[VisionSubscriber] = []
        self.overwatch: bool = True

        self.default_settings()

    def get_overwatch(
        self
    ) -> bool:
        return self.overwatch

    def set_overwatch(
        self,
        value: bool
    ) -> None:
        self.overwatch = value

    def get_width(
        self
    ) -> int:
        return self.width

    def set_width(
        self,
        value: int
    ) -> None:
        self.width = value

    def get_height(
        self
    ) -> int:
        return self.height

    def set_height(
        self,
        value: int
    ) -> None:
        self.height = value

    def get_stream_is_done(
        self
    ) -> bool:
        return self.stream_is_done

    def set_stream_is_done(
        self,
        value: bool
    ) -> None:
        self.stream_is_done = value

    def default_settings(
        self
    ) -> None:
        if self.get_model() is None:
            self.set_model(
                VisionModel()
            )

        if self.get_overwatch():
            from observable.observers.visions.subscribers.loggingSubscriber \
                import LoggingSubscriber

            self.get_subscribers().append(
                LoggingSubscriber()
            )

    def skip(
        self
    ) -> None:
        self.get_stream().skip()

    def update(
        self
    ) -> None:
        frame = self.get_stream().fetch()

        if frame is None:
            self.set_stream_is_done(
                True
            )
            return None

        areas = self.split_into_vision_areas(
            frame
        )
        size_of_areas: int = len(
            areas
        )
        del frame

        areas = self.convert_pillow_images_into_arrays(
            areas
        )

        areas = numpy.array(
            areas
        )

        self.update_predict_on_images(
            images = areas,
            size_of_batches = size_of_areas
        )

        return None

    def update_predict_on_images(
        self,
        images: numpy.array,
        size_of_batches: int
    ) -> None:
        results: list = list()
        predictions = self.get_model().predict_on_batches(
            images
        )

        for index in range(
            size_of_batches
        ):
            image = images[index]

            boxes = self.retrieve_box_predictions(
                index,
                predictions
            )

            classes = self.retrieve_class_predictions(
                index,
                predictions
            )

            confidences = self.retrieve_confidence_predictions(
                index,
                predictions
            )

            result: dict = {
                'image': image,
                'boxes': boxes,
                'classes': classes,
                'confidences': confidences,
                'number_of_detections': len(
                    boxes
                )
            }

            results.append(
                result
            )

        self.stream_to_subscribers(
            results
        )

    def retrieve_box_predictions(
        self,
        index: int,
        predictions: numpy.array
    ) -> list:
        filtered_boxes: list = list()

        boxes = predictions['boxes'][index]
        number_of_boxes = len(
            boxes
        )

        for idx in range(
            number_of_boxes
        ):
            box = boxes[idx]
            none_value: float = -1.0

            if not (
                (box[0] == none_value)
                and
                (box[1] == none_value)
                and
                (box[2] == none_value)
                and
                (box[3] == none_value)
            ):
                filtered_boxes.append(
                    box.tolist()
                )

        return filtered_boxes

    def retrieve_confidence_predictions(
        self,
        index: int,
        predictions: numpy.array
    ):
        filtered_output: list = list()

        confidences = predictions['confidence'][index]

        size_of_confidences: int = len(
            confidences
        )

        none_value: float = -1.0

        for idx in range(
            size_of_confidences
        ):
            confidence = confidences[idx]

            if not(
                confidence == none_value
            ):
                filtered_output.append(
                    float(
                        confidence
                    )
                )

        return filtered_output

    def retrieve_class_predictions(
        self,
        index: int,
        predictions: numpy.array
    ):
        filtered_output: list = list()
        classes = predictions['classes'][index]

        size_of_classes: int = len(
            classes
        )

        for index in range(
            size_of_classes
        ):
            label: int = classes[index]

            if not(
                label == -1
            ):
                filtered_output.append(
                    int(
                        label
                    )
                )

        return filtered_output

    def stream_to_subscribers(
        self,
        results: list[dict]
    ) -> None:
        for subscriber in self.subscribers:
            subscriber.subscribe(
                results=results
            )

    def convert_pillow_images_into_arrays(
        self,
        input_images: list
    ):
        output_images = input_images
        size_of_areas = len(
            output_images
        )

        for index in range(
            size_of_areas
        ):
            area = output_images[index]
            output_images[index] = numpy.array(
                area
            )

        return output_images

    def split_into_vision_areas(
        self,
        value: Image
    ):
        output: list = list()
        width, height = (value.width, value.height)

        number_of_frames_for_width, number_of_frames_for_height = (
            width / self.get_width(),
            height / self.get_height()
        )

        for idy in range(
            int(
                ceil(
                    number_of_frames_for_height
                )
            )
        ):
            height_position: int = int(
                idy
                *
                self.height
            )
            next_height_position: int = height_position + self.height

            for idx in range(
                int(
                    ceil(
                        number_of_frames_for_width
                    )
                )
            ):
                width_position: int = int(
                    idx
                    *
                    self.width
                )
                next_width_position: int = width_position + self.width

                output.append(
                    value.crop(
                        (
                            width_position,
                            height_position,
                            next_width_position,
                            next_height_position
                        )
                    )
                )

        return output

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
