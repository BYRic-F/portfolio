import streamlit as st
import os
from streamlit_option_menu import option_menu
import fitz  # PyMuPDF

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Frédéric Bayen | Data Strategy",
    layout="wide",
)

# --- LOAD CSS ---
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- NAVIGATION ---
# Moving navigation to the top for a more modern, full-width feel
selected = option_menu(
    menu_title=None,
    options=["Accueil", "Projets Python", "Projets Power BI", "Mon CV"],
    icons=["house", "code-slash", "bar-chart", "file-earmark-person"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "transparent", "border-radius": "0"},
        "icon": {"font-size": "14px"},
        "nav-link": {"font-size": "14px", "text-align": "center", "margin": "0px", "font-weight": "500", "text-transform": "uppercase", "letter-spacing": "0.1em"},
        "nav-link-selected": {"background-color": "#0f172a", "color": "white", "border-radius": "4px"},
    }
)

# --- PROJECT DISPLAY FUNCTION ---
def display_project_card(title, impact, context, challenge, solution, tags, image_folder, github_url=None, pdf_path=None):
    st.markdown(f'<div class="project-header"><h2>{title}</h2></div>', unsafe_allow_html=True)
    
    # Layout Principal
    col_text, col_img = st.columns([1, 1], gap="large")
    
    with col_text:
        st.markdown(f"""
        <div class="insight-header">
            <h4>Impact Business</h4>
            <p style="margin:0; font-size: 1.1rem; color: #0f172a; font-weight: 500;">{impact}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<p class="section-title">Contexte</p>', unsafe_allow_html=True)
        st.write(context)
        
        st.markdown('<p class="section-title">Challenge</p>', unsafe_allow_html=True)
        st.write(challenge)
        
        st.markdown('<p class="section-title">Solution</p>', unsafe_allow_html=True)
        st.write(solution)

        # Tags Row
        st.markdown('<p class="section-title">Technologies</p>', unsafe_allow_html=True)
        tag_html = "".join([f'<span class="tag">{tag}</span>' for tag in tags])
        st.markdown(f'<div style="margin-bottom: 25px;">{tag_html}</div>', unsafe_allow_html=True)
        
        # Buttons Row
        btn_col1, btn_col2 = st.columns([1, 1])
        with btn_col1:
            if github_url:
                st.markdown(f'<a href="{github_url}" target="_blank" class="github-btn">Consulter le code</a>', unsafe_allow_html=True)
        with btn_col2:
            if pdf_path and os.path.exists(pdf_path):
                with open(pdf_path, "rb") as f:
                    st.download_button(
                        label="Télécharger l'étude (PDF)",
                        data=f,
                        file_name=os.path.basename(pdf_path),
                        mime="application/pdf",
                        key=title
                    )

    with col_img:
        if image_folder and os.path.exists(image_folder):
            images = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
            if images:
                st.image(os.path.join(image_folder, images[0]), use_container_width=True)
                if len(images) > 1:
                    sub_cols = st.columns(min(len(images)-1, 3))
                    for idx, img_name in enumerate(images[1:min(len(images), 4)]):
                        with sub_cols[idx]:
                            st.image(os.path.join(image_folder, img_name), use_container_width=True)

# --- PAGES ---

if selected == "Accueil":
    # Hero Section
    st.markdown('<div class="hero-container">', unsafe_allow_html=True)
    st.markdown('<h1 class="main-title">Je transforme vos flux de données complexes<br>en leviers de croissance mesurables.</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Data Strategy • MLOps & Automation • Business Intelligence</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([0.8, 2], gap="large")
    with col1:
        photo_path = "data/CV/photo_profil_redimenssionnee.png"
        if os.path.exists(photo_path):
            st.markdown('<div class="profile-img-container">', unsafe_allow_html=True)
            st.image(photo_path, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
        <div style="background: #f8fafc; padding: 1.5rem; border-radius: 4px; border: 1px solid #e2e8f0;">
            <p style="margin-bottom:12px; font-weight: 700; text-transform: uppercase; font-size: 0.75rem; letter-spacing: 0.1em; color: #64748b;">Contact</p>
            <p style="margin: 4px 0; font-size: 0.9rem;">📧 <a href="mailto:frederic.bayen@live.fr" style="color:#0f172a; text-decoration: none;">frederic.bayen@live.fr</a></p>
            <p style="margin: 4px 0; font-size: 0.9rem;">🔗 <a href="https://www.linkedin.com/in/frédéric-bayen" style="color:#0f172a; text-decoration: none;">LinkedIn</a></p>
            <p style="margin: 4px 0; font-size: 0.9rem;">💻 <a href="https://github.com/BYRic-F" style="color:#0f172a; text-decoration: none;">GitHub</a></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.write("")  # Spacer
        st.markdown("""
        ### Expertise & vision
        
        En tant que Data Analyst, je simplifie la gestion de vos données pour en faire des outils d'aide à la décision. De l'automatisation technique à la visualisation finale, mon but est de rendre vos informations accessibles et exploitables.
        
        ### Piliers stratégiques
        
        **Préparation & flux de données**
        Mise en place de pipelines (SQL, ETL) pour garantir des données propres, bien structurées et prêtes à être exploitées.
        
        **MLOps**
        Création et déploiement de modèles prédictifs (XGBoost, RandomForest...) via des outils robustes (FastAPI, Docker) pour qu'ils soient réellement utilisables au quotidien.
        
        **Business Intelligence**
        Conception d'écosystèmes décisionnels (Power BI, DAX) permettant un pilotage en temps réel.
        """)
        
        st.markdown("<br>", unsafe_allow_html=True)
        # Unified Tags for Skills
        skills = ["Power BI", "Python", "SQL", "MLOps", "Business Strategy", "ETL", "Docker", "Git", "DAX", "FastAPI"]
        skill_html = "".join([f'<span class="tag">{skill}</span>' for skill in skills])
        st.markdown(f'<div style="display:flex; gap:3px; flex-wrap:wrap;">{skill_html}</div>', unsafe_allow_html=True)
        
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown('<a href="mailto:frederic.bayen@live.fr" class="cta-button">Discuter d\'un projet</a>', unsafe_allow_html=True)

elif selected == "Projets Python":
    st.markdown('<h1 class="main-title" style="text-align:left; font-size: 3rem !important;">Data Solutions Python</h1>', unsafe_allow_html=True)
    tabs = st.tabs(["DÉTECTION DE FRAUDES", "IA PROSPECTOR", "MOTEUR DE RECOMMANDATION HYBRIDE"])
    
    with tabs[0]:
        st.markdown('<div class="project-header"><h2>Détection de fraudes en temps réel</h2></div>', unsafe_allow_html=True)

        # Storytelling Hook
        st.markdown("""
        <div class="insight-header">
            <h4>Le Défi Business</h4>
            <p style="margin:0; font-size: 1.15rem; color: #0f172a; font-weight: 500;">
                Stopper une hémorragie financière de <b>plusieurs centaines de millions de Shillings kényans par an</b> due à la fraude transactionnelle, 
                tout en garantissant une expérience fluide pour des millions d'utilisateurs quotidiens.
            </p>
        </div>
        """, unsafe_allow_html=True)

        col_text, col_viz = st.columns([1.2, 1], gap="large")

        with col_text:
            st.markdown('<p class="section-title">Performance & Impact</p>', unsafe_allow_html=True)
            # Table des métriques
            st.markdown("""
            | Métrique | Score | Impact |
            | :--- | :--- | :--- |
            | **Recall (Le bouclier)** | **87 %** | Interception de la grande majorité des fraudes. |
            | **Spécificité (La fluidité)** | **99,4 %** | Moins de 1% de clients honnêtes impactés. |
            | **Latence (La vitesse)** | **< 30ms** | Décision instantanée, transparence totale. |
            """)

            st.markdown('<p class="section-title">L\'Approche Technique (MLOps)</p>', unsafe_allow_html=True)
            st.markdown("""
            Plutôt qu'un modèle statique, nous avons conçu une **architecture vivante et auto-adaptative** :
            - **Ingestion** : Pipeline asynchrone via **FastAPI** et buffer **Redis** pour une résilience totale.
            - **Cerveau prédictif** : Modélisation **XGBoost** optimisée pour le déséquilibre de classes massif (0.13% de fraudes).
            - **Automatisation & Model Gating** : Orchestration via **Prefect**. Le système se réentraîne sur **BigQuery** et ne déploie la nouvelle version que si elle surpasse le record de performance précédent.
            """)

            # Tags & Buttons
            st.markdown('<p class="section-title">Technologies</p>', unsafe_allow_html=True)
            tags = ["Python", "XGBoost", "FastAPI", "MLOps", "Redis", "BigQuery", "Prefect", "Docker", "Grafana", "BigQuery"]
            tag_html = "".join([f'<span class="tag">{tag}</span>' for tag in tags])
            st.markdown(f'<div style="margin-bottom: 25px;">{tag_html}</div>', unsafe_allow_html=True)
            st.write(" ")

            btn_col1, btn_col2 = st.columns([1, 1])
            st.write(" ")
            with btn_col1:
                st.markdown(f'<a href="https://github.com/BYRic-F/projet_fraude_cb" target="_blank" class="github-btn" style="width:100%; text-align:center;">Consulter le code</a>', unsafe_allow_html=True)
            with btn_col2:
                st.markdown(f'<a href="https://www.youtube.com/watch?v=oukKv2ohZn0" target="_blank" class="github-btn" style="width:100%; text-align:center;">Démonstration Vidéo</a>', unsafe_allow_html=True)

        with col_viz:
            # Affichage des GIFs avec la disposition d'origine (un grand, les autres en dessous)
            img_path = "data/images/Python_detection_fraudes"
            if os.path.exists(img_path):
                st.image(os.path.join(img_path, "page_fraude.gif"), caption="Pilotage Temps Réel (Streamlit)", use_container_width=True)
                
                sub_cols = st.columns(2)
                with sub_cols[0]:
                    st.image(os.path.join(img_path, "grafanaa.gif"), caption="Monitoring (Grafana)", use_container_width=True)
                with sub_cols[1]:
                    st.image(os.path.join(img_path, "prefect2 (1).gif"), caption="MLOps (Prefect)", use_container_width=True)
        
    with tabs[1]:
        st.markdown('<div class="project-header"><h2>IA Prospector - Insee</h2></div>', unsafe_allow_html=True)
        
        # Storytelling Hook
        st.markdown("""
        <div class="insight-header">
            <h4>Le Défi Business</h4>
            <p style="margin:0; font-size: 1.15rem; color: #0f172a; font-weight: 500;">
                <b>Enrichir la base CRM de RH Performances</b> grâce à un ciblage automatisé et intelligent, permettant d'isoler les prospects à fort potentiel en éliminant 90 % du bruit des bases SIRENE.
            </p>
        </div>
        """, unsafe_allow_html=True)

        col_text, col_viz = st.columns([1.2, 1], gap="large")
        
        with col_text:
            st.markdown('<p class="section-title">Performance & Expertise</p>', unsafe_allow_html=True)
            st.markdown("""
            | Métrique | Impact |
            | :--- | :--- |
            | **Efficacité de Ciblage** | **100% de succès** sur 50 tests sectoriels intensifs. |
            | **Précision IA** | Traduction sémantique des métiers en **codes NAF techniques**. |
            | **Modèles** | Architectures hybrides **Gemini 3 & 3.1 Flash-Lite**. |
            """)

            st.markdown('<p class="section-title">Ingénierie de Précision</p>', unsafe_allow_html=True)
            st.markdown("""
            Conçu pour répondre aux exigences critiques d'un cabinet de recrutement (RH Performances) :
            - **Nomenclature NAF 2008** : Scan intelligent de **1700+ codes NAF** pour garantir une compatibilité à 100% avec l'API Sirene réelle.
            - **Batching Intelligent** : Découpage dynamique des requêtes pour les zones denses (Paris, Lyon, Marseille) afin d'éviter la saturation de l'API.
            - **Optimisation mobile (OSINT)** : Transformation automatique des numéros en **liens cliquables (tel:)** pour une prospection directe sur smartphone.
            """)

            # Tags & Buttons
            st.markdown('<p class="section-title">Technologies</p>', unsafe_allow_html=True)
            tags = ["Gemini AI", "Streamlit", "API Insee", "OSINT", "Python", "NAF 2008", "Data Engineering"]
            tag_html = "".join([f'<span class="tag">{tag}</span>' for tag in tags])
            st.markdown(f'<div style="margin-bottom: 25px;">{tag_html}</div>', unsafe_allow_html=True)
            
            btn_col1, btn_col2 = st.columns([1, 1])
            with btn_col1:
                st.markdown(f'<a href="https://github.com/BYRic-F/Insee_prospector_cloud" target="_blank" class="github-btn" style="width:100%; text-align:center;">Consulter le code</a>', unsafe_allow_html=True)
            with btn_col2:
                st.markdown(f'<a href="https://inseeprospectorcloud.streamlit.app/" target="_blank" class="github-btn" style="width:100%; text-align:center;">Accéder à l\'application</a>', unsafe_allow_html=True)

        with col_viz:
            # Affichage des images (GIF en principal, screenshots en dessous)
            img_path = "data/images/Python_Inspector_insee"
            if os.path.exists(img_path):
                st.image(os.path.join(img_path, "demonstration_insee.gif"), caption="Démonstration du ciblage intelligent", use_container_width=True)
                
                sub_cols = st.columns(2)
                with sub_cols[0]:
                    st.image(os.path.join(img_path, "Page_accueil1.png"), caption="Interface d'accueil & export CRM", use_container_width=True)
                with sub_cols[1]:
                    st.image(os.path.join(img_path, "Page_graphique2.png"), caption="Analyses géographiques & sectorielles", use_container_width=True)

    with tabs[2]:
        st.markdown('<div class="project-header"><h2>Système de recommandation hybride (Content & collaborative)</h2></div>', unsafe_allow_html=True)
        
        # Storytelling Hook
        st.markdown("""
        <div class="insight-header">
            <h4>Le Défi Business</h4>
            <p style="margin:0; font-size: 1.15rem; color: #0f172a; font-weight: 500;">
                Maximiser la rétention utilisateur en proposant des recommandations ultra-pertinentes dès la première connexion, 
                en résolvant le problème critique du <b>"Cold Start"</b>.
            </p>
        </div>
        """, unsafe_allow_html=True)

        col_text, col_viz = st.columns([1.2, 1], gap="large")
        
        with col_text:
            st.markdown('<p class="section-title">Performance & Innovation</p>', unsafe_allow_html=True)
            st.markdown("""
            | Métrique | Impact |
            | :--- | :--- |
            | **Catalogue** | **10 000+ titres** premium rigoureusement filtrés. |
            | **Authentification** | **Adaptation de l'interface Streamlit** pour débloquer les fonctionnalités avancées du modèle SVD uniquement pour les utilisateurs authentifiés.|
            | **Algorithme** | Système **hybride** (KNN Sémantique + SVD collaboratif). |
            | **Temps réel** | Projection instantanée du profil dans l'espace latent. |            
            """)

            st.markdown('<p class="section-title">Ingénierie de la Donnée</p>', unsafe_allow_html=True)
            st.markdown("""
            Pipeline ETL complet pour transformer des données brutes massives en un moteur fluide :
            - **Hybride KNN/SVD** : Combinaison de la similarité cosinus sur les résumés (**SpaCy**) et de la décomposition en valeurs singulières (**Surprise SVD**).
            - **Optimisation DuckDB** : Traitement SQL haute performance pour gérer des bases de données lourdes sans saturation RAM.
            - **Résolution du "Cold Start"** : Interface d'onboarding interactive imposant la notation de 5 films dès l'inscription pour alimenter l'algorithme SVD et garantir des recommandations personnalisées immédiates.
            """)

            # Tags & Buttons
            st.markdown('<p class="section-title">Technologies</p>', unsafe_allow_html=True)
            tags = ["NLP", "SpaCy", "DuckDB", "SVD", "KNN", "Python", "ETL", "Streamlit", "Scikit-Learn"]
            tag_html = "".join([f'<span class="tag">{tag}</span>' for tag in tags])
            st.markdown(f'<div style="margin-bottom: 25px;">{tag_html}</div>', unsafe_allow_html=True)
            
            btn_col1, btn_col2 = st.columns([1, 1])
            with btn_col1:
                st.markdown(f'<a href="https://github.com/BYRic-F/project_reco_movie_streamlit" target="_blank" class="github-btn" style="width:100%; text-align:center;">Consulter le code</a>', unsafe_allow_html=True)
            with btn_col2:
                st.markdown(f'<a href="https://byric-f-project-reco-movie-streamlit-app-3pm0kb.streamlit.app/" target="_blank" class="github-btn" style="width:100%; text-align:center;">Accéder à l\'application</a>', unsafe_allow_html=True)

        with col_viz:
            # Affichage des images (GIF en principal, screenshots en dessous)
            img_path = "data/images/Python_Recommandations_films"
            if os.path.exists(img_path):
                st.image(os.path.join(img_path, "Python_recommandations films.gif"), caption="Expérience utilisateur & Recommandations", use_container_width=True)
                
                sub_cols = st.columns(2)
                with sub_cols[0]:
                    st.image(os.path.join(img_path, "Page_d_accueil.png"), caption="Page d'accueil", use_container_width=True)
                with sub_cols[1]:
                    st.image(os.path.join(img_path, "Resultat_recherche.png"), caption="Analyse sémantique & détails", use_container_width=True)

elif selected == "Projets Power BI":
    st.markdown('<h1 class="main-title" style="text-align:left; font-size: 3rem !important;">Strategic BI</h1>', unsafe_allow_html=True)
    tabs = st.tabs(["OPTIMA CYCLES", "GAMING INTELLIGENCE", "MISSION HUMANITAIRE", "PILOTAGE 360°"])
    
    with tabs[0]:
        st.markdown('<div class="project-header"><h2>Optima Cycles - Étude d\'implantation</h2></div>', unsafe_allow_html=True)
        
        # Storytelling Hook
        st.markdown("""
        <div class="insight-header">
            <h4>Vision Stratégique</h4>
            <p style="margin:0; font-size: 1.15rem; color: #0f172a; font-weight: 500;">
                Valider l'ouverture d'un point de vente physique par la donnée : 
                <b>Ciblage Californie</b>, mois de <b>Mars</b>, et focus sur le segment <b>35-64 ans</b>.
            </p>
        </div>
        """, unsafe_allow_html=True)

        col_text, col_viz = st.columns([1.2, 1], gap="large")
        
        with col_text:
            st.markdown('<p class="section-title">Indicateurs de Performance</p>', unsafe_allow_html=True)
            st.markdown("""
            | KPI | Valeur | Impact Stratégique |
            | :--- | :--- | :--- |
            | **Profit Global** | **$6.0 M** | Performance robuste sur le marché californien. |
            | **Taux de Marge** | **44,0 %** | Rentabilité élevée sur les produits choisis. |
            | **Moteur de Profit** | **56,8 %** | Part du profit généré par le segment 35-64 ans. |
            """)

            st.markdown('<p class="section-title">Piliers de l\'Étude</p>', unsafe_allow_html=True)
            st.markdown("""
            Une recommandation d'investissement basée sur trois axes d'optimisation :
            - **Saisonnalité & timing** : Ouverture stratégique en Mars pour capter le pic annuel de rentabilité printanier.
            - **Optimisation du catalogue** : Rationalisation du stock (2 modèles de vélos sur 3 retenus et uniquement une sélection d'accessoires) pour maximiser la rotation de trésorerie.
            - **Ciblage démographique** : Identification précise du profil client "moteur" pour orienter les campagnes marketing.
            """)

            st.markdown('<p class="section-title">Rigueur d\'Analyste</p>', unsafe_allow_html=True)
            st.markdown("""
            *   **Agilité** : Étude complète réalisée en **8 heures**, prouvant une capacité de réaction rapide pour les décideurs.
            *   **Esprit critique** : Vigilance sur le **biais géographique** (sur-représentation de la Californie) et sur la nature **monosource du dataset**. Une étude de marché terrain est indispensable pour valider si ces tendances sont généralisables à l'ensemble du marché américain
            """)

            # Tags & Buttons
            st.markdown('<p class="section-title">Outils & Livrables</p>', unsafe_allow_html=True)
            tags = ["Power BI", "DAX", "Data Storytelling", "Market Analysis", "Business Strategy", "Python"]
            tag_html = "".join([f'<span class="tag">{tag}</span>' for tag in tags])
            st.markdown(f'<div style="margin-bottom: 25px;">{tag_html}</div>', unsafe_allow_html=True)
            
            st.info("💡 Fichier .pbix disponible pour une exploration interactive approfondie.")
            st.write(" ")

            btn_col1, btn_col2 = st.columns([1, 1])
            with btn_col1:
                st.markdown(f'<a href="https://github.com/BYRic-F" target="_blank" class="github-btn" style="width:100%; text-align:center;">Consulter le code</a>', unsafe_allow_html=True)
            with btn_col2:
                pdf_path = "data/presentations_pdf/Optima_cycle/Power_Point_Presentation.pdf"
                if os.path.exists(pdf_path):
                    with open(pdf_path, "rb") as f:
                        st.download_button(
                            label="Télécharger l'étude (PDF)",
                            data=f,
                            file_name="Optima_Cycles_Strategie.pdf",
                            mime="application/pdf",
                            key="optima_pdf"
                        )

        with col_viz:
            # Affichage des images (Performance en principal, thumbnails en dessous)
            img_path = "data/images/Power_bi_Optima_Cycles"
            if os.path.exists(img_path):
                st.image(os.path.join(img_path, "performance-du-marché.png"), caption="Analyse de performance & saisonnalité", use_container_width=True)
                
                sub_cols = st.columns(2)
                with sub_cols[0]:
                    st.image(os.path.join(img_path, "profiling-segementation-produits.png"), caption="Profiling & segmentation", use_container_width=True)
                with sub_cols[1]:
                    st.image(os.path.join(img_path, "execution-et-pilotage.png"), caption="Exécution & plan de route", use_container_width=True)

    with tabs[1]:
        display_project_card(
            "Gaming Market Intelligence",
            "Recommandation : Positionnement MMORPG Premium à 50€ pour maximiser la LTV.",
            "Analyse du marché mondial du jeu vidéo (83k+ titres).",
            "Investir dans le bon genre et au bon prix dans un marché ultra-saturé.",
            "Dashboard décisionnel intégrant Metacritic et analyses de cycle de vie des produits.",
            ["DAX", "Market Intelligence", "Gaming Strategy"],
            "data/images/Power_BI_Video_game_market",
            pdf_path="data/presentations_pdf/Video_game_market/Presentation_video_game.pdf"
        )

    with tabs[2]:
        display_project_card(
            "Accès à l'Eau - World Vision",
            "Ciblage vital du Tchad. Déploiement recommandé d'unités de purification solaires.",
            "Pilotage de mission humanitaire en Afrique (Tchad, Somalie).",
            "Prioriser les investissements pour réduire drastiquement la mortalité infantile.",
            "Modélisation Star Schema mettant en évidence l'impact de la stabilité politique sur les forages.",
            ["Social Impact", "NGO Strategy", "Power BI"],
            "data/images/PowerBi_acces_eau",
            pdf_path="data/presentations_pdf/Acces_eau/Présentation_projet_eau.pdf"
        )

    with tabs[3]:
        display_project_card(
            "Toys & Models - Pilotage 360°",
            "Optimisation de la trésorerie via la réduction de 15% des délais de paiement identifiés.",
            "ERP-Dashboarding pour distributeur international.",
            "Rapprocher les données de Ventes, Finance et RH pour un pilotage unifié.",
            "Requêtage MySQL avancé (CTE) et mesures DAX de performance commerciale.",
            ["MySQL", "Finance BI", "Supply Chain"],
            "data/images/PowerBi_Toys_and_models",
            pdf_path="data/presentations_pdf/Toys and models/Presentation_toys_and_models.pdf"
        )

elif selected == "Mon CV":
    st.markdown('<h1 class="main-title" style="text-align:left; font-size: 3rem !important;">Profil & Expertise</h1>', unsafe_allow_html=True)
    
    cv_dir = "data/CV"
    cv_files = [f for f in os.listdir(cv_dir) if f.lower().endswith(".pdf")]
    
    if cv_files:
        cv_path = os.path.join(cv_dir, cv_files[0])
        
        with open(cv_path, "rb") as f:
            pdf_bytes = f.read()
        
        col_btn1, col_btn2 = st.columns([1, 1])
        with col_btn1:
            st.download_button(
                label="📥 Télécharger le CV (PDF)",
                data=pdf_bytes,
                file_name="CV_Frédéric_Bayen.pdf",
                mime="application/pdf"
            )
        
        doc = fitz.open(cv_path)
        
        # Container stylisé pour le CV
        st.markdown('<div style="margin-top: 30px; border: 1px solid #e2e8f0;">', unsafe_allow_html=True)
        for page in doc:
            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
            img_data = pix.tobytes("png")
            st.image(img_data, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        doc.close()

# Footer
st.markdown(f'<div class="footer-text">Frédéric Bayen • Data Strategy Expert • 2026<br>Propulsé par Streamlit & Expertise</div>', unsafe_allow_html=True)
