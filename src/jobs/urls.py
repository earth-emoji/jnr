from django.urls import include, path

from . import views

urlpatterns = [
    path('jobs/', include(([
        path('', views.public_jobs, name='all-jobs'),
        path('<uuid:slug>/view/', views.public_job_view, name="public-job-details"),
        path('<uuid:slug>/edit/', views.employer_job_view, name="employer-job-edit"),
        path('<uuid:slug>/update/', views.employer_job_update, name="employer-job-update")
    ], 'jobs'))),
]
