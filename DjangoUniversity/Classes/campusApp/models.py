from django.db import models

# Create your models here.
class UniversityCampus(models.Model):
    campus_name = models.CharField(max_length=60, default="", blank=True, null=False)
    state = models.CharField(max_length=2, default="", blank=True, null=False)
    campus_id = models.IntegerField(null=False, blank=True, default="")

    object = models.Manager()

    # displays the object output values in the form of a string
    def __str__(self):
        display_campus = '{0.campus_name}'
        return display_campus.format(self)

    # removes added 's' that Django adds to the model name in the browser display
    class Meta:
        verbose_name_plural = "University Campus" # this will display 'University Campus' instead
                                                    # of 'University Campuss'
