from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.urls import reverse
from django.db.models.aggregates import Count
from django.contrib.sites.shortcuts import get_current_site
from .models import Link, Click
from .forms import ShortLinkForm


## This view renders the home page
@require_http_methods(["GET"])
def home(request):
    
    return render(request, 'core/home.html', {'form':ShortLinkForm()})


## This view creates the short link
@require_http_methods(["POST"])
def make_shortlink(request):
    form = ShortLinkForm(request.POST)
    if form.is_valid():
        new_link = form.save()

        new_link.save()
        return JsonResponse({"success":True, 
                            "shorted_link":reverse('goto_shortlink', args=[new_link.shorted_url]),
                            "detail_link":reverse('detail', args=[new_link.detail_url])}, status=200)
    return JsonResponse({"success":False}, status=400)


## This view redirects to the original link
@require_http_methods(["GET"])
def goto_shortlink(request, slug):
    link = get_object_or_404(Link, shorted_url=slug)
    click = Click(link=link)
    click.save()
    return redirect(link.original_url)


## This view render the details and a chart for the link
@require_http_methods(["GET"])
def detail(request, slug):
    labels = []
    data = []
    
    link = get_object_or_404(Link, detail_url=slug)
    link.shorted_url = 'http://' + get_current_site(request).domain + reverse('goto_shortlink', args=[link.shorted_url])
    link.detail_url = 'http://' + get_current_site(request).domain + reverse('detail', args=[link.detail_url])
    
    clicks = Click.objects.filter(link__detail_url=slug).extra(select={'day': "TO_CHAR(click_date, 'YYYY-MM-DD')"}).values('day').annotate(count=Count('click_date__date'))
    
    for click in clicks:
        labels.append(click['day'])
        data.append(click['count'])
    return render(request, 'core/link_detail.html', {'labels':labels, 'data':data, 'link':link})


## This view handles the link deletion functionality
@require_http_methods(["GET", "POST"])
def confirm_delete(request, id):
    link = get_object_or_404(Link, id=id)
    
    if request.method == 'GET':
        return render(request, 'core/link_confirm_delete.html', {'link':link})
    
    if request.method == 'POST':
        link.delete()
        return render(request, 'core/link_delete_successful.html')