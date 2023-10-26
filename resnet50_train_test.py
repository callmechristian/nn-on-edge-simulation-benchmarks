import matplotlib.pyplot as plt
import numpy as np
import PIL as image_lib
import tensorflow as tf

from keras.layers import Flatten
from keras.layers import Dense
from keras.models import Sequential
from keras.optimizers import Adam

import pathlib
import matplotlib.pyplot as plt

demo_dataset = "https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz"
directory = tf.keras.utils.get_file('flower_photos', origin=demo_dataset, untar=True)
data_directory = pathlib.Path(directory)

# train
img_height,img_width=180,180

batch_size=32

train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    data_directory,
    validation_split=0.2,
    subset="training",
    seed=123,
    label_mode='categorical',
    image_size=(img_height, img_width),
    batch_size=batch_size
    )

# val
validation_ds = tf.keras.preprocessing.image_dataset_from_directory(
    data_directory,
    validation_split=0.2,
    subset="validation",
    seed=123,
    label_mode='categorical',
    image_size=(img_height, img_width),
    batch_size=batch_size
    )



plt.figure(figsize=(10, 10))

epochs=10

for images, labels in train_ds.take(1):

  for var in range(6):

    ax = plt.subplot(3, 3, var + 1)

    plt.imshow(images[var].numpy().astype("uint8"))

    plt.axis("off")

# # inspect data
# plt.show() # uncomment to inspect 6 random data samples in the training set

# pretrained model
demo_resnet_model = Sequential()

pretrained_model_for_demo= tf.keras.applications.ResNet50(include_top=False,
                                                        input_shape=(180,180,3),
                                                        pooling='avg',classes=5,
                                                        weights='imagenet'
                                                        )

for each_layer in pretrained_model_for_demo.layers:
        each_layer.trainable=False

demo_resnet_model.add(pretrained_model_for_demo)

# add some layers
demo_resnet_model.add(Flatten())
demo_resnet_model.add(Dense(512, activation='relu'))
demo_resnet_model.add(Dense(5, activation='softmax'))

# train
demo_resnet_model.compile(optimizer=Adam(lr=0.001),loss='categorical_crossentropy',metrics=['accuracy'])
history = demo_resnet_model.fit(train_ds, validation_data=validation_ds, epochs=epochs)

# analyse
plt.figure(figsize=(8, 8))
epochs_range= range(epochs)

plt.plot( epochs_range, history.history['accuracy'], label="Training Accuracy")
plt.plot(epochs_range, history.history['val_accuracy'], label="Validation Accuracy")
plt.axis(ymin=0.4,ymax=1)
plt.grid()
plt.title('Model Accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epochs')
plt.legend(['train', 'validation'])