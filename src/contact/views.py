from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from .forms import contactForm

# Create your views here.
def contact(request):
    form = contactForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        subject = 'Message from QPG93 PythonAnywhere.com'
        emailFrom = form.cleaned_data['email']
        emailTo = [settings.EMAIL_HOST_USER]
        message = '%s\n%s\n%s' % (comment, emailFrom, name)
        send_mail(subject, message, emailFrom, emailTo, fail_silently=False)

    context = locals()
    template = 'contact.html'
    return render(request, template, context)