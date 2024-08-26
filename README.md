# Handwritten-Digit-Recognition
Model Architecture: 
The model architecture includes the following layers:

1. Conv2D Layer: 32 filters with a kernel size of (3, 3), using ReLU activation. Input shape: (28, 28, 1) representing grayscale images of 28x28 pixels.

2. MaxPooling2D Layer: Pool size of (2, 2) to reduce the spatial dimensions of the output.

3. Conv2D Layer: 64 filters with a kernel size of (3, 3), using ReLU activation.

4. MaxPooling2D Layer: Pool size of (2, 2) for further dimensionality reduction.

5. Conv2D Layer: 64 filters with a kernel size of (3, 3), using ReLU activation.

6. Flatten Layer: Flattens the 2D matrices into a 1D vector to prepare for the fully connected layers.

7. Dense Layer: 64 units with ReLU activation to introduce non-linearity.

8. Dropout Layer: Dropout rate of 0.5 to prevent overfitting.

9. Dense Layer: 10 units with softmax activation to output probabilities for each digit (0-9).

Training:

The model was trained using the Adam optimizer with a categorical crossentropy loss function. It was trained for 100 epochs with a batch size of 64 and a validation split of 20%. The model achieved a strong accuracy on the test dataset, which is detailed in the repository.

Usage:
The trained model is saved as digit_recognition.keras and can be loaded for inference or further fine-tuning.

