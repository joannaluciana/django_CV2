from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.timezone import now
from work.models import Project


class Reviews(models.Model):
    # dodaje User.reviews relacje odwrotna autor1.project_set.filter(costam)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=False,
        blank=False,

        verbose_name='author',
        help_text='',
    )
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name="project name",
        help_text="",
    )
    title = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name='title',
        help_text='',
    )
    content = models.TextField(
        blank=False,
        verbose_name='Content',
        help_text='',
    )
    pub_date = models.DateField(
        null=True,
        blank=True,
        verbose_name='Date of timestamp',
        help_text='',
    )
    STATE_CHOICES = (
        ('draft', 'Draft'),
        ('in_moderation', 'In moderation'),
        ('rejected', 'Rejected'),
        ('published', 'Published'),
    )

    state = models.CharField(
        choices=STATE_CHOICES,
        max_length=40,
        null=False,
        blank=False,
        verbose_name='title',
        help_text='',
    )

    grade = models.PositiveIntegerField(
        null=False,
        blank=False,
        verbose_name='grade',
        help_text='Validate project from 1 - 10',
        validators=[
            MinValueValidator(1),
            MaxValueValidator(11),
        ],
    )





class Grade(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        null=False,
        blank=False,
        verbose_name='author',
        help_text='',
    )

    grade = models.PositiveIntegerField(
        null=False,
        blank=False,
        verbose_name='grade',
        help_text='Validate project from 1 - 10',
        validators=[
            MinValueValidator(1),
            MaxValueValidator(11),
        ],
    )
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name='Project',
        help_text='',
    )
