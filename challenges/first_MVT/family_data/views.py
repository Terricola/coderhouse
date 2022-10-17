from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import date, datetime
from family_data.models import BasicData


# Create your views here.
#format = "%d-%m-%Y""
def add_data(
    request,
    name: str,
    last_name: str,
    age: int,
    birth_date: datetime, # datetime.strftime()
    ):

    template = loader.get_template("index_data.html")
    birth_date = datetime.strptime(birth_date, "%d-%m-%Y")
    basic_data = BasicData(name=name, last_name=last_name, age=age, birth_date=birth_date)
    basic_data.save()

    context_dict = {"basic_data": basic_data}
    render = template.render(context_dict)
    return HttpResponse(render)

def show_data(request):
    event_list = BasicData.objects.all()
    template = loader.get_template("index_family.html")
    context_dict = {"event_list": event_list}
    render = template.render(context_dict)
    return HttpResponse(render)


    # event_list = BasicData.objects.all()
    # return render(request, "Templates/index_family.html",
    #             {"even_list": event_list})