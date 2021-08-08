from django.shortcuts import render
def index(request):
    # list out objects 
    # could be search
    qs = None
    template_name = 'Department/index.html'
    context = {'object_list': qs}
    return render(request, template_name, context) 

# Create your views here.
