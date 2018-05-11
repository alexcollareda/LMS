from django.db import models

class StatusLms(models.Model):
    ID_STATUS_LMS = models.IntegerField(primary_key=True)
    DESCRICAO = models.CharField(null=False, max_length=20)

     def __str__(self):
        return self.ID_STATUS_LMS

class Pessoa(models.Model):
    ID_PESSOA = models.IntegerField(unique=True, primary_key=True)
    NOME = models.CharField(max_length=255, null=False)
    EMAIL = models.CharField(max_length=100, null=False, unique=True)
    CELULAR = models.CharField(max_length=20, null=False, unique=True)
    LOGIN = models.IntegerField(null=False, unique=True)
    SENHA models.CharField(max_length=20, null=False),
    DT_EXPIRACAO = models.DateField(default= '1900-01-01')

    def __str__(self):
        return self.ID_PESSOA

class Cordenador(models.Model):
    ID_COORDENADOR = models.IntegerField()
    ID_PESSOA INT = models.IntegerField()
    ID_COORDENADOR = models.IntegerField(primary_key=True)
    ID_PESSOA = models.ForeignKey(Pessoa)
    
    def __str__(self):
        return self.ID_COORDENADOR

class Aluno(models.Model):
    ID_COORDENADOR = models.IntergerField(unique=True)
    ID_PESSOA = models.IntergerField()
    ID_PESSOA = models.ForeignKey(Pessoa) 

    def __str__(self):
        return self.ID_COORDENADOR

class Professor(models.Model):
    ID_PROFESSOR = models.IntegerField(primary_key=True)
    ID_PESSOA = models.IntegerField()
    APELIDO = models.CharField(max_length=30, unique=True)
    ID_PESSOA = models.ForeignKey(Pessoa)

    def __str__(self):
        return self.ID_PROFESSOR

class Mensagem(models.Model):
    id_Mensagem = models.IntegerField(null=False, primary_key=True)
    id_Aluno = models.ForeignKey(Aluno)
    id_Professor = models.ForeignKey(Professor)
    assuntoMensagem = models.CharField(max_length=50)
    referenciaMensagem = models.CharField(max_length=200)
    conteudoMensagem = models.CharField(max_length=500)
    ID_STATUS_MENSAGEM = models.ForeignKey(StatusLms)
    dataEnvioMensagem = models.DateField(auto_now=True)
    dtMensagemResposta = models.DateField(auto_now_add=True)
    respostaMensagem = models.CharField(max_length=500)

    def __str__(self):
        return self.id_Mensagem

class Curso(models.Model):
    ID_CURSO = models.IntegerField(primary_key=True)
    NOME_CURSO = models.CharField(null=False, max_length= 100, unique=True)
    
    def __str__(self):
        return self.ID_CURSO

class Disciplina(models.Model):
    ID_COORDENADOR = models.ForeignKey(Cordenador)
    id_Disciplina = models.IntegerField(null=False, primary_key=True)
    NOME = models.CharField(max_length=30, null=False, unique=False)
    data models.DateField(auto_now=True)
    PLANO_ENSINO = models.CharField(max_length=100)
    CARGA_HORARIA = models.CharField(max_length=30, choices=CARGA_HORARIA_CHOICES)
    COMPETENCIAS = models.CharField(max_length=300)
    HABILIDADES = models.CharField(max_length=100)
    EMENTA = models.CharField(max_length=300)
    CONTEUDO_PROGRAMATICO = models.CharField(max_length=300)
    BIBLIOGRAFIA_BASICA = models.CharField(max_length=300)
    BIBLIOGRAFIA_COMPLEMENTAR = models.CharField(max_length=300)
    PERCENTUAL_PRATICO  = models.DecimalField() #decimal(3)
    PERCENTUAL_TEORICO  = models.DecimalField() #decimal(3)
    ID_STATUS_LMS = models.ForeignKey(StatusLms)

    def __str__(self):
        return self.ID_COORDENADOR

class SolicitacaoMatricula(models.Model):
    ID_SOLICITACAO_MATRICULA = models.IntegerField(primary_key=True)
    ID_ALUNO = models.ForeignKey(Aluno)
    ID_DISCIPLINA_OFERTADA = models.ForeignKey(DisciplinaOfertada) #falta class
    DT_SOLICITACAO = models.DateField(null=True, auto_now=True)
    ID_COORDENADOR_APROVACAO models.ForeignKey(Cordenador)
    ID_STATUS_LMS models.ForeignKey(StatusLms)

    def __str__(self):
        return self.nome

class Atividade(models.Model):
    id_Atividade = models.IntegerField(null=False, primary_key=True)
    id_Professor = models.ForeignKey(Professor)
    tituloAtiv  = models.CharField(max_length=100, unique=True)
    descricaoAtiv = models.CharField(max_length=100)
    conteudoAtiv = models.CharField(max_length=100)
    tipoAtiv = models.CharField(max_length=50)
    extrasAtiv = models.CharField(max_length=80)
 
    def __str__(self):
        return self.nome

class AtividadeVinculada(models.Model):
    id_Atividade_Vinculada = models.IntegerField(null=True, primary_key=True)
    id_Professor = models.ForeignKey(Professor)
    id_Atividade = models.ForeignKey(Atividade)
    id_Disciplina_Ofertada = models.ForeignKey(DisciplinaOfertada)#falta class
    ID_STATUS_ATIVIDADE_VINCULADA = models.ForeignKey(StatusLms)
    dataAtivInicio = models.DateField(auto_now=True)
    dataAtivEncerramento = models.DateField(auto_now=True)
    rotuloAtivVinculada = models.CharField(unique=True, max_length=10)
  
    def __str__(self):
        return self.nome

class Entrega(models.Model):
    id_Entrega = models.IntegerField(primary_key=True, null=True)
    id_Aluno = models.ForeignKey(Aluno)
    id_Professor = models.ForeignKey(Professor)
    id_Atividade_Vinculada = models.ForeignKey(AtividadeVinculada)
    tituloEntrega = models.CharField(max_length= 100)
    respostaEntrega  = models.CharField(max_length= 100)
    dataEntrega = models.DateField(auto_now=True)
    ID_STATUS_ENTREGA INT = models.ForeignKey(StatusLms)
    notaEntrega = models.DecimalField()
    dataAvaliacaoEntrega = models.DateField(auto_now=True)
    obsEntrega = models.CharField(max_length= 300)    
    
    def __str__(self):
        return self.nome


