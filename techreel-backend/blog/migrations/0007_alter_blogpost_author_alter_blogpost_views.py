# Generated by Django 4.0.3 on 2022-04-02 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
        ('blog', '0006_alter_blogpost_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='author', to='authors.author'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
