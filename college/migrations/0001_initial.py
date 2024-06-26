# Generated by Django 5.0.6 on 2024-06-26 00:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gvernorate', models.CharField(max_length=255)),
                ('City', models.CharField(max_length=255)),
                ('line_1', models.CharField(max_length=255)),
                ('line_2', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Duration', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('F_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('F_Name', models.CharField(max_length=255)),
                ('L_Name', models.CharField(max_length=255)),
                ('F_Phone', models.CharField(max_length=255)),
                ('L_Phone', models.CharField(max_length=255)),
                ('Birth_Date', models.DateField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Exams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Time', models.TimeField()),
                ('Duration', models.DurationField()),
                ('C_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='college.course')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('D_name', models.CharField(max_length=255)),
                ('F_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='college.faculty')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('F_Name', models.CharField(max_length=255)),
                ('L_Name', models.CharField(max_length=255)),
                ('age', models.PositiveIntegerField()),
                ('Salary', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image', models.ImageField(upload_to='')),
                ('D_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='college.department')),
                ('F_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='college.faculty')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='P_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='college.professor'),
        ),
        migrations.CreateModel(
            name='Course_Enrolment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('C_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='college.course')),
                ('Stu_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='college.student')),
            ],
        ),
        migrations.CreateModel(
            name='Student_Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('A_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='college.address')),
                ('Stu_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='college.student')),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sub_name', models.CharField(max_length=255)),
                ('Sub_code', models.CharField(max_length=255, unique=True)),
                ('F_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='college.faculty')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='Sub_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='college.subjects'),
        ),
    ]
