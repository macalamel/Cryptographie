class Crypto_mono_occurrence:
    def __init__(self) -> None:
        self.alpha=Traitement_texte().alpha
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
    
    

    def calcule_distances(self,nombre_1:float,nombre_2:float):
        return abs(nombre_1-nombre_2)

    def correspond_occurrences(self,dico:dict):

        liste_freq_code,liste_lettre_code=Cryptographie().make_list_from_dict(dico)
        liste_freq_model,liste_lettre_model=Cryptographie().make_list_from_dict(self.model_occurrences)
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
        self.alpha=Traitement_texte().alpha
        self.model_bigrame=['ES', 'LE', 'DE', 'RE', 'EN', 'ON', 'NT', 'ER', 'TE', 'ET', 'EL', 'AN', 'SE', 'LA',
                            'AI', 'NE', 'OU', 'QU', 'ME', 'IT', 'IE', 'EM', 'ED', 'UR', 'IS', 'EC', 'UE', 'TI',
                            'RA', 'NS', 'IN', 'TA', 'CE', 'AR', 'EE', 'EU', 'SA', 'CO', 'EP', 'ND', 'IL', 'SS',
                            'ST', 'SI', 'TR', 'AL', 'UN', 'PA', 'AU', 'EA', 'AT', 'MA', 'RI', 'SD', 'SO', 'US',
                            'UI', 'LL', 'NC', 'VE', 'LI', 'RO', 'IO', 'OR', 'PE', 'OI', 'PR', 'PO', 'IR', 'NA',
                            'UT', 'TD', 'CH', 'OM', 'SP', 'SL', 'DA', 'AS', 'MO', 'AC', 'DI', 'RS', 'DU', 'TL',
                            'TO', 'TS', 'RT', 'AM', 'AP', 'SC', 'LO', 'AV', 'SU', 'EV', 'NO', 'RL', 'NI', 'GE',
                            'RD', 'LU', 'NN', 'HE', 'PL', 'IQ', 'EF', 'MI', 'VA', 'TU', 'VI', 'CA', 'EQ', 'CI',
                            'TT', 'IC', 'UX', 'MM', 'OL', 'AG', 'VO', 'EI', 'MP', 'TP', 'SM', 'UL', 'HA', 'FI',
                            'FA', 'IM', 'EG', 'ID', 'AD', 'GR', 'SQ', 'AB', 'BL', 'UV', 'IV', 'NG', 'TC', 'IA',
                            'OT', 'CL', 'RC', 'RM', 'OS', 'OP', 'CT', 'FO', 'UC', 'UP', 'RR', 'JE', 'HO', 'UD',
                            'CR', 'EB', 'EO', 'IF', 'FR', 'RU', 'UA', 'NP', 'IG', 'BA', 'BR', 'OC', 'CU', 'FE',
                            'UM', 'EX', 'BI', 'BE', 'GN', 'MB', 'AF', 'HI', 'EJ', 'NF', 'GI', 'PP', 'GA', 'FF',
                            'PU', 'BO', 'SF', 'SR', 'LS', 'TQ', 'OD', 'PH', 'TM', 'DR', 'NU', 'NV', 'PI', 'OB',
                            'GU', 'NL', 'OG', 'JO', 'IP', 'TH', 'RP', 'SB', 'JA', 'NM', 'SN', 'YS', 'MU', 'UB',
                            'VR', 'SV', 'YA', 'XE', 'RG', 'EZ', 'CC', 'NQ', 'IB', 'SG', 'NR', 'AE', 'RV', 'LD',
                            'EH', 'SH', 'AY', 'PT', 'OY', 'XP', 'DS', 'RQ', 'TF', 'FL', 'YE', 'SJ', 'LH', 'JU',
                            'LT', 'FU', 'UF', 'AQ', 'IX', 'PS', 'TN', 'XI', 'GO', 'UG', 'TJ', 'TV', 'RB', 'UO',
                            'LQ', 'SY', 'AA', 'TB', 'HU', 'AJ', 'BU', 'OF', 'XD', 'RF', 'LP', 'NB', 'UJ', 'GL',
                            'HY', 'UU', 'LN', 'XA', 'LY', 'NH', 'XT', 'XC', 'NJ', 'OV', 'II', 'LC', 'DD', 'LF',
                            'YC', 'LM', 'DM', 'BS', 'DH', 'LG', 'VU', 'CD', 'AH', 'YP', 'TY', 'TG', 'CS', 'OQ',
                            'XM', 'LR', 'ZE', 'CK', 'AO', 'UQ', 'CY', 'WA', 'KO', 'XQ', 'XL', 'DL', 'RJ', 'IJ',
                            'FS', 'XS', 'XV', 'HR', 'RY', 'GT', 'OE', 'BJ', 'GM', 'LV', 'HN', 'IU', 'EY', 'XU',
                            'NY', 'KE', 'AZ', 'MD', 'RH', 'YO', 'YR', 'ZL', 'ZO', 'MY', 'SW', 'YM', 'DP', 'LB',
                            'XO', 'GS', 'CQ', 'RK', 'OA', 'MS', 'OH', 'ZA', 'DC', 'KA', 'NZ', 'XF', 'DT', 'PD',
                            'YL', 'ZV', 'MN', 'UH', 'BT', 'DJ', 'XX', 'YD', 'EW', 'OO', 'XB', 'ML', 'GD', 'YT',
                            'EK', 'ZD', 'DY', 'XN', 'KI', 'YN', 'BB', 'ZM', 'CM', 'AX', 'CP', 'LJ', 'FD', 'WE',
                            'ZP', 'UY', 'YF', 'AK', 'HM', 'ZI', 'DN', 'MT', 'WI', 'XR', 'SX', 'DQ', 'XH', 'IZ',
                            'XG', 'SK', 'OJ', 'KH', 'HL', 'OX', 'ZC', 'XJ', 'OZ', 'ZY', 'DV', 'AW', 'DF', 'LK',
                            'PM', 'ZU', 'NK', 'MC', 'DG', 'IH', 'PC', 'ZS', 'FN', 'CN', 'BY', 'CF', 'GH', 'KR',
                            'TZ', 'UZ', 'RX', 'SZ', 'NW', 'GG', 'QA', 'UK', 'IK', 'HS', 'FM', 'BD', 'JC', 'HT',
                            'HB', 'RW', 'ZB', 'YI', 'OW', 'FP', 'ZQ', 'RZ', 'DB', 'XY', 'CV', 'NX', 'JI', 'ZF',
                            'ZR', 'GC', 'YV', 'CB', 'YB', 'WO', 'YG', 'FC', 'WT', 'GY', 'KL', 'KM', 'ZN', 'VJ',
                            'MR', 'HC', 'HD', 'ZT', 'XW', 'FG', 'GQ', 'GP', 'MQ', 'KD', 'DW', 'OK', 'KS', 'ZH',
                            'GF', 'BV', 'BN', 'HV', 'PF', 'QC', 'VD', 'FB', 'MJ', 'WR', 'IY', 'HW', 'CJ', 'GB',
                            'YU', 'HP', 'FQ', 'PY', 'JY', 'TW', 'QM', 'TK', 'WY', 'YJ', 'BP', 'TX', 'VT', 'VL',
                            'HF', 'WB', 'BM', 'GV', 'FH', 'WS', 'FT', 'MF', 'PQ', 'WN', 'KY', 'WH', 'ZZ', 'ZJ',
                            'IW', 'PN', 'KB', 'KC', 'KP', 'KU', 'ZG', 'YQ', 'VC', 'LW', 'LZ', 'YK', 'MG', 'MV',
                            'HQ', 'VS', 'HJ', 'PG', 'PV', 'CG', 'MH', 'DK', 'WW', 'QD', 'BH', 'ZK', 'PJ', 'JR',
                            'CZ', 'YZ', 'QP', 'HK', 'VF', 'JH', 'HH', 'VP', 'MX', 'LX', 'QE', 'YH', 'QO', 'KX',
                            'GK', 'QL', 'VQ', 'CW', 'BC', 'VG', 'QB', 'QF', 'BG', 'YX', 'WD', 'XZ', 'UW', 'HG',
                            'KW', 'KV', 'WM', 'WL', 'KT', 'KQ', 'VM', 'PB', 'QH', 'WP', 'MW', 'WQ', 'QG', 'JB',
                            'MK', 'VK', 'FY', 'WU', 'VN', 'QS', 'PK', 'DX', 'PW', 'JK', 'QR', 'JP', 'JQ', 'YW',
                            'GJ', 'YY', 'DZ', 'BF', 'JS', 'VV', 'VY', 'XK', 'GW', 'VB', 'GZ', 'FJ', 'FK', 'FV',
                            'KN', 'KK', 'KJ', 'KF', 'BK', 'PZ', 'QY', 'FW', 'JD', 'JF', 'FX', 'JG', 'CX', 'QX',
                            'WV', 'QQ', 'WX', 'JJ', 'QW', 'WZ', 'BX', 'VW', 'PX', 'JL', 'JM', 'JN', 'VX', 'FZ',
                            'VZ', 'VH', 'QN', 'WC', 'BQ', 'QV', 'JT', 'JV', 'JW', 'KZ', 'WF', 'WG', 'GX', 'QK',
                            'QJ', 'WJ', 'WK', 'BW', 'QT', 'HX', 'HZ', 'MZ', 'KG', 'QI', 'BZ', 'QZ', 'ZW']

    def occurance_bigrame(self,text:str):
        dico_occurrences_bigrame={}
        for i in range(0,len(text)-1):
            bigrame=text[i:i+2]
            if " " not in bigrame:
                if bigrame in dico_occurrences_bigrame.keys():
                    dico_occurrences_bigrame[bigrame]+=((1/len(text))*100)
                else:
                    dico_occurrences_bigrame[bigrame]=((1/len(text))*100)
        print(dico_occurrences_bigrame)
        return dico_occurrences_bigrame

    def asso_bigrame(self,occ:dict):
        list_bigrame=Cryptographie().make_list_from_dict(occ)[1]
        print(list_bigrame)
        print(self.model_bigrame[0:len(list_bigrame)])

    


