from django.urls import path
from . import views
urlpatterns = [
    path('',views.HomePageView),
    path('<int:id>',views.SurveyView.as_view())
]