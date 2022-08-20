# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Ads(models.Model):
    ad_id = models.TextField(db_column='AD_ID', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    status = models.TextField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    started_date = models.TextField(db_column='Started_date', blank=True, null=True)  # Field name made lowercase.
    profile_pic = models.TextField(blank=True, null=True)
    links = models.TextField(blank=True, null=True)
    images = models.TextField(blank=True, null=True)
    videos = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    footer_text = models.TextField(db_column='Footer_TEXT', blank=True, null=True)  # Field name made lowercase.
    footer_action = models.TextField(db_column='Footer_action', blank=True, null=True)  # Field name made lowercase.
    page_name = models.TextField(db_column='Page_name', blank=True, null=True)  # Field name made lowercase.
    ad_occurance = models.IntegerField(db_column='AD_occurance', blank=True, null=True)  # Field name made lowercase.
    page_id_1 = models.TextField(db_column='Page_ID_1', blank=True, null=True)  # Field name made lowercase.
    page_id_2 = models.TextField(db_column='Page_ID_2', blank=True, null=True)  # Field name made lowercase.
    page_likes = models.IntegerField(db_column='Page_likes', blank=True, null=True)  # Field name made lowercase.
    insta_followers = models.IntegerField(blank=True, null=True)
    ads_count = models.IntegerField(db_column='Ads_count', blank=True, null=True)  # Field name made lowercase.
    search_term = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ads'

