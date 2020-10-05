# Generated by Django 3.0.5 on 2020-10-05 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Category name')),
                ('description', models.TextField(blank=True, verbose_name='Descritpion')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of project', max_length=50, verbose_name='Project name')),
                ('description', models.TextField(help_text='Name of project', verbose_name='Project descripton')),
                ('date_of_create', models.DateField(blank=True, null=True, verbose_name='Date of create')),
                ('web_site', models.URLField(blank=True, verbose_name='Web site Address')),
                ('portfolio', models.ImageField(blank=True, default='', upload_to='', verbose_name='Cover_image')),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work.Category', verbose_name='Categories')),
            ],
        ),
    ]
