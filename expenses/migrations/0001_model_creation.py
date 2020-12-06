# Generated by Django 3.1.4 on 2020-12-06 18:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('commons', '0003_changed_table_names'),
        ('users', '0003_changed_table_names'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('title', models.CharField(max_length=80, null=True)),
                ('description', models.CharField(blank=True, max_length=150, null=True)),
                ('value', models.DecimalField(decimal_places=2, max_digits=19)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='commons.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='users.user')),
            ],
        ),
    ]
