class Crypto_mono_occurrence:
    def __init__(self) -> None:
        self.alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.ponctuation=",;:!?./%ùµ*^$¨£+°=)àç_è-()"
        self.model_occurrences={'A': 8.11,
        'B': 0.81,
        'C': 3.38,
        'D': 4.27,
        'E': 17.27,
        'F': 1.12,
        'G': 1.27,
        'H': 0.77,
        'I': 7.34,
        'J': 0.61,
        'K': 0.04,
        'L': 5.68,
        'M': 3.24,
        'N': 7.15,
        'O': 5.14,
        'P': 2.89,
        'Q': 1.34,
        'R': 6.46,
        'S': 7.90,
        'T': 7.26,
        'U': 6.24,
        'V': 1.83,
        'W': 0.04,
        'X': 0.39,
        'Y': 0.24,
        'Z': 0.15}

    def occurrences(self,text:list)->dict:
        text=text.upper()
        list=[]
        for i in text:
            if not i in list:
                list.append(i)
        dico={}
        len_text=0
        for i in text:
            if i in self.alpha:
                if not i in dico.keys():
                    dico[i]=1
                else:
                    dico[i]+=1
                len_text+=1

        for i in dico.keys():
            dico[i]/=len_text
            dico[i]*=100
        for k,v in dico.items():
            print(k,":",v)
        return dico
    
    def make_list_from_dict(self,dico:dict)->list:
        liste_lettre=list(dico.keys())
        liste_frequence=list(dico.values())
        liste_lettre_new=[]
        liste_frequence_new=[]
        for i in range(len(liste_frequence)):
            maxi=max(liste_frequence)
            index_maxi=liste_frequence.index(maxi)
            liste_frequence_new.append(maxi)
            corresp_lettre=liste_lettre[index_maxi]
            liste_lettre_new.append(corresp_lettre)
            liste_frequence.remove(maxi)
            liste_lettre.remove(corresp_lettre)
        return liste_frequence_new,liste_lettre_new

    def calcule_distances(self,nombre_1:float,nombre_2:float):
        return abs(nombre_1-nombre_2)

    def correspond_occurrences(self,dico:dict):

        liste_freq_code,liste_lettre_code=self.make_list_from_dict(dico)
        liste_freq_model,liste_lettre_model=self.make_list_from_dict(self.model_occurrences)
        alpha_correspond={liste_lettre_code[i]:liste_lettre_model[i] for i in range(len(liste_lettre_code))}
        return alpha_correspond


        # alpha_correspond={}
        # for k,v in dico.items():
        #     mini=None
        #     for key,value in self.model_occurrences.items():
        #         if type(mini) is not list:
        #             mini=[key,self.calcule_distances(v,value)]
        #         else:
        #             dist=self.calcule_distances(v,value)
        #             if mini[1]>dist:
        #                 mini=[key,self.calcule_distances(v,value)]
        #     alpha_correspond[k]=mini[0]
        # for k,v in alpha_correspond.items():
        #     print(k,":",v)
        # return alpha_correspond

    def inverse_dico(self,dico:dict)->dict:
        return {v:k for k,v in dico.items()}
    
class Crypto_bigrames:
    def __init__(self) -> None:
        self.alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def occurance_bigrame(self,text):
        dico_occurrences_bigrame={}
        for i in range(0,len(text)-1):
            bigrame=text[i:i+2]
            if bigrame in dico_occurrences_bigrame.keys():
                dico_occurrences_bigrame[bigrame]+=((1/len(text))*100)
            else:
                dico_occurrences_bigrame[bigrame]=((1/len(text))*100)
        for k,v in dico_occurrences_bigrame.items():
            print(k,":",v)
        print(dico_occurrences_bigrame["ES"])

    


class Cryptographie:
    def __init__(self) -> None:
        self.alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.mono=Crypto_mono_occurrence()

    def traduction(self,text:list,dico:dict)->str:
        result=""
        for i in text :
            if i in dico.keys():
                result += dico[i]
            else :
                result += i
        return result
    
    def switch_symbole_to_lettre(self,liste_symbole):
        dico_symbole={}
        alpha_dispo=self.alpha
        for i in liste_symbole:
            if not i in dico_symbole.keys():
                dico_symbole[i]=alpha_dispo[0]
                alpha_dispo=alpha_dispo[1:]
        text_lettre=self.traduction(liste_symbole,dico_symbole)
        return text_lettre
    
    def nett_normal_mode(self,text)->str:
        liste_lettre=list(text)
        while " " in liste_lettre:
            liste_lettre.remove(" ")
        text="".join(liste_lettre)
        return text
    
    def nett_symbole_mode(self,text,delimiter)->str:
        liste_symbole=text.split(delimiter)
        print(liste_symbole)
        while "" in liste_symbole:
            liste_symbole.remove("")
        text_lettre=self.switch_symbole_to_lettre(liste_symbole)

    def normal_mode(self)->None:
        text=str(input("votre message : "))
        dico_occurrence=self.mono.occurrences(text)
        dico_traduction=self.mono.correspond_occurrences(dico_occurrence)
        claire=self.traduction(text.upper(),dico_traduction)
        print(claire)

    def symbole_mode(self)->None:
        text=str(input("votre message : "))
        delimiter=str(input("delimiter : "))
        text_lettre=self.nett_symbole_mode(text,delimiter)
        dico_occurrence=self.mono.occurrences(text_lettre)
        dico_traduction=self.mono.correspond_occurrences(dico_occurrence)
        claire=self.traduction(text_lettre,dico_traduction)
        print(claire)


class Traitement_texte:
    def __init__(self) -> None:
        self.alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        # self.ponctuation=",;:!?./%ùµ*^$¨£+°=)àç_è-()"
    
    def clean_accent(texte:str)->str:
        """
        fonction qui retire tous les accents d'un texte
        """

        # creation des liste pour les lettre a plusieurs accents

        liste_e=["é","è","ê","ë"]
        liste_a=["à","â","ä","ã"]
        liste_o=["ô","ö","õ","ò"]
        liste_i=["ï","î","ì"]
        liste_u=["û","ü","ù"]

        # on met le texte en forme de liste pour pouvoir traiter
        liste_texte=list(texte)

        # traitement du texte et suppression des accents
        for i in range(len(liste_texte)):
            if liste_texte[i] in liste_e:
                liste_texte[i]="e"
            elif liste_texte[i] in liste_a:
                liste_texte[i]="a"
            elif liste_texte[i] in liste_i:
                liste_texte[i]="i"
            elif liste_texte[i] in liste_o:
                liste_texte[i]="o"
            elif liste_texte[i] in liste_u:
                liste_texte[i]="u"
            elif liste_texte[i]=="ÿ":
                liste_texte[i]="y"
            elif liste_texte[i]=="ç":
                liste_texte[i]="c"

        # on reforme le texte 
        texte_clean="".join(liste_texte)

        # on retourne le texte
        return texte_clean
    
        
        pass
"""

"""
    
if __name__=="__main__":
    # teste=Crypto_bigrames()
    # text=Cryptographie().nett_normal_mode(str(input("votre message")))
    # teste.occurance_bigrame(text)

    test=Traitement_texte
    print(test.clean_accent(input("message : ")))