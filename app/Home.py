import streamlit as st
from pathlib import Path

st.set_page_config(page_title="CV | Sarah Benaddad", page_icon="📄", layout="wide")

# ======================
# PATHS (ROBUSTES CLOUD)
# ======================
APP_DIR = Path(__file__).resolve().parent        # .../app
ASSETS_DIR = APP_DIR / "assets"
PHOTO_PATH = ASSETS_DIR / "photo.jpg"
PDF_PATH = ASSETS_DIR / "Cv_alternance.pdf"

# ---------- CSS ----------
st.markdown("""
<style>
.center { text-align:center; }
.small { font-size:0.95rem; opacity:0.85; }

.pills { display:flex; flex-wrap:wrap; gap:8px; justify-content:center; margin-top:10px; }
.pill {
  padding:6px 12px; border-radius:999px;
  background:#262730; border:1px solid #3a3b3f;
  font-size:0.85rem;
}

.hero-title { font-weight: 900; font-size: 2rem; line-height: 1.1; }
.hero-sub { font-size: 1.05rem; opacity: 0.9; margin-top: 8px; }

.kpi-wrap{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;margin-top:14px;}
.kpi{border:1px solid #2e3136;border-radius:14px;padding:14px;background:rgba(255,255,255,0.02);}
.kpi .t{font-size:0.9rem;opacity:.75;margin-bottom:6px;}
.kpi .v{font-size:1.05rem;font-weight:700;line-height:1.25;word-break:break-word;}
@media (max-width: 900px){.kpi-wrap{grid-template-columns:repeat(1,minmax(0,1fr));}}

.spacer { height: 12px; }
</style>
""", unsafe_allow_html=True)

# ---------- Sidebar ----------
with st.sidebar:
    st.title("Sarah Benaddad")
    st.caption("Alternance Data • 2026–2027")
    st.write("Le Kremlin-Bicêtre")
    st.write("sarah.benaddad@hotmail.com")
    st.divider()
    st.link_button("LinkedIn", "https://www.linkedin.com/in/sarah-benaddad-876483250")
    st.link_button("GitHub", "https://github.com/sarah-benaddad")
    st.link_button("Email", "mailto:sarah.benaddad@hotmail.com")

# ---------- HERO ----------
left, right = st.columns([1, 2], gap="large")

with left:
    # Photo (cloud-safe)
    if PHOTO_PATH.exists():
        # Qualité meilleure
        st.image(str(PHOTO_PATH), width=180, output_format="PNG")
    else:
        with st.container(border=True):
            st.write("Ajoute une photo : `app/assets/photo.jpg` (optionnel)")

    st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)

    # Boutons sous la photo
    b1, b2, b3 = st.columns(3)
    with b1:
        st.link_button("LinkedIn", "https://www.linkedin.com/in/sarah-benaddad-876483250")
    with b2:
        st.link_button("GitHub", "https://github.com/sarah-benaddad")
    with b3:
        st.link_button("Email", "mailto:sarah.benaddad@hotmail.com")

    st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)

    # Télécharger CV (cloud-safe)
    if PDF_PATH.exists():
        st.download_button(
            label="⬇️ Télécharger mon CV (PDF)",
            data=PDF_PATH.read_bytes(),
            file_name="Sarah_Benaddad_CV.pdf",
            mime="application/pdf",
            use_container_width=True
        )
    else:
        st.warning("Ajoute ton PDF dans `app/assets/Cv_alternance.pdf`")

with right:
    st.markdown("<div class='hero-title'>Sarah Benaddad</div>", unsafe_allow_html=True)
    st.markdown("<div class='hero-sub'>Data Analyst / Data Scientist • BI • Automatisation • SQL Databricks • Python</div>", unsafe_allow_html=True)
    st.markdown("<div class='small'>Le Kremlin-Bicêtre / Île-de-France • sarah.benaddad@hotmail.com</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="pills">
      <span class="pill">Python</span>
      <span class="pill">SQL</span>
      <span class="pill">Databricks</span>
      <span class="pill">AWS (SageMaker)</span>
      <span class="pill">Power BI</span>
      <span class="pill">Fraude / Scoring</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)

    st.info("Recherche d’une alternance en **Data** (septembre 2026 → août 2027) | Rythme : 2 semaines entreprise / 1 semaine cours")

st.divider()

# ---------- En un coup d’œil ----------
st.markdown("## En un coup d’œil")
st.markdown("""
<div class="kpi-wrap">
  <div class="kpi"><div class="t">Ce que je fais</div><div class="v">Plateforme data • Pipelines • Reporting</div></div>
  <div class="kpi"><div class="t">Ce que j’aime</div><div class="v">Automatisation • Qualité data • IA appliquée</div></div>
  <div class="kpi"><div class="t">Secteurs</div><div class="v">Impact • Santé publique • Économie circulaire</div></div>
</div>
""", unsafe_allow_html=True)

st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)

# ---------- Pitch ----------
st.markdown("## Pitch")
st.write(
    "Je travaille sur des sujets data à la croisée du **métier** et de la **tech** : "
    "construction de datasets, automatisations Python, SQL sur Databricks, et restitution BI. "
    "J’aime les projets où la donnée sert un **pilotage concret** (qualité, fraude, prévisions) "
    "et où l’on peut livrer des résultats clairs et actionnables."
)

st.divider()

# ---------- Ce que je recherche ----------
st.markdown("## Ce que je recherche")
c1, c2 = st.columns(2, gap="large")

with c1:
    with st.container(border=True):
        st.markdown("### Alternance Data (2026–2027)")
        st.write("Septembre 2026 → Août 2027")
        st.write("Rythme : 2 semaines entreprise / 1 semaine cours")
        st.write("Île-de-France (ou hybride)")

with c2:
    with st.container(border=True):
        st.markdown("### Types de missions")
        st.markdown("""
- Data analysis / BI (KPI, dashboards, reporting)
- Data platform / analytics engineering (SQL, pipelines, qualité data)
- Automatisation Python / industrialisation (cloud, exécutions récurrentes)
- IA appliquée : scoring, détection d’anomalies, prévisions
""")

st.divider()

# ---------- Soft skills & Langues ----------
st.markdown("## Soft skills & Langues")
s1, s2 = st.columns(2, gap="large")

with s1:
    with st.container(border=True):
        st.markdown("### Soft skills")
        st.markdown("""
- Autonome, rigoureuse, orientée résultats  
- Bon relationnel (DSI ↔ métiers), capacité de vulgarisation  
- Esprit d’analyse, sens du détail (data quality)
""")

with s2:
    with st.container(border=True):
        st.markdown("### Langues")
        st.markdown("""
- Français : natif  
- Anglais : avancé  
- Espagnol : notions
""")
