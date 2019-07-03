from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE, null=True)
    telefone = models.CharField(max_length=20, null=False)
    nome_empresa = models.CharField(max_length=255, null=False)
    contatos = models.ManyToManyField('Perfil')

    @property
    def email(self):
        return self.user.email

    def convidar(self, perfil_convidado):
        convite = Convite(solicitante=self, convidado=perfil_convidado)
        print(self.id)
        print(perfil_convidado.id)
        convite.save()
        print('ddd')


class Convite(models.Model):
    solicitante = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='convites_feitos')
    convidado = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='convites_recebidos')

    def aceitar(self):
        self.solicitante.contatos.add(self.convidado)
        self.convidado.contatos.add(self.solicitante)
        self.delete()

# t = Perfil(nome="Joelma",nome_empresa="Calipso",telefone="99885522",email="joojo@hotmail.com")
