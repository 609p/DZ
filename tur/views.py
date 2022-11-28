from django.shortcuts import render
from django.http import HttpResponseRedirect, FileResponse
from .models import Posts
from django.core.files.storage import FileSystemStorage
import xml.etree.cElementTree as ET
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def index(request):
    return render(request, 'home.html',{'user':request.user})

def profile(request):
    return render(request, 'profile.html')


def posts(request):
    posts = Posts.objects.all()
    return render(request, 'posts.html', {'posts': posts})

def content(request):
    content = Posts.objects.get(id=id)
    return render(request, 'post.html', {'content': content})


def newposts(request):
    title = request.POST.get('title')
    text = request.POST.get('text')
    file = request.FILES['file']
    content = request.POST.get('content')
    fss = FileSystemStorage('app1/static/images')
    saved_file = fss.save(file.name, file)
   
    post = Posts()
    post.title = title
    post.text = text
    post.content = content
    post.image = file.name
    post.save()
    return HttpResponseRedirect('/posts')

def post(request,id):
    post = Posts.objects.get(id = id)
    username = request.user
    return render(request, 'post.html', {'post': post, 'username':username})


def editpost(request,id):
    post = Posts.objects.get(id = id)
    return render(request, 'editpost.html', {'post': post})


def saveeditpost(request,id):
    post = Posts.objects.get(id = id)
    title = request.POST.get('title')
    text = request.POST.get('text')
    content = request.POST.get('content')
    if 'file' in request.FILES:
        file = request.FILES['file']
        fss = FileSystemStorage('app1/static/images')
        saved_file = fss.save(file.name, file)
        post.image = file.name
    else:
        pass
    post.title = title
    post.text = text
    post.content = content
    post.save()
    return HttpResponseRedirect('/posts')

def deletepost(request,id):
    post = Posts.objects.get(id = id)
    post.delete()
    return HttpResponseRedirect('/posts')



def registration(request):
    if request.method == 'POST':
        name =  request.POST.get('name')
        mail =  request.POST.get('mail')
        password =  request.POST.get('password')
        user= User.objects.create_user(name, mail, password)
        user.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'registration.html')

        
def login_user(request):
    if request.method == 'POST':
        name =  request.POST.get('name')
        password =  request.POST.get('password')

        user = authenticate(username = name, password = password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/')
        else:
            print('error')
       
            return HttpResponseRedirect('/login')
            
    else:
        return render(request, 'login.html')
    




def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')



def export(request):
    posts = Posts.objects.all()
    data = ET.Element('data')
    for post in posts:
        element = ET.SubElement(data,'post')
        element.set('title',post.title)

    ET.ElementTree(data).write("post.xml",encoding = 'utf-8')
    return HttpResponseRedirect('/posts')


