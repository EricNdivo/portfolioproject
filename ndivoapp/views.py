from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import path
from .import views
from portfolioproject import settings
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
import mimetypes
import os
from django.http.response import HttpResponse, Http404
from django.conf import settings
from .models import PdfFile
from django.shortcuts import render


def index(request):
    #context={'file':PdfFile.objects.all()}
    return render(request, 'templates/index.html')
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if len(password) < 8:
            messages.error(request, "Password must be at least 8 characters long.")
            return redirect('signup.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('signup.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already taken.")
            return redirect('signup.html')

        if password != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('signup.html')

        if not username.isalnum():
            messages.error(request, "Username must be alphanumeric.")
            return redirect('signup.html')

        myuser = User.objects.create_user(username=username, email=email, password=password)

        subject = "Welcome to FIN7 Login"
        message = f"Hello, {username}!\nConfirmation Email sent to your email address.\nCheck your inbox to activate your account."
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)

        messages.success(request, 'Account successfully created')
        return redirect('login')

    return render(request, 'signup.html')

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, 'User does not exist')
            return render(request, 'login.html')  

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Username or Password does not exist')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    messages.success(request, 'Successfully logged out')
    return redirect('/')

def contact(request):
    print(request.user)
    if request.method == "POST":
        name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_subject = request.POST['message-subject']
        message = request.POST['message']
        #Sending an Email
        send_mail(
            name, #subject
            message, #message
            message_email , #from email
            ['ndivoeric288@gmail.com'], #To Email 
            fail_silently=False
        )
    return render(request, 'contact.html')

def about(request):
    print(request.user)
    return render(request, 'about.html')

def download_file(request,path):
    print(request.user)
    file_path=os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as enm:
            response=HttpResponse(enm.read(),content_type="application/adminupload")
            response['Content-Disposition']='Inline;filename='+os.path.basename(file_path)
            return response
    raise Http404


def upload_pdf(request):
    if request.method == 'POST':
        pdf_file = request.FILES['pdf']
        pdf = PdfFile(file=pdf_file)
        pdf.save()
        return redirect('pdf_list')
    return render(request, 'upload_pdf.html')


def linkedin_profile(request):
    print(request.user)
    linkedln_handle = "Eric Ndivo"
    linkedln_url = f"https://www.linkedin.com/in/eric-ndivo/"
    
    return HttpResponseRedirect(linkedln_url)


def download_pdf(request):
    pdf = pdf.objects.first()
    response = HttpResponse(pdf.file, content_type='application/pdf')
    return response 

def services(request):
    print(request.user)
    return render(request,'services.html')

def blog(request):
    return HttpResponse("Tab still in Development ...")

def homepage(request):
    return redirect('/')

def instagram(request):
    instagram_handle = "eric.ndivo"
    instagram_url = f"https://www.instagram.com/EricNdivo/"
    
    return HttpResponseRedirect(instagram_url)

def x(request):
    print(request.user)
    x_handle = "j_69whiskey"
    x_url = f"https://www.x.com/j_69whiskey/"
    
    return HttpResponseRedirect(x_url)


def webdev(request):
    print(request.user)
    return HttpResponse("In Development")


def mobdev(request):
    print(request.user)
    return HttpResponse("In Development")


def readmore(request):
    print(request.user)
    return HttpResponse("In Development")


def hire(request):
    print(request.user)
    return render(request, 'hire.html')



