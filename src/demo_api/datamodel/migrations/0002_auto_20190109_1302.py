# Generated by Django 2.1.4 on 2019-01-09 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamodel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='bron_link',
            field=models.URLField(blank=True, help_text='Link naar de oorspronkelijke bron.', verbose_name='bron link'),
        ),
        migrations.AddField(
            model_name='quote',
            name='bron_naam',
            field=models.CharField(default='(Onbekend)', help_text='Naam van de bron.', max_length=200, verbose_name='bron naam'),
            preserve_default=False,
        ),
    ]