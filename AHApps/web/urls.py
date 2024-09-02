from django.urls import path
from .views import *

urlpatterns = [
    path('', index_view, name='index_view'),
    path('mydata/', mydata, name='mydata'),
    path('bio/', mybiodata, name='mybiodata')
]