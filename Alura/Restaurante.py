import os
def exibir_nome_do_programa():
    print("""
█████████████████████▀███████████████████████████████████████████████████████████████
█─▄─▄─█▄─▄██▀▄─██─▄▄▄▄█▄─██─▄█▄─▄█▄─▀█▄─▄███─▄▄▄─█─▄▄─█▄─▀█▀─▄█▄─▄█▄─▄▄▀██▀▄─██─▄▄▄▄█
███─████─███─▀─██─██▄─██─██─███─███─█▄▀─████─███▀█─██─██─█▄█─███─███─██─██─▀─██▄▄▄▄─█
▀▀▄▄▄▀▀▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▀▄▄▄▄▀▀▄▄▄▀▄▄▄▀▀▄▄▀▀▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▄▀▀▄▄▀▄▄▀▄▄▄▄▄▀
""")
def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair\n')


def finalizar_app():
    os.system('cls')
    print('Finalizando App\n')

def escolher_opcoes():
    opcao_escolhida = int(input('Escolha uma opção: '))
        
    if opcao_escolhida ==  1:
        print('Cadastrar Restaurante')
    elif opcao_escolhida ==  2:
        print('Listar Restaurante')
    elif opcao_escolhida ==  3:
        print('Ativar Restaurante')
    elif opcao_escolhida == 4 :
        finalizar_app()

def main(): 
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()
    
if __name__ == '__main__':
    main()