# Generated by Django 3.2 on 2023-02-12 12:59

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutTheAnimal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animals_name', models.CharField(max_length=200, null=True)),
                ('animal_nickname', models.CharField(max_length=100, null=True)),
                ('featured_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('type_of_animal', models.CharField(choices=[('CAT', 'Cat'), ('DOG', 'Dog'), ('RABBIT', 'Rabbit'), ('GUINEA PIGS', 'Guinea pigs'), ('BIRDS', ' BIRDS')], default=1, max_length=11)),
                ('approximate_age', models.PositiveIntegerField(default=1)),
                ('about_the_animal', models.TextField(max_length=300)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
