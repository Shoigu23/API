# Generated by Django 4.1.7 on 2023-02-20 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('directions', models.CharField(choices=[('Backend', 'Back-End'), ('FrontEnd', 'Front-End'), ('Fullstack', 'Fullstack'), ('UX/UI', 'UX/UI')], max_length=1500)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Famale', 'Famale')], max_length=100)),
            ],
        ),
    ]
