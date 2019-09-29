import os
import glob
import pandas as pd
from shutil import copyfile


#################
#               #
#   gerechten   #
#               #
#################


#----------------------------------------------------------------------

index = 'P1'

specs_1 = {'index': index,
           'gerecht': ['Verse tagiatelle met cherrytomatensaus'],
           'tijd': [40], 
           'veggie': [True]}

ingr_1 = {'index': index,
          'gerecht': ['Verse tagiatelle met cherrytomatensaus']*5,
          'ingredienten': ['ajuin', 
                           'cherrytomaat', 
                           'knoflookteen', 
                           'tagiatelle', 
                           'geraspte kaas'], 
          '1p': [0.5,300,0.5,125,15],
          '2p': [1,600,1,250,25],
          '3p': [1.5,900,1.5,375,40],
          '4p': [2,1200,2,500,50],
         }

specs_df = pd.DataFrame(specs_1).set_index('gerecht')
ingr_df = pd.DataFrame(ingr_1).set_index('gerecht')

#----------------------------------------------------------------------

index = 'P20'

specs = {'index': index,
         'gerecht': ['Farfalle met bospaddenstoelenpesto'],
         'tijd': [20], 
         'veggie': [True]}

ingr = {'index': index,
          'gerecht': ['Farfalle met bospaddenstoelenpesto']*7,
          'ingredienten': ['farfalle', 
                           'sjalot', 
                           'champignons', 
                           'bospaddenstoelenpesto', 
                           'veldsla',
                           'peterselie',
                           'geraspte kaas'],
          '1p': [90,0.5,125,40,20,2.5,15],
          '2p': [180,1,250,80,40,5,25],
          '3p': [270,1.5,375,120,60,7.5,50],
          '4p': [360,2,500,160,80,10,75],
         }

specs_df = specs_df.append(pd.DataFrame(specs).set_index('gerecht'))
ingr_df = ingr_df.append(pd.DataFrame(ingr).set_index('gerecht'))

#----------------------------------------------------------------------

index = 'V7'

specs = {'index': index,
           'gerecht': ['Gepanneerde heekfilet'],
           'tijd': [35], 
           'veggie': [True]}

ingr = {'index': index,
          'gerecht': ['Gepanneerde heekfilet']*5,
          'ingredienten': ['aardappelen', 
                           'prei', 
                           'peterselie', 
                           'spinazie', 
                           'heekfilet'],
          '1p': [200,0.5,2.5,100,1],
          '2p': [400,1,5,200,2],
          '3p': [600,1.5,7.5,300,3],
          '4p': [800,2,10,400,4]
         }

specs_df = specs_df.append(pd.DataFrame(specs).set_index('gerecht'))
ingr_df = ingr_df.append(pd.DataFrame(ingr).set_index('gerecht'))

#----------------------------------------------------------------------

index = 'V22'

specs = {'index': index,
           'gerecht': ['parelcouscous met heekfilet'],
           'tijd': [25], 
           'veggie': [True]}

ingr = {'index': index,
          'gerecht': ['parelcouscous met heekfilet']*6,
          'ingredienten': ['knoflookteen', 
                           'prei', 
                           'witloof', 
                           'parelcouscous', 
                           'kruidenkaas',
                           'heekfilet'],
          '1p': [1,0.5,1,85,25,1],
          '2p': [2,1,2,170,50,2],
          '3p': [2,1.5,3,250,75,3],
          '4p': [3,2,4,335,100,4]
         }

specs_df = specs_df.append(pd.DataFrame(specs).set_index('gerecht'))
ingr_df = ingr_df.append(pd.DataFrame(ingr).set_index('gerecht'))


#----------------------------------------------------------------------

index = 'V6'
gerecht = 'Warme maaltijdsalade met gerookte forel'

specs = {'index': [index],
           'gerecht': [gerecht],
           'tijd': [20], 
           'veggie': [True]}

