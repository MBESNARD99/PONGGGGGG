"""
Programme affichage
"""
import pygame

#constantes de la fenêtre d'affichage
import pygame.sprite

HAUTEUR=500
LARGEUR=500      #largeur de la fenêtre
ROUGE=(255,0,0)     # définition de 3 couleurs
VERT=(0,255,0)
BLEU=(0,0,255)

#Utilisation de la bibliothèque pygame
pygame.init()
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("PONGGGGGGGGGGGGGGGGGGGGGGGGGGGG")             #titre de la fenêtre
font = pygame.font.Font('freesansbold.ttf', 35)     #choix de la police de caractères
font2 = pygame.font.Font('freesansbold.ttf', 23)
frequence = pygame.time.Clock()                     #mode animation dans pygame


score_bleu=0
score_rouge=0
txt_score_bleu_0 = font.render ( "0", 1 , (0,0,255) )
txt_score_rouge_0 = font.render ( "0", 1 , (255,0,0) )
txt_score_bleu_1 = font.render ( "1", 1 , (0,0,255) )
txt_score_rouge_1 = font.render ( "1", 1 , (255,0,0) )
txt_score_bleu_2 = font.render ( "2", 1 , (0,0,255) )
txt_score_rouge_2 = font.render ( "2", 1 , (255,0,0) )
txt_score_bleu_3 = font.render ( "3", 1 , (0,0,255) )
txt_score_rouge_3 = font.render ( "3", 1 , (255,0,0) )
txt_score_mid = font.render ( "-", 1, (255, 255, 255))

txt_win_bleu = font2.render ( "Victoire du Joueur Bleu !", 1, (255, 255, 255))
txt_win_rouge = font2.render ( "Victoire du Joueur Rouge !", 1, (255, 255, 255))
txt_win_restart = font2.render ( "Appuyez sur Espace pour Rejouer !", 1, (255, 255, 255))

play_end = False

#variables de gestion de la balle
RAYONBALLE=10
balleX=LARGEUR//2
balleY=HAUTEUR//2          #position x y de la balle au milieu dans la fenêtre
vecteurBalleX=5            #vecteur de déplacement
vecteurBalleY=4

rectangleBleuY=HAUTEUR//2
vecteurBleuY=3
rectangleRougeY=HAUTEUR//2
vecteurRougeY=3


def afficheRectangleBleu(x,y,largeur,hauteur):
    """
    affiche un rectangle en position x,y avec une largeur et une hauteur
    """
    pygame.draw.rect(fenetre, BLEU, [x, y, largeur, hauteur])




def afficheRectangleRouge(x,y,largeur,hauteur):
    """
    affiche un rectangle en position x,y avec une largeur et une hauteur
    """
    pygame.draw.rect(fenetre, ROUGE, [x, y, largeur, hauteur])






def afficheBalle():
    """
    affiche un cercle aux coordonnées x,y avec un rayon
    """
    pygame.draw.circle(fenetre, VERT, (balleX,balleY), RAYONBALLE)

def deplacementBalle():
    """
    deplace la balle
    """
    global balleX,balleY        #permet de modifier les variables balleX,balleY
    balleX=balleX+vecteurBalleX #on deplace la balle selon l'axeX
    balleY=balleY+vecteurBalleY

def deplacementRectangleBleu():

    global rectangleBleuY

    rectangleBleuY = rectangleBleuY + vecteurBleuY

def deplacementRectangleRouge():

    global rectangleRougeY

    rectangleRougeY = rectangleRougeY + vecteurRougeY

