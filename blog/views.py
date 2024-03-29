from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.views.generic import ListView, View
from django.conf import settings

from .forms import BlogPostForm, CommentForm, NewsletterForm
from .models import Newsletter, Post


class PostList(ListView):
    """
    Lists all the blog Posts on the page
    """
    model = Post
    queryset = Post.objects.order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):
    """
    Allows a user to view a post
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """
        Display or comment on a post
        """
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        form = CommentForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.name = self.request.user
            form.email = request.user.email
            form.post = post
            form.save()
        else:
            form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "form": form,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )

    def form_valid(self, form):
        """validate form and connect to user"""
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class PostLike(View):
    """
    Allows a user to like a Post
    """
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse("post_detail", args=[slug]))


@login_required
def create_post(request):
    """
    Allows a user to create a Blog Post
    """
    if request.user:

        if request.method == "POST":
            form = BlogPostForm(request.POST, request.FILES)
            if form.is_valid():
                blog_post = form.save(commit=False)
                blog_post.author = request.user
                blog_post.save()
                messages.info(request, "Blog has been posted!")
                return redirect(reverse("home"))
            else:
                messages.error(
                    request,
                    "Please check the form for errors. \
                    Blog failed to add.",
                )
        else:
            form = BlogPostForm()
    else:
        messages.error(
            request,
            "Sorry, you do not have permission to do that."
        )
        return redirect(reverse("home"))

    template = "new_post.html"

    context = {
        "form": form,
    }
    return render(request, template, context)


@login_required
def update_post(request, slug):
    """
    Allow all users to edit the blogs they created
    """
    if request.user:

        blog_post = get_object_or_404(Post, slug=slug)
        if blog_post.author != request.user:
            redirect(reverse("home"))
        if request.method == "POST":
            if request.user == blog_post.author:
                form = BlogPostForm(
                    request.POST,
                    request.FILES,
                    instance=blog_post
                )
                if form.is_valid():
                    form.save()
                    messages.success(
                        request,
                        "Blog post updated successfully!"
                    )
                    return redirect("home")
                else:
                    messages.error(
                        request,
                        "Please check the form for errors. \
                        Blog post failed to update.",
                    )
            else:
                messages.error(
                    request, "sorry you are not authorised to edit this post"
                )
                return redirect(reverse("home"))
        else:
            form = BlogPostForm(instance=blog_post)
            messages.info(request, f"Editing {blog_post.title}")
    else:
        messages.error(request, "Sorry, you do not have permission for that.")
        return redirect(reverse("home"))

    template = "update_post.html"

    context = {
        "form": form,
        "blog_post": blog_post,
    }

    return render(request, template, context)


@login_required
def delete_post(request, blog_post_id):
    """User can delete their own blog post"""
    if request.method == "POST":
        blog_post = get_object_or_404(Post, pk=blog_post_id)
        blog_post.delete()
    else:
        return render(request, "delete_blog.html")
    messages.success(request, "The blog has been deleted successfully!")

    return redirect("/")


def subscribe(request):
    """A user or guest can subscribe for updates"""
    form = NewsletterForm(request.POST)
    if form.is_valid():
        form = form.save(commit=False)
        if request.user.is_authenticated:
            form.user_id = request.user
        else:
            form.user_id = None
        form.save()
    return redirect("/")


def unsubscribe(request):
    """A user or guest can ubsubscribe / delete their emial from updates"""
    form = NewsletterForm(request.POST)
    if request.user.is_authenticated:
        newsletter = Newsletter.objects.get(user_id=request.user)
        newsletter.delete()
    else:
        if form.is_valid():
            newsletter = Newsletter.objects.get(
                email=form.cleaned_data["email"]
            )
            newsletter.delete()
    return HttpResponseRedirect(reverse("home"))


def editemail(request):
    """Allows a user to update their newsletter email if logged in"""
    form = NewsletterForm(request.POST)
    if request.user.is_authenticated:
        newsletter = Newsletter.objects.get(user_id=request.user)
        newsletter.email = form.data["email"]
        newsletter.save()
        send_mail(
            "Subject here",
            "Here is the message.",
            "from@example.com",
            [form.data["email"]],
            fail_silently=False,
        )
        return redirect("create_post")


def new_email(request):
    subject = "Thanks for subscribing"
    message = "Hello world"
    email_from = settings.EMAIL_HOST_USER
    recipients = ["eoghankb@gmail.com"]

    send_mail(subject=subject, message=message, from_email=email_from, recipient_list=recipients, fail_silently=False)
    return redirect("/")