ingr = {'index': [index]*8,
          'gerecht': [gerecht]*8,
          'ingredienten': ['krieltjes', 
                           'rode paprika', 
                           'rode ajuin', 
                           'knoflookteen', 
                           'slahart',
                           'citroen',
                           'dille',
                           'gerookte forelfilet'],
          '1p': [200,0.5,0.5,0.5,1,0.5,2.5,1],
          '2p': [400,1,1,1,2,1,5,2],
          '3p': [600,1.5,1.5,1.5,3,1.5,7.5,3],
          '4p': [800,2,2,2,4,2,10,4]
         }

specs_df = specs_df.append(pd.DataFrame(specs).set_index('gerecht'))
ingr_df = ingr_df.append(pd.DataFrame(ingr).set_index('gerecht'))


#----------------------------------------------------------------------

index = 'F17'
gerecht = 'Veggieburger met zoete aardappelpartjes'

specs = {'index': [index],
           'gerecht': [gerecht],
           'tijd': [35], 
           'veggie': [True]}

ingr = {'index': [index]*6,
          'gerecht': [gerecht]*6,
          'ingredienten': ['zoete aardappel', 
                           'munt', 
                           'tomaat', 
                           'veggieburger', 
                           'hamburgerbol',
                           'sla'],
          '1p': [200,5,2,1,1,30],
          '2p': [400,10,3,2,2,60],
          '3p': [600,15,4,3,3,90],
          '4p': [750,20,5,4,4,120]
         }

specs_df = specs_df.append(pd.DataFrame(specs).set_index('gerecht'))
ingr_df = ingr_df.append(pd.DataFrame(ingr).set_index('gerecht'))


#----------------------------------------------------------------------

index = 'F2'
gerecht = 'Portobelloburger met spiegelei'

specs = {'index': [index],
           'gerecht': [gerecht],
           'tijd': [45], 
           'veggie': [True]}

ingr = {'index': [index]*7,
          'gerecht': [gerecht]*7,
          'ingredienten': ['aardappelen', 
                           'rode ajuin', 
                           'courgette', 
                           'portobello', 
                           'geraspte kaas',
                           'hamburgerbol',
                           'ei'],
          '1p': [250,0.5,0.5,1,25,1,1],
          '2p': [500,1,1,2,50,2,2],
          '3p': [750,1.5,1.5,3,75,3,3],
          '4p': [1000,2,2,4,100,4,4]
         }

specs_df = specs_df.append(pd.DataFrame(specs).set_index('gerecht'))
ingr_df = ingr_df.append(pd.DataFrame(ingr).set_index('gerecht'))

#----------------------------------------------------------------------

index = 'F16'
gerecht = 'Mexicaanse nachos'

ingredienten = ['tortilla',
                'geraspte kaas',
                'limoen',
                'tomaat',
                'zwarte bonen',
                'koriander',
                'knoflookteen',
                'avocado',
                'pompoenpitten',
                'zure room']

specs = {'index': [index],
           'gerecht': [gerecht],
           'tijd': [25], 
           'veggie': [True]}

ingr = {'index': [index]*len(ingredienten),
          'gerecht': [gerecht]*len(ingredienten),
          'ingredienten': ingredienten,
          '1p': [2,25,0.5,1.5,0.5,2.5,0.25,0.5,5,25],
          '2p': [4,50,1,3,1,5,0.5,1,10,50],
          '3p': [6,75,1.5,4.5,1.5,7.5,0.75,1.5,15,75],
          '4p': [8,100,2,6,2,10,1,2,20,100]
         }

specs_df = specs_df.append(pd.DataFrame(specs).set_index('gerecht'))
ingr_df = ingr_df.append(pd.DataFrame(ingr).set_index('gerecht'))

#----------------------------------------------------------------------

index = 'F6'
gerecht = 'Tonijnburger'

ingredienten = ['krieltjes',
                'komkommer',
                'tomaat',
                'tonijn in blik',
                'ei',
                'panko']

specs = {'index': [index],
          'gerecht': [gerecht],
           'tijd': [20], 
           'veggie': [True]}

ingr = {'index': [index]*len(ingredienten),
          'gerecht': [gerecht]*len(ingredienten),
          'ingredienten': ingredienten,
          '1p': [200,0.5,1,1,1,12.5],
          '2p': [400,1,2,1,2,25],
          '3p': [600,1.5,3,2,3,32.5],
          '4p': [800,2,4,2,4,50]
         }

