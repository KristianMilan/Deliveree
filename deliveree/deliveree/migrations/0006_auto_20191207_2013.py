# Generated by Django 2.2.7 on 2019-12-08 01:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deliveree', '0005_choice_question'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
