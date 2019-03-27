from django.db import models
from django.db.models import ObjectDoesNotExist
from django.contrib.auth.models import User

from commons.models import Variable
from commons.tools.randomizer import key_generator

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User,
        on_delete=models.CASCADE, primary_key=True)
    code = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return "UserProfile: " + str(self.user)

    def save(self):
        if self.code == "":
            self.code = self.generate_code()
        return super().save()

    def generate_code(self):
        value = 3
        variable_object = None
        treshold = 10
        try:
            variable_object = Variable.objects.get(
                keyword="user_profile_key_length")
            value = variable_object.value_int
        except ObjectDoesNotExist as e:
            pass

        code = ""
        while code == "":
            itr = 0
            while code == "":
                code = key_generator(value)
                try:
                    UserProfile.objects.get(code=code)
                    code = ""
                    itr += 1
                except ObjectDoesNotExist as e:
                    pass
                if itr >= treshold:
                    value += 1
                    if variable_object:
                        variable_object.value_int = value
                        variable_object.save()
                    break
        return code


class Worker(models.Model):

    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    code = models.CharField(max_length=31, unique=True)

    def __str__(self):
        return self.code + ": " + str(self.user)

    def save(self):
        if self.code == "":
            self.code = self.generate_code()
        return super().save()

    def generate_code(self):
        value = 5
        variable_object = None
        treshold = 10
        try:
            variable_object = Variable.objects.get(
                keyword="cpu_worker_key_length")
            value = variable_object.value_int
        except ObjectDoesNotExist as e:
            pass

        code = ""
        while code == "":
            itr = 0
            while code == "":
                code = key_generator(value)
                try:
                    UserProfile.objects.get(code=code)
                    code = ""
                    itr += 1
                except ObjectDoesNotExist as e:
                    pass
                if itr >= treshold:
                    value += 1
                    if variable_object:
                        variable_object.value_int = value
                        variable_object.save()
                    break
        return code