specs_df = specs_df.append(pd.DataFrame(specs).set_index('gerecht'))
ingr_df = ingr_df.append(pd.DataFrame(ingr).set_index('gerecht'))

#----------------------------------------------------------------------

index = 'F15'
gerecht = 'Pizza funghi'

ingredienten = ['champignons',
                'courgette',
                'rode ajuin',
                'knoflookteen',
                'mozzarella',
                'passata',
                'flat bread',
                'rucola']

specs = {'index': [index],
          'gerecht': [gerecht],
           'tijd': [40], 
           'veggie': [True]}

ingr = {'index': [index]*len(ingredienten),
          'gerecht': [gerecht]*len(ingredienten),
          'ingredienten': ingredienten,
          '1p': [125,0.5,0.5,0.5,60,100,2,20],
          '2p': [250,1,1,1,125,200,4,40],
          '3p': [375,1.5,1.5,1.5,185,300,6,60],
          '4p': [500,2,2,2,250,400,8,80]
         }

specs_df = specs_df.append(pd.DataFrame(specs).set_index('gerecht'))
ingr_df = ingr_df.append(pd.DataFrame(ingr).set_index('gerecht'))

#----------------------------------------------------------------------

index = 'F14'
gerecht = 'Lasagne met prei en courgette'

ingredienten = ['knoflookteen',
                'prei',
                'room',
                'courgette',
                'rode peper',
                'lasagnebladen',
                'geraspte kaas']

specs = {'index': [index],
          'gerecht': [gerecht],
           'tijd': [50], 
           'veggie': [True]}

ingr = {'index': [index]*len(ingredienten),
          'gerecht': [gerecht]*len(ingredienten),
          'ingredienten': ingredienten,
          '1p': [1,0.5,50,0.5,0.33,125,15],
          '2p': [2,1,100,1,0.66,250,25],
          '3p': [3,1.5,150,1.5,1,375,35],
          '4p': [4,2,200,2,1.33,500,50]
         }

specs_df = specs_df.append(pd.DataFrame(specs).set_index('gerecht'))
ingr_df = ingr_df.append(pd.DataFrame(ingr).set_index('gerecht'))

#----------------------------------------------------------------------

index = 'C6'
gerecht = 'Shakshuka met geitenkaas'

ingredienten = ['ajuin',
                'knoflookteen',
                'rode peper',
                'rode paprika',
                'pruimtomaat',
                'peterselie',
                'ei',
                'geitenkaas']

specs = {'index': [index],
          'gerecht': [gerecht],
           'tijd': [30], 
           'veggie': [True]}

ingr = {'index': [index]*len(ingredienten),
          'gerecht': [gerecht]*len(ingredienten),
          'ingredienten': ingredienten,
          '1p': [0.5,1,0.25,0.5,2,2.5,2,50],
          '2p': [1,2,0.5,1,4,5,4,75],
          '3p': [1.5,3,0.75,1.5,6,7.5,6,100],
          '4p': [2,3,1,2,8,10,8,125]
         }

specs_df = specs_df.append(pd.DataFrame(specs).set_index('gerecht'))
ingr_df = ingr_df.append(pd.DataFrame(ingr).set_index('gerecht'))


#----------------------------------------------------------------------


index = 'P8'
gerecht = 'Spaghetti met geroosterde groeten'

ingredienten = ['courgette',
                'kerstomaten',
                'spaghetti',
                'knoflookteen',
                'zwarte olijven',
                'kappertjes',
                'feta',
                'munt']

specs = {'index': [index],
           'gerecht': [gerecht],
           'tijd': [20], 
           'veggie': [True]}

ingr = {'index': [index]*len(ingredienten),
          'gerecht': [gerecht]*len(ingredienten),
          'ingredienten': ingredienten,
          '1p': [0.5,125,90,0.5,15,15,40,1],
          '2p': [1,250,180,1,30,30,75,2],
          '3p': [1.5,375,270,1.5,45,45,100,3],
          '4p': [2,500,360,2,60,60,125,4]
         }

