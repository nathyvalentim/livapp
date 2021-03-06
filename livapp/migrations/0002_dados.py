# Generated by Django 3.2 on 2021-06-24 01:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('livapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dados',
            fields=[
                ('ciclo', models.AutoField(primary_key=True, serialize=False)),
                ('avatar', models.CharField(choices=[('SH', 'Super'), ('CA', 'Cachorro'), ('MC', 'McQueen'), ('TR', 'Trem')], max_length=200)),
                ('tema_1', models.CharField(choices=[('BO', 'Bola'), ('CR', 'Carro'), ('DO', 'Doce'), ('LI', 'Livro')], max_length=200)),
                ('tema_2', models.CharField(choices=[('BO', 'Bola'), ('CR', 'Carro'), ('DO', 'Doce'), ('LI', 'Livro')], max_length=200)),
                ('tema_3', models.CharField(choices=[('BO', 'Bola'), ('CR', 'Carro'), ('DO', 'Doce'), ('LI', 'Livro')], max_length=200)),
                ('tema_4', models.CharField(choices=[('BO', 'Bola'), ('CR', 'Carro'), ('DO', 'Doce'), ('LI', 'Livro')], max_length=200)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'dados',
                'managed': True,
                'unique_together': {('aluno', 'ciclo')},
            },
        ),
    ]
