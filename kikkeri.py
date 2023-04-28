from pygame import *
import pygame
import sys
import os
import time

# Initialiser Pygame
pygame.init()
pygame.font.init()

# Définir la taille de la fenêtre
largeur = 1000
hauteur = 700
pygame.display.set_caption('Kikkeri')
fenetre = pygame.display.set_mode((largeur, hauteur))

#ajouter les images dont on a besoin pour le jeu
#pour les images de boutons, on crée aussi un masque avec la fonction "get_rect"
#boutons
bouton_commencer = pygame.image.load(os.path.join("images","commencer.png"))
bouton_commencer_rect = bouton_commencer.get_rect()
bouton_commencer_rect.x = 350
bouton_commencer_rect.y = 400
bouton_jouer = pygame.image.load('images/ji.png')
bouton_jouer_rect = bouton_jouer.get_rect()
bouton_jouer_rect.x = 300
bouton_jouer_rect.y = 450
bouton_fin = pygame.image.load('images/fin.png')
bouton_fin_rect = bouton_fin.get_rect()
bouton_fin_rect.x = 900
bouton_fin_rect.y = 20
bouton_rejouer = pygame.image.load('images/rejouer.png')
bouton_rejouer_rect = bouton_rejouer.get_rect()
bouton_rejouer_rect.x = 138
bouton_rejouer_rect.y = 450
bouton_quitter = pygame.image.load('images/quitter.png')
bouton_quitter_rect = bouton_quitter.get_rect()
bouton_quitter_rect.x = 600
bouton_quitter_rect.y = 450
bouton_j3 = pygame.image.load('images/3d3b.png')
bouton_j3_rect = bouton_j3.get_rect()
bouton_j3_rect.x = 500
bouton_j3_rect.y = 450
bouton_j5 = pygame.image.load('images/j5.png')
bouton_j5_rect = bouton_j5.get_rect()
bouton_j5_rect.x = 155
bouton_j5_rect.y = 540
bouton_j10 = pygame.image.load('images/j10.png')
bouton_j10_rect = bouton_j10.get_rect()
bouton_j10_rect.x = 500
bouton_j10_rect.y = 540
#fonds
instructions = pygame.image.load('images/instructions.png')
fondblanc = pygame.image.load('images/fondblanc.png')
bannière = pygame.image.load('images/logo.png')
fondfin = pygame.image.load('images/kikkerifin.png')
fond = pygame.image.load('images/nvfond2.png')
#ballon
ballon = pygame.image.load('images/ballon.png')
#pales
i1a = pygame.image.load('images/rpetitebleue.png')
i1b = pygame.image.load('images/petitebleue.png')
i1c = pygame.image.load('images/rgrandebleue.png')
i1d = pygame.image.load('images/grandebleue.png')
i2a = pygame.image.load('images/rpetiterouge.png')
i2b = pygame.image.load('images/petiterouge.png')
i2c = pygame.image.load('images/rgranderouge.png')
i2d = pygame.image.load('images/granderouge.png')

# Définir les couleurs utilisées dans le jeu
blanc = (255, 255, 255)
noir = (0, 0, 0)
bleu = (0, 0, 255)
rouge = (255, 0, 0)
vertpelouse = (126, 217, 87)


# Créer les contours du terrain
contour_a = pygame.Rect(108, 170, 2, 130)
contour_b = pygame.Rect(108, 170, 790, 2)
contour_c = pygame.Rect(895, 170, 2, 130)
contour_d = pygame.Rect(108, 645, 790, 2)
contour_e = pygame.Rect(108, 515, 2, 130)
contour_f = pygame.Rect(895, 515, 2, 130)
contour_g = pygame.Rect(90, 295, 2, 225)
contour_h = pygame.Rect(915, 295, 2, 225)

# Créer la balle
balle = ballon.get_rect()

#si un des joueurs clique sur "quitter", un message s'affiche, puis 4 secondes après le programme se ferme 
def clique_quitter():
    jeu = True 
    while jeu == True :
      police1 = pygame.font.Font('police/ARCADECLASSIC.TTF', 50)
      fenetre.blit(fondfin, (0,0))
      message_fin = "Merci  d avoir joue !" 
      aff_mess = police1.render(str(message_fin), 1, noir)
      fenetre.blit(aff_mess, (250, 150))
      pygame.display.update()
      pygame.time.wait(3000)
      pygame.quit()
      sys.exit()

