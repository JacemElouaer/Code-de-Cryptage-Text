
import numpy as np





#  noeuds :  noeuds de la theorie de graph


class noeuds:
#il y a trois deferent couleur
    def __init__(self,color,voisin):
        #coleur et un identifiant des differences tout au long les opperation
        self.color = color
        #voisin liste des noeuds qui contient les noeuds voisins de cette noeud
        self.voisin = voisin
    def affichage(self):
        self.color
    def affichage_total(self):
        print(self.color)
        print(self.voisin)

#input
#l'exemple --> devrait respecter les theories de
#Exemple -->
#5011003314202132024303423


class program:
    file =[]
    def __init__(self,raw,n_noeuds,ens_noeuds):
        self.raw_text = raw
        self.n_noeuds = n_noeuds
        self.ens_noeuds = ens_noeuds

    def set_up(self):
        self.n_noeuds = int(self.raw_text[0:1])
        self.raw_text= self.raw_text[1:len(self.raw_text)]

    def formulate(self):
        print(self.n_noeuds)
        for  i in range(self.n_noeuds):
            self.ens_noeuds["noeud_%s" % i] = noeuds("blue",[])
    def affichage(self):
        print(self.raw_text)
        print(self.n_noeuds)
    def affichage_noeuds(self):
        for key in self.ens_noeuds:
            print(key , " -> " , self.ens_noeuds[key].color)
    def set_voisin(self):
        ens=self.ens_noeuds
        indice_1 = ""
        indice_2 = ""
        liste =list(self.raw_text)
        print(list)
        for i in range(len(liste)):


            if(i%2==1):
                print(i,"pass")
            else:
                indice_1 = "noeud_"
                indice_2 = "noeud_"
                indice_1 += str(liste[i])
                indice_2 += str(liste[i+1])
                print(indice_1,indice_2)
            self.ens_noeuds[indice_1].voisin.append(self.ens_noeuds[indice_2])

    def affichage_total(self):
        for key in self.ens_noeuds:
            print(key , " -> " , self.ens_noeuds[key].color)
            for i in self.ens_noeuds[key].voisin :
                print(i)
    def algo_larg(self):
        file=[]
        f=self.ens_noeuds["noeud_0"]

        while(f.color!="noir"):
            f.color="gris"
            for i in f.voisin:

                if (i.color=="blue"):
                    i.color="gris"
                    print ("changer couleur vers blanc ",i)
                file.append(i)


            f.color = "noir"
            print ("changer couleur vers black")
            file = program.modify_file(file)
            f=file[0]

    def algo_long(self):
        file = []
        f = self.ens_noeuds["noeud_0"]
        while (f.color == "noir"):
            f.color = "gris"
            for i in f.voisin:
                if (i.color == "blue"):
                    i.color = "gris"
                file.insert(1,i)

            f.color = "noir"
            file = program.modify_file(file)
            f = file[0]
    @staticmethod
    def modify_file(file):
        file= file [0: len(file)-1]
        return file





if __name__ == "__main__" :

    algo_largeur  = program(input("donner le raw text     : :   "), 0 ,{})
    algo_largeur.set_up()
    algo_largeur.affichage()
    algo_largeur.formulate()
    algo_largeur.affichage_noeuds()

    print("*" * 25, "Affichage  des noeuds voisin", "*" * 25)
    algo_largeur.set_voisin()

    print("*"*25,"Affichage total des noeuds voisin","*"*25)
    algo_largeur.affichage_total()

    print("*"*25,"parcourt par longueur","*"*25)
    print()
    algo_largeur.algo_larg()
    print()
    print("*"*25,"parcourt par longueur","*"*25)
    algo_largeur.algo_long()









