from django.forms import ModelForm
from polls.models import Store


class AddStoreForm(ModelForm):
    class Meta:
        model = Store
        fields = ['name', 'book']