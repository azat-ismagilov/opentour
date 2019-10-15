from .models import Contest,Problem,Participation

template_row = '<td class="{0}" title="{1}" rowspan="{2}" colspan="{3}" style="min-width: {4}px;{6}">{5}</td>'
template_row_header = '<td class="{0}" title="{1}" rowspan="{2}" colspan="{3}" style="min-width: {4}px;">{5}</td>'

def get_points(participation, problem):
    return 100

def get_color(points):
    return "background-color: rgb(144, 238, 144); "

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
        results_row.append(template_row.format("", "", 2, 1, 50, {},""))
        results_row.append(template_row.format("", "", 2, 1, 200, participation.user.first_name + " " + participation.user.last_name,""))
        results_row.append(template_row.format("", "", 2, 1, 50, sum_points,""))
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
