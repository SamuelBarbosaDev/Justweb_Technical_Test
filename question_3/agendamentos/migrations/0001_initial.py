# Generated by Django 4.2.5 on 2023-09-23 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agendamentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=13)),
                ('data', models.DateTimeField()),
                ('cancelamento', models.BooleanField(default=False)),
            ],
        ),
    ]