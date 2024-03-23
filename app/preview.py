import os
from fastapi import APIRouter, status, Form
from fastapi.responses import JSONResponse
from .preview_utils import render_html_template

router = APIRouter(prefix='/preview-pdf')

@router.post("/", status_code=status.HTTP_200_OK)
async def preview_endpoint(
    doc_date: str = Form(...),
    recipient_name: str = Form(...),
    document_type: str = Form(...),
    nationality: str = Form(...),
    passport_number: str = Form(...),
    position: str = Form(...),
    account_number: str = Form(...),
    start_date: str = Form(...),
    monthly_pay: str = Form(...),
    ):
    app_directory = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(app_directory, 'index.html')
    output_path = os.path.join(app_directory, 'template.html')

    variables = {
        'doc_date': doc_date,
        'recipient_name': recipient_name,
        'document_type': document_type,
        'nationality': nationality,
        'passport_number': passport_number,
        'position': position,
        'account_number': account_number,
        'start_date': start_date,
        'monthly_pay': monthly_pay,
        }
    render_html_template(output_path, template_path, variables)

    response_message = f'HTML template successfully rendered and saved to {output_path}.'
    return JSONResponse(content={'message': response_message})
