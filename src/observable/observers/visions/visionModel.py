import keras
import keras_cv

from keras.saving \
  import load_model

from keras.optimizers           \
  import                        \
  SGD

from numpy \
    import array


class VisionModel:
    def __init__(
        self,
        path_to_model: str = '/opt/mjoelner/model.keras'
    ):
        self.model = load_model(
            path_to_model,
            compile = False
        )

        self.verbosity: int = 0
        self.build()

    def build(
        self
    ) -> None:
        optimizer = SGD(
            learning_rate   = 0.0,
            global_clipnorm = 0.0,
            use_ema         = True
        )

        self.get_model().compile(
            classification_loss = 'binary_crossentropy',
            box_loss            = 'ciou',
            optimizer           = optimizer
        )

    def predict_on_batches(
        self,
        values: array
    ) -> array:
        predictions = self.get_model().predict(
            values,
            verbose = self.get_verbosity()
        )

        return predictions

    def get_model(
        self
    ):
        return self.model

    def set_model(
        self,
        value
    ):
        self.model = value

    def get_verbosity(
        self
    ) -> int:
        return self.verbosity

    def set_verbosity(
        self,
        value: int
    ) -> None:
        self.verbosity = value
