# Generated by Django 3.0.6 on 2020-10-02 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200930_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='end_date',
            field=models.DateTimeField(null=True),
        ),
    ]