#si un des joueurs clique sur "fin", un message s'affiche pour déclarer le vainqueur
def clique_fin(s1,s2):
    jeu = True 
    while jeu == True :
      police1 = pygame.font.Font('police/RCADECLASSIC.TTF', 50)
      fenetre.blit(fondblanc, (0,0))
      fenetre.blit(bouton_rejouer,bouton_rejouer_rect)
      fenetre.blit(bouton_quitter,bouton_quitter_rect)
     
      if s1 > s2 :
        recap  = "Le joueur 1 a gagne !"
        afficherecap = police1.render(str(recap), 1, noir)  
        fenetre.blit(afficherecap, (300, 220))
      elif s1 < s2 :
        recap = "Le joueur 2 a gagne !"
        afficherecap = police1.render(str(recap), 1, noir)  
        fenetre.blit(afficherecap, (300, 220))
      else :
        recap = 'Il y   a   egalite   entre'
        recap2 = 'les deux  joueurs!'
        afficherecap = police1.render(str(recap), 1, noir)
        afficherecap2 = police1.render(str(recap2), 1, noir)
        fenetre.blit(afficherecap, (300, 220))
        fenetre.blit(afficherecap2, (320, 260))
        
      pygame.display.update()
      for evenement in pygame.event.get():
        if evenement.type == QUIT:
              pygame.quit()
              sys.exit()
        #si le joueur clique sur rejouer, on revient sur la page avec les instructions
        elif  evenement.type == pygame.MOUSEBUTTONDOWN:
          if bouton_rejouer_rect.collidepoint(evenement.pos):
              page_instructions()
          elif bouton_quitter_rect.collidepoint(evenement.pos):
              clique_quitter()
          
#fonction principale
def page_jeu(seuil):
    jeu = True
    FPS = 150
    balle.x = 310
    balle.y = 230
    vitesse_balle = [3, 3]
    vmax = [20, 20]
    score_j1 = 0
    score_j2 = 0
    montre = pygame.time.Clock()
    police1 = pygame.font.Font('police/ARCADECLASSIC.TTF', 40)
    joueur_1a = i1a.get_rect()
    joueur_1a.x = 357
    joueur_1a.y = 640
    joueur_1b = i1b.get_rect()
    joueur_1b.x = 355
    joueur_1b.y = 105
    joueur_1c = i1c.get_rect()
    joueur_1c.x = 97
    joueur_1c.y = 515
    joueur_1d = i1d.get_rect()
    joueur_1d.x = 101
    joueur_1d.y = 193
    joueur_2a = i2a.get_rect()
    joueur_2a.x = 628
    joueur_2a.y = 645
    joueur_2b = i2b.get_rect()
    joueur_2b.x = 627
    joueur_2b.y = 105
    joueur_2c = i2c.get_rect()
    joueur_2c.x = 882
    joueur_2c.y = 513
    joueur_2d = i2d.get_rect()
    joueur_2d.x = 884
    joueur_2d.y = 197

    joueur_1a_init = joueur_1a.copy()
    joueur_1b_init = joueur_1b.copy()
    joueur_1c_init = joueur_1c.copy()
    joueur_1d_init = joueur_1d.copy()
    joueur_2a_init = joueur_2a.copy()
    joueur_2b_init = joueur_2b.copy()
    joueur_2c_init = joueur_2c.copy()
    joueur_2d_init = joueur_2d.copy()

  #cette fonction permet de mettre à jour la fenêtre pour que les joueurs puissent voir la balle se déplacer, les scores augmenter, les pales bouger, etc.
    def maj_fenetre():
        fenetre.blit(fond, (0, 0))
        fenetre.blit(ballon, balle)
        score1 = police1.render("Score J1    " + str(score_j1), 1, noir)
        score2 = police1.render("Score J2    " + str(score_j2), 1, noir)
        fenetre.blit(score1, (100, 40))
        fenetre.blit(score2, (600, 40))
        pygame.draw.rect(fenetre, noir, contour_a)
        pygame.draw.rect(fenetre, noir, contour_b)
        pygame.draw.rect(fenetre, noir, contour_c)
        pygame.draw.rect(fenetre, noir, contour_d)
        pygame.draw.rect(fenetre, noir, contour_e)
        pygame.draw.rect(fenetre, noir, contour_f)
        pygame.draw.rect(fenetre, vertpelouse, contour_g)
        pygame.draw.rect(fenetre, vertpelouse, contour_h)
        fenetre.blit(i1a, joueur_1a)
        fenetre.blit(i1b, joueur_1b)
        fenetre.blit(i1c, joueur_1c)
        fenetre.blit(i1d, joueur_1d)
        fenetre.blit(i2a, joueur_2a)
        fenetre.blit(i2b, joueur_2b)
        fenetre.blit(i2c, joueur_2c)
        fenetre.blit(i2d, joueur_2d)
        fenetre.blit(bouton_fin, bouton_fin_rect)
        pygame.display.update()

    while jeu == True :
        montre.tick(FPS)
        maj_fenetre()

    # Gérer les événements
        for evenement in pygame.event.get():
            if evenement.type == pygame.MOUSEBUTTONDOWN :
                if bouton_fin_rect.collidepoint(evenement.pos):
                  clique_fin(score_j1,score_j2)

          
            if evenement.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

                # Déplacer les joueurs
            if evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_a:
                    joueur_1d.move_ip(0, 90)
                if evenement.key == pygame.K_q:
                    joueur_1c.move_ip(0, -90)
                if evenement.key == pygame.K_z:
                    joueur_1b.move_ip(0, 60)
                if evenement.key == pygame.K_s:
                    joueur_1a.move_ip(0, -60)
                if evenement.key == pygame.K_p:
                    joueur_2d.move_ip(0, 90)
                if evenement.key == pygame.K_m:
                    joueur_2c.move_ip(0, -90)
                if evenement.key == pygame.K_o:
                    joueur_2b.move_ip(0, 60)
                if evenement.key == pygame.K_l:
                    joueur_2a.move_ip(0, -60)

            elif evenement.type == pygame.KEYUP:
                if evenement.key == pygame.K_a:
                    joueur_1d = joueur_1d_init.copy()
                if evenement.key == pygame.K_q:
                    joueur_1c = joueur_1c_init.copy()
                if evenement.key == pygame.K_z:
                    joueur_1b = joueur_1b_init.copy()
                if evenement.key == pygame.K_s:
                    joueur_1a = joueur_1a_init.copy()
                if evenement.key == pygame.K_p:
                    joueur_2d = joueur_2d_init.copy()
                if evenement.key == pygame.K_m:
                    joueur_2c = joueur_2c_init.copy()
                if evenement.key == pygame.K_o:
                    joueur_2b = joueur_2b_init.copy()
                if evenement.key == pygame.K_l:
                    joueur_2a = joueur_2a_init.copy()

        # Déplacer la balle
        balle.move_ip(vitesse_balle)
        if balle.top < 175 or balle.bottom > 647:
            vitesse_balle[1] += 2
            vitesse_balle[1] = -vitesse_balle[1]
        if balle.colliderect(joueur_1c) or balle.colliderect(joueur_1d) or balle.colliderect(contour_a) or balle.colliderect(contour_e):
            vitesse_balle[0] += 2
            vitesse_balle[0] = abs(vitesse_balle[0])
        
        if balle.colliderect(joueur_2c) or balle.colliderect(joueur_2d) or balle.colliderect(contour_c) or balle.colliderect(contour_f):
            vitesse_balle[0] += 2
            vitesse_balle[0] = abs(vitesse_balle[0])
        
        if balle.colliderect(joueur_1a) or balle.colliderect(
                joueur_1b) or balle.colliderect(joueur_2a) or balle.colliderect(
                    joueur_2b) or balle.colliderect(
                        joueur_2c) or balle.colliderect(
                            joueur_2d) or balle.colliderect(
                                    contour_c) or balle.colliderect(contour_f):
            vitesse_balle[0] += 2
            vitesse_balle[0] = -vitesse_balle[0]
            
        if vitesse_balle[0] > vmax[0]:
            vitesse_balle[0] -= 3
        if vitesse_balle[1] > vmax[1]:
            vitesse_balle[1] -= 3
        if vitesse_balle[0] > vmax[0] and vitesse_balle[1] > vmax[1]:
            vitesse_balle[0] -= 3
            vitesse_balle[1] -= 3
            
        # Correction de bugs
        
        if balle.y < 170:
            vitesse_balle[1] += 2
            vitesse_balle[1] = abs(vitesse_balle[1])
            balle.y = 170
    
        if balle.colliderect(contour_g):
            vitesse_balle[1] += 2
            vitesse_balle[1] = -vitesse_balle[1]
            score_j2 += 1
            balle.x = 850
            balle.y = 230
            pygame.time.wait(250)
            vitesse_balle = [-5, -5]

        if balle.colliderect(contour_h):
            vitesse_balle[1] += 2
            vitesse_balle[1] = -vitesse_balle[1]
            score_j1 += 1
            balle.x = 310
            balle.y = 230
            pygame.time.wait(250)
            vitesse_balle = [5, 5]

        if seuil != None :
          if score_j1 == seuil or score_j2 == seuil :
            clique_fin(score_j1,score_j2)

