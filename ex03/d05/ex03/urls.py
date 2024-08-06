
# from django.urls import path
# from .views import ex03_view

# urlpatterns = [
#     path('', ex03_view, name='ex03'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.table, name='table'),
]