class Cryptographie:
    def __init__(self) -> None:
        self.alpha=Traitement_texte().alpha
        self.mono=Crypto_mono_occurrence()

    def brut_decalage(self,texte):
        
        for i in range(len(self.alpha)):
            trad=""
            for j in range(len(texte)):
                trad+=self.alpha[(i+self.alpha.index(texte[j]))%25]
            print(trad)

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



class Traitement_texte:
    def __init__(self) -> None:
        self.alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ "
        # self.ponctuation=",;:!?./%ùµ*^$¨£+°=)àç_è-()"
    
    def clean_accent(self,texte:str)->str:
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
    
    def clean_alpha(self,texte:str)->str:
        liste_texte=[i for i in texte.upper() if i in self.alpha]
        return "".join(liste_texte)

    def run(self,texte:str)->str:
        print(type(texte))
        texte_sans_accents=self.clean_accent(texte)
        texte_clean=self.clean_alpha(texte_sans_accents)
        return texte_clean

    
if __name__=="__main__":
    texte=open('texte_model.txt','r').read()
    print(texte)
    # teste=Crypto_bigrames()
    # text=Cryptographie().nett_normal_mode(str(input("votre message")))
    # teste.occurance_bigrame(text)

    # test=Traitement_texte()
    # print(test.run(input("message : ")))

    # test=Crypto_mono_occurrence()
    # test.occurrences(Traitement_texte().run(input("message : ")))
    
    
    # test=Cryptographie()
    # test.brut_decalage(input("message : "))


    test=Crypto_bigrames()
    test.asso_bigrame(test.occurance_bigrame(texte))








    