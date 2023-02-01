# Generated by Django 4.1.6 on 2023-02-01 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0004_teacher_class_taught'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('due_date', models.DateTimeField()),
                ('class_obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.class')),
            ],
        ),
    ]
