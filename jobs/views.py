from django.shortcuts import render, get_object_or_404
from .models import Job, Application

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

def job_detail(request, id):
    job = get_object_or_404(Job, id=id)

    if request.method == "POST":
        Application.objects.create(job=job)
        return render(request, 'jobs/job_detail.html', {
            'job': job,
            'message': "Application submitted successfully!"
        })

    return render(request, 'jobs/job_detail.html', {'job': job})