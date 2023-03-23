import pygame as pg
import random

window = pg.display.set_mode((1000, 700))

pg.font.init()
clock = pg.time.Clock()

preto = (0, 0, 0)
branco = (255, 255, 255)
font1 = pg.font.SysFont('Courier New', 70)
font2 = pg.font.SysFont('Courier New', 30)

palavras = [
  'TESTE',
  'PARALELEPIPEDO',
  'APARTAMENTO',
  'XICARA',
  'BANANA',
  'CANETA'
]

tentativas_de_letras = [' ' , '-']

palavra_escolhida = ' '

palavra_camuflada = ' '

end_game = True
 
chance = 0

acertos = 0
erros = 0

letra = ' '

click_last_status = False

def modulagem_forca(window, chance):
  pg.draw.rect(window, branco, (0, 0, 1000, 700))
  pg.draw.line(window, preto, (55, 650), (100, 96), 10) #linha vertical grande
  pg.draw.line(window, preto, (50, 650), (950, 650), 10) #linha horizontal base
  pg.draw.line(window, preto, (100, 100), (305, 100), 10) #linha horizontal topo
  pg.draw.circle(window, preto, (300,100), 15, 15) #circulo topo
  pg.draw.line(window, preto, (300, 100), (300, 150), 10) #linha vertical ponta
  if chance >= 1:
    pg.draw.circle(window, preto, (300, 200), 50, 10) #circulo cabeça
  if chance >= 2:
    pg.draw.line(window, preto, (300, 250), (300, 350), 10) #linha corpo
  if chance >= 3:
    pg.draw.line(window, preto, (300, 260), (225, 350), 10) #linha braço
  if chance >= 4:
    pg.draw.line(window, preto, (300, 260), (375, 350), 10) #linha braço
  if chance >= 5:
    pg.draw.line(window, preto, (300, 350), (375, 450), 10) #linha perna
  if chance >= 6:
    pg.draw.line(window, preto, (300, 350), (225, 450), 10) #linha perna
    
def button_restart(window):
  pg.draw.rect(window, preto, (750, 20, 200, 65), 0, 10)
  texto = font2.render('Restart', True, branco)
  window.blit(texto, (790, 35))
  
def sorteando_palavra(palavras, palavra_escolhida, end_game):
  if end_game == True:
    palavra_n = random.randint(0, len(palavras) -1)
    palavra_escolhida = palavras[palavra_n]
    end_game = False
  return palavra_escolhida, end_game #é uma função que retorna duas variáveis

def camuflando_palavra(palavra_escolhida, palavra_camuflada, tentativas_de_letras):
  palavra_camuflada = palavra_escolhida
  for n in range(len(palavra_camuflada)):
    if palavra_camuflada[n:n + 1] not in tentativas_de_letras:
      palavra_camuflada = palavra_camuflada.replace(palavra_camuflada[n], "*")
  return palavra_camuflada

def tentando_uma_letra(tentativas_de_letras, palavra_escolhida, letra, chance):
  if letra not in tentativas_de_letras:
    tentativas_de_letras.append(letra)
    if letra not in palavra_escolhida:
      chance += 1
  elif letra in tentativas_de_letras:
    pass
  return tentativas_de_letras, chance

def palavra_do_jogo(window, palavra_camuflada):
  palavra = font1.render(palavra_camuflada, True, preto)
  window.blit(palavra, (200, 550))
  
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


while True:
  for event in pg.event.get():
    if event.type == pg.QUIT:
      pg.quit()
      quit()
    if event.type == pg.KEYDOWN:
      letra = str(pg.key.name(event.key)).upper()
  
  mouse = pg.mouse.get_pos()
  mouse_position_x = mouse[0]
  mouse_position_y = mouse[1]
  
  click = pg.mouse.get_pressed()

      
  modulagem_forca(window, chance)
  button_restart(window)
  palavra_escolhida, end_game = sorteando_palavra(palavras, palavra_escolhida, end_game)
  palavra_camuflada = camuflando_palavra(palavra_escolhida, palavra_camuflada, tentativas_de_letras)
  tentativas_de_letras, chance = tentando_uma_letra(tentativas_de_letras, palavra_escolhida, letra, chance)
  palavra_do_jogo(window, palavra_camuflada)
  end_game, chance, tentativas_de_letras, letra = restart_do_jogo(palavra_camuflada, end_game, chance, letra, tentativas_de_letras, click_last_status, click, mouse_position_x, mouse_position_y)
  
  
  if click[0] == True:
    click_last_status = True
  else:
    click_last_status = False
  
  pg.display.update()
  clock.tick(60)