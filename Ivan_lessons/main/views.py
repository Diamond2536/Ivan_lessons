from django.shortcuts import render, get_object_or_404
from .models import Lesson, Comments


def index(request):
    lessons = Lesson.objects.all()
    return render(request, 'index.html', {'lessons':lessons})


def lesson(request, id, slug):
    lesson = get_object_or_404(Lesson, id=id, slug=slug)
    comments = Comments.objects.filter(lesson = lesson)
    if request.method == "POST":
        user_name = request.POST.get("user_name", False)
        text = request.POST.get("text", False)
        new_comment = Comments(user = user_name, text = text, lesson = lesson)
        new_comment.save()
    return render(request, 'lesson.html', {'lesson':lesson, 'comments':comments})

