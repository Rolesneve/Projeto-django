from django.db import models


class Autor(models.Model):

    primeiroNome = models.CharField(max_length=250)
    sobrenome = models.CharField(max_length=250)
    imagem = models.ImageField(upload_to='imagens')

    def __str__(self):
        return self.primeiroNome


class Orientador(models.Model):

    primeiroNome = models.CharField(max_length=250)
    sobrenome = models.CharField(max_length=250)
    linkCurriculoLattes = models.URLField(max_length=200)

    def __str__(self):
        return self.primeiroNome

class Curso(models.Model):

    modalidades = (('Bacharelado', 'Bacharelado'), ('Licenciatura', 'Licenciatura'), ('Tecnológo', 'Tecnológo'))

    nome = models.CharField(max_length=250)
    modalidade = models.CharField(max_length=250, choices = modalidades)

    def __str__(self):
        return self.nome


class Tcc(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    orientador = models.ForeignKey(Orientador, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    anoDocumento = models.IntegerField(verbose_name="anoDocumento")
    resumo = models.TextField(max_length=300)
    arquivo = models.FileField(upload_to='tccs')
    palavrasChave = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo

