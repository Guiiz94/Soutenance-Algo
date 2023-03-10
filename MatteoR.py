import pygame 


# Question 1

class AB:
    def __init__(self, racine=None, gauche=None, droit=None):
        self._racine = [racine] if racine is not None else []
        self._gauche = gauche
        self._droit = droit

    def set_racine(self, racine):
        self._racine = [racine] if racine is not None else []

    def set_gauche(self, gauche):
        self._gauche = gauche

    def set_droit(self, droit):
        self._droit = droit


# Question 2

    def estVide(self):
        if self._racine == [] and self._gauche is None and self._droit is None:
            return True
        else:
            return False
        

# Question 8 

    def taille(self):
        if self.estVide():
            return 0
        else:
            if self._gauche is None and self._droit is None:
                return 1
            else:
                if self._gauche is None:
                    return 1 + self._droit.taille()
                else:
                    if self._droit is None:
                        return 1 + self._gauche.taille()
                    else:
                        return 1 + self._gauche.taille() + self._droit.taille()
                    

# Question 11 

    def prefixe(self):
        if not self.estVide():
            print(self._racine[0], end=' ')
            if self._gauche is not None:
                self._gauche.prefixe()
            if self._droit is not None:
                self._droit.prefixe()


# Question 13 

    def postfixe(self):
        if not self.estVide():
            if self._gauche:
                self._gauche.postfixe()
            if self._droit:
                self._droit.postfixe()
            print(self._racine, end=' ')

    def infixe(self):
        if not self.estVide():
            if self._gauche:
                self._gauche.infixe()
            print(self._racine, end=' ')
            if self._droit:
                self._droit.infixe()


# Question 14

    def hauteur(self):
        if self.estVide():
            return 0
        else:
            if self._gauche is not None and self._droit is not None:
                return 1 + max(self._gauche.hauteur(), self._droit.hauteur())
            else:
                if self._gauche is not None:
                    return 1 + self._gauche.hauteur()
                else:
                    if self._droit is not None:
                        return 1 + self._droit.hauteur()
                    else:
                        return 0
        


# Question 15

    def estABR(self):
        if self.estVide():
            return True
        else:
            if self._gauche is None and self._droit is None:
                return True
            else:
                if self._gauche is None:
                    return self._racine[0] < self._droit._racine[0] and self._droit.estABR()
                else:
                    if self._droit is None:
                        return self._racine[0] > self._gauche._racine[0] and self._gauche.estABR()
                    else:
                        return self._racine[0] > self._gauche._racine[0] and self._racine[0] < self._droit._racine[0] and self._gauche.estABR() and self._droit.estABR()
                    

# Question 16

    def estEquilibre(self):
        if self.estVide():
            return True
        else:
            if self._gauche is None and self._droit is None:
                return True
            else:
                if self._gauche is None:
                    return self._droit.hauteur() <= 1 and self._droit.estEquilibre()
                else:
                    if self._droit is None:
                        return self._gauche.hauteur() <= 1 and self._gauche.estEquilibre()
                    else:
                        return abs(self._gauche.hauteur() - self._droit.hauteur()) <= 1 and self._gauche.estEquilibre() and self._droit.estEquilibre()
                    

# Partie dessin

def dessineAB(Atest, x, y, dx, dy, screen):
    if not Atest.estVide():
        pygame.draw.circle(screen, (255, 255, 255), (x, y), 20)
        pygame.draw.circle(screen, (0, 0, 0), (x, y), 20, 2)
        font = pygame.font.SysFont('Arial', 20)
        text = font.render(str(Atest._racine[0]), True, (0, 0, 0))
        screen.blit(text, (x - 5, y - 10))
        if Atest._gauche is not None:
            pygame.draw.line(screen, (0, 0, 0), (x, y + 18), (x - dx, y + dy), 2)
            dessineAB(Atest._gauche, x - dx, y + dy, dx // 2, dy, screen)
        if Atest._droit is not None:
            pygame.draw.line(screen, (0, 0, 0), (x, y + 18), (x + dx, y + dy), 2)
            dessineAB(Atest._droit, x + dx, y + dy, dx // 2, dy, screen)


