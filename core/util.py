from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO
from django.http import HttpResponse

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    
    # Correct usage: output should be a file-like object (not bytes)
    pdf = pisa.pisaDocument(BytesIO(html.encode("utf-8")), dest=result)
    
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    
    return HttpResponse("Error rendering PDF", status=400)