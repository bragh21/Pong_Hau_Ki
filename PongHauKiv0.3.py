from os import system
from time import sleep

# VARIAVEIS 

PECAS = lambda cor: "\U0001f535" if cor == 'a' else "\U0001f534"
# PECAS = {
#   'a': "\U0001f535",
#   'v': "\U0001f534"
# }

tabuleiro = {
  1: PECAS('a'), 
  2: PECAS('a'), 
  3: '', 
  4: PECAS('v'),
  5: PECAS('v')
}

qttd_partidas = 0
qtdd_jogadas = {}
pecas_jogadores = {}
inicia_jogando = ""
posicao_jogavel = 3
jogadores = ""

# ------------------------------------------------
def redefine_tabuleiro():
  global tabuleiro
  tabuleiro = {
    1: PECAS('a'), 
    2: PECAS('a'), 
    3: '', 
    4: PECAS('v'),
    5: PECAS('v')
  }


def banner(rodada=None):
  print(f"{'#'*90}")
  if rodada:
    frase = f'PONG HAU KI - {rodada}ª RODADA!'
    print(f"#{frase.center(88)}#")
  else:
    print(f"#{'PONG HAU KI':^88}#")
  print(f"{'#'*90}")

def inicia_jogo():
  banner()
  print()

  # Declara que irá utilizar a variavel do escopo global dentro da função
  global qtdd_jogadas
  global pecas_jogadores
  global jogadores

  # Coleta o nome do 1º jogador e coleta as cores que cada um irá utilizar
  jogador1 = input("Qual o nome do 1º jogador: ").strip().capitalize() or "Jogador 1"
  cor_J1 = input("Peças Azuis ou Vermelhas? [A/V]: ").strip().lower() or "a"

  # Valida se a cor selecionada existe no 'banco de dados' kk
  if cor_J1 not in 'av':
    print(f"Opção inválida! {jogador1} ficou com as peças azuis")
    cor_J1 = 'a'
    cor_J2 = 'v'
  
  if cor_J1 == 'a':
    cor_J2 = 'v'
  else:
    cor_J2 = 'a'
  
  # Coleta o nome do 2º jogador
  jogador2 = input("Qual o nome do 2º jogador: ").strip().capitalize() or "Jogador 2"

  # Armazena as pecas
  pecas_jogadores = {
    jogador1: PECAS(cor_J1),
    jogador2: PECAS(cor_J2)
  }

  # Armazena os jogadores
  jogadores = [i for i in pecas_jogadores.keys()]

def main_loop():
  global qttd_partidas
  global inicia_jogando
  global jogadores

  system('cls')
  banner(qttd_partidas+1)
  if qttd_partidas == 0:
    escolhas = {
      'p' : "",
      'i': ""
    }
    
    # Sempre começará pedindo ao 1º jogador
    opc = input(f"{jogadores[0]} PAR ou ÍMPAR? [P/I]: ") or "p"
    opc = opc.strip().lower()

    while not opc in 'pi':
      system('cls')
      banner()
      print(f"{qttd_partidas+1}ª RODADA!")
      print("Opção inválida! Somente [P/I] são permitidos.")
      opc = input(f"{jogadores[0]} PAR ou ÍMPAR? [P/I]: ") or "p"
      opc = opc.strip().lower()

    if opc == 'p':
      escolhas[jogadores[0]] = 'p'
      escolhas[jogadores[1]] = 'i'
    else:
      escolhas[jogadores[0]] = 'i'
      escolhas[jogadores[1]] = 'p'

    # Sorteia numeros
    from random import choice
    vitoria = ''
    print("\nCerto... Vamos ver quem vai ganhar ", end="",)
    sleep(1)
    print(" . ", end="", flush=True)
    sleep(1)
    print(" . ", end="", flush=True)
    sleep(1)
    print(" . ", flush=True)
    num1 = choice(range(0,5))
    num2 = choice(range(0,5))  
    
    # Define quem ganhou
    if (num1 + num2) % 2 == 0:
      # É PAR!
      vitoria = 'p'
    else:
      vitoria = 'i'
    
    inicia_jogando = \
      jogadores[0] if escolhas[jogadores[0]] == vitoria else jogadores[1]

    print(f"{jogadores[0]} ({escolhas[jogadores[0]]}) tirou: {num1}")
    print(f"{jogadores[1]} ({escolhas[jogadores[1]]}) tirou: {num2}")
    print(f"Resultado: {num1 + num2}")
    print(f"\n{inicia_jogando} começará jogando!")
    sleep(2)
    print("Jogo começará em 5-",end="")
    sleep(1)
    print("4-", end="", flush=True)
    sleep(1)
    print("3-", end="", flush=True)
    sleep(1)
    print("2-", end="", flush=True)
    sleep(1)
    print("1", end="", flush=True)

  else:
    print(f"\n{inicia_jogando} começará jogando!")
    sleep(2)

  game_loop()

