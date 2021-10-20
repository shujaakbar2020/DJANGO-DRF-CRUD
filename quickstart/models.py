from django.db import models


TYPES = (
    (1, 'Holy'),
    (2, 'Action'),
    (3, 'Fantasy'),
    (4, 'Historical'),
    (5, 'Horror')
)


class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255, null=True, blank=True)
    chapter = models.IntegerField()
    type = models.IntegerField(choices=TYPES, default=3, null=True)

    def __str__(self) -> str:
        return self.name
