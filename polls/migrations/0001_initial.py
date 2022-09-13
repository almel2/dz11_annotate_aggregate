# Generated by Django 4.0.5 on 2022-09-08 12:31

from django.db import migrations, models
import django.db.models.deletion
import polls.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('age', models.IntegerField()),
            ],
            options={
                'ordering': ['id'],
            },
            bases=(models.Model, polls.models.MyMeta),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('page', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('rating', models.FloatField()),
                ('pubdate', models.DateField()),
                ('authors', models.ManyToManyField(to='polls.author')),
            ],
            options={
                'ordering': ['id'],
            },
            bases=(models.Model, polls.models.MyMeta),
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
            options={
                'ordering': ['id'],
            },
            bases=(models.Model, polls.models.MyMeta),
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('book', models.ManyToManyField(to='polls.book')),
            ],
            options={
                'ordering': ['id'],
            },
            bases=(models.Model, polls.models.MyMeta),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.publisher'),
        ),
    ]
