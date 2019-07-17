from django.db import models
import secrets
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True,
                                help_text='Um nome curto que será usado para identificá-lo de forma única na plataforma')
    first_name = models.CharField(max_length=120, blank=False, null=True)
    last_name = models.CharField(max_length=120, blank=False, null=True)
    photo = models.ImageField(upload_to='avatar')
    is_staff = models.BooleanField('Equipe', default=False)
    email = models.EmailField('E-mail', unique=True)
    bio = models.CharField(max_length=180, blank=True)
    email_verified = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False)
    verification_code = models.CharField(max_length=128, blank=False, db_index=True, unique=True)
    friendship = models.ManyToManyField('User')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    @property
    def full_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    def save(self, *args, **kwargs):
        token = secrets.token_hex(20)
        while len(User.objects.filter(verification_code=token)) > 0:
            token = secrets.token_hex(20)
        self.verification_code = token
        super(User, self).save(*args, **kwargs)

    def send_invite(self, recipient):
        self.invite.add(recipient=recipient)

    def convidar(self, perfil_convidado):
        convite = Convite(solicitante=self, convidado=perfil_convidado)
        convite.save()



class Convite(models.Model):
    solicitante = models.ForeignKey(User, on_delete=models.CASCADE, related_name='convites_feitos')
    convidado = models.ForeignKey(User, on_delete=models.CASCADE, related_name='convites_recebidos')

    def aceitar(self):
        self.solicitante.friendship.add(self.convidado)
        self.convidado.friendship.add(self.solicitante)
        self.delete()

    def recusar(self):
        self.delete()
