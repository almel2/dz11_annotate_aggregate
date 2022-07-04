from django.contrib import messages
from django.shortcuts import render, redirect
from celery_app.forms import ReminderForm
from celery_app.tasks import send_mail_reminder


def reminder(request):
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            reminder = form.cleaned_data.get('reminder')
            detetime = form.cleaned_data.get('datetime')
            send_mail_reminder.apply_async(('Alex_primer', reminder, [email, ]), eta=detetime)
            messages.success(request, 'Reminder cool done !!')
            messages.add_message(request, messages.SUCCESS, 'Reminder Done')
            return redirect('celery_reminder')
    else:
        form = ReminderForm()
    return render(request, 'celery_app/reminder.html', {'form': form})
