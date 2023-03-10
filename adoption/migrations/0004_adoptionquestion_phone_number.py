# Generated by Django 3.2 on 2023-03-07 18:50

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('adoption', '0003_alter_adoptionquestion_what_type_of_pet'),
    ]

    operations = [
        migrations.AddField(
            model_name='adoptionquestion',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, unique=True),
        ),
    ]
