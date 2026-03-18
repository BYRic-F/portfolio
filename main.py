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
        st.markdown("""
        <div class="insight-header">
            <h4>Le Défi Business</h4>
            <p style="margin:0; font-size: 1.15rem; color: #0f172a; font-weight: 500;">
                Stopper une hémorragie financière de <b>plusieurs centaines de millions de Shillings kényans par an</b> due à la fraude transactionnelle.
            </p>
        </div>
        """, unsafe_allow_html=True)

        col_text, col_viz = st.columns([1.2, 1], gap="large")
        with col_text:
            st.markdown('<p class="section-title">Performance & Impact</p>', unsafe_allow_html=True)
            st.markdown("""
            | Métrique | Score | Impact |
            | :--- | :--- | :--- |
            | **Recall** | **87 %** | Interception de la grande majorité des fraudes. |
            | **Spécificité** | **99,4 %** | Moins de 1% de faux positifs. |
            | **Latence** | **< 30ms** | Décision instantanée. |
            """)

            st.markdown('<p class="section-title">L\'Approche Technique (MLOps)</p>', unsafe_allow_html=True)
            st.markdown("""
            - **Ingestion** : Pipeline asynchrone via **FastAPI** et **Redis**.
            - **Modèle** : **XGBoost** optimisé pour le déséquilibre de classes.
            - **Automatisation** : Orchestration via **Prefect** et monitoring **Grafana**.
            """)

            tags = ["Python", "XGBoost", "FastAPI", "MLOps", "Redis", "Prefect", "Docker", "Grafana"]
            tag_html = "".join([f'<span class="tag">{tag}</span>' for tag in tags])
            st.markdown(f'<div style="margin-bottom: 25px;">{tag_html}</div>', unsafe_allow_html=True)
            
            btn_col1, btn_col2 = st.columns([1, 1])
            with btn_col1:
                st.markdown(f'<a href="https://github.com/BYRic-F/projet_fraude_cb" target="_blank" class="github-btn" style="width:100%; text-align:center;">Consulter le code</a>', unsafe_allow_html=True)
            with btn_col2:
                st.markdown(f'<a href="https://www.youtube.com/watch?v=oukKv2ohZn0" target="_blank" class="github-btn" style="width:100%; text-align:center;">Démonstration Vidéo</a>', unsafe_allow_html=True)

        with col_viz:
            img_path = "data/images/Python_detection_fraudes"
            if os.path.exists(img_path):
                st.image(os.path.join(img_path, "page_fraude.gif"), caption="Pilotage Temps Réel", use_container_width=True)
                sub_cols = st.columns(2)
                with sub_cols[0]: st.image(os.path.join(img_path, "grafanaa.gif"), use_container_width=True)
                with sub_cols[1]: st.image(os.path.join(img_path, "prefect2 (1).gif"), use_container_width=True)
        
    with tabs[1]:
        st.markdown('<div class="project-header"><h2>IA Prospector - Insee</h2></div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="insight-header">
            <h4>Le Défi Business</h4>
            <p style="margin:0; font-size: 1.15rem; color: #0f172a; font-weight: 500;">
                <b>Enrichir le CRM</b> par un ciblage automatisé via Gemini AI et l'API Insee.
            </p>
        </div>
        """, unsafe_allow_html=True)

        col_text, col_viz = st.columns([1.2, 1], gap="large")
        with col_text:
            st.markdown('<p class="section-title">Performance & Expertise</p>', unsafe_allow_html=True)
            st.markdown("""
            | Métrique | Impact |
            | :--- | :--- |
            | **Efficacité** | Ciblage précis sur 1700+ codes NAF. |
            | **IA** | Modèles Gemini 3.1 Flash-Lite. |
            """)

            st.markdown('<p class="section-title">Technologies</p>', unsafe_allow_html=True)
            tags = ["Gemini AI", "Streamlit", "API Insee", "OSINT", "Python", "Data Engineering"]
            tag_html = "".join([f'<span class="tag">{tag}</span>' for tag in tags])
            st.markdown(f'<div style="margin-bottom: 25px;">{tag_html}</div>', unsafe_allow_html=True)
            
            btn_col1, btn_col2 = st.columns([1, 1])
            with btn_col1:
                st.markdown(f'<a href="https://github.com/BYRic-F/Insee_prospector_cloud" target="_blank" class="github-btn" style="width:100%; text-align:center;">Consulter le code</a>', unsafe_allow_html=True)
            with btn_col2:
                st.markdown(f'<a href="https://inseeprospectorcloud.streamlit.app/" target="_blank" class="github-btn" style="width:100%; text-align:center;">Accéder à l\'application</a>', unsafe_allow_html=True)

        with col_viz:
            img_path = "data/images/Python_Inspector_insee"
            if os.path.exists(img_path):
                st.image(os.path.join(img_path, "demonstration_insee.gif"), use_container_width=True)
                sub_cols = st.columns(2)
                with sub_cols[0]: st.image(os.path.join(img_path, "Page_accueil1.png"), use_container_width=True)
                with sub_cols[1]: st.image(os.path.join(img_path, "Page_graphique2.png"), use_container_width=True)

    with tabs[2]:
        st.markdown('<div class="project-header"><h2>Moteur de Recommandation Hybride</h2></div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="insight-header">
            <h4>Le Défi Business</h4>
            <p style="margin:0; font-size: 1.15rem; color: #0f172a; font-weight: 500;">
                Résoudre le <b>Cold Start</b> par un système hybride KNN/SVD.
            </p>
        </div>
        """, unsafe_allow_html=True)

        col_text, col_viz = st.columns([1.2, 1], gap="large")
        with col_text:
            st.markdown('<p class="section-title">Performance & Innovation</p>', unsafe_allow_html=True)
            st.markdown("""
            | Métrique | Impact |
            | :--- | :--- |
            | **Algorithme** | Hybride (KNN Sémantique + SVD). |
            | **Données** | 10 000+ titres filtrés. |
            """)

            st.markdown('<p class="section-title">Technologies</p>', unsafe_allow_html=True)
            tags = ["NLP", "SpaCy", "DuckDB", "SVD", "Python", "Scikit-Learn"]
            tag_html = "".join([f'<span class="tag">{tag}</span>' for tag in tags])
            st.markdown(f'<div style="margin-bottom: 25px;">{tag_html}</div>', unsafe_allow_html=True)
            
            btn_col1, btn_col2 = st.columns([1, 1])
            with btn_col1:
                st.markdown(f'<a href="https://github.com/BYRic-F/project_reco_movie_streamlit" target="_blank" class="github-btn" style="width:100%; text-align:center;">Consulter le code</a>', unsafe_allow_html=True)
            with btn_col2:
                st.markdown(f'<a href="https://byric-f-project-reco-movie-streamlit-app-3pm0kb.streamlit.app/" target="_blank" class="github-btn" style="width:100%; text-align:center;">Accéder à l\'application</a>', unsafe_allow_html=True)

        with col_viz:
            img_path = "data/images/Python_Recommandations_films"
            if os.path.exists(img_path):
                st.image(os.path.join(img_path, "Python_recommandations films.gif"), use_container_width=True)
                sub_cols = st.columns(2)
                with sub_cols[0]: st.image(os.path.join(img_path, "Page_d_accueil.png"), use_container_width=True)
                with sub_cols[1]: st.image(os.path.join(img_path, "Resultat_recherche.png"), use_container_width=True)

