# Generated by Django 5.0.6 on 2024-06-28 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("oc_lettings_site", "0002_alter_address_id_alter_letting_address_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="letting",
            name="address",
        ),
        migrations.DeleteModel(
            name="Address",
        ),
        migrations.DeleteModel(
            name="Letting",
        ),
    ]
