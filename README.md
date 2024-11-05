# Custom Canopy Mockup Generator API

This project is an API built with **FastAPI** for generating customized canopy mockups. Users can upload a logo, specify a background color, and add custom text to create mockups of canopies. The generated images are stored on the server and are available for download as a ZIP file.

## Features

- Accepts user-provided logo, background color (BGR format), and optional text.
- Overlays these inputs onto predefined canopy mockups.
- Saves generated mockup images in a directory for access.
- Provides a downloadable ZIP file with all generated mockups.

## Prerequisites

1. **Python 3.9+**  
   Ensure Python 3.9 or higher is installed on your system.

2. **Virtual Environment (Recommended)**  
   It's recommended to use a virtual environment to manage dependencies.

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd custom-canopy-mockup-generator
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies** Use the `requirements.txt` file to install all required dependencies.

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Server

To run the FastAPI server, use Uvicorn or FastApi:

```bash
# Using uvicorn
uvicorn app.main:app --reload 
# Using fastapi
fastapi dev app/main.py
```

### API Endpoints

#### 1. `POST /create-mockups/`

**Description**: Creates customized mockups with the provided logo, color, and optional text.

- **Parameters**:
  - `color` (str, optional): string representing the BGR color (e.g., `"[255, 0, 0]"` for blue). Defaults to white
  - `text` (str, optional): Custom text to overlay. Defaults to the empty string.
  - `logo` (file): PNG file to use as the logo overlay.

#### 2. `GET /images/`

**Description**: Retrieves a ZIP file containing all generated mockup images.

- **Response**: A downloadable ZIP file named `images.zip`.


