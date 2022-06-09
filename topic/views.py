from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Marks
from .models import Skill


def index(request):
    mymarks = Marks.objects.all().values()
    mysk = Skill.objects.all().values()
    temp = loader.get_template('assign.html')
    context = {
        'mymarks': mymarks,
        'myskills': mysk,
    }
    return HttpResponse(temp.render(context, request))

