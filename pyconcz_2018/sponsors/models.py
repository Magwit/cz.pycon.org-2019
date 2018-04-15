from django.db import models


class Sponsor(models.Model):
    LEVEL = (
        (1, 'Platinum'),
        (2, 'Gold'),
        (3, 'Silver'),
        (4, 'Bronze'),
        (5, 'Diversity'),
        (6, 'Media'),
        (7, 'Partners'),
        (8, 'Coffee sponsor'),
        (9, 'Con­nectiv­ity sponsor'),
        (10, 'Tea sponsor'),
    )

    level = models.PositiveSmallIntegerField(choices=LEVEL, default=3)

    name = models.CharField(max_length=200)
    logo = models.FileField(upload_to='sponsors/pyconcz_2018/')

    description = models.TextField()
    link_url = models.URLField()
    twitter = models.URLField(null=True, blank=True, help_text='full URL')
    facebook = models.URLField(null=True, blank=True, help_text='full URL')

    published = models.BooleanField(default=False)

    class Meta:
        ordering = ["level", "name"]

    def __str__(self):
        return self.name
