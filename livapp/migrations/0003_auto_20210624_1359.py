# Generated by Django 3.2 on 2021-06-24 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livapp', '0002_dados'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dados',
            name='avatar',
            field=models.CharField(choices=[('Super Heroi', 'Super Heroi'), ('Cachorro', 'Cachorro'), ('McQueen', 'McQueen'), ('Trem', 'Trem')], max_length=200),
        ),
        migrations.AlterField(
            model_name='dados',
            name='tema_1',
            field=models.CharField(choices=[('Bola', 'Bola'), ('Carro', 'Carro'), ('Doce', 'Doce'), ('Livro', 'Livro')], max_length=200),
        ),
        migrations.AlterField(
            model_name='dados',
            name='tema_2',
            field=models.CharField(choices=[('Bola', 'Bola'), ('Carro', 'Carro'), ('Doce', 'Doce'), ('Livro', 'Livro')], max_length=200),
        ),
        migrations.AlterField(
            model_name='dados',
            name='tema_3',
            field=models.CharField(choices=[('Bola', 'Bola'), ('Carro', 'Carro'), ('Doce', 'Doce'), ('Livro', 'Livro')], max_length=200),
        ),
        migrations.AlterField(
            model_name='dados',
            name='tema_4',
            field=models.CharField(choices=[('Bola', 'Bola'), ('Carro', 'Carro'), ('Doce', 'Doce'), ('Livro', 'Livro')], max_length=200),
        ),
    ]