def testCollisionMurs():
    """
    test les collisions avec les murs
    """
    global vecteurBalleX,vecteurBalleY,vecteurBleuY,rectangleBleuY,vecteurRougeY,rectangleRougeY,balleX,balleY,score_rouge,score_bleu

    if balleX == 20:
        if rectangleBleuY <= balleY <= rectangleBleuY+80:
            vecteurBalleX=vecteurBalleX*-1

    if balleX == 480:
        if rectangleRougeY <= balleY <= rectangleRougeY+80:
            vecteurBalleX=vecteurBalleX*-1

    if balleX < 20:
        print("Perdu joueur Bleu / Gagné joueur Rouge")
        vecteurBalleY=4
        vecteurBalleX=5
        balleX=HAUTEUR/2
        balleY=HAUTEUR//2
        score_rouge += 1
    if balleX > 480:
        print("Perdu joueur Rouge / Gagné joueur Bleu")
        vecteurBalleY=4
        vecteurBalleX=5
        balleX=HAUTEUR/2
        balleY=HAUTEUR//2
        score_bleu += 1

    if balleX+RAYONBALLE>LARGEUR:
        vecteurBalleX=vecteurBalleX*-1
    if balleX-RAYONBALLE<0:
        vecteurBalleX=vecteurBalleX*-1
    if balleY+RAYONBALLE>HAUTEUR:
        vecteurBalleY=vecteurBalleY*-1
    if balleY-RAYONBALLE<0:
        vecteurBalleY=vecteurBalleY*-1

    if rectangleBleuY+80>HAUTEUR:
        vecteurBleuY=vecteurBleuY*0-1
    if rectangleBleuY<0:
        vecteurBleuY=vecteurBleuY*0+1

    if rectangleRougeY+80>HAUTEUR:
        vecteurRougeY=vecteurRougeY*0-1
    if rectangleRougeY<0:
        vecteurRougeY=vecteurRougeY*0+1


loop=True
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False            #fermeture de la fenêtre (croix rouge)
        if event.type == pygame.KEYDOWN:  #une touche a été pressée...laquelle ?
            if event.key == pygame.K_ESCAPE or event.unicode == 'q': #touche q pour quitter
                loop = False

    keys = pygame.key.get_pressed()         #recupération des touches appuyées en continu
    if play_end == False:
        if keys[pygame.K_UP]:    #est-ce la touche UP
            vecteurBleuY=-5
        elif keys[pygame.K_DOWN]:  #est-ce la touche DOWN
            vecteurBleuY=5
        else:
            vecteurBleuY=0
        if keys[pygame.K_z]:    #est-ce la touche UP
            vecteurRougeY=-5
        elif keys[pygame.K_s]:  #est-ce la touche DOWN
            vecteurRougeY=5
        else:
            vecteurRougeY=0

    if keys[pygame.K_SPACE]:
        if play_end == True:
            score_bleu=0
            score_rouge=0
            balleX=HAUTEUR//2
            balley=HAUTEUR//2
            vecteurBalleX=5
            vecteurBalleY=4
            play_end = False

    fenetre.fill((0,0,0))   #efface la fenêtre
    afficheBalle()
    deplacementBalle()
    testCollisionMurs()
    afficheRectangleBleu(20,rectangleBleuY,10,80)
    deplacementRectangleBleu()
    afficheRectangleRouge(480,rectangleRougeY,10,80)
    deplacementRectangleRouge()
    if score_bleu == 0:
        fenetre.blit(txt_score_bleu_0, (200, 10))
    if score_rouge == 0:
        fenetre.blit(txt_score_rouge_0, (270, 10))
    if score_bleu == 1:
        fenetre.blit(txt_score_bleu_1, (200, 10))
    if score_rouge == 1:
        fenetre.blit(txt_score_rouge_1, (270, 10))
    if score_bleu == 2:
        fenetre.blit(txt_score_bleu_2, (200, 10))
    if score_rouge == 2:
        fenetre.blit(txt_score_rouge_2, (270, 10))
    if score_bleu == 3:
        fenetre.blit(txt_score_bleu_3, (200, 10))
    if score_rouge == 3:
        fenetre.blit(txt_score_rouge_3, (270, 10))

    if score_rouge > 2:
        vecteurBalleY=0
        vecteurBalleX=0
        balleX=HAUTEUR/2
        balleY=HAUTEUR//2
        fenetre.blit(txt_win_rouge, (120, 130))
        fenetre.blit(txt_win_restart, (60, 380))
        play_end = True
    if score_bleu > 2:
        vecteurBalleY=0
        vecteurBalleX=0
        balleX=HAUTEUR/2
        balleY=HAUTEUR//2
        fenetre.blit(txt_win_bleu, (120, 130))
        fenetre.blit(txt_win_restart, (60, 380))
        play_end = True

    fenetre.blit(txt_score_mid, (240, 10))
    frequence.tick(60)
    pygame.display.update() #mets à jour la fenêtre graphique
pygame.quit()