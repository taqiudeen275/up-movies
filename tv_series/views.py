from django.shortcuts import render

def tv_series(request):
    return render(request, 'tv_series.html')
