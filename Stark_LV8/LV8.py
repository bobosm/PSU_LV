from tensorflow import keras
from tensorflow.keras import layers, models, callbacks
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import confusion_matrix, accuracy_score, ConfusionMatrixDisplay
import numpy as np
import matplotlib.pyplot as plt

#zadatak 1

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

x_train_s = x_train.reshape(-1, 28, 28, 1) / 255.0
x_test_s = x_test.reshape(-1, 28, 28, 1) / 255.0

y_train_s = to_categorical(y_train, num_classes=10)
y_test_s = to_categorical(y_test, num_classes=10)

model = models.Sequential([
    layers.Input(shape=(28, 28, 1)),
    layers.Conv2D(32, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
    ])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

tensorboard_callback = callbacks.TensorBoard(log_dir='./logs')

checkpoint_callback = callbacks.ModelCheckpoint(
    filepath='najbolji_model_mnist.keras',
    save_best_only=True,
    monitor='val_accruracy',
    mode='max',
    verbose=1
    )

EPOCHS = 5
history = model.fit(
    x_train_s, y_train_s,
    epochs=EPOCHS,
    batch_size=32,
    validation_split=0.1,
    callbacks=[tensorboard_callback, checkpoint_callback]
    )

najbolji_model = keras.models.load_model('najbolji_model_mnist.keras')

print("Evaluacija:\n")

loss_train, acc_train = najbolji_model.evaluate(x_train_s, y_train_s, verbose=0)
print(f"Točnost na skupui za učenje: {acc_train:.4f}\n")

loss_test, acc_test = najbolji_model.evaluate(x_test_s, y_test_s, verbose=0)
print(f"Točnost na skupu za testiranje: {acc_test:.4f}\n")

print("Matrica zabune:")
y_test_pred = najbolji_model.predict(x_test_s)
y_test_pred_classes = np.argmax(y_test_pred, axis=1)
y_test_true_classes = np.argmax(y_test_s, axis=1)

cm_test = confusion_matrix(y_test_true_classes, y_test_pred_classes)

plt.figure(figsize=(8, 6))
disp_test = ConfusionMatrixDisplay(confusion_matrix=cm_test)
disp_test.plot(cmap=plt.cm.Blues)
plt.title("Matrica zabune - Testni skup")
plt.show()

y_train_pred = najbolji_model.predict(x_train_s)
y_train_pred_classes = np.argmax(y_train_pred, axis=1)
y_train_true_classes = np.argmax(y_train_s, axis=1)

cm_train = confusion_matrix(y_train_true_classes, y_train_pred_classes)

plt.figure(figsize=(8, 6))
disp_train = ConfusionMatrixDisplay(confusion_matrix=cm_train)
disp_train.plot(cmap=plt.cm.Greens)
plt.title("Matrica zabune - Skup za učenje")
plt.show()