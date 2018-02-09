from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class List(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    firstname = models.CharField(max_length=50, null=True, blank=True)
    lastname = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return "%s %s" % (self.firstname, self.lastname)

    class Meta:
        unique_together = ('title', 'firstname', 'lastname',)


@python_2_unicode_compatible
class Card(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    list = models.ForeignKey(List, related_name="cards")
    story_points = models.IntegerField(null=True, blank=True)
    business_value = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return "Card: {}".format(self.title)
