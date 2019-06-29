from django.db import models


# Create your models here.

class Perfil(models.Model):
    nome = models.CharField(max_length=255, null=False)
    telefone = models.CharField(max_length=20, null=False)
    nome_empresa = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)
    contatos = models.ManyToManyField('Perfil')

    def __str__(self):
        return self.nome

    def convidar(self, perfil_convidado):
        convite = Convite(solicitante=self, convidado=perfil_convidado)
        convite.save()


class Convite(models.Model):
    solicitante = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='convites_feitos')
    convidado = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='convites_recebidos')

    def aceitar(self):
        self.solicitante.contatos.add(self.convidado)
        self.convidado.contatos.add(self.solicitante)
        self.delete()

# t = Perfil(nome="Joelma",nome_empresa="Calipso",telefone="99885522",email="joojo@hotmail.com")
