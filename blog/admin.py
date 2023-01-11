from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment
from .models import Newsletter

# Register your models here.


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ("title", "slug", "created_on")
    search_fields = ["title", "content"]
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ["created_on"]
    summernote_fields = "content"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ("name", "body", "post", "created_on", "approved")
    search_fields = ("name", "email", "body")
    actions = ["disable_comments"]

    def disable_comments(self, request, queryset):
        queryset.update(approved=False)


class NewsletterAdmin(admin.ModelAdmin):
    readonly_fields = ("email", "date", "user_id")

    fields = ("date", "email", "user_id")

    list_display = ("email", "date", "user_id")

    ordering = ("-date",)


admin.site.register(Newsletter, NewsletterAdmin)
