from ai_library import ask_ai
import glob
import base64
import os

files = glob.glob("images/*.jpg")
files += glob.glob("images/*.png")

for file in files:
    with open(file, "rb") as f:
        base64_encoded = base64.b64encode(f.read()).decode('utf-8')
        
        # Determine the image file type (e.g., png, jpeg)
        file_extension = file.split('.')[-1].lower()
        mime_type = f"image/{file_extension}"
        
        # Create the Base64 data URL
        data_url = f"data:{mime_type};base64,{base64_encoded}"
    

    # data_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"

    prompt = f"Please read and analysis the image content. Then suggest a filename from this image. Only return the filename without any other text."
    response = ask_ai(prompt, image_url=data_url, model="openai/gpt-4o-mini")
    print(f"Image: {file}")
    print(f"Suggested filename: {response}")

    # rename the file
    new_filename = response.strip()
    os.rename(file, os.path.join("images", new_filename))
    print(f"Renamed {file} to {new_filename}")

    #prompt2 = f"Please read and analysis the image content."
    #response = ask_ai(prompt2, image_url=data_url, model="openai/gpt-4o-mini")
    #print(f"Analysis result: {response}")