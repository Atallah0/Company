# Generated by Django 4.1 on 2022-08-31 17:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Payroll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='payroll', max_length=50)),
                ('date', models.DateField(null=True)),
                ('basic_salary', models.PositiveIntegerField(default=0)),
                ('extra_work_hours', models.PositiveIntegerField(default=0)),
                ('extra_paid', models.PositiveIntegerField(default=0)),
                ('bonus', models.PositiveIntegerField(default=0)),
                ('income_tax', models.PositiveIntegerField(default=0)),
                ('percent', models.PositiveIntegerField(default=100)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payrolls', to='payroll_app.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='managers', to='payroll_app.employee')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='payroll_app.manager'),
        ),
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dep_name', models.CharField(max_length=20)),
                ('dep_place', models.CharField(max_length=20)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departments', to='payroll_app.manager')),
            ],
        ),
    ]
