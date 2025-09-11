from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Gerenciador Personalizado para filtrar os excluidos
class ClientQuerySet(models.QuerySet):
    # Função que retorna só os ativos
    def actives(self):
        return self.filter(is_deleted=False)

    # Função para retornar ativos e deletados
    def with_deleted(self):
        return self.all()


# Manager para associar aos modelos
class ClientManager(models.Manager):
    def get_queryset(self):
        return ClientQuerySet(self.model, using=self._db)

    def actives(self):
        return self.get_queryset().actives()

    def with_deleted(self):
        return self.get_queryset().all()


# Adicionando classe base para registro de criação e modificação
class BaseModel(models.Model):
    # Atributos para Auditoria
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # soft delete
    is_deleted = models.BooleanField(default=False)
    # registro do soft delete para auditoria
    deleted_at = models.DateTimeField(null=True, blank=True)

    # Novo gerenciador do soft delete
    objects = ClientManager()

    class Meta:
        abstract = True

    # Realiza soft delete sem remover do banco
    def delete(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    # Restaura o registro deletado
    def restore(self):
        self.is_deleted = False
        self.deleted_at = None
        self.save()


class Carteira(BaseModel):
    # 1 carteira por usuário
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100, default="Minha Carteira")
    saldo_inicial = models.DecimalField(
        max_digits=10, decimal_places=2, default=0
    )

    def __str__(self):
        return f"{self.usuario.username} - {self.nome}"
