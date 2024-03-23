import os
from jinja2 import Template

def render_html_template(output_file_path, template_path, variables):
    # Read the HTML content from the file
    with open(template_path, 'r', encoding='utf-8') as template_file:
        template_string = template_file.read()

    # Create Jinja2 template
    template = Template(template_string)

    # Render the template with provided variables
    rendered_html = template.render(variables)

    # Save the rendered HTML to the specified output file path
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(rendered_html)

