# Generated by Django 4.0.5 on 2022-09-20 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='search_term',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_term', models.TextField(blank=True, null=True)),
                ('search_type', models.TextField(blank=True, choices=[('keyword', 'keyword'), ('page', 'page')], null=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'search_terms',
            },
        ),
        migrations.AddConstraint(
            model_name='search_term',
            constraint=models.UniqueConstraint(fields=('search_term', 'search_type'), name='only_one_search'),
        ),
    ]
