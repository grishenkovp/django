from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def start_page(request):
    return render(request,'account/start_page.html')
