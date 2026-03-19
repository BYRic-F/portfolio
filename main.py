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

# --- PAGES ---

if selected == "Accueil":
    # Hero Section
    st.markdown('<div class="hero-container">', unsafe_allow_html=True)
    st.markdown('<h1 class="main-title">Je transforme vos flux de données complexes<br>en leviers de croissance mesurables.</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Data Strategy • MLOps & Automation • Business Intelligence</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([0.8, 2], gap="large")
    with col1:
        photo_path = "data/CV/photo_profil_redimenssionnee.webp"
        if os.path.exists(photo_path):
            st.markdown('<div class="profile-img-container">', unsafe_allow_html=True)
            st.image(photo_path, width="stretch", output_format="png")
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
            - **Pipeline MLOps & Model Gating** : Orchestration du cycle de vie via **Prefect**. Ingestion automatisée depuis **BigQuery** et réentraînement périodique. Déploiement sécurisé par une stratégie de Champion-Challenger : la nouvelle version n'est promue en production que si elle surpasse le record de Recall et F1-score historique
            """)

            st.markdown('<p class="section-title">Axes d\'amélioration</p>', unsafe_allow_html=True)
            st.markdown("""
            - **Migration Cloud** : Déploiement de l'architecture sur **GCP** (Cloud Run / GKE) pour une scalabilité horizontale réelle et une haute disponibilité.
            - **Modern Data Stack** : Intégration de **dbt** pour orchestrer et versionner les transformations de données dans BigQuery, garantissant la qualité (tests automatisés) et la lignée des données.
            """)

            # Tags & Buttons
            st.markdown('<p class="section-title">Technologies</p>', unsafe_allow_html=True)
            tags = ["Python", "XGBoost", "FastAPI", "MLOps", "Redis", "BigQuery", "Prefect", "Docker", "Grafana"]
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
            st.write("") 
            st.write("")# Spacer
            # Affichage des GIFs avec la disposition d'origine (un grand, les autres en dessous)
            img_path = "data/images/Python_detection_fraudes"
            if os.path.exists(img_path):
                st.image(os.path.join(img_path, "page_fraude.gif"), caption="Détection de fraudes en temps réel", width="stretch")
                
                sub_cols = st.columns(2)
                with sub_cols[0]:
                    st.image(os.path.join(img_path, "grafanaa.gif"), caption="Monitoring (Grafana)", width="stretch")
                with sub_cols[1]:
                    st.image(os.path.join(img_path, "prefect2 (1).gif"), caption="MLOps (Prefect)", width="stretch")
        
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
            | **Efficacité de ciblage** | **100% de succès** sur 50 tests sectoriels intensifs. |
            | **Précision IA** | Traduction sémantique des métiers en **codes NAF techniques**. |
            | **Modèles** | Architectures hybrides **Gemini 3 & 3.1 Flash-Lite**. |
            """)

            st.markdown('<p class="section-title">Ingénierie de Précision</p>', unsafe_allow_html=True)
            st.markdown("""
            Conçu pour répondre aux exigences critiques d'un cabinet de recrutement (RH Performances) :
            - **Nomenclature NAF 2008** : Scan intelligent de **1700+ codes NAF** pour garantir une compatibilité à 100% avec l'API Sirene réelle.
            - **Batching intelligent** : Découpage dynamique des requêtes pour les zones denses (Paris, Lyon, Marseille) afin d'éviter la saturation de l'API.
            - **Optimisation mobile (OSINT)** : Transformation automatique des numéros en **liens cliquables (tel:)** pour une prospection directe sur smartphone.
            """)

            st.markdown('<p class="section-title">Axes d\'amélioration</p>', unsafe_allow_html=True)
            st.markdown("""
            - **Enrichissement Multi-Sources** : Interfaçage avec le **MCP Data.gouv** pour croiser les données Insee avec des indicateurs financiers (bilans simplifiés), juridiques (certifications RSE) et administratifs (subventions), offrant un ciblage 360° aux recruteurs.
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
            st.write("") 
            st.write("")# Spacer
            # Affichage des images (GIF en principal, screenshots en dessous)
            img_path = "data/images/Python_Inspector_insee"
            if os.path.exists(img_path):
                st.image(os.path.join(img_path, "demonstration_insee.gif"), caption="Démonstration du ciblage intelligent", width="stretch")
                
                sub_cols = st.columns(2)
                with sub_cols[0]:
                    st.image(os.path.join(img_path, "Page_accueil1.webp"), caption="Interface d'accueil & export CRM", width="stretch", output_format="png")
                with sub_cols[1]:
                    st.image(os.path.join(img_path, "Page_graphique2.webp"), caption="Analyses géographiques & sectorielles", width="stretch", output_format="png")

    with tabs[2]:
        st.markdown('<div class="project-header"><h2>Système de recommandation hybride (Content & collaborative)</h2></div>', unsafe_allow_html=True)
        
        # Storytelling Hook
        st.markdown("""
        <div class="insight-header">
            <h4>Le Défi Business</h4>
            <p style="margin:0; font-size: 1.15rem; color: #0f172a; font-weight: 500;">
                Maximiser la rétention utilisateur en proposant des recommandations pertinentes dès la première connexion, 
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

            st.markdown('<p class="section-title">Axes d\'amélioration</p>', unsafe_allow_html=True)
            st.markdown("""
            - **Infrastructure relationnelle** : Migration de la gestion des utilisateurs (actuellement sur Google Sheets) vers une base de données **SQL (PostgreSQL)** pour renforcer la sécurité des données et accroître la rapidité des requêtes.
            - **Gestion d'identité avancée** : Implémentation d'un système d'authentification robuste incluant la récupération de mot de passe et d'identifiants perdus.
            """)

            # Tags & Buttons
            st.markdown('<p class="section-title">Technologies</p>', unsafe_allow_html=True)
            tags = ["NLP", "SpaCy", "DuckDB", "SVD", "KNN", "Python", "ETL", "Streamlit", "Scikit-Learn"]
            tag_html = "".join([f'<span class="tag">{tag}</span>' for tag in tags])
            st.markdown(f'<div style="margin-bottom: 25px;">{tag_html}</div>', unsafe_allow_html=True)
            st.info("💡 Les identifiants pour tester l'application sont : Username : test500 / Password : test500")
            
            btn_col1, btn_col2 = st.columns([1, 1])
            with btn_col1:
                st.markdown(f'<a href="https://github.com/BYRic-F/project_reco_movie_streamlit" target="_blank" class="github-btn" style="width:100%; text-align:center;">Consulter le code</a>', unsafe_allow_html=True)
            with btn_col2:
                st.markdown(f'<a href="https://byric-f-project-reco-movie-streamlit-app-3pm0kb.streamlit.app/" target="_blank" class="github-btn" style="width:100%; text-align:center;">Accéder à l\'application</a>', unsafe_allow_html=True)

        with col_viz:
            st.write("") 
            st.write("")# Spacer
            st.write("")
            # Affichage des images (GIF en principal, screenshots en dessous)
            img_path = "data/images/Python_Recommandations_films"
            if os.path.exists(img_path):
                st.image(os.path.join(img_path, "Python_recommandations films.gif"), caption="Expérience utilisateur & Recommandations", width="stretch")
                
                sub_cols = st.columns(2)
                with sub_cols[0]:
                    st.image(os.path.join(img_path, "Page_d_accueil.webp"), caption="Page d'accueil", width="stretch", output_format="png")
                with sub_cols[1]:
                    st.image(os.path.join(img_path, "Resultat_recherche.webp"), caption="Analyse sémantique & détails", width="stretch", output_format="png")

elif selected == "Projets Power BI":
    st.markdown('<h1 class="main-title" style="text-align:left; font-size: 3rem !important;">Strategic BI</h1>', unsafe_allow_html=True)
    tabs = st.tabs(["OPTIMA CYCLES", "TOYS & MODELS", "MISSION HUMANITAIRE","GAMING INTELLIGENCE"])
    
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
            | KPI | Valeur | Impact stratégique |
            | :--- | :--- | :--- |
            | **Profit global** | **$6.0 M** | Performance robuste sur le marché californien. |
            | **Taux de marge** | **44,0 %** | Rentabilité élevée sur les produits choisis. |
            | **Moteur de profit** | **56,8 %** | Part du profit généré par le segment 35-64 ans. |
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
                st.markdown(f'<a href="https://github.com/BYRic-F/Data-Driven-Retail-Launch" target="_blank" class="github-btn" style="width:100%; text-align:center;">Consulter le code</a>', unsafe_allow_html=True)
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
            st.write("") 
            st.write("")# Spacer
            # Affichage des images (Performance en principal, thumbnails en dessous)
            img_path = "data/images/Power_bi_Optima_Cycles"
            if os.path.exists(img_path):
                st.image(os.path.join(img_path, "performance-du-marché.webp"), caption="Analyse de performance & saisonnalité", width="stretch", output_format="png")
                
                sub_cols = st.columns(2)
                with sub_cols[0]:
                    st.image(os.path.join(img_path, "profiling-segementation-produits.webp"), caption="Profiling & segmentation", width="stretch", output_format="png")
                with sub_cols[1]:
                    st.image(os.path.join(img_path, "execution-et-pilotage.webp"), caption="Exécution & plan de route", width="stretch", output_format="png")

    with tabs[3]:
        st.markdown('<div class="project-header"><h2>Gaming Market intelligence</h2></div>', unsafe_allow_html=True)
        
        # Storytelling Hook
        st.markdown("""
        <div class="insight-header">
            <h4>Mission de Conseil : GameQuest Productions</h4>
            <p style="margin:0; font-size: 1.15rem; color: #0f172a; font-weight: 500;">
                Accompagner <b>Édouard</b> (éditeur Mid-Tier) dans la sécurisation d'un investissement majeur 
                parmi <b>83 000 titres</b> concurrents.
            </p>
        </div>
        """, unsafe_allow_html=True)

        col_text, col_viz = st.columns([1.2, 1], gap="large")
        
        with col_text:
            st.markdown('<p class="section-title">Seuils de Succès & ROI</p>', unsafe_allow_html=True)
            st.markdown("""
            | Indicateur | Cible critique | Impact Business |
            | :--- | :--- | :--- |
            | **Score Metacritic** | **≥ 79 / 100** | Seuil de visibilité et de crédibilité critique. |
            | **Avis Positifs** | **≥ 82 %** | Garantie d'un bouche-à-oreille organique fort. |
            | **Prix de Vente** | **50,00 €** | Positionnement Premium vs guerre des prix. |
            """)

            st.markdown('<p class="section-title">Recommandation Stratégique</p>', unsafe_allow_html=True)
            st.markdown("""
            Une feuille de route pour maximiser la **LTV (Lifetime Value)** :
            - **Genre & modèle** : Développement d'un **MMORPG Premium** avec une stratégie de 2 à 3 DLC pour assurer la persistance des revenus.
            - **Fenêtres de tir** : Lancement prioritaire en **Mars** ou **Septembre** pour éviter les creux de saisonnalité.
            - **Indice de risque (24.5)** : Modèle calculé sur la complexité technique et la saturation du marché, compensé par une localisation multilingue (5+ langues).
            """)

            st.markdown('<p class="section-title">Maîtrise Technique</p>', unsafe_allow_html=True)
            st.markdown("""
            - **Pipeline** : Extraction et normalisation de **83 000 titres** via script Python.
            - **BI Avancée** : Mesures **DAX** pour isoler les leviers de rentabilité.
            - **Agilité** : Étude complète livrée en **1,5 jour**, alliant profondeur d'analyse et rapidité d'exécution.
            """)

            # Tags & Buttons
            st.markdown('<p class="section-title">Outils & Livrables</p>', unsafe_allow_html=True)
            tags = ["Power BI", "Python", "DAX", "Market Intelligence", "Consulting", "ETL"]
            tag_html = "".join([f'<span class="tag">{tag}</span>' for tag in tags])
            st.markdown(f'<div style="margin-bottom: 25px;">{tag_html}</div>', unsafe_allow_html=True)
            
            st.info("💡 Fichier .pbix disponible pour exploration interactive des 83k titres.")
            st.write("")

            btn_col1, btn_col2 = st.columns([1, 1])
            with btn_col1:
                st.markdown(f'<a href="https://github.com/BYRic-F/VideoGame-Market" target="_blank" class="github-btn" style="width:100%; text-align:center;">Consulter le code</a>', unsafe_allow_html=True)
            with btn_col2:
                pdf_path = "data/presentations_pdf/Video_game_market/Presentation_video_game.pdf"
                if os.path.exists(pdf_path):
                    with open(pdf_path, "rb") as f:
                        st.download_button(
                            label="Télécharger l'étude (PDF)",
                            data=f,
                            file_name="Gaming_Intelligence_Strategie.pdf",
                            mime="application/pdf",
                            key="gaming_pdf"
                        )

        with col_viz:
            st.write("") 
            st.write("")# Spacer
            # Affichage des images (Choix stratégique en principal, thumbnails en dessous)
            img_path = "data/images/Power_BI_Video_game_market"
            if os.path.exists(img_path):
                st.image(os.path.join(img_path, "Choix stratégique.webp"), caption="Recommandation Business Plan & LTV", width="stretch", output_format="png")
                
                sub_cols = st.columns(2)
                with sub_cols[0]:
                    st.image(os.path.join(img_path, "Santé du marché.webp"), caption="Diagnostic : Saturation & prix", width="stretch", output_format="png")
                with sub_cols[1]:
                    st.image(os.path.join(img_path, "Leviers de rentabilité.webp"), caption="Analyse de la qualité & saisonnalité", width="stretch", output_format="png")

    with tabs[2]:
        st.markdown('<div class="project-header"><h2>Stratégie Data-Driven : Analyse décisionnelle pour l\'accès à l\'eau</h2></div>', unsafe_allow_html=True)
        
        # Storytelling Hook
        st.markdown("""
        <div class="insight-header">
            <h4>Mission de conseil stratégique</h4>
            <p style="margin:0; font-size: 1.15rem; color: #0f172a; font-weight: 500;">
                Optimiser l'allocation des fonds de l'ONG <b>World Vision</b> par une analyse prédictive des zones de crise, 
                transformant la donnée brute en un plan d'urgence vital et pérenne.
            </p>
        </div>
        """, unsafe_allow_html=True)

        col_text, col_viz = st.columns([1.2, 1], gap="large")
        
        with col_text:
            st.markdown('<p class="section-title">Indicateurs d\'urgence & décision</p>', unsafe_allow_html=True)
            st.markdown("""
            | Métrique | Observation clé | Recommandation stratégique |
            | :--- | :--- | :--- |
            | **Écart Rural/Urbain** | **-32 %** d'accès en zone rurale (Afrique). | Investissement prioritaire en forages solaires autonomes. |
            | **Risque vital** | **101 / 100k** décès (Tchad). | Déploiement ciblé d'unités de purification mobiles. |
            | **Corrélation politique** | Impact direct de l'instabilité sur la pérennité. | Sécurisation des infrastructures plutôt que simple réparation. |
            """)

            st.markdown('<p class="section-title">Piliers de l\'Expertise</p>', unsafe_allow_html=True)
            st.markdown("""
            Une approche centrée sur l'impact et l'agilité technique :
            - **Analyse de résilience** : Identification du lien critique entre stabilité politique et dégradation des infrastructures. L'insight stratégique : sécuriser l'infrastructure est aussi vital que de la construire.
            - **Ciblage "Glocal"** : Définition de l'épicentre du risque mondial (mortalité 3x supérieure à la moyenne) avec une segmentation granulaire pour maximiser le ROI humanitaire.
            - **Agilité record** : Maîtrise complète de la stack avec un livrable stratégique finalisé en seulement **7 heures**.
            """)

            st.markdown('<p class="section-title">Rigueur d\'Analyste & Biais</p>', unsafe_allow_html=True)
            st.markdown("""
            Une analyse experte repose sur la transparence des limites identifiées pour sécuriser la décision :
            - **Biais temporel** : L'étude s'appuie sur des indicateurs de 2016. Une mise à jour avec les flux 2024-2025 de l'OMS est indispensable pour un déploiement opérationnel.
            - **Vigilance Zones de conflit** : Les données (Tchad, Somalie) peuvent présenter un biais de sous-déclaration lié aux difficultés de recensement sur le terrain.
            - **Scalabilité** : L'architecture est conçue pour intégrer instantanément ces nouveaux flux OMS afin de réactualiser les priorités en temps réel.
            """)

            # Tags & Buttons
            st.markdown('<p class="section-title">Outils & Expertises</p>', unsafe_allow_html=True)
            tags = ["Power BI", "NGO Strategy", "Social Impact", "Scalable Pipeline", "Power Query", "DAX"]
            tag_html = "".join([f'<span class="tag">{tag}</span>' for tag in tags])
            st.markdown(f'<div style="margin-bottom: 25px;">{tag_html}</div>', unsafe_allow_html=True)
            
            st.info("💡 Fichier .pbix disponible pour une exploration interactive approfondie.")
            st.write(" ")

            btn_col1, btn_col2 = st.columns([1, 1])
            with btn_col1:
                st.markdown(f'<a href="https://github.com/BYRic-F/PowerBi_acces_eau" target="_blank" class="github-btn" style="width:100%; text-align:center;">Consulter le code</a>', unsafe_allow_html=True)
            with btn_col2:
                pdf_path = "data/presentations_pdf/Acces_eau/Présentation_projet_eau.pdf"
                if os.path.exists(pdf_path):
                    with open(pdf_path, "rb") as f:
                        st.download_button(
                            label="Télécharger l'étude (PDF)",
                            data=f,
                            file_name="Stratégie_World_Vision_Eau.pdf",
                            mime="application/pdf",
                            key="eau_pdf"
                        )

        with col_viz:
            st.write("") 
            st.write("")# Spacer            
            # Affichage des images (Vue Monde en principal, thumbnails en dessous)
            img_path = "data/images/PowerBi_acces_eau"
            if os.path.exists(img_path):
                st.image(os.path.join(img_path, "Vue_monde.webp"), caption="Analyse mondiale & corrélations politiques", width="stretch", output_format="png")
                
                sub_cols = st.columns(2)
                with sub_cols[0]:
                    st.image(os.path.join(img_path, "Vue_region.webp"), caption="Focus Afrique & fractures rurales", width="stretch", output_format="png")
                with sub_cols[1]:
                    st.image(os.path.join(img_path, "Vue_pays.webp"), caption="Priorisation par pays (Risque vital)", width="stretch", output_format="png")

    with tabs[1]:
        st.markdown('<div class="project-header"><h2>Toys & Models - Pilotage 360°</h2></div>', unsafe_allow_html=True)
        
        # Storytelling Hook
        st.markdown("""
        <div class="insight-header">
            <h4>Vision Holistique</h4>
            <p style="margin:0; font-size: 1.15rem; color: #0f172a; font-weight: 500;">
                Transformer une base de données brute en un écosystème décisionnel unifié pour piloter les 
                <b>ventes</b>, les <b>finances</b> et les <b>Ressources Humaines</b> d'un distributeur mondial.
            </p>
        </div>
        """, unsafe_allow_html=True)

        col_text, col_viz = st.columns([1.2, 1], gap="large")
        
        with col_text:
            st.markdown('<p class="section-title">Impact Business & Trésorerie</p>', unsafe_allow_html=True)
            st.markdown("""
            | Axe d'analyse | Résultat clé | Valeur ajoutée |
            | :--- | :--- | :--- |
            | **Finances** | **Optimisation trésorerie** | Identification des problèmatiques de paiement. |
            | **Ventes** | **Fidélisation** | Calcul automatisé du taux de retour client par région et des performances produits|
            | **RH** | **Sécurisation des Encaissements** | Corrélation directe entre CA généré et ratio d'impayés par agent. |
            """)

            st.markdown('<p class="section-title">Périmètre de Pilotage (360°)</p>', unsafe_allow_html=True)
            st.markdown("""
            - **Dashboard Ventes** : Analyse du CA par bureau, suivi de la **fidélisation** (taux de retour) et de l'efficacité commerciale (panier moyen par catégorie).
            - **Dashboard Finance** : Calcul de la **marge brute** par produit, suivi de la croissance trimestrielle et gestion fine des créances (taux de recouvrement).
            - **Dashboard RH** : Classement des performances agents, responsabilisation sur les impayés.
            """)

            st.markdown('<p class="section-title">Piliers de l\'Architecture</p>', unsafe_allow_html=True)
            st.markdown("""
            Une solution intégrée reposant sur une modélisation robuste :
            - **Intelligence SQL** : Utilisation de requêtes complexes (**CTE**, **Window Functions**) pour extraire des KPIs croisés inaccessibles via un export standard.
            - **Modélisation Star Schema** : Restructuration complète de la base MySQL vers un schéma en étoile (FACT_ORDER, DIM_PRODUCT...) pour une performance analytique optimale.
            - **Gestion du Cash-Flow** : Responsabilisation des commerciaux sur le cycle de vie complet de la vente (de la commande au paiement réel).
            """)

            st.markdown('<p class="section-title">Insights Stratégiques</p>', unsafe_allow_html=True)
            st.markdown("""
            - **Risque de concentration** : Mise en évidence d'une dépendance critique envers deux clients majeurs. Préconisation de diversification du portefeuille.
            - **Optimisation du catalogue** : Analyse de rotation suggérant le retrait de la gamme "Trains" pour libérer du fonds de roulement.
            """)

            # Tags & Buttons
            st.markdown('<p class="section-title">Stack Technique</p>', unsafe_allow_html=True)
            tags = ["MySQL", "Power BI", "DAX", "Data Modeling", "Finance BI", "Supply Chain"]
            tag_html = "".join([f'<span class="tag">{tag}</span>' for tag in tags])
            st.markdown(f'<div style="margin-bottom: 25px;">{tag_html}</div>', unsafe_allow_html=True)
            
            st.info("💡 Fichiers .pbix (Ventes, Finances, RH) disponibles pour une exploration interactive.")
            st.write(" ")

            btn_col1, btn_col2 = st.columns([1, 1])
            with btn_col1:
                st.markdown(f'<a href="https://github.com/BYRic-F/Toys_and_models" target="_blank" class="github-btn" style="width:100%; text-align:center;">Consulter le code</a>', unsafe_allow_html=True)
            with btn_col2:
                pdf_path = "data/presentations_pdf/Toys and models/Presentation_toys_and_models.pdf"
                if os.path.exists(pdf_path):
                    with open(pdf_path, "rb") as f:
                        st.download_button(
                            label="Télécharger l'étude (PDF)",
                            data=f,
                            file_name="Toys_Models_Business_Case.pdf",
                            mime="application/pdf",
                            key="toys_pdf"
                        )

        with col_viz:
            st.write("") 
            st.write("")# Spacer            
            # Affichage des images (Ventes en principal, thumbnails en dessous)
            img_path = "data/images/PowerBi_Toys_and_models"
            if os.path.exists(img_path):
                st.image(os.path.join(img_path, "Ventes.webp"), caption="Pilotage de la performance commerciale", width="stretch", output_format="png")
                
                sub_cols = st.columns(2)
                with sub_cols[0]:
                    st.image(os.path.join(img_path, "Finances.webp"), caption="Analyse de rentabilité & trésorerie", width="stretch", output_format="png")
                with sub_cols[1]:
                    st.image(os.path.join(img_path, "RH.webp"), caption="Suivi des performances RH", width="stretch", output_format="png")

elif selected == "Mon CV":
    st.markdown('<h1 class="main-title" style="text-align:left; font-size: 3rem !important;">Profil & expertise</h1>', unsafe_allow_html=True)
    
    cv_dir = "data/CV"
    cv_files = [f for f in os.listdir(cv_dir) if f.lower().endswith(".pdf")]
    
    if cv_files:
        cv_path = os.path.join(cv_dir, cv_files[0])
        col_left, col_cv, col_right = st.columns([0.75, 1.5, 0.75])
        
        with col_cv:
            with open(cv_path, "rb") as f:
                pdf_bytes = f.read()
            st.markdown("""
            <div style="background: #f8fafc; padding: 2rem; border-radius: 4px; border: 1px solid #e2e8f0; margin-bottom: 2rem; text-align: center;">
                <h3 style="margin-top:0; color: #0f172a;">Prêt pour de nouveaux défis</h3>
                <p style="color: #64748b; font-size: 1.1rem; max-width: 600px; margin: 0 auto 1.5rem auto;">
                    Mon profil combine expertise technique (Python/SQL) et vision stratégique BI. 
                    N'hésitez pas à télécharger mon CV complet ou à me contacter pour discuter de vos projets.
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            # Affichage du CV
            doc = fitz.open(cv_path)
            st.markdown('<div style="margin-top: 20px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);">', unsafe_allow_html=True)
            for page in doc:
                pix = page.get_pixmap(matrix=fitz.Matrix(1.3, 1.3))
                img_data = pix.tobytes("png")
                st.image(img_data, width="stretch", output_format="png")
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.write(" ")
            # Micro-ajustement pour un centrage visuel parfait du bouton
            btn_col_left, btn_col_mid, btn_col_right = st.columns([1.1, 1, 0.9])
            with btn_col_mid:
                st.download_button(
                    label="Télécharger le CV complet (PDF)", 
                    data=pdf_bytes, 
                    file_name="CV_Frédéric_Bayen.pdf", 
                    mime="application/pdf", 
                    width="stretch"
                )
            doc.close()

# Footer
st.markdown(f'<div class="footer-text">Frédéric Bayen • Data Strategy • 2026<br>Propulsé par Streamlit</div>', unsafe_allow_html=True)