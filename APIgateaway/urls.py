from django.urls import path
from .views import JobView, JobFilterView
app_name = 'APIgateway'

urlpatterns = [
    path('job/', JobView.as_view()),
    path('job/<int:page>', JobView.as_view()),
    path('job-filter/', JobFilterView.as_view()),
    path('job-filter/<int:page>', JobFilterView.as_view()),
]
