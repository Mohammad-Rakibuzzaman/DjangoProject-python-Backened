from django.http import HttpResponse


def home(request):
    return HttpResponse("This is a Home request")

def contact(request):
    return HttpResponse("This is a contact request")