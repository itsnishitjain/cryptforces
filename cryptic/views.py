from django.shortcuts import render
from cryptic.models import Question
from django.http import HttpResponse
# Create your views here.
def problem(request, problem_id):
    if request.method == 'POST':
        problem = Question.objects.get(id=problem_id)
        answer = request.POST['answer']
        if problem.answer == answer:
            return HttpResponse("Correct answer")
        else:
            return HttpResponse("Wrong answer")
    problem = Question.objects.get(id=problem_id)
    return render(request, 'problem.html', {'problem': problem})

def check_answer(request, problem_id):
    problem = Question.objects.get(id=problem_id)
    answer = request.POST['answer']
    if problem.answer == answer:
        return HttpResponse("Correct answer")
    else:
        return HttpResponse("Wrong answer")
