from django.shortcuts import render

# Create your views here.
def index(request):
    # Strona główna aplikacji blogs
    return render(request, 'blogs/index.html')