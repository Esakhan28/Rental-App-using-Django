# Generated by Django 3.0.5 on 2020-08-08 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_auto_20200806_1312'),
    ]

    operations = [
        migrations.CreateModel(
            name='Additions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insurance', models.IntegerField(blank=True, null=True)),
                ('fuel', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
