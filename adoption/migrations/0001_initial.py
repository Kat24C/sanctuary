# Generated by Django 3.2 on 2023-02-16 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdoptionQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perspective_pet_parent', models.CharField(blank=True, max_length=40, null=True)),
                ('User_email', models.EmailField(blank=True, max_length=70, unique=True)),
                ('other_pets', models.CharField(blank=True, choices=[('NO', 'No'), ('YES', 'Yes')], max_length=10)),
                ('please_give_details', models.TextField(max_length=400)),
                ('what_type_of_pet', models.CharField(blank=True, choices=[('CAT', 'Cat'), ('DOG', 'Dog'), ('RABBIT', 'Rabbit'), ('GUINEA PIGS', 'Guinea pigs'), ('BIRDS', ' BIRDS')], max_length=11)),
                ('pet_you_want', models.TextField(max_length=400)),
                ('where_will_the_pet', models.CharField(blank=True, choices=[('INSIDE', 'Inside'), ('OUTSIDE', 'Outside'), ('ANIMAL HOUSE', 'Outdoor animal house')], max_length=20)),
            ],
        ),
    ]
