from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class List(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    firstname = models.CharField(max_length=50, null=False, blank=False)
    lastname = models.CharField(max_length=50, null=True, blank=True)
    about = models.CharField(max_length=5000, null=True, blank=True)

    def __str__(self):
        if self.lastname:
            return "%s, %s" % (self.lastname, self.firstname)
        else:
            return self.firstname

    class Meta:
        unique_together = ('firstname', 'lastname',)
        ordering = ['lastname']


@python_2_unicode_compatible
class Quote(models.Model):
    category = models.CharField(max_length=30)
    text = models.TextField(max_length=1000)
    list = models.ForeignKey(List, related_name="quotes")

    def __str__(self):
        return "%s: %s - %s..." % (self.list.lastname, self.category, self.text[:50])

    class Meta:
        ordering = ['list', 'category']
