# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

#
# class Departamento(models.Model):
#     nome = models.CharField(max_length=255)


# Create your models here.
class Setor(models.Model):
    nome = models.CharField(max_length=255)
    # departamento = models.ForeignKey(Departamento)

    def __unicode__(self):
        return self.nome


class Funcionario(models.Model):
    nome = models.CharField(max_length=255)
    setor = models.ForeignKey(Setor)

    def __unicode__(self):
        # return u"%s (%s/%s)".format(self.nome, self.setor.nome, self.setor.departamento.nome)
        return u"%s (%s/%s)".format(self.nome, self.setor.nome)

