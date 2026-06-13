# Solicitando informações de acesso ao usuário
email = input("Digite o email de acesso: ")
senha = input("Digite a senha de acesso: ")

# Verificando se o e-mail está cadastrado
if email == "teste@teste.com.br":
    print("Email correto")
else:
    print("Usuário não cadastrado")

# Verificando se a senha está correta e liberando acesso ao sistemas
if senha == "123456":
    print("bem vindo ao sistema da fabrica")
else:
    print("Senha incorreta")