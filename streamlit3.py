import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_authenticator import Authenticate
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px 

# Création du menu qui va afficher les choix qui se trouvent dans la variable options
selection = option_menu(
            menu_title=None,
            options = ["Accueil", "Photos"]
        )

# On indique au programme quoi faire en fonction du choix
if selection == "Accueil":
    st.write("Bienvenue sur la page d'accueil !")
elif selection == "Photos":
    st.write("Bienvenue sur mon album photo")
# ... et ainsi de suite pour les autres pages

import streamlit as st

# Création de 3 colonnes 
col1, col2, col3= st.columns(3)

# Contenu de la première colonne : 

with col1:
    st.header("Planet mercury")
    st.image("https://wallpapercave.com/wp/wp4047226.jpg")

with col2:
    st.header("Planet Venus")
    st.image("https://www.lecosmographe.com/wp-content/uploads/2021/01/Venus.jpg")

with col3:
  st.header("Planet earth")
  st.image("https://images.sudouest.fr/2015/07/22/57eb956066a4bd7760c39754/default/1000/la-nasa-publie-sa-premiere-photo-de-la-terre-vue-de-l-espace-depuis-1972.jpg")

col4, col5, col6,= st.columns(3)

with col4:
  st.header("Planet Mars")
  st.image("https://wiki.fed-space.com/images/thumb/1/1b/Mars.jpg/1200px-Mars.jpg")

with col5:
  st.header("Planet Jupiter")
  st.image("https://static.vecteezy.com/system/resources/thumbnails/021/184/177/original/jupiter-planet-3d-footage-space-exploration-video.jpg") 

with col6:
  st.header("Planet Saturn")
  st.image("https://starwalk.space/gallery/images/saturn-planet-guide/1920x1080.jpg")

col7, col8, col9= st.columns(3)

with col7:
    st.header("Planet Uranus")
    st.image("https://wallpaperaccess.com/full/415311.jpg")

with col8:
    st.header("Planet Neptune")
    st.image("https://millionfacts.co.uk/wp-content/uploads/2023/02/Interesting-facts-about-Neptune.jpg")

with col9:
    st.header("Planet Pluto")
    st.image("https://desetoilespourtous.com/wp-content/uploads/2022/06/Pluton.png")


  # Création de deux colonnes où col2 est deux fois plus large que col1 :
col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns([1, 2, 1, 1, 1, 1, 1, 1, 1])

import streamlit as st

# On affiche un menu déroulant (selectbox) DANS la barre latérale (sidebar)
# L'utilisateur peut choisir son moyen de contact préféré parmi trois options
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?", # Question affichée
    ("Email", "Home phone", "Mobile phone") # Options proposées
)

# Autre façon d'utiliser la sidebar avec un "with", pour grouper plusieurs éléments
with st.sidebar:
    # On affiche des boutons radio dans la sidebar pour choisir un mode de livraison
    add_radio = st.radio(
        "Choose a shipping method",  # Titre de la question
        ("Standard (5-15 days)", "Express (2-5 days)")  # Choix proposés
    )



# Chargement des utilisateurs depuis le fichier CSV
@st.cache_data
def load_users(csv_path='https://raw.githubusercontent.com/KarimLM20/pjtstreamw/refs/heads/main/team.csv'):
    return pd.read_csv(csv_path)

users_df = load_users()

# Interface de connexion
st.title("Connexion")

username = st.text_input("Nom d'utilisateur")
password = st.text_input("Mot de passe", type="password")

if st.button("Se connecter"):
    user = users_df[
        (users_df['username'] == username) & (users_df['password'] == password)
    ]

    if not user.empty:
        st.session_state["logged_in"] = True
        st.session_state["username"] = username
        st.session_state["role"] = user.iloc[0]["role"]
        st.success(f"Connecté en tant que {username} ({st.session_state['role']})")
    else:
        st.error("Nom d'utilisateur ou mot de passe incorrect.")

# Affichage après connexion
if st.session_state.get("logged_in"):
    st.write(f"Bienvenue **{st.session_state['username']}** 🎉")
    if st.button("Se déconnecter"):
        st.session_state.clear()

def accueil():
      st.title("Bienvenu sur le contenu réservé aux utilisateurs connectés")


# Sous-titre (taille 2), utile pour organiser le contenu par sous-sections
st.subheader("Statistiques planétes")

dataplanet = pd.read_csv('https://raw.githubusercontent.com/KarimLM20/pjtstreamw/refs/heads/main/planets.csv')
# Chargement des datasets disponibles

df = st.selectbox("Quel dataset veux-tu utiliser ?",dataplanet)# Liste déroulante pour choisir le dataset

set = sns.load_dataset("planets") # Liste des datasets disponibles

dfchoisi= set.columns.to_list()
#dfchoisi = set.columns.to_list() # Liste des colonnes du dataset choisi

st.dataframe(set) # Affiche le dataframe sous forme de tableau interactif
# Affiche une liste déroulante avec les colonnes du dataset flight
X = st.selectbox("Choisissez la colonne X",dfchoisi)
Y = st.selectbox("Choisissez la colonne Y", dfchoisi) # Liste déroulante pour choisir la colonne Y

choixgraphique = ['scatter_chart', 'line_chart', 'bar_chart'] # Liste des types de graphiques disponibles
# Liste déroulante pour choisir le type de graphique

graphique = st.selectbox("Quel graphique veux-tu utiliser ?", choixgraphique) # Liste déroulante pour choisir le type de graphique
# Liste des types de graphiques disponibles

dictgraph= {
    'scatter_chart': st.scatter_chart,
    'line_chart': st.line_chart,
    'bar_chart': st.bar_chart
}
# Dictionnaire pour associer les types de graphiques aux fonctions correspondantes
# Affiche le graphique choisi
graph = dictgraph[graphique]  
graph(set, x=X, y=Y)

# Affiche un histogramme de la colonne choisie

if st.checkbox(label = "Afficher la matrice de corrélation",  key="corr_matrix_1"):
    # Affiche la matrice de corrélation
    numeric_df = set.select_dtypes(include=['number'])
    fig, ax = plt.subplots()
    sns.heatmap(numeric_df.corr(), annot=True, fmt=".2f", cmap='coolwarm', ax=ax)
    st.pyplot(fig)


