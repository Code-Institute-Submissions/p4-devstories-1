from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Comment, Newsletter, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("body",)
        labels = {
            "body": (""),
        }


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "slug", "content", "featured_image", "excerpt")
        lables = {
            "title": _(""),
            "slug": _(""),
            "content": _(""),
            "featured_image": _(""),
            "excerpt": (""),
        }


# Part of the custom model forms part
class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = [
            "email",
        ]

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "border-black rounded-0"
            self.fields[field].label = False
