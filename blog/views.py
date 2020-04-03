import os

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from .models import Comment, ImageUpload
from .forms import CommentForm, ImageUploadForm, WidthForm


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


@login_required
@require_POST
def ajax_image_upload(request):
    data = dict()

    form = ImageUploadForm(request.POST, request.FILES)
    if form.is_valid():
        image = form.save(commit=False)
        image.user = request.user
        image.save()
        data['is_valid'] = True
        form = WidthForm(instance=image)

        data['html_image'] = render_to_string('blog/comment/image.html',
                                            {'image': image, 'form': form},
                                            request=request)
            
        name = os.path.basename(image.image.name)

        data['markdown_image'] = f'![{ name }]({ image.image.url }#w-{ image.width })'
    else:
        data['is_valid'] = False

    return JsonResponse(data)


@login_required
@require_POST
def ajax_change_width(request, image_id):
    data = dict()
    image = get_object_or_404(ImageUpload, id=image_id)
    form = WidthForm(request.POST, instance=image)
    if form.is_valid():
        form.save()

    name = os.path.basename(image.image.name)
    data['markdown_image'] = f'![{ name }]({ image.image.url }#w-{ image.width })'

    return JsonResponse(data)


@login_required
@require_POST
def ajax_delete_image(request, image_id):
    data = dict()
    image = get_object_or_404(ImageUpload, user=request.user, id=image_id)
    image.delete()
    data['image_placeholder'] = render_to_string('blog/comment/image_placeholder.html')

    return JsonResponse(data)
