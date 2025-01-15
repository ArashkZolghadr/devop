from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
from .forms import NameForm
from django.contrib import messages
from accounts.models import Profile

def index_view(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'اطلاعات شما ثبت گردید ')
        else:
            messages.error(request, 'اطلاعات شما ثبت نگردید')
        # دریافت اطلاعات از فرم
    form = NameForm()

    
    arashk = Profile.objects.get(author=1)
    amin = Profile.objects.get(author=2)

    context = {
        'arashk': arashk,
        'amin': amin,
        'form' : form 
       }
    return render(request, 'website/index.html', context)

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'اطلاعات شما ثبت گردید ')
        else:
            messages.error(request, 'اطلاعات شما ثبت نگردید')
        # دریافت اطلاعات از فرم
    form = NameForm()

    # ذخیره‌سازی در دیتابیس با save()
    
    # نمایش پیام موفقیت
    return render(request, 'website/contact.html', {
        'form' : form 
    })
    