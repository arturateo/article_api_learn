# Generated by Django 4.2.2 on 2023-07-21 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_article_author_comment_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'permissions': [('write_rate', 'Написать рецензию')], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
    ]