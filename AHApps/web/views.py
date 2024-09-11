from django.shortcuts import render, redirect
from django.contrib import messages

from functools import wraps

from AHApps.artist.models import Artist, ArtistProfile

# Create your views here.

def login_required(view_func):
    """
    Decorator that requires a user to be authenticated to access the view.
    """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.session.get('artist_id'):
            messages.error(request, 'You need to login first.')
            return redirect('login_view')
        return view_func(request, *args, **kwargs)
    return _wrapped_view


def login_view(request):
    if request.method == 'POST':
        artist_id_ = request.POST['artist_id']
        password_ = request.POST['password']

        try:
            check_artist = Artist.objects.get(artist_id=artist_id_)
        except Artist.DoesNotExist:
            messages.error(request, "Artist ID and password doesn't match.")
            return redirect('login_view')
        else:
            if check_artist.password == password_:
                request.session['artist_id'] = check_artist.artist_id
                messages.success(request, "Now, You are logged In.")
                return redirect('dashboard_view')
            else:
                messages.error(request, "Artist ID and password doesn't match.")
                return redirect('login_view')

    return render(request, r'web\login.html')

@login_required
def logout(request):
    if 'artist_id' in request.session:
        del request.session['artist_id']
        messages.success(request, "Now you are logged out.")
        return redirect('login_view')
    else:
        messages.error(request, 'You are not logged In yet.')
        return redirect('login_view')
    
def register_view(request):
    return render(request, r'web\register.html')

@login_required
def dashboard_view(request):
    return render(request, r'web\dashboard.html')

@login_required
def catalogue_view(request):
    return render(request, r'web\catalogue.html')
@login_required
def profile_view(request):
    artist_id = request.session['artist_id']
    print(artist_id)
    artist_profile = ArtistProfile.objects.get(artist_id_id=artist_id)
    print(artist_profile)
    context = {
        'profile':artist_profile
    }
    return render(request, r'web\profile.html', context)


