# from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic import View, TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inject']='BASIC INJECTION'
        return context



# class CBView(View):
#     def get(self, request):
#         return HttpResponse("CLASS BASED VIEWS ARE COOL!")
#
# # Create your views here.
# def index(request):
#     return render(request, 'index.html')
