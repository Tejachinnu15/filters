from django.shortcuts import render

# Create your views here.
import datetime
def built_in_filters(request):
    d={'data':'Today Going TO HOMe','dt':2,'de':0}
    return render(request,'built_in_filters.html',d)