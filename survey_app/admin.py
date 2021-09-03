from django.contrib import admin

from .models import Survey,Question,SurveyReports

admin.site.register(SurveyReports)


class QuestionInLineModel(admin.StackedInline):
    model = Question
    fields = ['survey','title','order','type','options']
    extra = 0


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    fields = ['title']
    inlines = [
        QuestionInLineModel,
    ]

