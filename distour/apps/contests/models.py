from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime

def format_delta(delta):
    return str(delta)[:-7]

class Contest(models.Model):
    name = models.CharField(max_length=100, help_text="Enter a contest name (e.g. APIO2018, EJOI2009)")
    secretname = models.CharField(max_length=100, help_text="Enter a contest title (e.g. some japanese tasks)",blank=True)

    starting_time = models.DateTimeField(default=timezone.now,help_text="Enter a contest starting time")
    duration = models.DurationField(default=datetime.timedelta(hours=5),help_text="Entar a contest duration")
    ending_time = models.DateTimeField(default=(timezone.now() + datetime.timedelta(days=7)),help_text="Enter a contest ending time")

    def __str__(self):
        return self.name

    def is_running(self):
        return (self.starting_time <= timezone.now() and timezone.now() <= self.ending_time)

    def is_ended(self):
        return (timezone.now() > self.ending_time)

    def is_started(self):
        return (timezone.now() > self.starting_time)        

    def untill_start(self):
        return format_delta(self.starting_time - timezone.now())

    def untill_end(self):
        return format_delta(self.ending_time - timezone.now())

class Problem(models.Model):
    name = models.CharField(max_length=100, help_text="Enter a problem name (e.g. Arranging Shoes)")

    oj_id = models.CharField(max_length=100, help_text="Enter a oj.uz problem id (e.g. IOI19_shoes)")

    contest = models.ForeignKey(Contest, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.oj_id

class Participation(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    contest = models.ForeignKey(Contest, on_delete=models.SET_NULL, null=True)

    starting_time = models.DateTimeField(default=timezone.now)
    ending_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.user.username) + ':' + str(self.contest.name)

    def is_running(self):
        return (self.starting_time <= timezone.now() and timezone.now() <= self.ending_time)

    def is_ended(self):
        return (timezone.now() > self.ending_time)

    def is_started(self):
        return (timezone.now() > self.starting_time)        

    def untill_start(self):
        return format_delta(self.starting_time - timezone.now())

    def untill_end(self):
        return format_delta(self.ending_time - timezone.now())

    def js_ending_time(self):
        return self.ending_time.strftime('%Y-%m-%dT%H:%M:%SZ')





