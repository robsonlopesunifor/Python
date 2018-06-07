from django.db import models
"""
model armazenar os dados 
	o nome da classe e o nome da tabela
	o nome do atibuto (filds) e como a coluna 
		Nos filds e possivel ter as mesmas propiedade que no SQL (chave primaria,etc)

No final e possivel converter em um banco de dados (mySql,Oracle,sqlLingth)

model https://docs.djangoproject.com/en/2.0/topics/db/models/ 
filds https://docs.djangoproject.com/en/2.0/ref/models/fields/
"""

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=100) 		# tipo Char tamanho 100
    dt_criacao = models.DateTimeField(auto_now_add=True) # tipo data, data atual 

    def __str__(self):	# nome que serao titulo 
        return self.nome # 

class Transacao(models.Model):
    data = models.DateTimeField() 			# tipo data, a ser definido 
    descricao = models.CharField(max_length=200)	# tipo Char tamanho 100
    valor = models.DecimalField(max_digits=7,decimal_places=2)	# tipo decimal 9999999.99
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE) # chave estranjeira, 
								      # delete tipo cascata
    observacoes = models.TextField(null=True,blank=True)# tipo texto nao obrigatorio
							# blak: selecionar ao abilitar

    class Meta:
        verbose_name_plural = 'Transacoes'	#define o plural do model
