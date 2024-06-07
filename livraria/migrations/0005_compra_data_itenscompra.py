# Generated by Django 5.0.6 on 2024-06-07 19:30

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livraria', '0004_compra'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='data',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='ItensCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(default=1)),
                ('preco_item', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens', to='livraria.compra')),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='livraria.livro')),
            ],
        ),
    ]