def game_loop():
  global qttd_partidas
  global qtdd_jogadas
  global pecas_jogadores
  global inicia_jogando
  global tabuleiro
  global posicao_jogavel
  global jogadores


  jogador_atual = inicia_jogando
  qtdd_jogadas = {jogador:0 for jogador in jogadores}
  while True:
    system("cls")
    banner(qttd_partidas+1)
    desenha_tabuleiro(tabuleiro)
    print()


    posicoes_atuais = \
      [str(pos) for pos, cor in tabuleiro.items() if cor == pecas_jogadores[jogador_atual]]
    
    if '2' in posicoes_atuais and posicao_jogavel == 4:
      posicoes_atuais.remove('2')
    elif '1' in posicoes_atuais and posicao_jogavel == 5:
      posicoes_atuais.remove('1')
    
    jogada = input(f"{jogador_atual}, deseja mover qual peça: [{'] ou ['.join(posicoes_atuais)}]: ") or 0
    
    # VALIDACOES
    # Jogador tentou mexer peça que não é sua ou não existe
    while jogada not in posicoes_atuais:
      system("cls")
      banner(qttd_partidas+1)
      desenha_tabuleiro(tabuleiro)
      print()
      print(f"Você só pode mover as peças [{'] ou ['.join(posicoes_atuais)}]")
      jogada = input(f"{jogador_atual} mover qual peça: [{'] ou ['.join(posicoes_atuais)}]: ") or 0
    
    
    
    # Grava jogada no tabuleiro
    tabuleiro[int(jogada)] = ''
    tabuleiro[posicao_jogavel] = pecas_jogadores[jogador_atual]
    qtdd_jogadas[jogador_atual]+=1

    # Valida vitoria
    posicao_jogavel = int(jogada)
    posicoes_atuais = \
      [str(pos) for pos, cor in tabuleiro.items() if cor == pecas_jogadores[jogador_atual]]

    if ('13' == "".join(posicoes_atuais) and posicao_jogavel == 4) \
      or ('23' == "".join(posicoes_atuais) and posicao_jogavel == 5):

      system("cls")
      banner(qttd_partidas+1)
      desenha_tabuleiro(tabuleiro)
      print(f"{jogador_atual}({pecas_jogadores[jogador_atual]}) VENCEU! ")
      print(f"{jogador_atual} precisou de {qtdd_jogadas[jogador_atual]} jogada(s) para ganhar.")

      inicia_jogando = jogador_atual
      qttd_partidas+=1
      redefine_tabuleiro()
      break
    
    else:
      if jogador_atual == jogadores[0]:
        jogador_atual = jogadores[1]
      else:
        jogador_atual = jogadores[0]

def desenha_tabuleiro(tabuleiro:dict):
  """Posições do Tabuleiro:
  
	 (1)-------------(2)
		| \           / |
		|   \				/		|
		|			\		/			|
		|      (3)      |
		|			/		\			|
		|		/				\		|
		|	/						\	|
   (4)             (5) 
  """
  # tabuleiro = {
  #   1: '\U0001f535', 
  #   2: '\U0001f535', 
  #   3: '', 
  #   4: '\U0001f534',
  #   5: '\U0001f534'
  # }

  for pos, peca in tabuleiro.items():
    
    if peca == "":
      peca = " "

    # Denha linha 1:
    if pos == 1:
      print()
      print("   [1]             [2]")
      if peca != " ":
        print(f"   ({peca})-----------", end="")
      else:
        print(f"   ({peca})------------", end="")

    elif pos == 2:
      if peca != " ":
        print(f"({peca})")
      else:
        print(f"-({peca})")
    
    elif pos == 3:

      print("    | \           / |")
      print("    |   \       /   |")
      print("    |     \[3]/     |")
      if peca != " ":
        print(f"    |     ({peca})      |")
      else: 
        print(f"    |      ({peca})      |")
      print("    |     /   \     |")
      print("    |   /       \   |")
      print("    | /           \ |")
    
    elif pos == 4:
      if peca != " ":
        print(f"   ({peca})           ", end="")
      else:
        print(f"   ({peca})            ", end="")
    
    else:
      if peca != " ":
        print(f"({peca})")
      else:
        print(f" ({peca})")
      
      print("   [4]             [5]")


if __name__ == "__main__":
  system("cls")
  inicia_jogo()
  while True:
    main_loop()
    opc = input("DESEJA JOGAR NOVAMENTE? [S/N]: ").strip().lower() or 'n'
    if not 's' in opc:
      print("Até Mais!")
      break

