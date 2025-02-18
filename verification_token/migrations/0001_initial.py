# Generated by Django 2.0 on 2018-07-15 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='VerificationToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('object_id', models.TextField()),
                ('key', models.CharField(max_length=100, unique=True)),
                ('expiration_in_minutes', models.PositiveIntegerField(blank=True, default=None, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('content_type', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]
