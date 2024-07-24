from dotenv import load_dotenv
load_dotenv() ## load all the environment variables from .env

import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Load Gemini pro vision model
model=genai.GenerativeModel(model_name="gemini-1.5-flash")

def get_gemini_response(input,image,user_prompt):
    response=model.generate_content([input,image[0],user_prompt])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
