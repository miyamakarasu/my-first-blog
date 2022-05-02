from django import template
register = template.Library()
from django.conf import settings
from django.utils.safestring import mark_safe
import markdown
from markdown.extensions import Extension



@register.filter
def markdown_to_html(text):
    """マークダウンをhtmlに変換する。"""
    html = markdown.markdown(text, extensions=settings.MARKDOWN_EXTENSIONS)
    return mark_safe(html)
