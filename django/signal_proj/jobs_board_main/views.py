from django.shortcuts import render

from django.http import HttpResponse


from .models import Job, Subscriber, Subscription
from .signals import new_subscriber


# Create your views here.
def get_jobs(request):
    jobs = Job.objects.all()

    return render(request, 'jobs_board_main/jobs.html', {'jobs': jobs})


def get_job(request, id):
    job = Job.objects.get(pk=id)
    return render(request, 'jobs_board_main/job.html', {'job': job})


def subscribe(request, id):
    job = Job.objects.get(pk=id)
    subscriber = Subscriber(email=request.POST.get('email'))
    subscriber.save()

    subscription = Subscription(user=subscriber, job=job, email=subscriber.email)
    subscription.save()

    new_subscriber.send(sender=subscription, job=job, subscriber=subscriber)

    payload = {
      'job': job,
      'email': request.POST['email']
    }
    return render(request, 'jobs_board_main/subscribed.html', {'payload': payload})
