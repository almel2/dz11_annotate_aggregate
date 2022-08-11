from django.forms import ModelForm
from polls.models import Store, Publisher


class AddStoreForm(ModelForm):
    class Meta:
        model = Store
        fields = ['name', 'book']


class PublisherAddForm(ModelForm):
    class Meta:
        model = Publisher
        fields = ['name']