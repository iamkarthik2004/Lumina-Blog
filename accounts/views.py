from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from blog.models import Post

def login_view(request):
    # Determine the template path based on file location
    # Since we configured DIRS to include BASE_DIR/templates, we can just use 'login.html'
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def home_view(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})
