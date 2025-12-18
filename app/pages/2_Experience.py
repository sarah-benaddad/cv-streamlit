import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Expérience | Sarah Benaddad", page_icon=None, layout="wide")

# ---------- CSS ----------
st.markdown("""
<style>
.center { text-align:center; }
.small { font-size:0.95rem; opacity:0.85; }

.role { font-weight: 800; font-size: 1.25rem; }
.company { font-size: 1.05rem; opacity: 0.9; }
.meta { font-size: 0.95rem; opacity: 0.8; }

.pills { display:flex; flex-wrap:wrap; gap:8px; justify-content:flex-start; align-items:flex-start; margin-top:10px; }
.pill {
  padding:6px 12px; border-radius:999px;
  background:#262730; border:1px solid #3a3b3f;
  font-size:0.85rem;
  line-height:1.2;
}

.spacer { height: 12px; }
</style>
""", unsafe_allow_html=True)

def pills(tags):
    st.markdown(
        "<div class='pills'>" + "".join([f"<span class='pill'>{t}</span>" for t in tags]) + "</div>",
        unsafe_allow_html=True
    )

def show_logo(logo_path: str, width: int = 90):
    """Affiche un logo si le fichier existe (PNG/JPG/WebP)."""
    p = Path(logo_path)
    if p.exists():
        st.image(str(p), width=width)

def experience_card(
    title: str,
    company: str,
    meta: str,
    summary: str,
    stack_tags: list[str],
    left_title: str,
    left_bullets: list[str],
    right_title: str,
    right_bullets: list[str],
    value_bullets: list[str] | None = None,
    logo_path: str | None = None,
    logo_width: int = 90,
):
    """Uniform card layout: logo top -> text down -> stack right."""
    with st.container(border=True):
        # Header row
        h1, h2 = st.columns([5, 2], gap="large")

        with h1:
            # Logo en haut
            if logo_path:
                show_logo(logo_path, width=logo_width)

            st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)

            # Titre/entreprise/meta descendus pour remplir l'espace
            st.markdown(f"<div class='role'>{title}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='company'>{company}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='meta'>{meta}</div>", unsafe_allow_html=True)

        with h2:
            st.markdown("**Stack**")
            pills(stack_tags)

        st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)

        # Summary
        st.markdown("**Résumé**")
        st.write(summary)

        st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)

        # Body (two columns)
        colA, colB = st.columns(2, gap="large")
        with colA:
            st.markdown(f"**{left_title}**")
            for b in left_bullets:
                st.write("•", b)

        with colB:
            st.markdown(f"**{right_title}**")
            for b in right_bullets:
                st.write("•", b)

        # Value / impact
        if value_bullets:
            st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)
            st.markdown("**Valeur / impact**")
            for v in value_bullets:
                st.write("•", v)

# ---------- Page header ----------
st.markdown("<h1 class='center'>Expérience</h1>", unsafe_allow_html=True)
st.markdown("<div class='center small'>Data • BI • Data Platform • Automatisation • IA appliquée</div>", unsafe_allow_html=True)
st.divider()

# ---------- ECOSYSTEM ----------
experience_card(
    title="Data Analyst / Data Platform (Alternance)",
    company="ECOSYSTEM — DSI & Data",
    meta="Paris-La Défense / Île-de-France • 2024 → fin 2025",
    summary=(
        "Mise en place d’une plateforme data commune et industrialisation des traitements "
        "(SQL Databricks + Python + Cloud), avec des cas d’usage BI, automatisation, "
        "prévisions et détection de fraude."
    ),
    stack_tags=["Databricks", "SQL", "Python", "AWS (SageMaker)", "Athena", "Power BI", "SAP / SAC"],
    left_title="Missions clés",
    left_bullets=[
        "Requêtes SQL sur Databricks (transformation, agrégation, datasets BI).",
        "Pipelines Python : extraction → nettoyage → structuration → export.",
        "Automatisation de runs / traitements sur AWS (SageMaker).",
        "Mise à disposition de données pour plusieurs services (exports internes / clients).",
        "Alimentation de dashboards (Power BI / SAC) et support aux demandes data.",
    ],
    right_title="Analyses avancées",
    right_bullets=[
        "Détection de comportements à risque : anomalies de montants / volumes / historiques.",
        "Mise en place de signaux faibles et règles de scoring.",
        "Préparation de datasets pour prévisions et analyses statistiques.",
        "Contrôles qualité automatisés (formats, doublons, écarts, cohérence KPI).",
    ],
    value_bullets=[
        "Données plus fiables et partage inter-services facilité.",
        "Livrables récurrents automatisés : moins de manuel, plus reproductible.",
        "Pilotage plus clair via KPIs et reporting.",
    ],
    logo_path="assets/logo_ecosystem.png",
    logo_width=110,  # adapte selon ton fichier
)

st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)

# ---------- EFS ----------
experience_card(
    title="Data Analyst Marketing (Stage)",
    company="Établissement Français du Sang (EFS) — Siège national",
    meta="Mai 2024 → Août 2024",
    summary=(
        "Analyse et reporting décisionnel autour des campagnes de don et des indicateurs nationaux, "
        "avec Power BI / Business Objects / Piano Analytics, et restitution multi-niveaux "
        "(opérationnel → direction)."
    ),
    stack_tags=["Power BI", "Business Objects", "SQL", "Piano Analytics", "Reporting"],
    left_title="Missions clés",
    left_bullets=[
        "Analyse nationale : rendez-vous, tendances, performance de campagnes.",
        "Création de rapports et dashboards (Power BI, Business Objects).",
        "Suivi de KPIs marketing et web analytics (Piano Analytics).",
    ],
    right_title="Restitution & collaboration",
    right_bullets=[
        "Reporting pour différents interlocuteurs (marketing, direction).",
        "Collaboration transverse (régions, communication, DSI).",
        "Contribution à la structuration/migration de données et aux bonnes pratiques.",
    ],
    value_bullets=[
        "Meilleure visibilité sur les indicateurs clés et aide à la décision.",
        "Analyses actionnables pour ajuster les campagnes et le pilotage.",
    ],
    # ⚠️ Streamlit gère mieux PNG/JPG que SVG selon versions. Si ton SVG pose souci, convertis en PNG.
    logo_path="assets/logo_efs.png",
    logo_width=85,
)

st.divider()

# ---------- Timeline ----------
st.markdown("### Timeline (résumé)")

t1, t2 = st.columns(2, gap="large")
with t1:
    with st.container(border=True):
        st.markdown("**2024 → fin 2025**")
        st.write("ECOSYSTEM — Alternance Data (DSI / Data Platform)")
        pills(["Databricks", "SQL", "Python", "AWS", "Power BI"])

with t2:
    with st.container(border=True):
        st.markdown("**Mai → Août 2024**")
        st.write("EFS — Stage Data Analyst Marketing (Siège national)")
        pills(["Power BI", "SQL", "Piano Analytics", "Business Objects"])
