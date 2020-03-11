from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from .forms import SignupFormCeo , SignupFormHr , SignupFormCto , SignupFormSeniorSE , SignupFormJuniorSE
from .forms import UploadPostForm
from .models import Post, User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect


# Create your views here.
# User = get_user_model()


def index(request):
    return render(request, 'main/base.html')


@login_required
def upload_post_view(request):
    if request.method == "POST":
        form = UploadPostForm(request.POST)
        if form.is_valid():
            post_obj = Post()
            post_obj.title = form.cleaned_data['title']
            post_obj.description = form.cleaned_data['description']
            post_obj.user = request.user
            post_obj.save()
            if request.user.is_ceo:
                return redirect('ceo_dashboard')  # HttpResponseRedirect(reverse("index"))
            elif request.user.is_hr:
                return redirect('hr_dashboard')
            elif request.user.is_cto:
                return redirect('cto_dashboard')
            elif request.user.is_senior_developer:
                return redirect('sse_dashboard')
            elif request.user.is_junior_developer:
                return redirect('jse_dashboard')
    else:
        form = UploadPostForm()
    return render(request, 'main/upload_post.html', {'form': form})


def signup_ceo(request, Form):
    if request.method == 'POST':
        f = Form(request.POST)
        if f.is_valid():
            if User.objects.filter(is_ceo=True).count() != 0:
                messages.error(request, "CEO Already Exist")
                return redirect('login')
            else:
                f.save()
                messages.success(request, "Account created successfully")
                return redirect('login')
    else:
        f = Form()
    return render(request, 'main/signup.html', {'form': f})


def signup_hr(request, Form):
    if request.method == 'POST':
        f = Form(request.POST)
        if f.is_valid():
            if User.objects.filter(is_hr=True).count() != 0:
                messages.error(request, "HR Manager Already Exist")
                return redirect('login')
            else:
                f.save()
                messages.success(request, "Account created successfully")
                return redirect('login')
    else:
        f = Form()
    return render(request, 'main/signup.html', {'form': f})


def signup_cto(request ,Form):
    if request.method == 'POST':
        f = Form(request.POST)
        if f.is_valid():
            if User.objects.filter(is_cto=True).count() != 0:
                messages.error(request, "CTO Already Exist")
                return redirect('login')
            else:
                f.save()
                messages.success(request, "Account created successfully")
                return redirect('login')
    else:
        f = Form()
    return render(request, 'main/signup.html', {'form': f})


def signup_engineer(request, Form):
    if request.method == 'POST':
        f = Form(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, "Account created successfully")
            return redirect('login')
    else:
        f = Form()
    return render(request, 'main/signup.html', {'form': f})


def logout_view(request):
    logout(request)
    return redirect('login')

def admin(request):
    return render(request , 'main/admin.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                if user.is_ceo:
                    return redirect('ceo_dashboard')
                elif user.is_hr:
                    return redirect('hr_dashboard')
                elif user.is_cto:
                    return redirect('cto_dashboard')
                elif user.is_senior_developer:
                    return redirect('sse_dashboard')
                elif user.is_junior_developer:
                    return redirect('jse_dashboard')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request,
                  template_name="main/login.html",
                  context={"form": form})
@login_required
@user_passes_test(lambda u: u.is_ceo)
def create_hr(request):
    if request.method == 'POST':
        f = SignupFormHr(request.POST)
        if f.is_valid():
            if User.objects.filter(is_hr=True).count() != 0:
                messages.error(request, "HR Manager Already Exist")
                return redirect('ceo_admin')
            else:
                f.save()
                messages.success(request, "Account created successfully")
                return redirect('ceo_admin')
    else:
        f = SignupFormHr()
    return render(request, 'main/signup.html', {'form': f})

@login_required
@user_passes_test(lambda u: u.is_ceo)
def create_cto(request):
    if request.method == 'POST':
        f = SignupFormCto(request.POST)
        if f.is_valid():
            if User.objects.filter(is_cto=True).count() != 0:
                messages.error(request, "CTO Already Exist")
                return redirect('ceo_admin')
            else:
                f.save()
                messages.success(request, "Account created successfully")
                return redirect('ceo_admin')
    else:
        f = SignupFormCto()
    return render(request, 'main/signup.html', {'form': f})

@login_required
@user_passes_test(lambda u: u.is_ceo)
def create_engineers(request, Form):
    if request.method == 'POST':
        f = Form(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, "Account created successfully")
            return redirect('ceo_admin')
    else:
        f = Form()
    return render(request, 'main/signup.html', {'form': f})



@login_required
@user_passes_test(lambda u: u.is_ceo)
def ceo_dashboard(request):
    post = Post.objects.all()
    return render(request, 'main/dashboard_page.html', {'user': request.user, 'Posts': post})


@login_required
@user_passes_test(lambda u: u.is_hr)
def hr_dashboard(request):
    post = Post.objects.filter(user__is_ceo=False)
    return render(request, 'main/dashboard_page.html', {'user': request.user, "Posts": post})


@login_required
@user_passes_test(lambda u: u.is_cto)
def cto_dashboard(request):
    post = Post.objects.filter(user__is_ceo=False) & Post.objects.filter(user__is_hr=False)
    return render(request, 'main/dashboard_page.html', {'user': request.user, "Posts": post})


@login_required
@user_passes_test(lambda u: u.is_senior_developer)
def sse_dashboard(request):
    post = Post.objects.filter(user__is_ceo=False) & Post.objects.filter(user__is_hr=False) & Post.objects.filter(
        user__is_cto=False)
    print(post)
    return render(request, 'main/dashboard_page.html', {'user': request.user, "Posts": post})


@login_required
@user_passes_test(lambda u: u.is_junior_developer)
def jse_dashboard(request):
    post = Post.objects.filter(user__is_ceo=False) & Post.objects.filter(user__is_hr=False) & Post.objects.filter(
        user__is_cto=False) & Post.objects.filter(user__is_senior_developer=False)
    print(post)
    return render(request, 'main/dashboard_page.html', {'user': request.user, "Posts": post})
