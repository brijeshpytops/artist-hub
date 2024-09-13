from django.urls import path
from .views import *

urlpatterns = [
    path('', login_view, name='login_view'),
    path('new-register/', register_view, name='register_view'),
    path('logout/', logout, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard_view'),
    path('catalogue/', catalogue_view, name='catalogue_view'),
    path('profile/', profile_view, name='profile_view'),
    path('profile-update/', profile_update, name='profile_update'),
    path('update-date-of-birth/', update_date_of_birth, name='update_date_of_birth'),
    
]