from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views import generic

from main.forms import CreateRequestForm, OnlineOfferForm


class UserRequestFormView(generic.FormView):
    form_class = CreateRequestForm
    template_name = 'form.html'

    def form_valid(self, form):
        # email = form.cleaned_data.get('email')
        form.save()

        return super(UserRequestFormView, self).form_valid(form)

    def get_success_url(self):
        message = "jkjskdjsd"
        return reverse('main:success', message)


def success(request):
    return render(request, "success.html")


class ContactPageView(generic.FormView):
    template_name = 'contact.html'
    form_class = OnlineOfferForm

    def get_success_url(self):
        return reverse('main:contact_url')

    def form_valid(self, form):
        send_mail('subject', 'message', 'sender@example.com', ['khojarbu@gmail.com'],
                  html_message='<b>Name: </b>' + form.cleaned_data.get('name') + '<br>' +
                               '<b>Subject: </b>' + form.cleaned_data.get('subject') + '<br>' +
                               '<b>Email: </b>' + form.cleaned_data.get('email') + '<br>' +
                               '<b>Message: </b>' + form.cleaned_data.get('message') + '<br>' +
                               '<b>Phone: </b>' + form.cleaned_data.get('phone') + '<br>'
                  )

        messages.add_message(self.request, messages.INFO, 'Thank you ! Your message has been sent.')
        return super().form_valid(form)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data()
    #     context['settings'] = SiteSettings.objects.first()
    #     return context
