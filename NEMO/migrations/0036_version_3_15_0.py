# Generated by Django 2.2.26 on 2022-02-07 19:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

from NEMO.migrations_utils import create_news_for_version


class Migration(migrations.Migration):

    dependencies = [
        ('NEMO', '0035_version_3_14_0'),
    ]

    def new_version_news(apps, schema_editor):
        create_news_for_version(apps, "3.15.0")

    operations = [
        migrations.RunPython(new_version_news),
        migrations.CreateModel(
            name='StaffAbsenceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of this absence type.', max_length=255)),
                ('description', models.CharField(help_text='The description for this absence type.', max_length=255)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='StaffAvailability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, help_text='The category for this staff member.', max_length=100, null=True)),
                ('start_time', models.TimeField(blank=True, help_text='The usual start time for this staff member.', null=True)),
                ('end_time', models.TimeField(blank=True, help_text='The usual end time for this staff member.', null=True)),
                ('monday', models.BooleanField(default=True, help_text='Check this box if the staff member usually works on Mondays.')),
                ('tuesday', models.BooleanField(default=True, help_text='Check this box if the staff member usually works on Tuesdays.')),
                ('wednesday', models.BooleanField(default=True, help_text='Check this box if the staff member usually works on Wednesdays.')),
                ('thursday', models.BooleanField(default=True, help_text='Check this box if the staff member usually works on Thursdays.')),
                ('friday', models.BooleanField(default=True, help_text='Check this box if the staff member usually works on Fridays.')),
                ('saturday', models.BooleanField(default=False, help_text='Check this box if the staff member usually works on Saturdays.')),
                ('sunday', models.BooleanField(default=False, help_text='Check this box if the staff member usually works on Sundays.')),
                ('staff_member', models.ForeignKey(help_text='The staff member to display on the staff status page.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Staff availability',
                'ordering': ['staff_member__first_name'],
            },
        ),
        migrations.CreateModel(
            name='StaffAbsence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_time', models.DateTimeField(auto_now_add=True, help_text="The date and time when the absence was created.")),
                ('start_date', models.DateField(help_text='The start date of the absence.')),
                ('end_date', models.DateField(help_text='The end date of the absence.')),
                ('full_day', models.BooleanField(default=True, help_text='Uncheck this box when the absence is only for part of the day.')),
                ('description', models.TextField(blank=True, help_text='The absence description.', null=True)),
                ('absence_type', models.ForeignKey(help_text='The absence type. This will only be visible to facility managers.', on_delete=django.db.models.deletion.CASCADE, to='NEMO.StaffAbsenceType')),
                ('staff_member', models.ForeignKey(help_text='The staff member who will be absent.', on_delete=django.db.models.deletion.CASCADE, to='NEMO.StaffAvailability')),
            ],
            options={
                'ordering': ['-creation_time']
            }
        ),
    ]
