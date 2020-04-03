from django import forms
from django.shortcuts import reverse

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import InlineRadios

from .models import Comment, ImageUpload
from .constants import WidthChoices


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'content', )


class ImageUploadForm(forms.ModelForm):

    class Meta:
        model = ImageUpload
        fields = ('image',)


class WidthForm(forms.ModelForm):
    width = forms.ChoiceField(widget=forms.RadioSelect, choices=WidthChoices.CHOICES)

    class Meta:
        model = ImageUpload
        fields = ('width',)

    def __init__(self, *args, **kwargs):
        super(WidthForm, self).__init__(*args, **kwargs)
        self.fields['width'].label = False
        self.helper = FormHelper()
        self.helper.form_class = 'js-width-form'
        self.helper.form_action = reverse('blog:ajax_change_width', args=[self.instance.id])
        self.helper.layout = Layout(
            InlineRadios('width'),
        )

