# Generated by Django 3.1.7 on 2021-04-13 22:16

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('utils', '0002_tracking'),
        ('images', '0002_customimage_file_hash'),
        ('wagtailcore', '0060_fix_workflow_unique_constraint'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('social_text', models.CharField(blank=True, max_length=255)),
                ('listing_title', models.CharField(blank=True, help_text='Override the page title used when this page appears in listings', max_length=255)),
                ('listing_summary', models.CharField(blank=True, help_text="The text summary used when this page appears in listings. It's also used as the description for search engines if the 'Meta description' field above is not defined.", max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('pronouns', models.CharField(blank=True, max_length=255)),
                ('person_type', models.CharField(blank=True, choices=[('curriculum', 'Curriculum & Pedagogy'), ('implementations', 'Program Implementations'), ('partnerships', 'Partnerships'), ('engineering', 'Engineering'), ('UX', 'UX Design & Research'), ('communications', 'Communications'), ('operations', 'Team Operations'), ('board', 'Board of directors'), ('advisory', 'Advisory Board')], max_length=255)),
                ('job_title', models.CharField(max_length=255)),
                ('biography', models.TextField(blank=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('listing_image', models.ForeignKey(blank=True, help_text='Choose the image you wish to be displayed when this page appears in listings', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.customimage')),
                ('photo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.customimage')),
                ('social_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.customimage')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='SocialMediaProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(choices=[('twitter', 'Twitter'), ('linkedin', 'LinkedIn')], max_length=200)),
                ('username', models.CharField(max_length=255)),
                ('person_page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_media_profile', to='people.personpage')),
            ],
        ),
        migrations.CreateModel(
            name='PersonPagePhoneNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=255)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='phone_numbers', to='people.personpage')),
            ],
        ),
        migrations.CreateModel(
            name='PersonIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('social_text', models.CharField(blank=True, max_length=255)),
                ('listing_title', models.CharField(blank=True, help_text='Override the page title used when this page appears in listings', max_length=255)),
                ('listing_summary', models.CharField(blank=True, help_text="The text summary used when this page appears in listings. It's also used as the description for search engines if the 'Meta description' field above is not defined.", max_length=255)),
                ('call_to_action', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='utils.calltoactionsnippet')),
                ('listing_image', models.ForeignKey(blank=True, help_text='Choose the image you wish to be displayed when this page appears in listings', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.customimage')),
                ('social_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.customimage')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='BoardPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('social_text', models.CharField(blank=True, max_length=255)),
                ('listing_title', models.CharField(blank=True, help_text='Override the page title used when this page appears in listings', max_length=255)),
                ('listing_summary', models.CharField(blank=True, help_text="The text summary used when this page appears in listings. It's also used as the description for search engines if the 'Meta description' field above is not defined.", max_length=255)),
                ('listing_image', models.ForeignKey(blank=True, help_text='Choose the image you wish to be displayed when this page appears in listings', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.customimage')),
                ('social_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.customimage')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='BoardMembers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('board_member_title', models.CharField(blank=True, max_length=255)),
                ('board_member_bio', models.TextField(blank=True)),
                ('board_member_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.customimage')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='board_members', to='people.boardpage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
