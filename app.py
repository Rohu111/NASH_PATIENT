# ──────────────────────────────────────────────────────────────────────────────
# 🔥 FUTURISTIC NASH UI THEME
# Replace your current st.markdown("""<style>....</style>""")
# with this complete upgraded version
# ──────────────────────────────────────────────────────────────────────────────

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&display=swap');

/* GLOBAL */
html, body, * {
    font-family: 'Outfit', sans-serif;
}

body {
    background: linear-gradient(135deg, #07111F 0%, #0B172A 45%, #101C33 100%);
    color: #EAF4FF;
}

#MainMenu, footer, header {
    visibility: hidden;
}

.block-container {
    padding: 1rem 2rem 2rem 2rem;
}

/* ROOT COLORS */
:root {
    --primary: #00E5FF;
    --primary-dark: #0099CC;
    --secondary: #7C4DFF;
    --accent: #00FFA3;
    --danger: #FF4D6D;
    --warning: #FFB703;

    --bg-dark: #07111F;
    --card-bg: rgba(17, 25, 40, 0.72);
    --glass: rgba(255,255,255,0.08);
    --border: rgba(255,255,255,0.12);

    --text: #EAF4FF;
    --text-soft: #AFC6E0;
}

/* ANIMATED GLOW BACKGROUND */
.bg-glow {
    position: fixed;
    top: -180px;
    right: -180px;
    width: 500px;
    height: 500px;
    background: radial-gradient(circle,
        rgba(0,229,255,0.16),
        transparent 70%);
    z-index: -1;
}

.bg-glow2 {
    position: fixed;
    bottom: -220px;
    left: -180px;
    width: 500px;
    height: 500px;
    background: radial-gradient(circle,
        rgba(124,77,255,0.18),
        transparent 70%);
    z-index: -1;
}

