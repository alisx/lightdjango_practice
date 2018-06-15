from django.urls import path
from .views import page


urlpatterns = (
    path('<slug>', page, name='page'),
    path('', page, name='homepage'),
)