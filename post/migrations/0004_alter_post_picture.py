# Generated by Django 4.0.4 on 2022-04-17 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_alter_post_options_alter_tag_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='uploads', verbose_name='Picture'),
        ),
    ]