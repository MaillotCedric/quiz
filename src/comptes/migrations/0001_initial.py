# Generated by Django 4.1.2 on 2022-11-14 03:26

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Metier',
            fields=[
                ('codeMetier', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('nomMetier', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'metier',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('codeRole', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('nomRole', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'role',
            },
        ),
        migrations.CreateModel(
            name='Secteur',
            fields=[
                ('codeSecteur', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('nomSecteur', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'secteur',
            },
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('matricule', models.CharField(default='AAAA', max_length=50)),
                ('codeMetier', models.ForeignKey(db_column='codeMetier', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='comptes.metier')),
                ('codeRole', models.ForeignKey(db_column='codeRole', default='admin', on_delete=django.db.models.deletion.DO_NOTHING, to='comptes.role')),
                ('codeSecteur', models.ForeignKey(db_column='codeSecteur', default='MKT', on_delete=django.db.models.deletion.DO_NOTHING, to='comptes.secteur')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddConstraint(
            model_name='utilisateur',
            constraint=models.UniqueConstraint(fields=('matricule',), name='unique matricule'),
        ),
        migrations.AddConstraint(
            model_name='utilisateur',
            constraint=models.UniqueConstraint(condition=models.Q(('codeRole', 'chef')), fields=('codeRole', 'codeSecteur'), name='unique chef de secteur'),
        ),
    ]
