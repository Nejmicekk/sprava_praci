from django.shortcuts import redirect, render, get_object_or_404
from .models import Work
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login/")
def work_detail(request, pk):
    work = get_object_or_404(Work, pk=pk)
    return render(request, 'work_detail.html', {"work" : work})

@login_required(login_url="/login/")
def schvalit_praci(request, pk):
    work = get_object_or_404(Work, pk=pk)
    if request.user.role == "ucitel":
        work.schvaleno = True
        work.schvalovatel = request.user
        work.save()
        return redirect("work_detail", pk=pk)
    
@login_required(login_url="/login/")
def zamitnout_praci(request, pk):
    work = get_object_or_404(Work, pk=pk)
    if request.user.role == "ucitel":
        work.delete()