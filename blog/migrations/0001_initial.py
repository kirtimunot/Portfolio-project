# Generated by Django 3.0.4 on 2020-05-24 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('pub_date', models.DateField()),
                ('body', models.CharField(max_length=1000)),
                ('image', models.ImageField(upload_to='media/')),
            ],
        ),
    ]