from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', homepage, name='homepage'),
    path('cari/panjang/', search_length_page, name='search_length'),
    path('cari/prefiks/', search_prefix_page, name='search_prefix'),
    path('cari/sufiks/', search_suffix_page, name='search_suffix'),
    path('cari/', search_words, name='search_words'),
    path('definisi/<str:word>', show_definition, name='show_definition'),
]