# Generated by Django 3.0.3 on 2020-02-16 01:12

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('iftar', '0002_auto_20200215_1930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donor',
            name='id',
        ),
        migrations.AddField(
            model_name='donor',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='donor',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='donor',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='donor',
            name='need',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='iftar.Need'),
        ),
    ]
