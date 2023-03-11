from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from main.models import Kata

# Functions
def search_by_length(words, length, max_length=None):
    result = []
    for word in words:
        if max_length:
            if length <= len(word.kata) <= max_length:
                result.append(word)
        else:
            if len(word.kata) == length:
                result.append(word)
    return result

def search_by_prefix(words, prefix):
    result = []
    for word in words:
        if word.kata.startswith(prefix):
            result.append(word)
    return result

def search_by_suffix(words, suffix):
    result = []
    for word in words:
        if word.kata.endswith(suffix):
            result.append(word)
    return result

# Create your views here.
def homepage(request):
    return render(request, "homepage.html")

def search_length_page(request):
    if request.method == 'POST':
        print(request.POST.get('panjang'))
        length = int(request.POST.get('panjang'))
        max_length = None
        if request.POST.get('batas'):
            max_length = int(request.POST.get('batas'))
        return search_length_function(request, length, max_length)
    
    return render(request, "search_length.html")

def search_prefix_page(request):
    if request.method == 'POST':
        prefix = str(request.POST.get('prefiks'))
        return search_prefix_function(request, prefix)

    return render(request, "search_prefix.html")

def search_suffix_page(request):
    if request.method == 'POST':
        suffix = str(request.POST.get('sufiks'))
        return search_suffix_function(request, suffix)
    
    return render(request, "search_suffix.html")

def show_definition(request, word):
    return render(request, "definition.html")

def search_length_function(request, length, max_length):
    words = Kata.objects.all()
    response = search_by_length(words, length, max_length)
    context = {'words' : response}
    return render(request, "result.html", context)

def search_prefix_function(request, prefix):
    words = Kata.objects.all()
    response = search_by_prefix(words, prefix)
    context = {'words' : response}
    return render(request, "result.html", context)

def search_suffix_function(request, suffix):
    words = Kata.objects.all()
    response = search_by_suffix(words, suffix)
    context = {'words' : response}
    return render(request, "result.html", context)

def search_words(request):
    # Example usage: http://localhost:8000/cari/?panjang=5&batas=10&prefiks=an&sufiks=i
    length = request.GET.get('panjang', None)
    max_length = request.GET.get('batas', None)
    prefix = request.GET.get('prefiks', None)
    suffix = request.GET.get('sufiks', None)
    print(length)
    response = []

    words = Kata.objects.all()

    if length:
        response = search_by_length(words, int(length), int(max_length))
        print(response)
    if prefix:
        if not(response):
            response = search_by_prefix(words, prefix)
        else:
            response = search_by_prefix(response, prefix)
    if suffix:
        if not(response):
            response = search_by_suffix(words, suffix)
        else:
            response = search_by_suffix(response, suffix)
    
    return HttpResponse(serializers.serialize("json", response), content_type="application/json")

def show_all_json(request):
    data = Kata.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_length(request, length):
    words = Kata.objects.all()
    response = search_by_length(words, length)
    return HttpResponse(serializers.serialize("json", response), content_type="application/json")

def show_json_by_start(request, prefix):
    words = Kata.objects.all()
    response = search_by_prefix(words, prefix)
    return HttpResponse(serializers.serialize("json", response), content_type="application/json")

def show_json_by_end(request, suffix):
    words = Kata.objects.all()
    response = search_by_suffix(words, suffix)
    return HttpResponse(serializers.serialize("json", response), content_type="application/json")