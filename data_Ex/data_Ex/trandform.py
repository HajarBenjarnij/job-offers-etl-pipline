import pandas as pd
def company(text):
  chaine=text.split('recrutement')[1].replace("-"," ")
  resultat = ""
  for caractere in chaine:
      if caractere.isdigit():
          break
      resultat += caractere
  return resultat

def transform(file):
    data=pd.read_csv(file)
    data["Entreprise"]=data["lien_publication"].apply(lambda x: company(x))
    data["poste"]=data["poste"].apply(lambda x: x.lstrip().split("|")[0])
    data["Location"]=data["Location"].apply(lambda x: x.split("|")[1])
    data['date publication'] = pd.to_datetime(data['date publication'], dayfirst=True)
    data['delai'] = pd.to_datetime(data['delai'])
    data.to_csv("C:\\Users\\Admin\\Desktop\\projet_offres_emplois1\\data_Ex\\data_Ex\\datatest_clear.csv")

transform("C:\\Users\\Admin\\Desktop\\projet_offres_emplois1\\data_Ex\\data_Ex\\datatest.csv")