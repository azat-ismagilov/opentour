from django.conf import settings
import requests
import datetime
from pytz import timezone
from bs4 import BeautifulSoup
import math
import pytz

from .models import Contest,Problem,Participation

oj_url = 'https://oj.uz/submissions?handle={0}&problem={1}&page={2}'

template_row = '<td class="{0}" title="{1}" rowspan="{2}" colspan="{3}" style="min-width: {4}px;{6}">{5}</td>'
template_row_header = '<td class="{0}" title="{1}" rowspan="{2}" colspan="{3}" style="min-width: {4}px;">{5}</td>'

def get_points(participation, problem):
    max_points=0
    for page in range(1, 100):
        url = oj_url.format(participation.user.username, problem.oj_id ,page)
        soup = BeautifulSoup(requests.get(url).text)
        
        submissions_list=soup.find('div', {'class':'table-responsive'}).find('tbody')
        
        submissions=submissions_list.find_all('tr')

        if not submissions:
            break

        for submission in submissions:
            points_str=submission.find('div', {'class':'text'}).text
            if points_str == 'Compilation error':
                continue
            points=int(points_str[:-6])
            time_str=submission.find('span', {'class':'render-datetime'}).text
            time=pytz.utc.localize(datetime.datetime.strptime(time_str,'%Y-%m-%dT%H:%M:%S Z'))
            if participation.starting_time <= time and time <= participation.ending_time:
                max_points=max(max_points, points)
    return max_points

def get_color(points):
    red = 240 + (144 - 240) * math.sqrt(points / 100);
    green = 128 + (238 - 128) * math.sqrt(points / 100);
    blue = 128 + (144 - 128) * math.sqrt(points / 100);
    return "background-color: rgb({}, {}, {}); ".format(red, green, blue)

def get_results(contest, problems, participations):
    results_tosort = []
    for i,participation in enumerate(participations):
        sum_points = 0
        points = []
        for problem in problems:
            point = get_points(participation=participation,problem=problem)
            sum_points += point 
            points.append(point)
        results_row = []
        results_row.append(template_row.format("", "", 1, 1, 50, {},""))
        results_row.append(template_row.format("", "", 1, 1, 200, participation.user.first_name + " " + participation.user.last_name,""))
        results_row.append(template_row.format("", "", 1, 1, 50, sum_points,""))
        for point,problem in zip(points,problems):
            results_row.append(template_row.format("gray", problem.name, 1, 1, 33, point, get_color(points=point)))
        results_row.append(template_row.format("gray", problem.name, 1, 1, 33, sum_points,""))
        results_tosort.append([sum_points, results_row])
    results_tosort.sort(reverse=True)
    position = 0
    last = -1
    results = []
    for i, res in enumerate(results_tosort):
        if res[0] != last:
            last = res[0]
            position = i + 1
        res[1][0] = res[1][0].format(position)
        results.append(res[1])
    #results.append(header)
    return results

def get_header(contest, problems):
    header = [] 
    #First line 
    header_row = []
    header_row.append(template_row_header.format("", "", 2, 1, 50, 'Place'))
    header_row.append(template_row_header.format("", "", 2, 1, 200, 'Name'))
    header_row.append(template_row_header.format("", "", 2, 1, 50, 'Points'))
    header_row.append(template_row_header.format("gray contest_title", "", 1, len(problems) + 1, 10, contest.name))
    header.append(header_row)
    ############
    #Second line
    header_row = []
    for i,problem in enumerate(problems):
        header_row.append(template_row_header.format("gray contest_title", problem.name, 1, 1, 33, chr(ord('A') + i)))
    header_row.append(template_row_header.format("gray contest_title", "", 1, 1, 33, 'Σ'))
    header.append(header_row)
    ############
    return header
