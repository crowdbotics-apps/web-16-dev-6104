# Generated by Django 2.2.13 on 2020-06-16 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200616_0719'),
    ]

    operations = [
        migrations.AddField(
            model_name='customtext',
            name='hfkhfkjh',
            field=models.ManyToManyField(blank=True, related_name='customtext_hfkhfkjh', to='home.HomePage'),
        ),
        migrations.AddField(
            model_name='customtext',
            name='nvgkhvjhv',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customtext_nvgkhvjhv', to='home.HomePage'),
        ),
    ]
