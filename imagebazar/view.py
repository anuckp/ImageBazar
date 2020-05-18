from django.http import HttpResponse

def show_about_page(request):
    return HttpResponse("hi this is about page")