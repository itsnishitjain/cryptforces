from django.shortcuts import render
from cryptic.models import Question
from django.http import HttpResponse
# Create your views here.
def problem(request, problem_id):
    if request.method == 'POST':
        problem = Question.objects.get(id=problem_id)
        answer = request.POST['answer']
        if problem.answer == answer:
            return render(request, 'problem.html', {'problem': problem, 'toast': "Correct"})
        else:
            return render(request, 'problem.html', {'problem': problem, 'toast': "Incorrect"})
    problem = Question.objects.get(id=problem_id)
    return render(request, 'problem.html', {'problem': problem})


def all_problems(request):
    problems = Question.objects.all()
    return render(request, 'all_problems.html', {'problems': problems})