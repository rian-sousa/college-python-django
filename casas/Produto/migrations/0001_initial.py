# Generated by Django 4.0.5 on 2022-06-08 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('nSerie', models.CharField(max_length=20)),
                ('tipo', models.CharField(max_length=20)),
                ('anoDoProduto', models.CharField(max_length=4)),
                ('quantidade', models.CharField(max_length=6)),
            ],
        ),
    ]