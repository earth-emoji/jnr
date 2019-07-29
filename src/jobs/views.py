from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.http import JsonResponse

from .forms import JobForm
from .models import Job
from accounts.models import Employer
from users.decorators import employer_required


def public_jobs(request):
    jobs = Job.objects.all()
    data = {
        'jobs': jobs
    }
    return render(request, 'jobs/public_job_list.html', data)

def public_job_view(request, slug):
    job = get_object_or_404(Job, slug=slug)
    return render(request, 'jobs/public_job_view.html', {'job': job})

@login_required
@employer_required
def employer_job_view(request, slug):
    job = get_object_or_404(Job, slug=slug)
    form = JobForm(instance=job)
    if not job.creator.id == request.user.employer.id:
        return JsonResponse("It is not yours ! You are not permitted !", status=403)
    return render(request, 'jobs/employer_job_view.html', {'job': job, 'form': form})


@login_required
@employer_required
def employer_job_update(request, slug):
    job = get_object_or_404(Job, slug=slug)
    if not job.creator.id == request.user.employer.id:
        return JsonResponse("It is not yours ! You are not permitted !", status=403)
    if request.POST:
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            c = form.save(commit=False)
            data = {
                'success': True,
                'name': c.name,
                'description': c.description,
                'positions': c.positions_to_fill
            }
            c.save()
            return JsonResponse(data)
        else:
            return JsonResponse({'error':form.errors})
    return JsonResponse("")

@login_required
@employer_required
def employer_jobs(request, slug):
    creator = Employer.objects.get(slug=slug, user=request.user)
    jobs = Job.objects.filter(creator=creator)
    return render(request, 'jobs/employer_job_list.html', {'jobs': jobs})

@login_required
@employer_required
def create_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            c = form.save(commit=False)
            c.creator = request.user.employer
            c.save()
            return redirect('employers:employer-jobs', request.user.employer.slug)
    else:
        form = JobForm()
    return render(request, 'jobs/job_form.html', {'form': form})
