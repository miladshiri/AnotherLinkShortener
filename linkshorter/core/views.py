from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.urls import reverse
from django.db.models.aggregates import Count

from .models import Link, Clicked
from .forms import ShortLinkForm


@require_http_methods(["GET"])
def home(request):
    return render(request, 'core/home.html', {'form':ShortLinkForm()})

@require_http_methods(["POST"])
def make_shortlink(request):
    form = ShortLinkForm(request.POST)
    if form.is_valid():
        new_link = form.save()

        new_link.save()
        print(new_link.detail_url)
        return JsonResponse({"success":True, 
                            "shorted_link":reverse('goto_shortlink', args=[new_link.shorted_url]),
                            "detail_link":reverse('detail', args=[new_link.detail_url])}, status=200)
    return JsonResponse({"success":False}, status=400)


@require_http_methods(["GET"])
def goto_shortlink(request, slug):
    link = get_object_or_404(Link, shorted_url=slug)
    clicked = Clicked(link=link)
    clicked.save()
    return redirect(link.original_url)

@require_http_methods(["GET"])
def detail(request, slug):
    clicks = Clicked.objects.filter(link__detail_url=slug).extra(select={'day': "TO_CHAR(click_date, 'YYYY-MM-DD')"}).values('day').annotate(count=Count('click_date__date'))
    return render(request, 'core/detail.html', {'clicks':clicks})