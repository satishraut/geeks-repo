from .views import get_jobs, subscribe,get_job

from django.urls import path

urlpatterns = [
    path('jobs/', get_jobs, name="jobs_view"),
    path('jobs/<int:id>', get_job, name="job_view"),
    path('jobs/<int:id>/subscribe', subscribe, name="subscribe_view"),
]
