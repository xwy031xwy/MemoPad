from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world. You're at the memo’s index.")
class Home(generic.TemplateView):
    template_name = 'home.html'
    def get(self, request, *args, **kwargs):
        context = super(Home, self).get_context_data()
        context.update({'my_message': 'Welcome to my site'})
        return render(request, 'home.html', context)