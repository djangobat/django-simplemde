from django import forms

from .models import Comment, ImageUpload


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'content', )


class ImageUploadForm(forms.ModelForm):

    class Meta:
        model = ImageUpload
        fields = ('image',)
