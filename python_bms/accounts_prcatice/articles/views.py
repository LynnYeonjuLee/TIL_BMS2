# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from django.views.decorators.http import require_http_methods, require_POST
# from .models import Article, Comment
# from .forms import ArticleForm, CommentForm

# # Create your views here.
# def index(request):
#     articles = Article.objects.order_by('-pk')
#     context = {
#         'articles': articles,
#     }
#     return render(request, 'articles/index.html', context)


# @login_required
# @require_http_methods(['GET', 'POST'])
# def create(request):
#     if request.method == 'POST':
#         form = ArticleForm(request.POST) 
#         if form.is_valid():
#             article = form.save(commit=False)
#             article.user = request.user
#             article.save()
#             return redirect('articles:detail', article.pk)
#     else:
#         form = ArticleForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'articles/create.html', context)


# def detail(request, pk):
#     # article = Article.objects.get(pk=pk)
#     article = get_object_or_404(Article, pk=pk)
#     comment_form = CommentForm()
#     comments = article.comment_set.all()
#     context = {
#         'article': article,
#         'comment_form': comment_form,
#         'comments': comments,
#     }
#     return render(request, 'articles/detail.html', context)


# @login_required
# @require_http_methods(['GET', 'POST'])
# def update(request, pk):
#     # article = Article.objects.get(pk=pk)
#     article = get_object_or_404(Article, pk=pk)
#     # 수정하는 유저와, 게시글 작성 유저가 같은지 ?
#     if request.user == article.user:
#         if request.method == 'POST':
#             form = ArticleForm(request.POST, instance=article)
#             if form.is_valid():
#                 form.save()
#                 return redirect('articles:detail', article.pk)
#         else:
#             form = ArticleForm(instance=article)
#     else:
#         return redirect('articles:index')
#     context = {
#         'form': form,
#         'article': article,
#     }
#     return render(request, 'articles/update.html', context)


# @require_POST
# def delete(request, pk):
#     if request.user.is_authenticated:
#         # article = Article.objects.get(pk=pk)
#         article = get_object_or_404(Article, pk=pk)
#         if request.user == article.user:
#             article.delete()
#             return redirect('articles:index')
#     return redirect('articles:detail', article.pk)


# @require_POST
# def comments_create(request, pk):
#     # article = Article.objects.get(pk=pk)
#     if request.user.is_authenticated:
#         article = get_object_or_404(Article, pk=pk)
#         comment_form = CommentForm(request.POST)
#         if comment_form.is_valid():
#             # Create, but don't save the new comment instance.
#             comment = comment_form.save(commit=False)
#             comment.article = article
#             comment.user = request.user
#             comment.save()
#             return redirect('articles:detail', article.pk)
#         context = {
#             'comment_form': comment_form,
#             'article': article,
#         }
#         return render(request, 'articles/detail.html', context)
#     return redirect('accounts:login')


# @require_POST
# def comments_delete(request, article_pk, comment_pk):
#     # comment = Comment.objects.get(pk=comment_pk)
#     if request.user.is_authenticated:
#         comment = get_object_or_404(Comment, pk=comment_pk)
#         if request.user == comment.user:
#             comment.delete()
#     return redirect('articles:detail', article_pk)


from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST
from .models import Article, Comment
from .forms import ArticleForm, CommentForm


# 1. GET 으로 들어가기 허용되는가?(POST 로만 들어올 수 있음  )안되면-> @require_POST
# (2. POST 로 들어가기 허용되는가?(GET으로만 들어올 수 있음)안되면-> @require_GET (한버도 쓴적없은 ))
        
        # if request.method == 'POST': return~~
# 3. 비로그인 상태로 들어가기 허용되는가?(로그인 상태로만 들어올 수 있음) 안되면@login_required
# 4. 로그인 상태로 들어가기 허용되는가?(비로그인 상태로만 들어올 수 있음 ) 안되면if request.user.is_authenticated: return ~~

# UPDATE 와 DELETE 에서만 확인해준다. 
# 조건부 .작성된 글을 변경/삭제할 수 있는 권한은 그 글을 작성한 유저뿐이다.
#  작성된 글을 작성한 유저와 로그인한 유저가 같은가? -> if request.user == article.user: 실행 
#      -> if request.user == -------.user: 실행 

# 1.+ 2. == @require_http_methods(['GET', 'POST'])
# 1. + 3. 은 함께 존재할 수 없다.  == @require_POST, if request.user.is_authenticated: 실행 



# Create your views here.

def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@require_http_methods(['GET', 'POST'])
@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST) 
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


def detail(request, pk):
    
    article = Article.objects.get(pk=pk)
    form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'form': form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)


@require_http_methods(['GET', 'POST'])
@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user ==article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
        context = {
            'form': form,
            'article': article,
        }
        return render(request, 'articles/update.html', context)
    else:
        return redirect('articles:detail', article.pk)

@require_POST
def delete(request, pk):
    if request.user.is_authenticated: 
        article = Article.objects.get(pk=pk)
        if request.user ==article.user:
            article.delete()
    return redirect('articles:index')

@require_POST
def comments_create(request, pk):
    if request.user.is_authenticated: 
        article = Article.objects.get(pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.article = article
            comment.save()
            return redirect('articles:detail', pk)

        context = {
            'article': article,
            'form': form,
        }
        return render(request, 'articles/detail.html', context)
    return redirect('accounts:login')

@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated: 
        comment = Comment.objects.get(pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
        return redirect('articles:detail', article_pk)
    return redirect('accounts:login')