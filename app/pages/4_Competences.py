import streamlit as st

st.set_page_config(page_title="Compétences | Sarah Benaddad", page_icon="", layout="wide")

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
.card-sub { font-size:0.95rem; opacity:0.85; margin-top:2px; }
.card-list { margin-top:10px; }
.card-list li { margin-bottom:6px; }
.spacer { height:14px; }

.kpi-wrap{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px;margin-top:10px;}
.kpi{border:1px solid #2e3136;border-radius:14px;padding:14px;background:rgba(255,255,255,0.02);}
.kpi .t{font-size:0.9rem;opacity:.75;margin-bottom:6px;}
.kpi .v{font-size:1.05rem;font-weight:700;line-height:1.25;word-break:break-word;}
@media (max-width: 900px){.kpi-wrap{grid-template-columns:repeat(2,minmax(0,1fr));}}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1 class='center'> Compétences</h1>", unsafe_allow_html=True)
st.markdown("<div class='center small'>Vue rapide : Data • BI • Automation • Data Platform • IA</div>", unsafe_allow_html=True)

# Quick stack (scan en 3 secondes)
st.markdown("""
<div class="pills">
  <span class="pill">Python</span>
  <span class="pill">SQL</span>
  <span class="pill">Databricks</span>
  <span class="pill">AWS (SageMaker)</span>
  <span class="pill">Athena</span>
  <span class="pill">Power BI</span>
  <span class="pill">SAP / SAP Analytics Cloud</span>
  <span class="pill">Piano Analytics</span>
  <span class="pill">Business Objects</span>
  <span class="pill">DataViz</span>
  <span class="pill">Fraude / Scoring</span>
  <span class="pill">Prévisions</span>
</div>
""", unsafe_allow_html=True)

st.divider()

# KPI cards (résumé)
st.markdown("""
<div class="kpi-wrap">
  <div class="kpi"><div class="t">Langages</div><div class="v">Python • SQL</div></div>
  <div class="kpi"><div class="t">Data Platform</div><div class="v">Databricks • Athena • AWS</div></div>
  <div class="kpi"><div class="t">BI / Reporting</div><div class="v">Power BI • SAC • BO</div></div>
  <div class="kpi"><div class="t">Méthodes</div><div class="v">Agile/SCRUM • Design Thinking</div></div>
</div>
""", unsafe_allow_html=True)

st.divider()

# 2 colonnes (cards)
left, right = st.columns(2, gap="large")

with left:
    with st.container(border=True):
        st.markdown("### Python (data & automation)")
        st.markdown("<div class='card-sub'>Traitement, automatisation, analyse & scripts</div>", unsafe_allow_html=True)
        st.markdown("""
<ul class="card-list">
  <li>Manipulation & nettoyage : <b>Pandas, NumPy</b></li>
  <li>Automatisation : scripts récurrents, exports, contrôles qualité</li>
  <li>Analyse : KPI, segmentation, signaux faibles, explorations</li>
  <li>Prévisions / ML (selon projets) : bases scikit-learn</li>
</ul>
""", unsafe_allow_html=True)
        st.markdown("""
<div class="pills">
  <span class="pill">Pandas</span><span class="pill">NumPy</span><span class="pill">logging</span>
  <span class="pill">datetime</span><span class="pill">requests</span><span class="pill">scikit-learn</span>
</div>
""", unsafe_allow_html=True)

    st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)

    with st.container(border=True):
        st.markdown("### BI & DataViz")
        st.markdown("<div class='card-sub'>Dashboards, KPIs, pilotage & restitution</div>", unsafe_allow_html=True)
        st.markdown("""
<ul class="card-list">
  <li>Création de dashboards & reporting décisionnel</li>
  <li>Modélisation d’indicateurs, suivi d’activité, analyses de tendances</li>
  <li>Restitution claire : data storytelling & synthèses actionnables</li>
</ul>
""", unsafe_allow_html=True)
        st.markdown("""
<div class="pills">
  <span class="pill">Power BI</span><span class="pill">SAP Analytics Cloud</span>
  <span class="pill">Business Objects</span><span class="pill">Tableau</span><span class="pill">QlikSense</span>
</div>
""", unsafe_allow_html=True)

