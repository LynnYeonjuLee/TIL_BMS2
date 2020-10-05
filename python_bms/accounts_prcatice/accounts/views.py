from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash


from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
# Create your views here.

# 1. GET 으로 들어가기 허용되는가?(POST 로만 들어올 수 있음  )안되면-> @require_POST
# 2. POST 로 들어가기 허용되는가?(GET으로만 들어올 수 있음)안되면-> @require_GET (한버도 쓴적없은 )
        
        # if request.method == 'POST': return~~
# 3. 비로그인 상태로 들어가기 허용되는가?(로그인 상태로만 들어올 수 있음) 안되면@login_required
# 4. 로그인 상태로 들어가기 허용되는가?(비로그인 상태로만 들어올 수 있음 ) 안되면if request.user.is_authenticated: return ~~
# 1.+ 2. == @require_http_methods(['GET', 'POST'])
# 1. + 3. 은 함께 존재할 수 없다.  == @require_POST, if request.user.is_authenticated: 실행 
@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get("next") or 'articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form':form, 
    }
    return render(request, 'accounts/login.html', context)

@require_POST
# @login_required
# 1. 3.
def logout(request):
    # 로그인일 때 
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('articles:index')
    # # 비로그인일때 
    # else: 
    #     return redirect('articles:index')

@require_POST
# 1. 3.
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
    return redirect('articles:index')

@require_http_methods(['GET', 'POST'])
@login_required    
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)

@require_http_methods(['GET', 'POST'])
@login_required  
def password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/password.html', context)