#une page avec les instructions et les différents modes de jeu
def page_instructions():
    jeu = True 
    while jeu == True :
      fenetre.blit(instructions, (0,0))
      fenetre.blit(bouton_jouer,bouton_jouer_rect)
      fenetre.blit(bouton_j3,bouton_j3_rect)
      fenetre.blit(bouton_j5,bouton_j5_rect)
      fenetre.blit(bouton_j10,bouton_j10_rect)
      
      pygame.display.update()
      for evenement in pygame.event.get():
        if evenement.type == QUIT:
              pygame.quit()
              sys.exit()
        elif evenement.type == pygame.MOUSEBUTTONDOWN:
          if bouton_jouer_rect.collidepoint(evenement.pos):
            seuil = None
            page_jeu(seuil)
          elif bouton_j3_rect.collidepoint(evenement.pos):
            seuil = 3
            page_jeu(seuil)
          elif bouton_j5_rect.collidepoint(evenement.pos):
            seuil = 5
            page_jeu(seuil)
          elif bouton_j10_rect.collidepoint(evenement.pos):
            seuil = 10
            page_jeu(seuil)
        


def page_lancement():
    jeu = True
    while jeu == True :
        fenetre.blit(bannière, (0,0))
        fenetre.blit(bouton_commencer, bouton_commencer_rect)
        pygame.display.update()
        for evenement in pygame.event.get():
            if evenement.type == QUIT:
                pygame.quit()
                sys.exit() 
            elif evenement.type == pygame.MOUSEBUTTONDOWN:
                if bouton_commencer_rect.collidepoint(evenement.pos):
                    page_instructions()

page_lancement()
