from django.shortcuts import render
from cryptic.models import Question
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
# Create your views here.
def problem(request, problem_id):
    if request.method == 'POST':
        problem = Question.objects.get(id=problem_id)
        answer = request.POST['answer']
        if problem.answer == answer:
            user = request.user
            user.points += problem.points
            if problem not in user.question_solved.all():
                user.question_solved.add(problem)
            user.save()
            return render(request, 'problem.html', {'problem': problem, 'toast': "Correct"})
        else:
            return render(request, 'problem.html', {'problem': problem, 'toast': "Incorrect"})
    problem = Question.objects.get(id=problem_id)
    return render(request, 'problem.html', {'problem': problem})


@login_required
def all_problems(request):
    problems = Question.objects.all()
    return render(request, 'all_problems.html', {'problems': problems})