# Generated by Django 2.1 on 2018-09-27 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0002_auto_20180920_1449'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'verbose_name': 'Autor', 'verbose_name_plural': 'Autores'},
        ),
        migrations.AlterModelOptions(
            name='editora',
            options={'verbose_name': 'Editora', 'verbose_name_plural': 'Editoras'},
        ),
        migrations.AlterModelOptions(
            name='livro',
            options={'verbose_name': 'Livro', 'verbose_name_plural': 'Livros'},
        ),
        migrations.AlterModelOptions(
            name='loja',
            options={'verbose_name': 'Loja', 'verbose_name_plural': 'Lojas'},
        ),
        migrations.AddField(
            model_name='livro',
            name='sinopse',
            field=models.TextField(blank=True, null=True),
        ),
    ]
