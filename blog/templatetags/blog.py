from markdown import markdown
from mdx_gfm import GithubFlavoredMarkdownExtension

from django import template
from django.utils.html import mark_safe


register = template.Library()


@register.filter(name='markdown')
def markdown_filter(value):
    return mark_safe(markdown(value, safe_mode='escape', extensions=[GithubFlavoredMarkdownExtension()]))
