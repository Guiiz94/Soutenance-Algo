from MatteoR import AB
from MatteoR import dessineAB
import pygame 


# Question 3

A1 = AB()

if A1.estVide():
    print("L'arbre A1 est vide.")
else:
    print("L'arbre A1 n'est pas vide.")


# Question 4

A2 = AB(racine=5)

if A2.estVide():
    print("L'arbre A2 est vide.")
else:
    print("L'arbre A2 n'est pas vide.")


# Question 5

A3 = AB(racine=3)


# Question 6

A2.set_gauche(A3)


# Question 7

Agauche = AB(racine=5, gauche=AB(racine=3), droit=AB(racine=8))
Aracine = AB(racine=10, gauche=Agauche, droit=AB(racine=12))
Atest = Aracine

print(Atest.estVide())


# Question 9

print(Atest.taille())


# Question 10

# La méthode taille() est récursive, elle s'arrête quand elle rencontre un arbre vide.


# Question 12

Atest.prefixe()
print()
# 10 5 3 8 12


# Question 13 (suite)

Atest.postfixe()
print()
# 3 8 5 12 10

Atest.infixe()
print()
# 3 5 8 10 12


# Question 14 (suite)

print(Atest.hauteur())



# Question 15 (suite)

print(Atest.estABR())


# Question 16 (suite)

print(Atest.estEquilibre())



BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Est-ce un ABR ?")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if pos[0] < 300 and Atest.estABR():
                text = "Oui"
                color = VERT
            elif pos[0] >= 300 and not Atest.estABR():
                text = "Non"
                color = VERT
            else:
                if pos[0] < 300:
                    text = "Oui"
                else:
                    text = "Non"
                color = ROUGE
    
    screen.fill(BLANC)
    dessineAB(Atest, 400, 50, 200, 100, screen)
    
    font = pygame.font.Font(None, 36)
    question = font.render("Est-ce un ABR ?", True, NOIR)
    screen.blit(question, (300, 400))

    
    font = pygame.font.Font(None, 24)
    oui = font.render("Oui", True, NOIR)
    non = font.render("Non", True, NOIR)
    screen.blit(oui, (250, 500))
    screen.blit(non, (500, 500))
    
    if "text" in locals():
        reponse = font.render(text, True, color)
        screen.blit(reponse, (380, 550))
    pygame.display.flip()

pygame.quit()
