from django.http import HttpResponse

# Blank index page
def index(request):
    return HttpResponse("Hello world! <3")