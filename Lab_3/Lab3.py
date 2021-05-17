import matplotlib.pyplot as plt
from sklearn import datasets, svm, metrics

# Завантаження даних
digits = datasets.load_digits()
images_and_labels = list(zip(digits.images, digits.target))

# Виведення даних тренування
for index, (image, label) in enumerate(images_and_labels[:8]):
    plt.subplot(2, 8, index + 1)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Train: %i' % label)

# Попередня обробка даних
n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))

# Навчання і тренування моделі розпізнавання даних
classifier = svm.SVC(gamma=0.001)
classifier.fit(data[:n_samples // 2], digits.target[:n_samples // 2])

# Прогнозовані значення
expected = digits.target[n_samples // 2:]
predicted = classifier.predict(data[n_samples // 2:])

# Виведення класифікатора тесту і матриці неточностей
print("Classification report for classifier %s:\n%s\n" % (classifier, metrics.classification_report(expected, predicted)))
print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))

# Виведення прогнозованих даних
images_and_predictions = list(zip(digits.images[n_samples // 2:], predicted))
for index, (image, prediction) in enumerate(images_and_predictions[:8]):
    plt.subplot(2, 8, index + 9)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Predict:%i' % prediction + "  ")

plt.show()