/* NAVBAR */
.nav-wrap {
    background: linear-gradient(135deg,
        #00E5FF 0%,
        #7C4DFF 100%);
    border-radius: 24px;
    padding: 1.3rem 2rem;
    margin-bottom: 1.5rem;

    display: flex;
    align-items: center;
    justify-content: space-between;

    box-shadow: 0 10px 40px rgba(0,229,255,0.35);

    border: 1px solid rgba(255,255,255,0.15);
}

.nav-logo {
    font-size: 2rem;
    font-weight: 900;
    color: white;
    letter-spacing: -0.5px;
}

.nav-sub {
    color: rgba(255,255,255,0.85);
    font-size: 0.78rem;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.nav-user {
    background: rgba(255,255,255,0.12);
    border-radius: 40px;
    padding: 0.55rem 1.2rem;

    display: flex;
    align-items: center;
    gap: 0.6rem;

    border: 1px solid rgba(255,255,255,0.15);

    backdrop-filter: blur(10px);

    color: white;
    font-weight: 700;
}

/* GLASS CARDS */
.vital-card,
.appt-card,
.report-row,
.profile-card,
.summary-box,
.sug-card,
.side-nav {

    background: rgba(17, 25, 40, 0.72);

    backdrop-filter: blur(18px);

    border: 1px solid rgba(255,255,255,0.10);

    box-shadow:
        0 8px 32px rgba(0,0,0,0.35);

    color: white;
}

/* PROFILE CARD */
.profile-card {
    border-radius: 24px;
    padding: 1.5rem;
    text-align: center;
}

.profile-avatar {
    width: 80px;
    height: 80px;

    border-radius: 50%;

    background: linear-gradient(
        135deg,
        #00E5FF,
        #7C4DFF
    );

    display: flex;
    align-items: center;
    justify-content: center;

    margin: auto;

    font-size: 2rem;

    box-shadow:
        0 0 25px rgba(0,229,255,0.45);
}

.profile-name {
    font-size: 1.3rem;
    font-weight: 900;
    color: white;
}

.profile-meta {
    color: var(--text-soft);
    font-size: 0.8rem;
}

/* SECTION HEADERS */
.sec-head {
    font-size: 1.15rem;
    font-weight: 800;

    color: var(--primary);

    display: flex;
    align-items: center;
    gap: 0.5rem;

    margin: 1.2rem 0 0.8rem 0;
}

.sec-line {
    flex: 1;
    height: 2px;

    background: linear-gradient(
        90deg,
        var(--primary),
        transparent
    );
}

/* VITAL CARDS */
.vital-card {
    border-radius: 22px;
    padding: 1.2rem;
    position: relative;
    overflow: hidden;

    transition: 0.3s ease;
}

.vital-card:hover {
    transform: translateY(-5px);

    box-shadow:
        0 10px 40px rgba(0,229,255,0.22);
}

.vital-card-icon {
    font-size: 2rem;
    margin-bottom: 0.5rem;
}

.vital-label {
    font-size: 0.72rem;
    font-weight: 700;

    color: var(--text-soft);

    text-transform: uppercase;
    letter-spacing: 1px;
}

.vital-value {
    font-size: 2.2rem;
    font-weight: 900;

    color: white;
}

.vital-unit {
    font-size: 0.85rem;
    color: var(--text-soft);
}

.vital-accent {
    position: absolute;
    top: 0;
    right: 0;

    width: 70px;
    height: 70px;

    border-radius: 0 20px 0 70px;

    opacity: 0.20;
}

/* BADGES */
.vital-badge {
    display: inline-block;

    padding: 0.22rem 0.7rem;

    border-radius: 30px;

    font-size: 0.68rem;
    font-weight: 700;

    margin-top: 0.45rem;
}

.badge-normal {
    background: rgba(0,255,163,0.14);
    color: #00FFA3;
}

.badge-warning {
    background: rgba(255,183,3,0.14);
    color: #FFB703;
}

.badge-danger {
    background: rgba(255,77,109,0.14);
    color: #FF4D6D;
}

/* LIVE STATUS */
.live-pill {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;

    background: rgba(0,255,163,0.12);

    color: #00FFA3;

    padding: 0.35rem 0.85rem;

    border-radius: 30px;

    border: 1px solid rgba(0,255,163,0.2);

    backdrop-filter: blur(8px);

    font-size: 0.74rem;
    font-weight: 700;
}

.pulse-dot {
    width: 8px;
    height: 8px;

    background: #00FFA3;

    border-radius: 50%;

    animation: pulse 1.4s infinite;
}

@keyframes pulse {
    0%,100% {
        opacity: 1;
        transform: scale(1);
    }

    50% {
        opacity: 0.5;
        transform: scale(1.5);
    }
}

/* APPOINTMENT CARDS */
.appt-card {
    border-radius: 18px;

    padding: 1rem 1.2rem;

    margin-bottom: 0.7rem;

    display: flex;
    align-items: center;
    gap: 1rem;

    transition: 0.3s ease;
}

.appt-card:hover {
    transform: translateY(-4px);

    box-shadow:
        0 8px 28px rgba(0,229,255,0.18);
}

.appt-avatar {
    width: 48px;
    height: 48px;

    border-radius: 50%;

    background: linear-gradient(
        135deg,
        #00E5FF,
        #7C4DFF
    );

    display: flex;
    align-items: center;
    justify-content: center;

    font-size: 1.3rem;
}

.appt-name {
    font-weight: 700;
    color: white;
}

.appt-spec {
    font-size: 0.76rem;
    color: var(--text-soft);
}

.appt-time {
    font-size: 0.75rem;
    color: #00E5FF;
}

/* PILLS */
.pill {
    display: inline-block;

    padding: 0.25rem 0.7rem;

    border-radius: 30px;

    font-size: 0.72rem;
    font-weight: 700;
}

.pill-green {
    background: rgba(0,255,163,0.12);
    color: #00FFA3;
}

.pill-red {
    background: rgba(255,77,109,0.12);
    color: #FF4D6D;
}

.pill-teal {
    background: rgba(0,229,255,0.12);
    color: #00E5FF;
}

.pill-rose {
    background: rgba(124,77,255,0.14);
    color: #B388FF;
}

.pill-peach {
    background: rgba(255,183,3,0.12);
    color: #FFB703;
}

/* SUMMARY BOX */
.summary-box {
    border-radius: 18px;
    padding: 1rem 1.2rem;
}

/* REPORT ROW */
.report-row {
    border-radius: 16px;
    padding: 1rem 1.2rem;

    margin-bottom: 0.7rem;

    display: flex;
    justify-content: space-between;
    align-items: center;
}

/* TABS */
.stTabs [data-baseweb="tab-list"] {

    background: rgba(255,255,255,0.06);

    border-radius: 16px;

    padding: 6px;

    gap: 6px;
}

.stTabs [data-baseweb="tab"] {

    border-radius: 12px;

    padding: 0.5rem 1.2rem;

    color: var(--text-soft);

    font-weight: 700;
}

.stTabs [aria-selected="true"] {

    background: linear-gradient(
        135deg,
        #00E5FF,
        #7C4DFF
    ) !important;

    color: white !important;
}

/* BUTTONS */
button[kind="primary"],
.stButton > button {

    background: linear-gradient(
        135deg,
        #00E5FF,
        #7C4DFF
    ) !important;

    border: none !important;

    border-radius: 14px !important;

    color: white !important;

    font-weight: 700 !important;

    padding: 0.65rem 1.3rem !important;

    transition: 0.3s ease !important;

    box-shadow:
        0 5px 20px rgba(0,229,255,0.25);
}

.stButton > button:hover {

    transform: scale(1.03);

    box-shadow:
        0 8px 30px rgba(124,77,255,0.35);
}

/* DATAFRAME */
[data-testid="stDataFrame"] {

    background: rgba(255,255,255,0.04);

    border-radius: 16px;

    border: 1px solid rgba(255,255,255,0.08);
}

/* DIVIDER */
.warm-div {

    height: 2px;

    background: linear-gradient(
        90deg,
        rgba(0,229,255,0.5),
        transparent
    );

    margin: 1rem 0;
}

/* FOOTER */
.footer {
    color: var(--text-soft);
}

</style>
""", unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────────────────────────
# ADD THIS BELOW CSS
# ──────────────────────────────────────────────────────────────────────────────

st.markdown("""
<div class='bg-glow'></div>
<div class='bg-glow2'></div>
""", unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────────────────────────
# UPDATE YOUR CHARTS
# Replace:
# plot_bgcolor='white'
# paper_bgcolor='white'
#
# WITH:
# ──────────────────────────────────────────────────────────────────────────────

plot_bgcolor='#101C33'
paper_bgcolor='#101C33'

# ALSO ADD:
font=dict(color='#EAF4FF')

# ──────────────────────────────────────────────────────────────────────────────
# DONE ✅
# ──────────────────────────────────────────────────────────────────────────────
