from django.shortcuts import render, get_object_or_404
from .models import Work

def work_detail(request, pk):
    work = get_object_or_404(Work, pk=pk)
    return render(request, 'works/work_detail.html', {"work" : work})