specs_df = specs_df.append(pd.DataFrame(specs).set_index('gerecht'))
ingr_df = ingr_df.append(pd.DataFrame(ingr).set_index('gerecht'))


#----------------------------------------------------------------------


index = 'F1'
gerecht = 'Broodje ommelet'

ingredienten = ['knoflookteen',
                'portobello',
                'zak wortel rode kool',
                'broodje',
                'ei',
                'geraspte kaas']

specs = {'index': [index],
           'gerecht': [gerecht],
           'tijd': [20], 
           'veggie': [True]}

ingr = {'index': [index]*len(ingredienten),
          'gerecht': [gerecht]*len(ingredienten),
          'ingredienten': ingredienten,
          '1p': [0.5,1,100,1,2,25],
          '2p': [1,2,200,2,4,50],
          '3p': [1.5,3,300,3,6,75],
          '4p': [2,4,400,4,8,100]
         }

specs_df = specs_df.append(pd.DataFrame(specs).set_index('gerecht'))
ingr_df = ingr_df.append(pd.DataFrame(ingr).set_index('gerecht'))

#----------------------------------------------------------------------


index = 'F3'
gerecht = 'Falafel met portobello'

ingredienten = ['aardappelen',
                'wortelen',
                'portobello',
                'sla',
                'tomaat',
                'rode ajuin',
                'falafel',
                'magere yoghurt']

specs = {'index': [index],
           'gerecht': [gerecht],
           'tijd': [20], 
           'veggie': [True]}

ingr = {'index': [index]*len(ingredienten),
          'gerecht': [gerecht]*len(ingredienten),
          'ingredienten': ingredienten,
          '1p': [150,1,2,0.5,0.5,0.5,1,25],
          '2p': [300,2,4,1,1,1,2,50],
          '3p': [450,3,6,1.5,1.5,1.5,3,75],
          '4p': [600,4,8,2,2,2,4,100]
         }

specs_df = specs_df.append(pd.DataFrame(specs).set_index('gerecht'))
ingr_df = ingr_df.append(pd.DataFrame(ingr).set_index('gerecht'))


#----------------------------------------------------------------------


index = 'A1'
gerecht = 'Gentse waterzooi'

ingredienten = ['gemarineerde kip drumsticks',
                'ajuin',
                'knoflookteen',
                'selder',
                'aardappelen',
                'wortelen',
                'prei',
                'room']

specs = {'index': [index],
           'gerecht': [gerecht],
           'tijd': [40], 
           'veggie': [False]}

ingr = {'index': [index]*len(ingredienten),
          'gerecht': [gerecht]*len(ingredienten),
          'ingredienten': ingredienten,
          '1p': [2,0.5,0.5,1,200,50,100,50],
          '2p': [4,1,1,2,400,100,200,100],
          '3p': [6,1.5,1.5,3,600,150,300,150],
          '4p': [8,2,2,4,600,200,400,200]
         }

specs_df = specs_df.append(pd.DataFrame(specs).set_index('gerecht'))
ingr_df = ingr_df.append(pd.DataFrame(ingr).set_index('gerecht'))


#----------------------------------------------------------------------


index = 'A3'
gerecht = 'Camembert uit de oven'

ingredienten = ['krieltjes',
                'venkel',
                'citroen',
                'sjalot',
                'camombert',
                'stokbrood',
                'gemengde sla']

specs = {'index': [index],
           'gerecht': [gerecht],
           'tijd': [35], 
           'veggie': [True]}

ingr = {'index': [index]*len(ingredienten),
          'gerecht': [gerecht]*len(ingredienten),
          'ingredienten': ingredienten,
          '1p': [150,0.5,0.5,0.5,80,0.5,30],
          '2p': [300,1,1,1,160,1,60],
          '3p': [450,1.5,1.5,1.5,240,1.5,90],
          '4p': [600,2,2,2,320,2,120]
         }

specs_df = specs_df.append(pd.DataFrame(specs).set_index('gerecht'))
ingr_df = ingr_df.append(pd.DataFrame(ingr).set_index('gerecht'))


#----------------------------------------------------------------------


index = 'A4'
gerecht = 'Gegratineerde aubergine met zoete aardappelpuree'