with right:
    with st.container(border=True):
        st.markdown("### SQL & Data Platform")
        st.markdown("<div class='card-sub'>Requêtes analytiques, transformation & mise à disposition</div>", unsafe_allow_html=True)
        st.markdown("""
<ul class="card-list">
  <li>SQL : <b>JOIN, CTE, agrégations</b> (+ fenêtrage si besoin)</li>
  <li>Préparation de datasets pour BI / analyses / exports</li>
  <li>Plateforme data : centralisation, structuration, gouvernance</li>
</ul>
""", unsafe_allow_html=True)
        st.markdown("""
<div class="pills">
  <span class="pill">Databricks</span><span class="pill">Athena</span><span class="pill">SQL</span>
</div>
""", unsafe_allow_html=True)

    st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)

    with st.container(border=True):
        st.markdown("### Cloud & industrialisation")
        st.markdown("<div class='card-sub'>Automatisation, exécution et fiabilisation des traitements</div>", unsafe_allow_html=True)
        st.markdown("""
<ul class="card-list">
  <li>Automatisation de traitements et exécutions (scripts, runs)</li>
  <li>Fiabilisation : reproductibilité, standardisation des livrables</li>
  <li>Qualité des données : contrôles, détection d’anomalies</li>
</ul>
""", unsafe_allow_html=True)
        st.markdown("""
<div class="pills">
  <span class="pill">AWS (SageMaker)</span><span class="pill">Automation</span><span class="pill">Data Quality</span>
</div>
""", unsafe_allow_html=True)

st.divider()

# 3 cards bas (domaines)
c1, c2, c3 = st.columns(3, gap="large")

with c1:
    with st.container(border=True):
        st.markdown("### Analyse fraude & conformité")
        st.markdown("""
<ul class="card-list">
  <li>Détection d’anomalies (volumes, historiques, incohérences)</li>
  <li>Règles de scoring / signaux faibles</li>
  <li>Support à la décision & priorisation des contrôles</li>
</ul>
""", unsafe_allow_html=True)

with c2:
    with st.container(border=True):
        st.markdown("### Marketing analytics")
        st.markdown("""
<ul class="card-list">
  <li>Analyse de performance de campagnes</li>
  <li>Web analytics & suivi d’indicateurs</li>
  <li>Reporting pour différents niveaux (opérationnel → direction)</li>
</ul>
""", unsafe_allow_html=True)
        st.markdown("<div class='pills'><span class='pill'>Piano Analytics</span><span class='pill'>KPI</span></div>", unsafe_allow_html=True)

with c3:
    with st.container(border=True):
        st.markdown("### Méthodes & produit")
        st.markdown("""
<ul class="card-list">
  <li>Agile / SCRUM • Waterfall</li>
  <li>Design Thinking : besoin utilisateur → prototypage → itérations</li>
  <li>Travail transverse & communication (équipes techniques / métiers)</li>
</ul>
""", unsafe_allow_html=True)
        st.markdown("<div class='pills'><span class='pill'>Agile</span><span class='pill'>SCRUM</span><span class='pill'>Design Thinking</span></div>", unsafe_allow_html=True)

st.markdown("<div class='spacer'></div>", unsafe_allow_html=True)

# Bonus : Web / design (optionnel mais utile)
with st.expander("➕ Autres compétences (web / design / outils)"):
    st.markdown("""
- **Web & prototypage** : WordPress, Bootstrap, HTML/CSS, Figma, PHP  
- **Bureautique** : Excel, PowerPoint, Word  
- **Langues** : Français (natif), Anglais (avancé), Espagnol (notions)
""")
