from django.shortcuts import render

from .models import Comment
from .forms import CommentForm, ImageUploadForm


def create_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save()
            
            form = CommentForm()

    else:
        form = CommentForm()

    context = {
        'form': form,
        'comments': Comment.objects.all(),
    }

    return render(request, 'blog/comment/create.html', context)
