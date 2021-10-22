from django.shortcuts import render, redirect, reverse
from django.views import generic
from .models import Blogpost
from .forms import CreatePostForm
from django.contrib import messages
import pytz


def home(request):
    if request.session.get('django_timezone') == None: #If the browser's timezone isn't set, ask user to set timezone
        return render(request, 'blogapp/settimezone.html', {'timezones': pytz.common_timezones})
    else:
        queryset = Blogpost.objects.filter(status=Blogpost.PUBLISH)
        return render(request, 'blogapp/home.html', {'post':queryset})

def settimezone(request):
    if request.method == 'POST':
        request.session['django_timezone'] = request.POST['timezone'] #Sets the request session's timezone to the user selected timezone, so all datetime objects will be rendered in the user's desired timezone
        return redirect(reverse("bloghome"))
    else:
        return render(request, 'blogapp/settimezone.html', {'timezones': pytz.common_timezones})
    return render(request, 'blogapp/settimezone.html', {'timezones': pytz.common_timezones})

class PostDetail(generic.DetailView):
    model = Blogpost
    template_name = 'blogapp/post_detail.html'
    
def createPost(request):
    queryset = Blogpost.objects.filter(status=Blogpost.PUBLISH)
    form = CreatePostForm()
    if request.method =='POST':
        if form.is_valid():
            thisPost = form.save(commit=False)
            thisPost.author = request.user #Gets the current logged in user, assigns the user to this post instance
            thisPost.save()
            messages.success(request, "'" + thisPost.title + "'" +" was created successfully. STATUS: " + thisPost.status )
            return render(request, 'blogapp/home.html', {'post': queryset})
        else:
            messages.error(request, "Error when creating post")
            return render(request, 'blogapp/home.html', {'post': queryset})

    return render(request, 'blogapp/create_post.html', {})