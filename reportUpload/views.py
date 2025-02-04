from django.shortcuts import render
from django.views.generic import TemplateView, FormView

class UploadPage(TemplateView):
    template_name = 'upload_file_page.html'

    