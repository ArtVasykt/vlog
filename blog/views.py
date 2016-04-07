from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from .models import Profile
from .forms import RegForm

def index_view(request):
    pass

def profile_view(request, profile_id):
    profile = get_object_or_404(Profile, pk=profile_id)
    return render(request, 'blog/profile.html', {'profile': profile})


def registration_view(request):
    if request.method == "POST":
        form = RegForm(request.POST)
        if form.is_valid():
            return redirect(reverse('profile', args=[1]))
        else:
            return render_to_response('blog/registration.html', context={'form': form})
    else:
        form = RegForm(request.POST)
        return render(request, 'blog/registration.html', {'form': form})


