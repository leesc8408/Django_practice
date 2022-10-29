from django.shortcuts import render, redirect
from .models import Day01
from .forms import artsForm

# Create your views here.
def index(request):
    articles = Day01.objects.order_by("-pk")
    context = {
        "articles": articles,
    }
    return render(request, "day01/index.html", context)


# def new(request):
#     arts_form = artsForm()
#     context = {
#         "arts_form": arts_form,
#     }
#     return render(request, "day01/new.html", context)


def create(request):
    if request.method == "POST":
        arts_form = artsForm(request.POST)
        if arts_form.is_valid():
            arts_form.save()
            return redirect("day01:index")
    else:
        arts_form = artsForm()
    context = {
        "arts_form": arts_form,
    }
    return render(request, "day01/new.html", context)


def detail(request, pk):
    article = Day01.objects.get(pk=pk)

    context = {
        "arts": article,
    }
    return render(request, "day01/detail.html", context)


def delete(request, pk):
    article = Day01.objects.get(pk=pk)
    article.delete()
    return redirect("day01:index")


def update(request, pk):
    article = Day01.objects.get(pk=pk)
    if request.method == "POST":
        arts_form = artsForm(request.POST, instance=article)
        if arts_form.is_valid():
            arts_form.save()
            return redirect("day01:detail", article.pk)
    else:
        arts_form = artsForm(instance=article)
    context = {
        "arts_form": arts_form,
        "arts": article,
    }
    return render(request, "day01/update.html", context)
