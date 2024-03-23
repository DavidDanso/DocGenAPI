# Document Template with FastAPI and Pyhanko Digital Signature

This repository provides a simple yet powerful document template generation and digital signing tool using FastAPI and Python. With this application, you can easily generate document templates in HTML format, convert them to PDF, preview them, and digitally sign the PDF documents.

## Features

- **HTML Template Generation**: Easily generate HTML templates using Jinja2 templating engine.
- **PDF Conversion**: Convert HTML templates to PDF documents.
- **Preview PDF Documents**: Preview generated PDF documents before signing.
- **Digital Signature**: Digitally sign PDF documents using PKCS#12 certificates.

## Project Structure

- `main.py`: FastAPI application with routings.
- `preview.py`: FastAPI router that generates a new HTML template from the data provided to the preview endpoint.
- `preview_utils.py`: Utility functions for rendering HTML templates.
- `download.py`: FastAPI router for converting an HTML template to a PDF, signing it, and providing the option to save the PDF to the file system or download it.
- `download_utils.py`: Utility functions for converting HTML to PDF.
- `sign_utils.py`: Utility functions for signing PDFs.
- `index.html`: HTML template for document generation.
- `requirements.txt`: List of project dependencies.
- `assets/`: Folder containing project assets (images, styles, etc).
- `setup.py`: Script for packaging and distributing the project.
- `README.md`: Project documentation.
  

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/DocGenAPI.git
    ```

2. Navigate into the project directory:

    ```bash
    cd DocGenAPI
    ```

3. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Unix/Linux
    .\venv\Scripts\activate    # On Windows
    ```

4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt --upgrade
    ```

2. Run the FastAPI application:

    ```
    uvicorn app.main:app --reload
    ```

3. Open your browser and go to [http://localhost:8000/docs](http://localhost:8000/docs) to interact with the API.
   

## Usage

1. **Prepare PKCS#12 Certificate**:

    You need a PKCS#12 certificate file (`test_pfx.pfx`) containing the private key and certificate for digital signing.

2. **Prepare Root Certificate**:

    You also need a root certificate file (`cert.pem`) for validation purposes.

3. **Sign PDF**:

    Update the paths to your PKCS#12 certificate (`test_pfx.pfx`) and root certificate (`cert.pem`) in the `sign_pdf()` function within the `sign_utils.py` file.

    ```python
    cms_signer = signers.SimpleSigner.load_pkcs12(pfx_file='/path/to/test_pfx.pfx', passphrase=b'your_passphrase_here')
    root_cert = load_cert_from_pemder('/path/to/cert.pem')
    ```
    
4. **Verify Signed PDF**:

    You can verify the signed PDF using any PDF viewer that supports digital signatures. Ensure that the root certificate used for signing is trusted by the viewer.

## Dependencies

- `FastAPI`: A modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
- `Jinja2`: A full-featured template engine for Python, which allows you to create HTML templates and generate HTML dynamically.
- `WeasyPrint`: A visual rendering engine for HTML and CSS that can export to PDF. Used for converting HTML templates to PDF documents.
- `PyHanko`: A library for signing and verifying PDF files in pure Python.
- `uvicorn`: A lightning-fast ASGI server, built on top of Starlette and asyncio.

## Additional Notes

- This project uses FastAPI for creating web APIs, Jinja2 for HTML templating, WeasyPrint for PDF generation, and PyHanko for PDF signing.
