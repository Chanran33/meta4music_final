# Generated by Django 4.1 on 2022-09-22 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('main_page', '0006_delete_login_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compose',
            name='adminid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.user'),
        ),
        migrations.AlterField(
            model_name='images',
            name='memberid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.user'),
        ),
        migrations.AlterField(
            model_name='lyrics',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.user'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
