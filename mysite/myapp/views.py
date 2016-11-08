from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello Harris!! A view!")

from os.path import join
from django.conf import settings


def csv(request):
    import pandas as pd

    county = join(settings.STATIC_ROOT, 'myapp/county.csv' )
    df = pd.read_csv(county)
    return HttpResponse(df.to_html())
