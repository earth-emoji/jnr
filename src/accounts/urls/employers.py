from django.urls import include, path

from accounts.views import employers
from jobs import views as jobs

urlpatterns = [
    path('employers/', include(([
        path('jobs-create/', jobs.create_job, name='create-job'),
        path('<uuid:slug>/', employers.employer_dashboard, name='dashboard'),
        path('<uuid:slug>/jobs/', jobs.employer_jobs, name='employer-jobs'),
    ], 'employers')))
]
