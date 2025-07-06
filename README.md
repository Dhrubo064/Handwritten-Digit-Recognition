# Handwritten Digit Recognition

🚀 Excited to Share My Latest Project! 🚀

I've built and deployed a Handwritten Digit Recognition app using Streamlit! This app leverages TensorFlow and deep learning to accurately recognize handwritten digits (0-9). The model is based on a Convolutional Neural Network (CNN) and trained on the MNIST dataset.

## Demo

https://handwritten-digit-recognition-by-diganta-das-droba.streamlit.app/

## Tech Stack

1. Streamlit
2. TensorFlow
3. Keras
4. MNIST Dataset

## Model Architecture

1. Conv2D Layer: 32 filters, kernel size (3, 3), ReLU activation, input shape (28, 28, 1)
2. MaxPooling2D Layer: Pool size (2, 2)
3. Conv2D Layer: 64 filters, kernel size (3, 3), ReLU activation
4. MaxPooling2D Layer: Pool size (2, 2)
5. Conv2D Layer: 64 filters, kernel size (3, 3), ReLU activation
6. Flatten Layer: Converts 2D matrices to 1D vector
7. Dense Layer: 64 units with ReLU activation
8. Dropout Layer: 0.5 dropout rate to prevent overfitting
9. Dense Layer: 10 units, softmax activation for digit prediction (0-9)

## Training

-> Optimizer: Adam

-> Loss Function: Categorical Crossentropy

-> Epochs: 100

-> Batch Size: 64

-> Validation Split: 20%

The model achieves strong accuracy on the test dataset.

## Usage

The trained model is saved as digit_recognition.keras and can be loaded for inference or further fine-tuning.

I'm thrilled with the learning experience this project provided and excited to dive deeper into the world of machine learning and AI!
