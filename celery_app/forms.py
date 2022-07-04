from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta
from django import forms


class ReminderForm(forms.Form):
    email = forms.EmailField(label='Emaile')
    reminder = forms.CharField(widget=forms.Textarea)
    datetime = forms.DateTimeField(
        widget=forms.widgets.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%d/%m/%Y %H:%M'],
    )

    def clean_datetime(self):
        time = timezone.now()
        date = self.cleaned_data['datetime']
        day_2 = time + timedelta(hours=48)
        if date < time :
            raise ValidationError('Your datetime is less than datetime now')
        elif date > day_2:
            raise ValidationError('Your datetime is more than 48 hours')
        return date
