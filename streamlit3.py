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






# Nos données utilisateurs doivent respecter ce format
lesDonneesDesComptes = {
    'usernames': {
        'utilisateur': {
            'name': 'utilisateur',
            'password': 'utilisateurMDP',
            'email': 'utilisateur@gmail.com',
            'failed_login_attemps': 0,  # Sera géré automatiquement
            'logged_in': False,          # Sera géré automatiquement
            'role': 'utilisateur'
        },
        'root': {
            'name': 'root',
            'password': 'rootMDP',
            'email': 'admin@gmail.com',
            'failed_login_attemps': 0,  # Sera géré automatiquement
            'logged_in': False,          # Sera géré automatiquement
            'role': 'administrateur'
        }
    }
}

authenticator = Authenticate(
    lesDonneesDesComptes,  # Les données des comptes
    "cookie name",         # Le nom du cookie, un str quelconque
    "cookie key",          # La clé du cookie, un str quelconque
    30,                    # Le nombre de jours avant que le cookie expire
)

authenticator.login()

# ----------------------------
# Pages
# ----------------------------
def page_accueil():
    st.title("🏠 Accueil")
    st.write("Bienvenue sur la page d'accueil !")

def page_photos():
    st.title("🪐 Album des planètes")

    planetes = [
        ("Mercure", "https://wallpapercave.com/wp/wp4047226.jpg"),
        ("Vénus", "https://www.lecosmographe.com/wp-content/uploads/2021/01/Venus.jpg"),
        ("Terre", "https://images.sudouest.fr/2015/07/22/57eb956066a4bd7760c39754/default/1000/la-nasa-publie-sa-premiere-photo-de-la-terre-vue-de-l-espace-depuis-1972.jpg"),
        ("Mars", "https://wiki.fed-space.com/images/thumb/1/1b/Mars.jpg/1200px-Mars.jpg"),
        ("Jupiter", "https://static.vecteezy.com/system/resources/thumbnails/021/184/177/original/jupiter-planet-3d-footage-space-exploration-video.jpg"),
        ("Saturne", "https://starwalk.space/gallery/images/saturn-planet-guide/1920x1080.jpg"),
        ("Uranus", "https://wallpaperaccess.com/full/415311.jpg"),
        ("Neptune", "https://millionfacts.co.uk/wp-content/uploads/2023/02/Interesting-facts-about-Neptune.jpg"),
        ("Pluton", "https://desetoilespourtous.com/wp-content/uploads/2022/06/Pluton.png")
    ]

    for i in range(0, len(planetes), 3):
        cols = st.columns(3)
        for col, (nom, url) in zip(cols, planetes[i:i+3]):
            with col:
                st.header(f"🌍 {nom}")
                st.image(url, use_column_width=True)

def page_utilisateur():
    st.title("👤 Espace réservé")
    st.success("Bienvenue, vous êtes connecté avec succès.")
    authenticator.logout("🔒 Déconnexion", "sidebar")

# ----------------------------
# Main App
# ----------------------------
if st.session_state["authentication_status"]:
    with st.sidebar:
        choix = option_menu(
            menu_title="Navigation",
            options=["Accueil", "Photos", "Espace Membre"],
            icons=["house", "image", "person"],
            menu_icon="cast",
            default_index=0
        )

    if choix == "Accueil":
        page_accueil()
    elif choix == "Photos":
        page_photos()
    elif choix == "Espace Membre":
        page_utilisateur()

elif st.session_state["authentication_status"] is False:
    st.error("Identifiants incorrects. Veuillez réessayer.")
elif st.session_state["authentication_status"] is None:
    st.warning("Veuillez entrer votre nom d'utilisateur et mot de passe.")
