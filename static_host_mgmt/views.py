from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView, ListView, TemplateView

from .models import IssueModel

# Create your views here.
class IssueCreate(CreateView):
    model = IssueModel
    template_name = 'issue_create.html'
    fields = '__all__'
    initial = {'status': 'New'}

class IssueUpdate(UpdateView):
    model = IssueModel
    fields = ['host', 'odo_link', 'description', 'status']
    fields = '__all__'
    template_name = 'issue_update.html'

class IssueDetail(DetailView):
    model = IssueModel
    template_name = 'issue_detail.html'

class IssueOverView(ListView):
    model = IssueModel
    template_name = 'issue_overview.html'

    def get_queryset(self):
        return IssueModel.objects.all()

class HomeView(TemplateView):
    template_name = 'home.html'
