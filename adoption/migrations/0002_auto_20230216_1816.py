# Generated by Django 3.2 on 2023-02-16 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adoption', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adoptionquestions',
            old_name='description_of_pet_you_want',
            new_name='pet_you_want',
        ),
        migrations.RenameField(
            model_name='adoptionquestions',
            old_name='where_will_the_pet_be_kept',
            new_name='where_will_the_pet',
        ),
    ]