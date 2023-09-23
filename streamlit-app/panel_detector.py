import streamlit as st
import cv2
import numpy as np
import os


st.title("PANEL DETECTOR")



st.header("Select an input image:")
uploaded_image = st.file_uploader("Upload an image (JPG or PNG)", type=["jpg", "png"])

if uploaded_image is not None:
    image = cv2.imdecode(np.fromstring(uploaded_image.read(), np.uint8), 1)
    st.image(uploaded_image, caption="Original Image", use_column_width=True)

    if st.button("Generate results"):
        image_copy = image.copy()  
        hsv_image = cv2.cvtColor(image_copy, cv2.COLOR_BGR2HSV)

        lower_blue = np.array([80, 50, 50], dtype=np.uint8) 
        upper_blue = np.array([150, 255, 255], dtype=np.uint8)  

       
        blue_mask = cv2.inRange(hsv_image, lower_blue, upper_blue)

        
        inverted_mask = cv2.bitwise_not(blue_mask)

       
        output_folder = "streamlit-app/Masks"
        os.makedirs(output_folder, exist_ok=True)
        mask_output_path = os.path.join(output_folder, "blue_mask.jpg")
        cv2.imwrite(mask_output_path, inverted_mask)

        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        non_blue_mask = cv2.bitwise_not(blue_mask)

        gray_result = cv2.bitwise_and(gray_image, gray_image, mask=non_blue_mask)

        color_result = cv2.bitwise_and(image, image, mask=blue_mask)

        gray_result = cv2.cvtColor(gray_result, cv2.COLOR_GRAY2BGR)

        result_image = cv2.addWeighted(color_result, 1, gray_result, 1, 0)

        st.image(inverted_mask, caption="Mask (Black and White with Blue in Bright) ", use_column_width=True)
        st.image(result_image, caption="Mask (White for Blue, Grayscale for Others) ", use_column_width=True)

        st.success("Successful")
