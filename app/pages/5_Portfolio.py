import streamlit as st

st.title("Portfolio")
st.caption("Sélection de projets et réalisations (contexte • actions • impact • stack).")
st.divider()

def pill(tags):
    st.markdown(
        " ".join([
            f"<span style='padding:4px 10px;border-radius:999px;"
            f"background:#262730;border:1px solid #3a3b3f;"
            f"font-size:12px;margin-right:6px'>{t}</span>"
            for t in tags
        ]),
        unsafe_allow_html=True
    )

def project_card(title, context, actions, impact, tags, repo_url=None, demo_url=None):
    with st.container(border=True):
        st.subheader(title)
        st.markdown(f"**Contexte :** {context}")
        st.markdown("**Ce que j’ai fait :**")
        for a in actions:
            st.write("•", a)

        if impact:
            st.markdown("**Impact / Résultats :**")
            for i in impact:
                st.write("•", i)

        pill(tags)

        c1, c2 = st.columns(2)
        with c1:
            if repo_url:
                st.link_button("GitHub", repo_url)
        with c2:
            if demo_url:
                st.link_button("Démo", demo_url)

# =========================
# PROJET PHARE (DSI / DATA PLATFORM)
# =========================
st.markdown("##  Projet phare — Data Platform & Automatisation (ECOSYSTEM)")

project_card(
    title="Plateforme data commune & automatisation des pipelines",
    context="DSI : centraliser les données et industrialiser les traitements pour répondre aux besoins métiers et partenaires.",
    actions=[
        "Requêtes SQL sur Databricks pour transformer/agréger des données volumineuses.",
        "Développement de scripts Python (Pandas/NumPy) pour extractions récurrentes et contrôles qualité.",
        "Automatisation de lancements de scripts sur AWS (SageMaker) pour fiabiliser l’exécution.",
        "Mise à disposition de datasets et exports pour équipes internes / clients.",
    ],
    impact=[
        "Réduction des extractions manuelles et des erreurs de manipulation.",
        "Données plus fiables et partage inter-services facilité.",
        "Accélération du delivery des demandes data (reporting, analyses ad hoc).",
    ],
    tags=["Databricks", "SQL", "Python", "AWS SageMaker", "Athena", "Power BI"]
)

st.divider()

# =========================
# DATA SCIENCE APPLIQUÉE
# =========================
st.markdown("##  Data science appliquée (fraude / prévisions)")

project_card(
    title="Détection de fraude — Fonds Réparation QualiRépar",
    context="Identifier des comportements suspects dans les demandes de remboursement et sécuriser le dispositif.",
    actions=[
        "Analyse de volumes, historiques, distributions et incohérences de montants.",
        "Construction de règles de scoring / signaux faibles pour prioriser les contrôles.",
        "Exports et synthèses actionnables pour les équipes conformité.",
    ],
    impact=[
        "Remontée de cas suspects et amélioration du ciblage des contrôles.",
        "Meilleure traçabilité des anomalies et suivi des réparateurs à risque.",
    ],
    tags=["Python", "Pandas", "Data Quality", "Fraude", "Scoring"]
)

project_card(
    title="Automatisations de prévisions & extraction pour analyses",
    context="Produire des extractions propres et répétables pour des besoins internes ou clients.",
    actions=[
        "Scripts Python pour extractions normalisées + contrôles automatiques (formats, doublons, écarts).",
        "Préparation de datasets pour modèles de prévision / analyses statistiques.",
    ],
    impact=[
        "Standardisation des livrables et gain de temps sur les demandes récurrentes.",
    ],
    tags=["Python", "Automatisation", "Prévisions", "Data Pipeline"]
)

st.divider()

# =========================
# BI / DATAVIZ
# =========================
st.markdown("##  BI & reporting")

project_card(
    title="Reporting décisionnel & dashboards",
    context="Restituer des KPIs fiables pour le pilotage (direction, métiers, partenaires).",
    actions=[
        "Création / alimentation de tableaux de bord Power BI.",
        "Reporting hebdomadaire dans SAP Analytics Cloud (SAC).",
        "Mise en cohérence des indicateurs entre sources (SAP, exports, traitements Python).",
    ],
    impact=[
        "Pilotage plus clair des activités et meilleure lisibilité des tendances.",
    ],
    tags=["Power BI", "SAP Analytics Cloud", "KPI", "Data Viz"]
)

st.divider()

# =========================
# PROJETS ACADÉMIQUES (OPTIONNEL)
# =========================
st.markdown("##  Projets académiques (sélection)")

project_card(
    title="Échange en Malaisie (APU) — Chatbot & Data Tourism",
    context="Programme d’échange EFREI : projets data, IA et méthode produit en contexte international.",
    actions=[
        "Développement d’un chatbot en Python (logique conversationnelle, IA de base).",
        "Analyse et dataviz sur des données touristiques malaisiennes avec Power BI.",
        "Approche Design Thinking + gestion de projet (workshops, prototypage, restitution).",
    ],
    impact=[
        "Projet présenté et soutenu en équipe multiculturelle (anglais).",
    ],
    tags=["Python", "Power BI", "IA", "Design Thinking", "Project Management"]
)
