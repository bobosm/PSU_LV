import os
import numpy as np 
import tensorflow as tf 
from tensorflow import keras 
from tensorflow.keras import layers
import matplotlib.pyplot as plt 
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

DATA_DIR_TRAIN = "C:/Users/student/Desktop/gtsrb/Train"
DATA_DIR_TEST = "C:/Users/student/Desktop/gtsrb/Test"

IMG_HEIGHT = 48
IMG_WIDTH = 48
BATCH_SIZE = 32

train_ds, val_ds = keras.utils.image_dataset_from_directory(DATA_DIR_TRAIN, validation_split=0.2, subset='both', seed=123, 
                                                            image_size=(IMG_HEIGHT, IMG_WIDTH), batch_size=BATCH_SIZE, label_mode='categorical')

test_ds = keras.utils.image_dataset_from_directory(DATA_DIR_TEST, image_size=(IMG_HEIGHT, IMG_WIDTH), batch_size=BATCH_SIZE, 
                                                   label_mode='categorical', shuffle=False)

AUTOTUNE = tf.data.AUTOTUNE
train_ds = train_ds.cache().prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)
test_ds = test_ds.cache().prefetch(buffer_size=AUTOTUNE)

model = keras.Sequential([layers.Input(shape=(IMG_HEIGHT, IMG_WIDTH, 3)), layers.Rescaling(1./255), layers.Conv2D(32, (3, 3), padding='same', activation='relu'), 
                          layers.Conv2D(32, (3, 3), padding='valid', activation='relu'), layers.MaxPooling2D(pool_size=(2, 2), strides=2), layers.Dropout(0.2),
                          layers.Conv2D(64, (3, 3), padding='same', activation='relu'), layers.Conv2D(64, (3, 3), padding='valid', activation='relu'), 
                          layers.MaxPooling2D(pool_size=(2, 2), strides=2), layers.Dropout(0.2), layers.Conv2D(128, (3, 3), padding='same', activation='relu'),
                          layers.Conv2D(128, (3, 3), padding='valid', activation='relu'), layers.MaxPooling2D(pool_size=(2, 2), strides=2), layers.Dropout(0.2),
                          layers.Flatten(), layers.Dense(512, activation='relu'), layers.Dropout(0.5), layers.Dense(43, activation='softmax')])

model.summary()

checkpoint_callback = keras.callbacks.ModelCheckpoint(filepath='L_model.keras', save_best_only=True, monitor='val_loss')

tensorboard_callback = keras.callbacks.TensorBoard(log_dir='./logs')

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

EPOCHS = 10
history = model.fit(train_ds, validation_data=val_ds, epochs=EPOCHS, callbacks=[checkpoint_callback, tensorboard_callback])

model = keras.models.load_model('L_model.keras')

loss, accuracy = model.evaluate(test_ds)
print(f"\nTočnost klasifikacije testnim podacima: {accuracy:.4f}")

preds_all = model.predict(test_ds)
y_pred = np.argmax(preds_all, axis=1)

y_true_batches = np.concatenate([labels for _, labels in test_ds], axis=0)
y_true = np.argmax(y_true_batches, axis=1)

cm = confusion_matrix(y_true, y_pred)
plt.figure(figsize=(15, 15))
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot(cmap=plt.cm.Blues, include_values=False)
plt.title("Matrica zabune za Gtsrb")
plt.show()    
