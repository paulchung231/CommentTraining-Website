# Generated by Django 2.1.2 on 2019-04-11 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.CharField(max_length=5000)),
                ('number_of_ratings', models.IntegerField(default=0)),
                ('rating_1', models.IntegerField(default=0)),
                ('rating_2', models.IntegerField(default=0)),
                ('rating_3', models.IntegerField(default=0)),
                ('mean_rating', models.DecimalField(decimal_places=3, default=0, max_digits=10)),
            ],
        ),
    ]
