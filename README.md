# NeuralPY
 Rede neural python

>> requirement.txt
  - para instalação dos package

>> python3 -m venv venv
>> source venv/bin/activate

def restart_do_jogo(palavra_camuflada, end_game, chance, letra, tentativas_de_letras, click_last_status, click, x, y):
  count = 0
  limite = len(palavra_camuflada)
  for n in range(len(palavra_camuflada)):
    if palavra_camuflada[n] != '*':
      count += 1
  if count == limite and click_last_status == False and click[0] == True:
    if x >= 750 and x <= 950 and y >= 25 and y <= 85:
      tentativas_de_letras = [' ', '-']
      end_game= True
      chance = 0
      letra = ' '
  return end_game, chance, tentativas_de_letras, letra