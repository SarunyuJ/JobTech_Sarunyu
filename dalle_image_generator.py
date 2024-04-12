#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 14:36:04 2024

@author: sarunyu.jitsophon
"""


import os
import streamlit as st
from openai import OpenAI, OpenAIError
import webbrowser

# Streamlit app title
st.title('DALL-E Image Generator')

# Text input for user prompt
api_key = st.text_area('Enter your OPEN_API_KEY here')
#OpenAI.api_key = key
#os.envion['OPENAI_API_KEY'] = key
client = OpenAI(api_key=api_key)
#client = OpenAI()
prompt = st.text_area('Enter your prompt')

# Button to generate image based on the input prompt
if st.button('Generate Image'):
    # Check if prompt is provided
    if prompt:
        # Generate image using OpenAI DALL-E model
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            quality="standard",
            n=1,
            size="1024x1024",
        )
        # Get the image URL from the response
        image_url = response.data[0].url
        # Display the generated image
        st.image(image_url, caption='Generated Image', use_column_width=True)

        # Show image URL
        st.write(f"Image URL: {image_url}")
    
    else:
        st.warning('Please enter a prompt to generate an image.')
