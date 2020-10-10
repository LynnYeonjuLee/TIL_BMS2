from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import get_user_model
from .forms import ProfileIntroduce


# Create your views here.
@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('community:review_list')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('community:review_list')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('community:review_list')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('community:review_list')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

    
@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
        return redirect('community:review_list')

def profile(request, username):
    User = get_user_model()
    person = get_object_or_404(User, username=username)
    # POST
    if request.method == "POST":
        form = ProfileIntroduce(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile', username=username)
    # GET 
    else:
        form = ProfileIntroduce()
    context = {
        'person':person,
        'form': form,
    }
    return render(request, 'accounts/profile.html', context)


def follow(request, user_pk):
    you = get_object_or_404(get_user_model(), pk=user_pk)
    me = request.user
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    # 나는 나 자신을 팔로우 할 수 없다. 
    if me != you:
    # 내가 상대방을 팔로우하고 있다면, 언팔을 하고 
        if you.followers.filter(pk=me.pk).exists():
            you.followers.remove(me)
    # 그렇지 않다면 팔로우를 한다.         
        else: 
            you.followers.add(me)
    return redirect('accounts:profile', you.username)


def followers(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    users = user.followers.all()
    context = {
        'users':users,
    }
    return render(request, 'accounts/followers.html', context)


def followings(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    users = user.followings.all()
    context = {
        'users':users,
    }
    return render(request, 'accounts/followings.html', context)

