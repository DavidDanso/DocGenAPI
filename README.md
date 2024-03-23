# docserve-test2

## Project Structure

- `main.py`: FastAPI application with routing.
- `preview.py`: FastAPI router that generates a new HTML template from the data provided to the preview endpoint.
- `preview_utils.py`: Utility functions for rendering HTML templates.
- `download.py`: FastAPI router for converting an HTML template to a PDF, signing it, and providing the option to save the PDF to the file system or download it.
- `download_utils.py`: Utility functions for converting HTML to PDF.
- `sign_utils.py`: Utility functions for signing PDFs.
- `index.html`: HTML template for document generation.
- `requirements.txt`: List of project dependencies.
- `assets/`: Folder containing project assets (images, styles, etc.).
- `setup.py`: Script for packaging and distributing the project.
- `README.md`: Project documentation.

## How to Run

1. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

2. Run the FastAPI application:

    ```
    uvicorn app.main:app --reload
    ```

3. Open your browser and go to [http://localhost:8000/docs](http://localhost:8000/docs) to interact with the API.

## Additional Notes

- This project uses FastAPI for creating web APIs, Jinja2 for HTML templating, WeasyPrint for PDF generation, and PyHanko for PDF signing.
