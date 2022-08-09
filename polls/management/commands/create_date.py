from django.core.management.base import BaseCommand
from faker import Faker
from random import randint, choice
from polls.models import Author, Publisher, Book, Store


class Command(BaseCommand):
    help = 'This command create date, has one argument "count_date"'

    def add_arguments(self, parser):
        parser.add_argument('count_data', type=int)

    def handle(self, *args, **options):
        fake = Faker()
        num = options['count_data']

        list_obj_author = []
        for _ in range(num):
            author = Author(name=fake.name(), age=randint(30, 70))
            list_obj_author.append(author)
        Author.objects.bulk_create(list_obj_author)
        authors_id = Author.objects.values_list('id', flat=True)

        list_obj_publisher = []
        for _ in range(num):
            publisher = Publisher(name=fake.company())
            list_obj_publisher.append(publisher)
        Publisher.objects.bulk_create(list_obj_publisher)
        publishers_id = Publisher.objects.values_list('id', flat=True)

        list_obj_book = []
        for _ in range(num):
            book = Book(
                name=fake.last_name(),
                page=randint(400, 1200),
                price=randint(100, 500),
                rating=randint(0, 10),
                publisher_id=choice(publishers_id),
                pubdate=fake.date(),
            )
            list_obj_book.append(book)
        Book.objects.bulk_create(list_obj_book)
        dooks_id = Book.objects.values_list('id', flat=True)

        for book in Book.objects.all():
            random_authors_id = set([choice(authors_id) for _ in range(randint(1, 10))])
            book.authors.add(*random_authors_id)

        list_obj_store = []
        for _ in range(num):
            store = Store(name=fake.company())
            list_obj_store.append(store)
        Store.objects.bulk_create(list_obj_store)

        for store in Store.objects.all():
            random_books_id = set([choice(dooks_id) for _ in range(randint(1, 10))])
            store.book.add(*random_books_id)

        length = len(authors_id)
        self.stdout.write(self.style.SUCCESS(f'Success create date count {length}'))
