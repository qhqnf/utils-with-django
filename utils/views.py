import os
from urllib.parse import quote
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

def response_excel(request):
    filepath = settings.MEDIA_ROOT + '/example.xlsx'
    filename = os.path.basename(filepath)

    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/vnd.ms-excel')

        encoded_filename = quote(filename)
        response['Content-Disposition'] = "attachment; filename*=utf-8''{}".format(encoded_filename)

    return response