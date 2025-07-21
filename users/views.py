from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def admin_dash(request): 
    return render(request, 'admin/dash.html', {})

