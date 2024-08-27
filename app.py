import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image, ImageOps
from streamlit_drawable_canvas import st_canvas

model = tf.keras.models.load_model('digit_recognition.h5')

st.title("Handwritten Digit Recognition")
st.write("Draw a digit (0-9) in the canvas below: (Try it in centre)")

canvas_result = st_canvas(
    fill_color="white",  
    stroke_width=10,     
    stroke_color="black",
    background_color="white", 
    height=250,          
    width=250,           
    drawing_mode="freedraw",  
    key="canvas"
)

if(st.button("Click to predict")):
    if canvas_result.image_data is not None:
        image = Image.fromarray(np.uint8(canvas_result.image_data))
        image = ImageOps.grayscale(image)
        image = image.resize((28, 28))
        image = ImageOps.invert(image)
        image_array = np.array(image).astype('float32') / 255
        image_array = image_array.reshape(1, 28, 28, 1)
        prediction = model.predict(image_array)
        predicted_digit = np.argmax(prediction)
        st.write(f"Predicted Digit: {predicted_digit}")