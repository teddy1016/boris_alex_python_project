from django.shortcuts import render
from django.http import HttpResponse
# from .models import ArticleSeries, Article

# Create your views here.
def homepage(request):
    # matching_series = ArticleSeries.objects.all()

    return render(request=request,
                  template_name='home.html',
                  context={"objects": "matching_series"}
                  )