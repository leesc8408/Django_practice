from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import MovieForm
from .models import Movie

# Create your views here.
def index(request):
    reviews = Movie.objects.all()
    context = {
        "reviews": reviews,
    }
    return render(request, "day02/index.html", context)


def create(request):
    if request.method == "POST":
        m_form = MovieForm(request.POST)
        if m_form.is_valid():
            m_form.save()
            return redirect("day02:index")
    else:
        m_form = MovieForm()
    context = {
        "m_form": m_form,
    }
    return render(request, "day02/create.html", context)


def detail(request, pk):
    review = Movie.objects.get(pk=pk)
    context = {
        "review": review,
    }
    return render(request, "day02/detail.html", context)


def delete(request, pk):
    review = Movie.objects.get(pk=pk)
    review.delete()
    return redirect("day02:index")


def update(request, pk):
    review = Movie.objects.get(pk=pk)
    if request.method == "POST":
        m_form = MovieForm(request.POST, instance=review)
        if m_form.is_valid():
            m_form.save()
            return redirect("day02:detail", review.pk)
    else:
        m_form = MovieForm(instance=review)
    context = {
        "m_form": m_form,
    }
    return render(request, "day02/update.html", context)
