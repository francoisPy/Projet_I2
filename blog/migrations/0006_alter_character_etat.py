# Generated by Django 4.2.7 on 2023-11-14 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_character_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='etat',
            field=models.CharField(choices=[('reposé', 'reposé'), ('pret', 'pret'), ('a faim', 'a faim'), ('rassasié', 'rassasié'), ('fatigué', 'fatigué')], max_length=200),
        ),
    ]
