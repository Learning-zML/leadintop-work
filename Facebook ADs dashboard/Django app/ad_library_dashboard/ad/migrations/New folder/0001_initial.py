# Generated by Django 4.0.5 on 2022-08-20 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('ad_id', models.TextField(blank=True, db_column='AD_ID', primary_key=True, serialize=False)),
                ('status', models.TextField(blank=True, db_column='Status', null=True)),
                ('started_date', models.TextField(blank=True, db_column='Started_date', null=True)),
                ('profile_pic', models.TextField(blank=True, null=True)),
                ('links', models.TextField(blank=True, null=True)),
                ('images', models.TextField(blank=True, null=True)),
                ('videos', models.TextField(blank=True, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('footer_text', models.TextField(blank=True, db_column='Footer_TEXT', null=True)),
                ('footer_action', models.TextField(blank=True, db_column='Footer_action', null=True)),
                ('page_name', models.TextField(blank=True, db_column='Page_name', null=True)),
                ('ad_occurance', models.IntegerField(blank=True, db_column='AD_occurance', null=True)),
                ('page_id_1', models.TextField(blank=True, db_column='Page_ID_1', null=True)),
                ('page_id_2', models.TextField(blank=True, db_column='Page_ID_2', null=True)),
                ('page_likes', models.IntegerField(blank=True, db_column='Page_likes', null=True)),
                ('insta_followers', models.IntegerField(blank=True, null=True)),
                ('ads_count', models.IntegerField(blank=True, db_column='Ads_count', null=True)),
                ('search_term', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ads',
                'managed': False,
            },
        ),
    ]
