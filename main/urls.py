from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', homepage, name='homepage'),
    path('cari/panjang/', search_length_page, name='search_length'),
    path('cari/prefiks/', search_prefix_page, name='search_prefix'),
    path('cari/sufiks/', search_suffix_page, name='search_suffix'),
    path('cari/panjang/<int:length>', show_json_by_length, name='show_json_by_length'),
    path('cari/prefiks/<str:letter>', show_json_by_start, name='show_json_by_start'),
    path('cari/sufiks/<str:letter>', show_json_by_end, name='show_json_by_end'),
    path('cari/', search_words, name='search_words'),
]