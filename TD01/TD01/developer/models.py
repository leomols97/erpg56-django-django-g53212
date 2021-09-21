from django.db import models


# Create your models here.

class Developer(models.Model):
    first_name = models.CharField(verbose_name="first name", max_length=200)
    last_name = models.CharField(max_length=200)

    # Ceci permet d'afficher les valeurs des attributs de la classe. Il faut concaténer
    def __str__(self):
        return '\nPrénom : ' + self.first_name \
               + '\nNom : ' + self.last_name + '\n\n'


class Task(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    assignee = models.ForeignKey(Developer, related_name="tasks",
                                 on_delete=models.CASCADE, null=True, verbose_name="assignee")

    # Ceci permet d'afficher les valeurs des attributs de la classe. Il faut concaténer
    def __str__(self):
        return 'Titre : ' + self.title \
               + '\nDescription : ' + self.description + '\n\n'
