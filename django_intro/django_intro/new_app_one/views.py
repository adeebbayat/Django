from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

def to_redirect(request):
    return redirect("first_route/redirected_route")

def redirected_route(request):
    return JsonResponse({"response" : "JSON response","status":True})
