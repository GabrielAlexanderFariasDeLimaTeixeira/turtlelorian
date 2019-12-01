# encoding = utf-8
import sys
import pygame
import pygameMenu

# AJUSTANDO VARIÁVEIS
WINDOW_SIZE = (1200, 800)

# TEXTO DO MENU DE AJUDA
HELP = ['Instrucoes: ',
        'Use  as  setas  para  cima  e  para  baixo  para',
        'mover  o  Turtlelorian.  Desvie  dos  obstaculos',
        'e  sobreviva  o  maximo  de  tempo  possivel!']

# TEXTO DO MENU DE CRÉDITOS
ABOUT = ['Universidade  do  Estado  do  Amazonas  -  UEA',
         'Bacharelado  Sistemas  da  Informacao',
         'Laboratorio  de Programacao  de  Computadores',
         'PROF.  DR.  JUCIMAR  JR',
         '                   ',
         'GABRIEL  ALEXANDER  FARIAS  DE  LIMA  TEIXEIRA',
         'HELDER  MELIK  SCHRAMM',
         'NATAN',
         '                   ',
         'Assets  de  terceiros:',
         'Pablo  Pizarro  R.  -  PygameMenu:  https://github.com/ppizarror/pygame-menu.git',
         'Agradecimentos  especiais:'
         'TECHWITHTIM  -  Tutorial  Pygame:  https://techwithtim.net']

# IMAGEM DE BACKGROUND DO JOGO
IMG_BACKGROUND = None

# COR DA TELA
COLOR_BACKGROUND = (128, 0, 128)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

# FPS DA TELA
FPS = 60.0

# IMAGEM DO BACKGROUND DO MENU
MENU_BACKGROUND = None

# RELÓGIO DE FRAMES
clock = None

# MENU PRINCIPAL
main_menu = None

# TELA DO JOGO
window = None


# COLORIR BACKGROUND
def main_background():
    global window
    window.fill(COLOR_BACKGROUND)


# PROGRAMAR AQUI O LOOP DO JOGO
def play_function():
    exit()


# CRIANDO LAÇO PRINCIPAL DO JOGO
def game_play(test=False):

    global clock
    global main_menu
    global window

    # Iniciando Pygame
    pygame.init()

    # Criando tela e objetos do jogo
    window = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Turtlelorian")
    clock = pygame.time.Clock()

    # Menu sobre o jogo
    about_menu = pygameMenu.TextMenu(window,
                                     bgfun=main_background,
                                     color_selected=COLOR_WHITE,
                                     font=pygameMenu.font.FONT_BEBAS,
                                     font_color=COLOR_BLACK,
                                     font_size=30,
                                     menu_alpha=100,
                                     menu_height=int(WINDOW_SIZE[1] * 0.8),
                                     menu_width=int(WINDOW_SIZE[0] * 0.8),
                                     onclose=pygameMenu.events.DISABLE_CLOSE,
                                     option_shadow=False,
                                     menu_color=COLOR_BACKGROUND,
                                     title='Sobre o jogo',
                                     window_height=WINDOW_SIZE[1],
                                     window_width=WINDOW_SIZE[0]
                                     )
    for l in ABOUT:
        about_menu.add_line(l)
    about_menu.add_line(pygameMenu.locals.TEXT_NEWLINE)
    about_menu.add_option('Return to menu', pygameMenu.events.BACK)

    # Menu de Instruções
    help_menu = pygameMenu.TextMenu(window,
                                    bgfun=main_background,
                                    color_selected=COLOR_WHITE,
                                    font=pygameMenu.font.FONT_BEBAS,
                                    font_color=COLOR_BLACK,
                                    font_size=30,
                                    menu_alpha=100,
                                    menu_height=int(WINDOW_SIZE[1] * 0.8),
                                    menu_width=int(WINDOW_SIZE[0] * 0.8),
                                    onclose=pygameMenu.events.DISABLE_CLOSE,
                                    option_shadow=False,
                                    menu_color=COLOR_BACKGROUND,
                                    title='Instrucoes',
                                    window_height=WINDOW_SIZE[1],
                                    window_width=WINDOW_SIZE[0]
                                    )
    for l in HELP:
        help_menu.add_line(l)
    help_menu.add_line(pygameMenu.locals.TEXT_NEWLINE)
    help_menu.add_option('Return to menu', pygameMenu.events.BACK)

    # Menu de Jogo
    play_menu = pygameMenu.Menu(window,
                                bgfun=main_background,
                                color_selected=COLOR_WHITE,
                                font=pygameMenu.font.FONT_BEBAS,
                                font_color=COLOR_BLACK,
                                font_size=30,
                                menu_alpha=100,
                                menu_color=COLOR_BACKGROUND,
                                menu_height=int(WINDOW_SIZE[1] * 0.8),
                                menu_width=int(WINDOW_SIZE[0] * 0.8),
                                onclose=pygameMenu.events.DISABLE_CLOSE,
                                option_shadow=False,
                                title='Turtlelorian',
                                window_height=WINDOW_SIZE[1],
                                window_width=WINDOW_SIZE[0]
                                )

    # Criando as opções do menu
    play_menu.add_option('Start', play_function)
    play_menu.add_option('Ajuda', help_menu)
    play_menu.add_option('Sobre', about_menu)
    play_menu.add_option('Sair', pygameMenu.events.EXIT)

    # Ajustando
    play_menu.set_fps(FPS)

    while True:

        # Frames
        clock.tick(FPS)

        # Background
        main_background()

        # Eventos
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and main_menu.is_disabled():
                    main_menu.enable()
                    return

        # Menu Principal
        play_menu.mainloop(events, disable_loop=test)

        # Atualizar tela
        pygame.display.flip()

        if test:
            break


if __name__ == '__main__':
    game_play()
