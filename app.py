# Importa o módulo os, usado aqui para limpar o terminal
import os

# Lista de restaurantes (estrutura principal do programa)
# Cada restaurante é um dicionário com:
# nome -> nome do restaurante
# categoria -> tipo de comida
# ativo -> se está ativo (True) ou desativado (False)
restaurantes = [
    {'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False},
    {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'ativo': True},
    {'nome': 'Cantina', 'categoria': 'Italiano', 'ativo': False}]

def exibir_nome_do_programa():
    print("\033[34m")  # Azul
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")
    print("\033[0m")  # Reseta a cor

# Exibe o menu principal com as opções disponíveis
def exibir_opcoes():
    print('\n1. Cadastrar restaurante')
    print('\n2. Listar restaurantes')
    print('\n3. Alternar estado do restaurante')
    print('\n4. Sair\n')

# Finaliza o aplicativo
def finalizar_app():
    print("\033[31m")  # Vermelho
    exibir_subtitulo('Finalizar app')
    print("\033[0m")   # Reseta a cor

# Aguarda o usuário apertar uma tecla e volta para o menu principal
def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu ')
    main()

# Exibida quando o usuário digita uma opção inválida
def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

# Exibe um subtítulo formatado e limpa a tela
def exibir_subtitulo(texto):
    os.system('cls')  # Limpa o terminal (Windows)
    linha = '*' * len(texto)  # Cria uma linha de * do tamanho do texto
    print(linha)
    print(texto)
    print(linha)
    print()

# Função responsável por cadastrar um novo restaurante
def cadastrar_novo_restaurante():
    """
    Essa função cadastra um novo restaurante na lista.

    Inputs:
    - Nome do restaurante
    - Categoria

    Output:
    - Adiciona um novo restaurante à lista 'restaurantes'
    """
    print("\033[31m")  # Vermelho
    exibir_subtitulo('Cadastro de novos restaurantes')
    print("\033[0m")   # Reseta a cor
    # Recebe os dados do usuário
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')

    # Cria o dicionário do restaurante
    dados_do_restaurante = {
        'nome': nome_do_restaurante,
        'categoria': categoria,
        'ativo': False  # Sempre começa como desativado
    }

    # Adiciona o restaurante à lista
    restaurantes.append(dados_do_restaurante)

    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

# Lista todos os restaurantes cadastrados
def listar_restaurantes():
    print("\033[31m")  # Vermelho
    exibir_subtitulo('Listando restaurantes')
    print("\033[0m")   # Reseta a cor

    # Cabeçalho da tabela
    print(f'{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status')

    # Percorre a lista de restaurantes
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'

        # Exibe os dados formatados
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

# Alterna o estado (ativo/desativado) de um restaurante
def alternar_estado_restaurante():
    print("\033[31m")  # Vermelho
    exibir_subtitulo('Alterando estado do restaurante')
    print("\033[0m")   # Reseta a cor
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    # Procura o restaurante pelo nome
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True

            # Inverte o valor booleano (True -> False / False -> True)
            restaurante['ativo'] = not restaurante['ativo']

            mensagem = (
                f'O restaurante {nome_restaurante} foi ativado com sucesso'
                if restaurante['ativo']
                else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            )
            print(mensagem)

    # Caso não encontre o restaurante
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()

# Função que lê a opção escolhida pelo usuário
def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        # Caso o usuário digite algo que não seja número
        opcao_invalida()

# Função principal do programa
def main():
    os.system('cls')  # Limpa o terminal (Windows)
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

# Garante que o programa só execute se este arquivo for o principal
if __name__ == '__main__':
    main()
