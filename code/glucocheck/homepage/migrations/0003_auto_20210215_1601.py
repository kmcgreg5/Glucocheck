# Generated by Django 3.1.6 on 2021-02-15 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_auto_20210214_1612'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='user',
            new_name='username',
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.country')),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='homepage.country'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='homepage.state'),
        ),
    ]
