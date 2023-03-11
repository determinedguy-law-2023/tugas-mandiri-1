from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', homepage, name='homepage'),
    path('panjang/<int:length>', show_json_by_length, name='show_json_by_length'),
    path('awal/<str:letter>', show_json_by_start, name='show_json_by_start'),
    path('akhir/<str:letter>', show_json_by_end, name='show_json_by_end'),
    path('cari/', search_words, name='search_words'),
]