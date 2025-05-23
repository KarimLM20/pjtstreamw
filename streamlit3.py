import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_authenticator import Authenticate
import pandas as pd

# ----------------------------
# Authentification configuration
# ----------------------------
lesDonneesDesComptes = {
    'usernames': {
        'utilisateur': {
            'name': 'utilisateur',
            'password': 'utilisateurMDP',
            'email': 'utilisateur@gmail.com',
            'failed_login_attemps': 0,
            'logged_in': False,
            'role': 'utilisateur'
        },
        'root': {
            'name': 'root',
            'password': 'rootMDP',
            'email': 'admin@gmail.com',
            'failed_login_attemps': 0,
            'logged_in': False,
            'role': 'administrateur'
        }
    }
}

authenticator = Authenticate(
    lesDonneesDesComptes,
    "cookie_name",
    "cookie_key",
    30
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
