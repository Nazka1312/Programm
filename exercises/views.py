from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Exercise


def index(request):
    exercises = Exercise.objects.all()
    return render(request, 'exercises/index.html', {'exercises': exercises})


@login_required
def training_view(request):
    if request.method == 'POST':
        user_answer = request.POST.get('answer', '')
        exercise_id = request.POST.get('exercise_id')

        if exercise_id:
            try:
                exercise = Exercise.objects.get(id=exercise_id)
                is_correct = user_answer.lower().strip() == exercise.correct_answer.lower().strip()
                return render(request, 'exercises/training.html', {
                    'exercise': exercise,
                    'result': is_correct,
                })
            except Exercise.DoesNotExist:
                pass  # optionally log the issue here

    # GET-запрос или первый запуск — загружаем случайное упражнение
    exercise = Exercise.objects.order_by('?').first()

    if not exercise:
        return render(request, 'exercises/no_exercises.html')

    return render(request, 'exercises/training.html', {'exercise': exercise})