ingredienten = ['aubergine',
                'parmezaamse kaas',
                'zoete aardappel',
                'rode paprika']

specs = {'index': [index],
           'gerecht': [gerecht],
           'tijd': [25], 
           'veggie': [True]}

ingr = {'index': [index]*len(ingredienten),
          'gerecht': [gerecht]*len(ingredienten),
          'ingredienten': ingredienten,
          '1p': [1,50,250,0.5],
          '2p': [2,100,500,1],
          '3p': [3,150,750,1.5],
          '4p': [4,200,1000,2]
         }

specs_df = specs_df.append(pd.DataFrame(specs).set_index('gerecht'))
ingr_df = ingr_df.append(pd.DataFrame(ingr).set_index('gerecht'))




#----------------------------------------------------------------------

'''
index = ''
gerecht = ''

ingredienten = ['',
                '',
                '',
                '',
                '',
                '']

specs = {'index': [index],
           'gerecht': [gerecht],
           'tijd': [25], 
           'veggie': [True]}

ingr = {'index': [index]*len(ingredienten),
          'gerecht': [gerecht]*len(ingredienten),
          'ingredienten': ingredienten,
          '1p': [],
          '2p': [],
          '3p': [],
          '4p': []
         }

specs_df = specs_df.append(pd.DataFrame(specs).set_index('gerecht'))
ingr_df = ingr_df.append(pd.DataFrame(ingr).set_index('gerecht'))

#----------------------------------------------------------------------

'''

plaats_dict = {'champignons': 'frigo',
                'zoete aardappel': 'droog',
                'gemarineerde kip drumsticks': 'slager',
                'farfalle': 'deegwaren',
                'veggieburger': 'frigo',
                'feta': 'frigo',
                'zak wortel rode kool': 'frigo',
                'ajuin': 'droog',
                'knoflookteen': 'droog',
                'munt': 'frigo',
                'mozzarella': 'frigo',
                'panko': 'deegwaren',
                'koriander': 'frigo',
                'avocado': 'frigo',
                'komkommer': 'frigo',
                'slahart': 'frigo',
                'kerstomaten': 'frigo',
                'tonijn in blik': 'blik',
                'selder': 'frigo',
                'parmezaamse kaas': 'frigo',
                'stokbrood': 'bakkerij',
                'falafel': 'frigo',
                'zure room': 'frigo',
                'geitenkaas': 'frigo',
                'rode paprika': 'frigo', 
                'hamburgerbol': 'bakkerij',
                'aubergine': 'frigo',
                'courgette': 'frigo',
                'tomaat': 'frigo',
                'room': 'frigo',
                'spaghetti': 'deegwaren',
                'gerookte forelfilet': 'frigo',
                'geraspte kaas': 'frigo',
                'bospaddenstoelenpesto': 'blik',
                'aardappelen': 'droog',
                'pruimtomaat': 'frigo',
                'heekfilet': 'frigo',
                'lasagnebladen': 'deegwaren',
                'pompoenpitten': 'droog',
                'dille': 'droog',
                'venkel': 'frigo',
                'parelcouscous': 'deegwaren',
                'veldsla': 'frigo',
                'tomaat': 'frigo',
                'camombert': 'frigo',
                'citroen': 'frigo',
                'tortilla': 'deegwaren',
                'sjalot': 'droog',
                'kruidenkaas': 'frigo',
                'zwarte olijven': 'blik',
                'spinazie': 'frigo',
                'sla': 'frigo',
                'ei': 'droog',
                'broodje': 'bakkerij',
                'magere yoghurt': 'frigo',
                'cherrytomaat': 'frigo',
                'portobello': 'frigo',
                'rode ajuin': 'frigo',
                'rucola': 'frigo',
                'krieltjes': 'droog',
                'passata': 'blik',
                'gemengde sla': 'frigo',
                'witloof': 'frigo',
                'kappertjes': 'blik',
                'peterselie': 'droog',
                'zwarte bonen': 'blik',
                'rode peper': 'frigo',
                'prei': 'frigo',
                'wortelen': 'frigo',
                'limoen': 'frigo',
                'flat bread': 'bakkerij',
                'tagiatelle': 'deegwaren'}


