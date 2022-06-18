from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'This command create date'

    def add_arguments(self, parser):
        parser.add_argument('count_date', type=int)

    def handle(self, *args, **options):
        pass
