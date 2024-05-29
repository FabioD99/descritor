from flask import Flask, request, render_template, redirect, url_for
from google.cloud import storage, vision
import os

app = Flask(__name__)

DELETE_PASSWORD = "vaideralo"

# Initialize Google Cloud clients
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./projetocn2324-b63a93bfd3a4.json"
storage_client = storage.Client()
vision_client = vision.ImageAnnotatorClient()

# Define your bucket name
BUCKET_NAME = 'visionapiimage'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', error='No file part in the request')

        file = request.files['file']

        if file.filename == '':
            return render_template('index.html', error='No file selected for uploading')

        if file:
            # Process the image with Google Vision API
            descriptions, image_url = process_image(file)

            return render_template('index.html', descriptions=descriptions, image_url=image_url)

    return render_template('index.html')

def process_image(file):
    # Process the image with Google Vision API
    content = file.read()
    image = vision.Image(content=content)
    response = vision_client.label_detection(image=image)
    labels = response.label_annotations
    descriptions = [label.description for label in labels]

    # Upload the image to the bucket as a JPEG file
    bucket = storage_client.bucket(BUCKET_NAME)
    blob = bucket.blob(file.filename)
    blob.upload_from_string(content, content_type='image/jpeg')

    # Add metadata to the blob
    blob.metadata = {'descriptions': ', '.join(descriptions)}
    blob.patch()
    blob.make_public()
    # Get the public URL of the uploaded image
    image_url = blob.public_url

    return descriptions, image_url


if __name__ == '__main__':
    app.run(debug=True)