plaats = pd.DataFrame(plaats_dict, index=['plaats']).T.reset_index()
plaats.columns = ['ingredienten', 'plaats']
plaats = plaats.set_index('ingredienten')




################
#              #
#   Functies   #
#              #
################



def bootschappenlijstje(gerechten, ingr_df):

    '''
    input:
        - gerechten df
        - ingredients df
    output:
        - ingredients per gerecht and persons
        - bootschappenlijstje
    '''

    # make lists of asked recipes and amounts
    personen = list(gerechten.query("select == True")['personen'])
    gerechten = list(gerechten.query("select == True")['gerecht'])


    # single recipe
    if len(gerechten) == 1:
        return ingr_df.loc[gerechten, ['ingredienten', personen]].set_index('ingredienten')


    # check if all recipes are present in database
    for el in gerechten:
        if el not in ingr_df.index:
            raise ValueError("gerecht '{}' niet in databank".format(el))


    # verbose
    print('\n{}~~ GESELECTEERDE GERECHTEN ~~'.format(' '*13))
    print('\n{}\n'.format('-'*55))


    # select correct amount column for each recipe
    lijstje = pd.DataFrame(columns=['gerecht', 'ingredienten','hoeveelheid']).set_index('gerecht')

    for gerecht, aantal in zip(gerechten, personen):

        aantal = str(aantal) + 'p'

        # verbose
        print('gerecht:\t{}'.format(gerecht))
        print('index:\t\t{}'.format(list(ingr_df.loc[gerecht, 'index'])[0]))
        print('personen:\t{}\n'.format(aantal))

        ingr_df_current = ingr_df.loc[gerecht, ['ingredienten', aantal]].rename(columns={aantal: 'hoeveelheid'})
        lijstje = pd.concat([lijstje, ingr_df_current])

        # verbose
        print(ingr_df_current.to_string(index=False))
        print('\n{}\n'.format('-'*55))


    # add amounts per ingredient
    lijstje['hoeveelheid_som'] = lijstje.groupby('ingredienten')['hoeveelheid'].transform('sum')
    lijstje  = lijstje[['hoeveelheid_som','ingredienten']].drop_duplicates().set_index('ingredienten')
    lijstje.rename(columns={'hoeveelheid_som': 'hoeveelheid'}, inplace=True)


    # check if no duplicates
    assert len(set(lijstje.index)) == len(lijstje.index)


    # add location
    lijstje_plaats = lijstje.join(plaats, how='left')
    assert list(lijstje_plaats.index) == list(lijstje.index)

    return lijstje_plaats.sort_values('plaats')



def pictures(gerechten, ingr_df):

    '''
    input:
        - gerechten df
    output:
        - folder with pictures of selected recipes
    '''

    gerechten = list(gerechten.query("select == True")['gerecht'])

    indexes = list(ingr_df.query("gerecht in @gerechten")['index'])

    files = glob.glob('geselecteerde gerechten/*')
    for f in files:
        os.remove(f)

    for index in indexes:
        try:
            copyfile('alle gerechten/{}_1.jpg'.format(index), 'geselecteerde gerechten/{}_1.jpg'.format(index))
            copyfile('alle gerechten/{}_2.jpg'.format(index), 'geselecteerde gerechten/{}_2.jpg'.format(index))
        except:
            print("[INFO]\t Foto van gerecht '{}' werd niet gevonden".format(index))






###########
#         #
#   Run   #
#         #
###########




if __name__ == '__main__':

    # read in wanted recipes
    gerechten = pd.read_excel('HelloFresh_gerechten.xlsx', name='Sheet1')

    # print all ingredients
    #print(set(ingr_df['ingredienten']))
    #exit()

    # make magic
    lijstje = bootschappenlijstje(gerechten, ingr_df)

    # copy pictures
    pictures(gerechten, ingr_df)

    # verbose
    print("\n\nRecepten bevinden zich in de folder 'geselecteerde recepten'")

    # verbose
    print('\n\n      ~~ BOOTSCHAPPENLIJSTJE ~~\n')
    print(lijstje)
    print()
