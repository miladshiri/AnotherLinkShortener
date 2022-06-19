from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.urls import reverse
from django.utils.crypto import get_random_string
from .models import Link


@require_http_methods(["GET"])
def home(request):
    return render(request, 'core/home.html', {})

@require_http_methods(["POST"])
def make_shortlink(request):
    shorted_url = get_random_string(5)
    original_url = request.POST['original_url']

    new_link = Link(original_url=original_url, shorted_url=shorted_url)
    new_link.save()
    return JsonResponse({"success":True, "shorted_link":reverse('goto_shortlink', args=[shorted_url])}, status=200)


@require_http_methods(["GET"])
def goto_shortlink(request, slug):
    link = Link.objects.get(shorted_url=slug)
    return redirect(link.original_url)