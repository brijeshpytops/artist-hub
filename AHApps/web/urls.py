from django.urls import path
from .views import *

urlpatterns = [
    path('', login_view, name='login_view'),
    path('new-register/', register_view, name='register_view'),
    path('logout/', logout, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard_view'),
    path('catalogue/', catalogue_view, name='catalogue_view'),
    path('profile/', profile_view, name='profile_view'),
    
]