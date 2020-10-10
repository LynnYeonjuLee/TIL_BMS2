from django.shortcuts import render, redirect, get_object_or_404
from .models import Review, Comment
from .forms import ReviewForm, CommentForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods, require_safe
# Create your views here.
def review_list(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews':reviews, 
    }
    return render(request, 'community/review_list.html', context)



def person_review_list(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    reviews = user.review_set.order_by('-pk')
    context = {
        'reviews':reviews, 
    }
    return render(request, 'community/person_review_list.html', context)


def review_detail(request, review_pk):
    comments = Comment.objects.all()
    comment_form = CommentForm()
    review = get_object_or_404(Review, pk=review_pk)
    context = {
        'review':review, 
        'comments':comments,
        'comment_form':comment_form,
    }
    return render(request, 'community/review_detail.html', context)

@login_required
def review_create(request):
    # POST
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('community:review_list')
    # GET
    else:
        form = ReviewForm()
    context = {
        'form':form,
    }
    return render(request, 'community/form.html', context)

@require_POST
def comments_create(request, review_pk):
    # POST
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.review = review
            comment.user = request.user
            comment.save()
            return redirect('community:review_detail', review.pk)
    # GET
        context = {
            'review':review, 
            'comment_form':comment_form,
        }
        return render(request, 'community/review_detail.html', context)
    return redirect('accounts:login')



@require_POST
def comments_delete(request, review_pk, comment_pk):
    review = get_object_or_404(Comment, pk=review_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user.is_authenticated:
        if request.user == comment.user:
            comment.delete()
            return redirect('community:review_detail', review.pk)


def like(request, review_pk):
    # 좋아요가 눌려져있으면 좋아요를 해제!
    review = get_object_or_404(Review, pk=review_pk)
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    # 로그인이 되어있지 않으면 로그인 페이지로 돌아간다.
    if review.like_users.filter(pk=request.user.pk).exists():
        review.like_users.remove(request.user)
    else: 
        review.like_users.add(request.user)
    return redirect('community:review_detail', review.pk)
    # 아니라면, 좋아요 추가!