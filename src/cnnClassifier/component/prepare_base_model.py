import tensorflow as tf
from cnnClassifier.config.configuration import PrepareBaseModelConfig
from pathlib import Path

class PrepareBaseModel:
    """
    To configure the parameters and train the model
    """
    def __init__(self, config: PrepareBaseModelConfig):
        self.config = config

    # Creates model by putting already set params and saves it
    def get_base_model(self):
        self.model = tf.keras.applications.vgg16.VGG16(
            input_shape=self.config.params_image_size,
            weights=self.config.params_weights,
            include_top=self.config.params_include_top
        )

        self.save_model(path=self.config.base_model_path, model=self.model)

    @staticmethod
    def prepare_full_model(model, classes, freeze_all, freeze_till, learning_rate):
        # Takes the model, classes, and main parameters up to what layer we want to freeze the base model
        # and eventually returns the full compiled model
        if freeze_all:
            for layer in model.layers:
                layer.trainable = False
        elif (freeze_all is not None and freeze_till>0):
            for layer in model.layers:
                layer.trainable = False

        flatten_in = tf.keras.layers.Flatten()(model.output)
        prediction = tf.keras.layers.Dense(units=classes, activation="softmax")(flatten_in)

        full_model = tf.keras.models.Model(inputs=model.input, outputs=prediction)

        return full_model


    # Taking the base model and making our own architecture on top of it
    def update_base_model(self):
        self.full_model = self.prepare_full_model(
            model = self.model,
            classes = self.config.params_classes,
            freeze_all=True,
            freeze_till=False,
            learning_rate=self.config.params_learning_rate
        )

        self.save_model(path=self.config.updated_base_model_path, model=self.full_model)

        self.full_model.compile(optimizer=tf.keras.optimizers.SGD(learning_rate=self.config.params_learning_rate),
                           loss=tf.keras.losses.CategoricalCrossentropy(),
                           metrics=['accuracy'])
        self.full_model.summary()
        self.save_model(path=self.config.updated_base_model_path, model=self.full_model)

    # To save the model at the path
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)