# Generated by Django 3.2 on 2023-03-01 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoption', '0002_auto_20230225_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adoptionquestion',
            name='what_type_of_pet',
            field=models.CharField(blank=True, choices=[('CAT', 'Cat'), ('DOG', 'Dog'), ('RABBIT', 'Rabbit'), ('GUINEA PIGS', 'Guinea pigs'), ('BIRDS', 'Birds'), ('HAMSTER', 'Hamster')], max_length=11),
        ),
    ]
