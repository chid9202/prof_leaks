from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.http import HttpResponse
from .models import Professor, Comment
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

def prof_list(request):
    college = "University of Southern California"
    prof_list = []
    Prof = Professor.objects.all()

    # Prof.objects.filter(college=college)

    # for p in Professor.objects.raw('SELECT fname, lname, dept FROM pl_app_Professor WHERE college = %s', [college]):
    #     prof_list.append(p)
    # name = p.prd_name
    return render(request, 'prof_list.html', {
        'prof_list': Prof
    })

def prof_detail(request, prof_name):
    # Cmt = Comment.objects.all().filter(rate=3)
    Cmt = Comment.objects.all()
    # Entry.objects.all().filter(pub_date__year=2006)

    return render(request, 'prof_detail.html', {
        'prof_name': prof_name,
        'comments': Cmt
    })
