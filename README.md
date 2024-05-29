# Image Upload and Management Service

A Flask web application for uploading, listing, and managing images in a Google Cloud Storage bucket. The application uses Google Cloud Vision API to generate descriptions for uploaded images.

## Features

- Upload images to Google Cloud Storage
- Generate image descriptions using Google Cloud Vision API
- List images stored in the bucket along with their descriptions
- Delete all images from the bucket with password protection

## Prerequisites

Before you begin, ensure you have the following:

- Python 3.x installed
- Google Cloud SDK installed and configured
- A Google Cloud project with the Cloud Storage and Vision API enabled
- Service account key JSON file for accessing Google Cloud services

## Setup

1. **Clone the repository:**

    ```sh
    git clone https://github.com/FabioD99/descritor.git
    cd descritor
    ```

2. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

3. **Set up environment variables:**

    Place your service account key JSON file in the project directory and set the environment variable for Google Application Credentials:

    ```sh
    export GOOGLE_APPLICATION_CREDENTIALS="./projetocn2324-b63a93bfd3a4.json"
    ```

4. **Update configuration:**

    Open the `app.py` file and update the `BUCKET_NAME` and the delete password:

    ```python
    BUCKET_NAME = 'your-bucket-name'
    DELETE_PASSWORD = 'your_password'
    ```

## Usage

1. **Run the application:**

    ```sh
    python app.py
   
