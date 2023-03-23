from django.shortcuts import render,redirect
from django.core.mail import send_mail
from myapp.forms import Email
from django.template.loader import render_to_string

# Create your views here.

def index(request):
    form=Email()
    if request.method=='POST':
        form=Email(request.POST)

        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            message=form.cleaned_data['message']
            html=render_to_string('feedback.html',{
                'name':name,'email':email,'message':message
            })
            send_mail('Message to your company ', 'hello sir we are very pleased writing to you to enquire nore about your company', 'zilo', ['billleynyuy@gmail.com'],html_message=html)
            return redirect("/")
        else:
            form=Email()

    return render(request,'index.html',{'form':form})
