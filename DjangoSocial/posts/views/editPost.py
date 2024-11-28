from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from .models import post TO DO
# from .forms import postForm TO DO

# View for Creating a Post
@login_required
def post_create(request):
    if request.method == 'POST':
        form = postForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('feed')
    else:
        form = postForm()
    return render(request, 'post_create.html', {'form': form })
