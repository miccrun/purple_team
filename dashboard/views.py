
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, TemplateView, DetailView
from dashboard.models import Group, Event


class GroupInfoView(DetailView):
    template_name = 'dashboard/groupInfo.html'

    def get_object(self):
        return get_object_or_404(Group, pk=self.kwargs["group_id"])

    def get_events(self):
        event_list = Event.objects.filter(
            group_id=self.kwargs["group_id"],
        )
        return event_list

    def get_context_data(self, **kwargs):
        context = super(GroupInfoView, self).get_context_data(**kwargs)
        context['text'] = 'Hello World, Purple Team'
        context['events'] = self.get_events()
        return context


class ResultView(ListView):
    template_name = 'dashboard/result.html'
    paginate_by = 30

    def get_queryset(self):
        group_field = self.request.GET.get("group_name", None)

        return Group.objects.filter(
            group_name__icontains=group_field,
        )

    def get_context_data(self, **kwargs):
        context = super(ResultView, self).get_context_data(**kwargs)
        context['text'] = 'Hello World, Purple Team'
        return context


class DashboardView(TemplateView):
    template_name = 'dashboard/index.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['text'] = 'Hello World, Purple Team'
        return context
