import os
import asyncio
from fastapi import APIRouter, status
from fastapi.responses import FileResponse, JSONResponse
from .download_utils import convert_html_to_pdf
from .sign_utils import sign_pdf

router = APIRouter(prefix='/download-pdf')

@router.get("/", status_code=status.HTTP_200_OK)
async def download_endpoint():
    try:
        # Display message to let the user know what's going on
        print("Converting HTML to PDF...")

        # Call the convert_html_to_pdf function from the first code
        convert_html_to_pdf()

        # Wait for 3 seconds
        await asyncio.sleep(1)

        app_directory = os.path.dirname(os.path.abspath(__file__))
        pdf_path = os.path.join(app_directory, 'template.pdf')

        # Sign the PDF
        position = (70, 300, 360, 240)
        await asyncio.to_thread(sign_pdf, pdf_path, position)

        # Save the signed PDF to the current project directory
        os.path.join(app_directory, 'signed-document.pdf')

        # Return a success response
        print('PDF generated and signed successfully')

        # Return the signed PDF as a FileResponse
        return FileResponse(path='signed-document.pdf', filename='signed-document.pdf', media_type='application/pdf')
    except Exception as e:
        # Return an error response if an exception occurs
        return JSONResponse(content={"error": str(e)}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
