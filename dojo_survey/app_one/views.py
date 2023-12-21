from django.shortcuts import render, HttpResponse,redirect

# Create your views here.
def index(request):
    return render(request,'form.html')

def submit_survey(request):
    print("Got Post Info")
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']

    return redirect('/result')

def result(request):
    context = {
        'name':request.session['name'],
        'location':request.session['location'],
        'language':request.session['language'],
        'comment':request.session['comment'],
    }
    return render(request,'result.html',context)