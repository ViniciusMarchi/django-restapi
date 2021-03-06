# Generated by Django 3.1.7 on 2021-06-03 02:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pets', '__first__'),
        ('veterinarios', '__first__'),
        ('clientes', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_consulta', models.DateTimeField()),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='animal', to='pets.animal')),
                ('cliente', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='cliente', to='clientes.cliente')),
                ('veterinario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='veterinario', to='veterinarios.veterinario')),
            ],
            options={
                'verbose_name': 'Consulta',
                'verbose_name_plural': 'Consultas',
                'db_table': 'consulta',
            },
        ),
    ]
