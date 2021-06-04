from wsgiref.util import FileWrapper
from django.conf import settings
from django.http import HttpResponse,HttpResponseRedirect
import os
from plotly.offline import plot
from plotly.graph_objs import Bar
from django.db.models import Avg



from django.shortcuts import render
from e_lms.models import Subject, Material, Survey, SurveyForm

# Create your views here.
def index(request):
    return render(request, "index.html")

def list_class(request):
    
    data = Subject.objects.all()
    context = {
        'course_list' : data
    }
    return render(request, "listclass.html", context)

def survey(request):
    return render(request, "survey.html")

def course(request):
    
    subject_code = request.GET.get('s')
    subject_query = Subject.objects.get(subject_id=subject_code)
    data = Material.objects.all().filter(subject_id=subject_code).order_by("upload_date")
    context = {
            'subject_id' : subject_query.subject_id,
            'subject_name' : subject_query.subject_name,
            'subject_description' : subject_query.subject_description,
            'material_list' : data,
    }
    return render(request, 'coursedetail.html', context)

def download(request):
    try:
        file_to_download = request.GET.get('f')
        file_path = settings.MEDIA_ROOT + "/" + file_to_download
        wrapper = FileWrapper(open(file_path, 'rb'))
        response = HttpResponse(wrapper, content_type='application/force-download')
        response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
        return response
    except Exception as e:
        return HttpResponse("Error downloading file "+str(e))

def survey(request):
    if request.method == 'POST':
        form=SurveyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/result/')

    context = {
        'form' : SurveyForm,
    }
    return render(request, "survey.html", context)

def survey_result(request):
    
    average_age = Survey.objects.all().aggregate(Avg('age'))['age__avg']
    
    x_data = ["Songkhla", "Yala", "Pattani", "Satul"]
    y_data = [
        Survey.objects.filter(province='Songkhla').count(),
        Survey.objects.filter(province='Yala').count(),
        Survey.objects.filter(province='Pattani').count(),
        Survey.objects.filter(province='Satul').count(),
    ]
    age_chart = plot([Bar(x=x_data, y=y_data)], output_type='div')

    context={
        'average_age' : average_age, 
        'age_chart': age_chart,
        'all_items' :  Survey.objects.all(),
    }
    return render(request, "surveyresult.html", context)
