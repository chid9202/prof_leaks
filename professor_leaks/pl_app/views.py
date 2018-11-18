from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render( request, 'index.html', {
        'name': "daehan"
    })


def school_list(request, search_school):
    # return HttpResponse("List page with %s." % search_school)

    return render( request, 'school_list.html', {
        'search_school': search_school,
    })

def school_detail(request, search_school):
    return render( request, 'school_detail.html', {
        'name': "daehan",
        'search_school': search_school,
    })
