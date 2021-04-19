from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

from django.template import loader

from .models import JVDjangoDBModel

from tic_tac_toe.problem_domain import databaseMapper

def index(request):
    context = None
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))

def refresh(request, id_user):
    register = JVDjangoDBModel(id_user)
    try:
        register = JVDjangoDBModel.objects.get(pk=id_user)
    except:
        register.save()
    finally:
        mapper = databaseMapper.DatabaseMapper(register)
        response_data = mapper.getState()
        return JsonResponse(response_data, safe=False)

def click(request, id_user, line, column):
    register = JVDjangoDBModel(id_user)
    try:
        register = JVDjangoDBModel.objects.get(pk=id_user)
    except:
        register.save()
    finally:
        mapper = databaseMapper.DatabaseMapper(register)
        response_data = mapper.click_position(line, column)
        return JsonResponse(response_data, safe=False)