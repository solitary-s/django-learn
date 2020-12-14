# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Subject(models.Model):
    no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    intro = models.CharField(max_length=1000)
    is_hot = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tb_subject'


class Teacher(models.Model):
    no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    sex = models.IntegerField()
    birth = models.DateField()
    intro = models.CharField(max_length=1000)
    photo = models.CharField(max_length=255)
    good_count = models.IntegerField()
    bad_count = models.IntegerField()
    subject = models.ForeignKey(Subject, models.DO_NOTHING, db_column='sno')

    class Meta:
        managed = False
        db_table = 'tb_teacher'
