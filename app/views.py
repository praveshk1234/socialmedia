import re
from django.shortcuts import render,redirect,get_object_or_404
from .models import  Post,Profile,Follow
from django.contrib import messages
from .forms import CustomUserCreationForm, ProfileForm
from django.contrib.auth.models import User
from .forms import PostForm
from .utils import followuser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate,logout
# Create your views here.
def likepost(request,pk):
    post = get_object_or_404(Post,id=request.POST.get('post_id'))
    print(post)
    liked = False
    if post.likes.filter(id=request.user.profile.id).exists():
        post.likes.remove(request.user.profile)
        liked=False
    else:
        post.likes.add(request.user.profile)
        liked=True
    return redirect("/")

def profileupdate(request,pk):
  
    form=ProfileForm(instance=request.user.profile)
    if request.method=='POST':
        print(form.errors)
        form=ProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if form.is_valid():
            form.save()
        
            return redirect('/')
    return render(request,'profileupdate.html',{'form':form})

def registerUser(request):
    form = CustomUserCreationForm()
    page= "Register"
    if request.method=='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            print("login")
            return redirect('home')
        else:
            print("error occur")
    context = {'page':page,'form':form}
    return render(request,"login_register.html",context)

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username=request.POST['username'].lower()
        password = request.POST['password']
        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request,'User does not exist')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else: 
            messages.error(request,'Username or Password is incorrect')
    return render(request,'login_register.html')

def logoutUser(request):
    logout(request)
    messages.info(request,"User is logged out")
    return redirect('login')
@login_required(login_url='login')
def postlist(request):
    form= PostForm()
    follower_to,followcount = followuser(request) 
    userprofile = []       
    for users in follower_to:
        userprofile.append(users.followed_to.firstname)
    profileuser= Profile.objects.filter(firstname__in=userprofile)
    posts= Post.objects.filter(profile__in=profileuser)
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.profile = request.user.profile
            obj.save()
    context = {'posts':posts,'form':form}
    return render(request,'home.html',context)
def profileUser(request):
    user= request.user

    profiles = Profile.objects.exclude(firstname=user)
    folower_to,followcount = followuser(request)        
    context = {'profile':user.profile,'other_profiles':profiles,'followcount':followcount,'followto':folower_to}
    return render(request,"profile.html",context)

def getprofiles(request,firstname):
    user= request.user
    queobj= Profile.objects.get(firstname=firstname)
    followed_users =[]
    objfollow = Follow.objects.filter(followed_by=user.profile)
    for listuser in objfollow:
        followed_users.append(listuser.followed_to.firstname)
    if queobj.firstname in followed_users:
        button_value = True
    else:
        button_value = False
    if request.method == 'POST':
        follow = request.POST['follow']
        another_profile = Profile.objects.get(firstname=follow)
        if button_value==False:
            follower,created= Follow.objects.get_or_create(followed_by=request.user.profile,followed_to=another_profile)
        else:
            delobj=  Follow.objects.get(followed_by=request.user.profile,followed_to=another_profile).delete()
        return redirect("profile")
    context = {"profileObj":queobj,'button_value':button_value}
    return render(request,'profileuser.html',context)
