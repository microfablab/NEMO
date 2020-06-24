# Generated by Django 2.2.10 on 2020-06-03 19:50

import django.db.models.deletion
import mptt
import mptt.fields
import mptt.managers
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NEMO', '0019_user_type_not_required'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='area',
            options={},
        ),
        migrations.AddField(
            model_name='area',
            name='level',
            field=models.PositiveIntegerField(default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='area',
            name='lft',
            field=models.PositiveIntegerField(default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='area',
            name='rght',
            field=models.PositiveIntegerField(default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='area',
            name='tree_id',
            field=models.PositiveIntegerField(db_index=True, default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='area',
            name='category',
            field=models.CharField(blank=True, db_column='category', help_text='Create sub-categories using slashes. For example "Category 1/Sub-category 1".', max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='area',
            name='parent_area',
            field=mptt.fields.TreeForeignKey(blank=True, help_text='Select a parent area, (building, floor etc.)', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='area_children_set', to='NEMO.Area'),
        ),
        migrations.AddField(
            model_name='area',
            name='logout_grace_period',
            field=models.PositiveIntegerField(blank=True, help_text='Number of minutes users have to logout of this area after their reservation expired before being flagged and abuse email is sent.', null=True),
        ),
        migrations.AddField(
            model_name='area',
            name='maximum_future_reservation_time',
            field=models.PositiveIntegerField(blank=True, db_column='maximum_future_reservation_time', help_text='The maximum amount of time (in minutes) that a user may reserve from the current time onwards.', null=True),
        ),
        migrations.AddField(
            model_name='area',
            name='maximum_reservations_per_day',
            field=models.PositiveIntegerField(blank=True, db_column='maximum_reservations_per_day', help_text='The maximum number of reservations a user may make per day for this area.', null=True),
        ),
        migrations.AddField(
            model_name='area',
            name='maximum_usage_block_time',
            field=models.PositiveIntegerField(blank=True, db_column='maximum_usage_block_time', help_text='The maximum amount of time (in minutes) that a user may reserve this area for a single reservation. Leave this field blank to indicate that no maximum usage block time exists for this area.', null=True),
        ),
        migrations.AddField(
            model_name='area',
            name='minimum_time_between_reservations',
            field=models.PositiveIntegerField(blank=True, db_column='minimum_time_between_reservations', help_text='The minimum amount of time (in minutes) that the same user must have between any two reservations for this area.', null=True),
        ),
        migrations.AddField(
            model_name='area',
            name='minimum_usage_block_time',
            field=models.PositiveIntegerField(blank=True, db_column='minimum_usage_block_time', help_text='The minimum amount of time (in minutes) that a user must reserve this area for a single reservation. Leave this field blank to indicate that no minimum usage block time exists for this area.', null=True),
        ),
        migrations.AddField(
            model_name='area',
            name='missed_reservation_threshold',
            field=models.PositiveIntegerField(blank=True, db_column='missed_reservation_threshold', help_text='The amount of time (in minutes) that a area reservation may go unused before it is automatically marked as "missed" and hidden from the calendar. Usage can be from any user, regardless of who the reservation was originally created for. The cancellation process is triggered by a timed job on the web server.', null=True),
        ),
        migrations.AddField(
            model_name='area',
            name='policy_off_between_times',
            field=models.BooleanField(db_column='policy_off_between_times', default=False, help_text='Check this box to disable policy rules every day between the given times'),
        ),
        migrations.AddField(
            model_name='area',
            name='policy_off_end_time',
            field=models.TimeField(blank=True, db_column='policy_off_end_time', help_text='The end time when policy rules should NOT be enforced', null=True),
        ),
        migrations.AddField(
            model_name='area',
            name='policy_off_start_time',
            field=models.TimeField(blank=True, db_column='policy_off_start_time', help_text='The start time when policy rules should NOT be enforced', null=True),
        ),
        migrations.AddField(
            model_name='area',
            name='policy_off_weekend',
            field=models.BooleanField(db_column='policy_off_weekend', default=False, help_text='Whether or not policy rules should be enforced on weekends'),
        ),
        migrations.AddField(
            model_name='area',
            name='requires_reservation',
            field=models.BooleanField(default=False, help_text='Check this box to require a reservation for this area before a user can login.'),
        ),
        migrations.AddField(
            model_name='area',
            name='reservation_horizon',
            field=models.PositiveIntegerField(blank=True, db_column='reservation_horizon', default=14, help_text='Users may create reservations this many days in advance. Leave this field blank to indicate that no reservation horizon exists for this area.', null=True),
        ),
        migrations.AddField(
            model_name='scheduledoutage',
            name='area',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='NEMO.Area'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='area',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='NEMO.Area'),
        ),
        migrations.AlterField(
            model_name='scheduledoutage',
            name='tool',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='NEMO.Tool'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='tool',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='NEMO.Tool'),
        ),
        migrations.AlterField(
            model_name='area',
            name='welcome_message',
            field=models.TextField(blank=True, help_text='The welcome message will be displayed on the tablet login page. You can use HTML and JavaScript.', null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='physical_access_levels',
            field=models.ManyToManyField(blank=True, to='NEMO.PhysicalAccessLevel'),
        ),
        migrations.AlterModelOptions(
            name='areaaccessrecord',
            options={},
        ),
        migrations.AlterField(
            model_name='scheduledoutage',
            name='resource',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='NEMO.Resource'),
        ),
        migrations.AddIndex(
            model_name='area',
            index=models.Index(fields=['name'], name='NEMO_area_name_1e7670_idx'),
        ),
        migrations.AddIndex(
            model_name='areaaccessrecord',
            index=models.Index(fields=['end'], name='NEMO_areaac_end_fae061_idx'),
        ),
    ]
