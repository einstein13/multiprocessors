from django.db import models

# Create your models here.

class Variable(models.Model):

    keyword = models.CharField(max_length=63, unique=True)
    value_string = models.CharField(max_length=255, null=True, blank=True)
    value_int = models.IntegerField(null=True, blank=True)
    value_boolean = models.NullBooleanField(blank=True)

    def __str__(self):
        result = self.keyword + ": "

        if self.value_string:
            result += self.value_string
            return result
        if self.value_int:
            result += str(self.value_int)
            return result
        if self.value_boolean:
            result += str(self.value_boolean)
            return result
        return result
