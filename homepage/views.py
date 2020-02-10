from django.http import HttpResponse
from django.template import loader

def policy(request):
    template = loader.get_template('homepage/policy.html')
    return HttpResponse(template.render())

def answers(request):
    template = loader.get_template('homepage/answers.html')
    return HttpResponse(template.render())