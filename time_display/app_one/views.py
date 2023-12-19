from django.shortcuts import render, HttpResponse
from time import gmtime, strftime
# Create your views here.
def index(request):
    context = {
        "time":strftime("%Y-%m-%d %H:%M %p",gmtime()),
        "new_time":strftime("%b %d, %Y",gmtime()),
        "new_hour":strftime("%I:%M %p")
    }
    return render(request,'index.html',context)