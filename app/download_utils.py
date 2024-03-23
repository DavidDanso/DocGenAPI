from weasyprint import HTML
import os

def convert_html_to_pdf():
    app_directory = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(app_directory, 'template.html')
    output_path = os.path.join(app_directory, 'template.pdf')

    try:
        # Load HTML file
        html = HTML(filename=input_path)

        # Generate PDF
        html.write_pdf(output_path)
        
        print(f"PDF generated successfully at {output_path}")
    except Exception as e:
        print(f"Error generating PDF: {str(e)}")

