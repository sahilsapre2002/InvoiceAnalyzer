from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os 
import pathlib
import textwrap
from PIL import Image

import google.generativeai as genai

secret_key= os.environ['GEMINI_API_KEY']
genai.configure(api_key=secret_key)

def get_gemini_respond(input, image, prompt):
  model = genai.GenerativeModel('gemini-pro-vision')
  response = model.generate_content([input,image[0],prompt])
  return response.text

def input_image_setup(uploaded_file):
  if uploaded_file is not None:
    bytes_data = uploaded_file.getValue()
    image_parts = [{
      "mime_type":
      uploaded_file.type, #Get the mime type of the uploaded file
      "data":bytes_data
    }]
    return image_parts
  else:



st.set_page_config(page_title="DOORLY CREATIVES Image Demo")
st.header = st.text_input("DOORLY CREATIVES")
input = st.text_input("Input Prompt:",key="input")
uploaded_file = st.file_uploader("Choose an image",type=["jpg","png","jpeg"])
image = ""
if uploaded_file is not None:
  image = Image.open(uploaded_file)
  st.image(image, caption='Uploaded Image.', use_column_width=True)

submit = st.button("Tell me about the Invoice")

