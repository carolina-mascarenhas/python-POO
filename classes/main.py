from pessoa import Pessoa

pessoa1 = Pessoa("carol", 26)
pessoa1.comer('cenoura')
pessoa1.falar('POO')
pessoa1.parar_comer()
pessoa1.falar('POO')
pessoa1.comer('cenoura')
pessoa1.parar_falar()
pessoa1.comer('cenoura')

print(pessoa1.ano_atual)
print(Pessoa.ano_atual)

pessoa1.get_ano_nascimento()
