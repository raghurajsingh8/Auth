from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login
from autheticatweb.models import Contact,Product,Post,Message
from django.contrib.auth import authenticate,login,logout
from math import ceil
from .forms import PostForm 
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')




def contact(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            # author_r=request.POST['real']
            name=request.POST['name']
            email=request.POST['email']
            desc=request.POST['desc']
            pnumber=request.POST['pnumber']
            myquery=Contact(name=name,email=email,desc=desc,phonenumber=pnumber)
            myquery.save()
            messages.info(request,"we will get back to you soon..")
            return render(request,'contact.html')
    else:
        messages.info(request,"First you have to login.  ")

        return render(request,'login.html')
    return render(request,'contact.html')

def addproduct(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
              form.save()
            return redirect('/addproduct')  # Redirect to home page or any other page
        else:
          form = PostForm()
        return render(request, 'addproduct.html', {'form': form})
    else:
        messages.info(request,"First you have to login.  ")

        return render(request,'login.html')
    return render(request,'addproduct.html')




     













def order(request):
    
    all_posts = Post.objects.all()



    
   
    return render(request,'order.html',{'all_posts': all_posts})













def logouthandle(request):
    logout(request)
    messages.info(request,"Logout Success")
    return redirect('/login')
    




def loginu(request):
    if request.method=='POST':
        username=request.POST['email']
        userpassword=request.POST['pass1']
        myuser=authenticate(username=username,password=userpassword)

        if myuser is not None:
            login(request,myuser)
            return redirect('/')
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('/login/')

    return render(request,'login.html')




def signup(request):
    # print("i am running the signup function ")
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
        if password !=confirm_password:
           messages.warning(request,"Password is not matching")
           return  render(request,'signup.html')
        try:
            if User.objects.get(username=email):
                messages.info(request,"Email is taken")
                # messages.warning(request,"User Already Exist")
                return  render(request,'signup.html')
        except Exception as identifier:
            pass
        user=User.objects.create_user(email,email,password)
    
        user.save()
        messages.success(request,"Registarion Successfull")
        

    return render(request,'signup.html')










def cart(request):
    return render(request,'cart.html')



def send_message(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        
        if text:
            Message.objects.create(text=text)
            return redirect('display_messages')  # Corrected redirection
    # If the request method is not POST or if text is empty, render the send_message.html template
    return render(request, 'send_message.html')

def display_messages(request):
    messages = Message.objects.all().order_by('-created_at')
    return render(request, 'display_messages.html', {'messages': messages})


def showmes(request):
    
    all_posts = Message.objects.all()



    
   
    return render(request,'send_message.html',{'all_posts': all_posts})


