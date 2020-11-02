from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views import generic

from main.forms import CreateRequestForm


class UserRequestFormView(generic.FormView):
    form_class = CreateRequestForm
    template_name = 'form.html'

    def form_valid(self, form):
        # email = form.cleaned_data.get('email')
        form.save()
        return super(UserRequestFormView, self).form_valid(form)

    def get_success_url(self):
        return reverse('main:success')


def success(request):
    return render(request, "success.html")
