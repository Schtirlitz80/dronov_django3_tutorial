from django.http import HttpResponse
from django.template import loader

from .models import Bb

# Create your views here.
def index(request):
    template = loader.get_template('bboard/index.html')
    return HttpResponse(s, content_type='text/plain; charset=utf-8')
