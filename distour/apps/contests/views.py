from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your views here.

from .models import Contest,Problem,Participation
from .results import get_results,get_header


def index(request):
    contests=Contest.objects.all()

    return render(request, 'contests/list.html', context={'contests':contests})

def detail(request, contest_id):
    try: 
        contest=Contest.objects.get(id = contest_id)
    except:
        raise Http404("Contest not found")
    if not request.user.is_authenticated:
    	return render(request, 'contests/detail_unlogined.html', context={'contest':contest})
    try:
        participation=contest.participation_set.get(user=request.user,contest=contest)
    except:
        return render(request, 'contests/detail_logined.html', context={'contest':contest})
    problems=contest.problem_set.all() 
    return render(request, 'contests/detail_started.html', context={'contest':contest,'problems':problems,'participation':participation})

def results(request, contest_id):
    try: 
        contest=Contest.objects.get(id=contest_id)
    except:
        raise Http404("Contest not found")
    problems=contest.problem_set.all() 
    participations=contest.participation_set.all()
    results = get_results(contest=contest,problems=problems,participations=participations) 
    header=get_header(contest=contest,problems=problems)
    if contest.is_ended():
        return render(request, 'contests/results.html',context={'contest':contest,'header':header,'results':results})
    else:
        try:
            participation=contest.participation_set.get(user=request.user,contest=contest)
        except:
            return render(request, 'contests/results_error.html',context={'contest':contest})
        if not participation.is_ended:
            return render(request, 'contests/results_error.html',context={'contest':contest})
        else:
            return render(request, 'contests/results.html',context={'contest':contest,'header':header,'results':results})

def start_vc(request, contest_id):
    try: 
        contest=Contest.objects.get(id=contest_id)
    except:
        raise Http404("Contest not found")
    if not request.user.is_authenticated:
        return render(request, 'contests/detail_unlogined.html', context={'contest':contest})
    try:
        participation=contest.participation_set.get(user=request.user,contest=contest)
    except:
        if timezone.now() < contest.ending_time:
            contest.participation_set.create(user=request.user,contest=contest,starting_time=timezone.now(),ending_time=min(contest.ending_time, timezone.now() + contest.duration))
    return HttpResponseRedirect(reverse('contests:detail', args = (contest_id,)))

def sign_up(request):
    return render(request, 'registration/sign_up.html')




