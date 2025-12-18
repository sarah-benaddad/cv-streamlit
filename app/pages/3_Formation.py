import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Formation | Sarah Benaddad", page_icon=None, layout="wide")

st.markdown("""
<style>
.center { text-align:center; }
.small { font-size:0.95rem; opacity:0.85; }

.role { font-weight:800; font-size:1.25rem; }
.school { font-size:1.05rem; opacity:0.9; }
.meta { font-size:0.95rem; opacity:0.8; }

.pills { display:flex; flex-wrap:wrap; gap:8px; justify-content:flex-start; margin-top:10px; }
.pill {
  padding:6px 12px; border-radius:999px;
  background:#262730; border:1px solid #3a3b3f;
  font-size:0.85rem;
  line-height:1.2;
}

.spacer { height:12px; }
</style>
""", unsafe_allow_html=True)

def pills(tags):
    st.markdown(
        "<div class='pills'>" + "".join([f"<span class='pill'>{t}</span>" for t in tags]) + "</div>",
        unsafe_allow_html=True
    )

def show_logo(logo_path: str, width: int = 90):
    p = Path(logo_path)
    if p.exists():
        st.image(str(p), width=width)

def formation_card(
    title: str,
    school: str,
    meta: str,
    tags: list[str] | None = None,
    content: str | None = None,
    extra: list[str] | None = None,
    logo_path: str | None = None,
    logo_width: int = 90,
):
    with st.container(border=True):
        h1, h2 = st.columns([5, 2], gap="large")

        with h1:
            # Logo en haut (si dispo)
            if logo_path:
                show_logo(logo_path, width=logo_width)

            st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)

            # Texte descendu dans l'espace
            st.markdown(f"<div class='role'>{title}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='school'>{school}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='meta'>{meta}</div>", unsafe_allow_html=True)

        with h2:
            if tags:
                st.markdown("**Mots-clés**")
                pills(tags)

        if content:
            st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)
            st.markdown(content)

        if extra:
            st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)
            with st.expander("Détails"):
                for x in extra:
                    st.write("•", x)

# ---------- Header ----------
st.markdown("<h1 class='center'>Formation</h1>", unsafe_allow_html=True)
st.markdown("<div class='center small'>Parcours académique & certificats</div>", unsafe_allow_html=True)
st.divider()

# ---------- EFREI ----------
formation_card(
    title="Licence Ingénierie Data et Marketing",
    school="EFREI — Grande école ingénieur du numérique (Villejuif) • Panthéon Assas",
    meta="2023 → 2026",
    tags=["Data", "Marketing", "BI", "Python", "SQL"],
    content=(
        "Axes mis en avant dans mon parcours : **data marketing**, **analyse prédictive**, "
        "**Python / SQL** et **visualisation**."
    ),
    extra=[
        "Analyse et visualisation de données géospatiales : optimisation de stratégies et campagnes (ex. Uber) avec Pandas, NumPy, Plotly.",
        "Analyse de données médicales : corrélation, ACP, réseaux de neurones, arbres de décision (diabète).",
    ],
    logo_path="assets/logo_efrei.png",
    logo_width=110,
)

st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)

# ---------- Université Paris Cité ----------
formation_card(
    title="Licence 1 — Sciences fondamentales et biomédicales (ingénierie & médical)",
    school="Université Paris Cité — Saint-Germain-des-Prés",
    meta="2022 → 2023",
    tags=["Sciences", "Biomédical", "Ingénierie", "Méthode"],
    content="Année de L1 en **sciences fondamentales et biomédicales** (orientation ingénierie & médical).",
    logo_path="assets/logo_upc.png",
    logo_width=90,
)

st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)

# ---------- Bac ----------
formation_card(
    title="Baccalauréat — Mention",
    school="Lycée privé catholique LaSalle Saint-Denis",
    meta="Diplômée en 2022",
    tags=["SVT", "Physique-Chimie", "Mathématiques complémentaires"],
    content="Options : **SVT**, **Physique-Chimie**, **Mathématiques complémentaires**.",
    extra=[
        "Lauréate concours national de la Résistance et la Déportation.",
        "Participation au concours « Je filme le métier qui me plaît » (métier choisi : réalisateur).",
    ],
    logo_path="assets/logo_lasalle.png",
    logo_width=95,
)

st.divider()

# ---------- Certifications (bloc 1) ----------
st.markdown("## Certifications")
c1, c2, c3 = st.columns(3, gap="large")

with c1:
    with st.container(border=True):
        # Logo optionnel
        if Path("assets/logo_cambridge.png").exists():
            show_logo("assets/logo_cambridge.png", width=110)
            st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)

        st.markdown("### B2 First")
        st.write("Cambridge University — 2022")

with c2:
    with st.container(border=True):
        st.markdown("### TOEIC")
        st.write("En cours")

with c3:
    with st.container(border=True):
        st.markdown("### Langues")
        st.write("Anglais : avancé • Espagnol : notions")

st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)

# ---------- Certifications complémentaires ----------
st.markdown("## Certifications complémentaires")
c4, c5 = st.columns(2, gap="large")

with c4:
    with st.container(border=True):
        # Logo optionnel
        if Path("assets/logo_skills4all.png").exists():
            show_logo("assets/logo_skills4all.png", width=120)
            st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)

        st.markdown("### Attestation de réussite — Formation Back End")
        st.write("Skills4All — spécialiste du digital learning certifiant")
        st.write("Date de délivrance : octobre 2025")
        st.code("Identifiant : NTMAxsujCf", language="text")

with c5:
    with st.container(border=True):
        # Logo EFREI optionnel (déjà en haut mais ici c'est une certif EFREI)
        if Path("assets/logo_efrei.png").exists():
            show_logo("assets/logo_efrei.png", width=110)
            st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)

        st.markdown("### Bases de l’IA générative")
        st.write("EFREI Paris")
        st.write("Date de délivrance : septembre 2025")
        st.code("Identifiant : OPENBADGEPASSPORT-992803", language="text")