elif selected == "Projets Power BI":
    st.markdown('<h1 class="main-title" style="text-align:left; font-size: 3rem !important;">Strategic BI</h1>', unsafe_allow_html=True)
    tabs = st.tabs(["TOYS & MODELS", "OPTIMA CYCLES", "MISSION HUMANITAIRE","GAMING INTELLIGENCE"])
    
    with tabs[0]:
        st.markdown('<div class="project-header"><h2>Toys & Models - Pilotage 360°</h2></div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="insight-header">
            <h4>Vision Holistique</h4>
            <p style="margin:0; font-size: 1.15rem; color: #0f172a; font-weight: 500;">
                Écosystème décisionnel unifié : Ventes, Finances et RH.
            </p>
        </div>
        """, unsafe_allow_html=True)

        col_text, col_viz = st.columns([1.2, 1], gap="large")
        with col_text:
            st.markdown('<p class="section-title">Périmètre de Pilotage (360°)</p>', unsafe_allow_html=True)
            st.markdown("""
            - **📊 Ventes** : Fidélisation (taux de retour), CA par bureau.
            - **💰 Finance** : Marge brute, gestion des créances.
            - **👥 RH** : Sécurisation des encaissements (ratio commandes/paiements).
            """)

            st.markdown('<p class="section-title">Insights Stratégiques</p>', unsafe_allow_html=True)
            st.markdown("""
            - ⚠️ **Risque de Concentration** : Dépendance critique envers deux clients majeurs.
            - 📉 **Optimisation Catalogue** : Retrait préconisé de la gamme "Trains".
            """)

            tags = ["MySQL", "Power BI", "DAX", "Data Modeling", "Finance BI"]
            tag_html = "".join([f'<span class="tag">{tag}</span>' for tag in tags])
            st.markdown(f'<div style="margin-bottom: 25px;">{tag_html}</div>', unsafe_allow_html=True)
            st.info("💡 Fichiers .pbix disponibles pour exploration.")

            btn_col1, btn_col2 = st.columns([1, 1])
            with btn_col1:
                st.markdown(f'<a href="https://github.com/BYRic-F/Toys_and_models" target="_blank" class="github-btn" style="width:100%; text-align:center;">Consulter le code</a>', unsafe_allow_html=True)
            with btn_col2:
                pdf_path = "data/presentations_pdf/Toys and models/Presentation_toys_and_models.pdf"
                if os.path.exists(pdf_path):
                    with open(pdf_path, "rb") as f:
                        st.download_button(label="Télécharger PDF", data=f, file_name="Toys_Models_Case.pdf", mime="application/pdf", key="toys_pdf")

        with col_viz:
            img_path = "data/images/PowerBi_Toys_and_models"
            if os.path.exists(img_path):
                st.image(os.path.join(img_path, "Ventes.png"), caption="Performance commerciale", use_container_width=True)
                sub_cols = st.columns(2)
                with sub_cols[0]: st.image(os.path.join(img_path, "Finances.png"), use_container_width=True)
                with sub_cols[1]: st.image(os.path.join(img_path, "RH.png"), use_container_width=True)

    with tabs[1]:
        st.markdown('<div class="project-header"><h2>Optima Cycles - Étude d\'implantation</h2></div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="insight-header">
            <h4>Vision Stratégique</h4>
            <p style="margin:0; font-size: 1.15rem; color: #0f172a; font-weight: 500;">
                Valider l'ouverture d'un point de vente par la donnée : Ciblage Californie, segment 35-64 ans.
            </p>
        </div>
        """, unsafe_allow_html=True)

        col_text, col_viz = st.columns([1.2, 1], gap="large")
        with col_text:
            st.markdown('<p class="section-title">Indicateurs de Performance</p>', unsafe_allow_html=True)
            st.markdown("""
            | KPI | Valeur | Impact |
            | :--- | :--- | :--- |
            | **Profit Global** | **$6.0 M** | Performance robuste en Californie. |
            | **Taux de Marge** | **44,0 %** | Rentabilité élevée. |
            """)

            tags = ["Power BI", "DAX", "Market Analysis", "Business Strategy"]
            tag_html = "".join([f'<span class="tag">{tag}</span>' for tag in tags])
            st.markdown(f'<div style="margin-bottom: 25px;">{tag_html}</div>', unsafe_allow_html=True)
            st.info("💡 Fichier .pbix disponible.")

            btn_col1, btn_col2 = st.columns([1, 1])
            with btn_col1:
                st.markdown(f'<a href="https://github.com/BYRic-F" target="_blank" class="github-btn" style="width:100%; text-align:center;">Consulter le code</a>', unsafe_allow_html=True)
            with btn_col2:
                pdf_path = "data/presentations_pdf/Optima_cycle/Power_Point_Presentation.pdf"
                if os.path.exists(pdf_path):
                    with open(pdf_path, "rb") as f:
                        st.download_button(label="Télécharger PDF", data=f, file_name="Optima_Strategy.pdf", mime="application/pdf", key="optima_pdf")

        with col_viz:
            img_path = "data/images/Power_bi_Optima_Cycles"
            if os.path.exists(img_path):
                st.image(os.path.join(img_path, "performance-du-marché.png"), use_container_width=True)
                sub_cols = st.columns(2)
                with sub_cols[0]: st.image(os.path.join(img_path, "profiling-segementation-produits.png"), use_container_width=True)
                with sub_cols[1]: st.image(os.path.join(img_path, "execution-et-pilotage.png"), use_container_width=True)

    with tabs[2]:
        st.markdown('<div class="project-header"><h2>Stratégie Data-Driven : Accès Universel à l\'Eau</h2></div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="insight-header">
            <h4>Mission Humanitaire</h4>
            <p style="margin:0; font-size: 1.15rem; color: #0f172a; font-weight: 500;">
                Optimiser l'allocation des fonds de l'ONG <b>World Vision</b> par une analyse décisionnelle.
            </p>
        </div>
        """, unsafe_allow_html=True)

        col_text, col_viz = st.columns([1.2, 1], gap="large")
        with col_text:
            st.markdown('<p class="section-title">Indicateurs & Décision</p>', unsafe_allow_html=True)
            st.markdown("""
            | Métrique | Observation | Recommandation |
            | :--- | :--- | :--- |
            | **Écart Rural** | **-32 %** d'accès. | Forages solaires autonomes. |
            | **Risque Vital** | **101/100k** décès. | Unités de purification mobiles. |
            """)

            st.markdown('<p class="section-title">Rigueur d\'Analyste & Biais</p>', unsafe_allow_html=True)
            st.markdown("""
            - ⏳ **Biais Temporel** : Données 2016. Mise à jour OMS 2024-2025 indispensable.
            - 🛡️ **Vigilance Conflit** : Sous-déclaration possible (Tchad, Somalie).
            """)

            tags = ["Power BI", "NGO Strategy", "Social Impact", "DAX"]
            tag_html = "".join([f'<span class="tag">{tag}</span>' for tag in tags])
            st.markdown(f'<div style="margin-bottom: 25px;">{tag_html}</div>', unsafe_allow_html=True)
            st.info("💡 Fichier .pbix disponible.")

            btn_col1, btn_col2 = st.columns([1, 1])
            with btn_col1:
                st.markdown(f'<a href="https://github.com/BYRic-F" target="_blank" class="github-btn" style="width:100%; text-align:center;">Consulter le code</a>', unsafe_allow_html=True)
            with btn_col2:
                pdf_path = "data/presentations_pdf/Acces_eau/Présentation_projet_eau.pdf"
                if os.path.exists(pdf_path):
                    with open(pdf_path, "rb") as f:
                        st.download_button(label="Télécharger PDF", data=f, file_name="World_Vision_Eau.pdf", mime="application/pdf", key="eau_pdf")

        with col_viz:
            img_path = "data/images/PowerBi_acces_eau"
            if os.path.exists(img_path):
                st.image(os.path.join(img_path, "Vue_monde.png"), use_container_width=True)
                sub_cols = st.columns(2)
                with sub_cols[0]: st.image(os.path.join(img_path, "Vue_region.png"), use_container_width=True)
                with sub_cols[1]: st.image(os.path.join(img_path, "Vue_pays.png"), use_container_width=True)

    with tabs[3]:
        st.markdown('<div class="project-header"><h2>Gaming Market Intelligence</h2></div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="insight-header">
            <h4>Mission de Conseil</h4>
            <p style="margin:0; font-size: 1.15rem; color: #0f172a; font-weight: 500;">
                Accompagner un éditeur dans la sécurisation d'un investissement majeur (83k titres).
            </p>
        </div>
        """, unsafe_allow_html=True)

        col_text, col_viz = st.columns([1.2, 1], gap="large")
        with col_text:
            st.markdown('<p class="section-title">Seuils de Succès</p>', unsafe_allow_html=True)
            st.markdown("""
            - **Metacritic ≥ 79** | Visibilité critique.
            - **Prix : 50,00 €** | Positionnement Premium.
            """)

            tags = ["Power BI", "Python", "DAX", "Market Intelligence"]
            tag_html = "".join([f'<span class="tag">{tag}</span>' for tag in tags])
            st.markdown(f'<div style="margin-bottom: 25px;">{tag_html}</div>', unsafe_allow_html=True)
            st.info("💡 Fichier .pbix disponible.")

            btn_col1, btn_col2 = st.columns([1, 1])
            with btn_col1:
                st.markdown(f'<a href="https://github.com/BYRic-F/VideoGame-Market" target="_blank" class="github-btn" style="width:100%; text-align:center;">Consulter le code</a>', unsafe_allow_html=True)
            with btn_col2:
                pdf_path = "data/presentations_pdf/Video_game_market/Presentation_video_game.pdf"
                if os.path.exists(pdf_path):
                    with open(pdf_path, "rb") as f:
                        st.download_button(label="Télécharger PDF", data=f, file_name="Gaming_Strategy.pdf", mime="application/pdf", key="gaming_pdf")

        with col_viz:
            img_path = "data/images/Power_BI_Video_game_market"
            if os.path.exists(img_path):
                st.image(os.path.join(img_path, "Choix stratégique.png"), use_container_width=True)
                sub_cols = st.columns(2)
                with sub_cols[0]: st.image(os.path.join(img_path, "Santé du marché.png"), use_container_width=True)
                with sub_cols[1]: st.image(os.path.join(img_path, "Leviers de rentabilité.png"), use_container_width=True)

elif selected == "Mon CV":
    st.markdown('<h1 class="main-title" style="text-align:left; font-size: 3rem !important;">Profil & Expertise</h1>', unsafe_allow_html=True)
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
                    Expertise technique (Python/SQL) et vision stratégique BI.
                </p>
            </div>
            """, unsafe_allow_html=True)
            # Affichage du CV
            doc = fitz.open(cv_path)
            st.markdown('<div style="margin-top: 20px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);">', unsafe_allow_html=True)
            for page in doc:
                pix = page.get_pixmap(matrix=fitz.Matrix(1.3, 1.3))
                img_data = pix.tobytes("png")
                st.image(img_data, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.write(" ")
            # Centrage millimétré du bouton
            btn_col_left, btn_col_mid, btn_col_right = st.columns([1, 1, 1])
            with btn_col_mid:
                st.download_button(
                    label="Télécharger le CV complet (PDF)", 
                    data=pdf_bytes, 
                    file_name="CV_Frédéric_Bayen.pdf", 
                    mime="application/pdf", 
                    use_container_width=True
                )
            doc.close()

st.markdown(f'<div class="footer-text">Frédéric Bayen • Data Strategy • 2026<br>Propulsé par Streamlit</div>', unsafe_allow_html=True)
