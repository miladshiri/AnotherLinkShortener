from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.urls import reverse
from .models import Link
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
    link = Link.objects.get(shorted_url=slug)
    return redirect(link.original_url)

@require_http_methods(["GET"])
def detail(request, slug):
    pass