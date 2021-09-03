from django.shortcuts import render,HttpResponse,redirect
from .models import Survey,Question,SurveyReports
from django.views import generic
import json
def HomePageView(request):
    survey = Survey.objects.all()
    return render(request,'home-page.html',{"survey":survey})


# def SurveyView(request,id):
#     if request.method == "GET":
#         questions = Question.objects.filter(survey_id=id).order_by('order')
#         context = {
#             "Questions": questions,
#             "id": id
#         }
#         return render(request, 'survey-page.html', context)
#     if request.method == "POST":
#         queryDict = dict(request.POST)
#         queryDict.pop('csrfmiddlewaretoken')
#         data = json.dumps(queryDict)
#         report = SurveyReports(survey_id=id,answer=data)
#         report.save()
#         return redirect('/survey')

class SurveyView(generic.View):
    def get(self,request,id):
        questions = Question.objects.filter(survey_id=id).order_by('order')

        context = {
            "Questions": questions,
            "id": id,
        }
        return render(request, 'survey-page.html', context)

    def post(self,request,id):
        queryDict = dict(request.POST)
        queryDict.pop('csrfmiddlewaretoken')
        data = json.loads(json.dumps(queryDict))
        print(data)
        report = SurveyReports(survey_id=id, answer=data)
        report.save()
        return redirect('/survey')