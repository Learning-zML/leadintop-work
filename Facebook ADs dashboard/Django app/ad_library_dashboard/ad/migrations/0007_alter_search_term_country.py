# Generated by Django 4.0.5 on 2022-09-26 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0006_remove_search_term_only_one_search_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search_term',
            name='country',
            field=models.TextField(default='ALL'),
        ),
    ]