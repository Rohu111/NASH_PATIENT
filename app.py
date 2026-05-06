import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime, timedelta
import random

# ─── PAGE CONFIG ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Nash · Patient Portal",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ─── CSS — CLEAN WHITE THEME ──────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@300;400;600;700;800;900&family=Lato:wght@300;400;700&display=swap');

html, body, * { font-family: 'Lato', sans-serif; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 1rem 2rem 2rem 2rem; background: #FFFFFF; }
.stApp { background: #FFFFFF !important; }
.stApp > div { background: #FFFFFF !important; }

:root {
    --rose:    #D94F45;
    --rose-lt: #FDF0EF;
    --rose-dk: #B03830;
    --teal:    #0D8A82;
    --teal-lt: #E8F6F5;
    --teal-dk: #096E68;
    --peach:   #E07840;
    --peach-lt:#FDF1E8;
    --cream:   #FFFFFF;
    --sand:    #F7F8FA;
    --text:    #111827;
    --text-sec:#4B5563;
    --success: #16A34A;
    --warning: #D97706;
    --danger:  #DC2626;
    --white:   #FFFFFF;
    --border:  #E5E7EB;
}

.nav-wrap {
    background: linear-gradient(120deg, #E8837A 0%, #F5A67D 50%, #F5C6A0 100%);
    border-radius: 20px;
    padding: 1.2rem 2rem;
    margin-bottom: 1.5rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-shadow: 0 8px 30px rgba(232,131,122,0.3);
}

.nav-logo {
    font-family: 'Nunito', sans-serif;
    font-size: 1.9rem;
    font-weight: 900;
    color: white;
}

.nav-sub {
    font-size: 0.78rem;
    color: rgba(255,255,255,0.85);
}

.nav-user {
    background: rgba(255,255,255,0.25);
    border-radius: 40px;
    padding: 0.5rem 1.1rem;
    color: white;
    font-size: 0.85rem;
    font-weight: 700;
}

.vital-card {
    background: #FFFFFF;
    border-radius: 18px;
    padding: 1.2rem 1.3rem;
    box-shadow: 0 2px 12px rgba(0,0,0,0.06);
    border: 1.5px solid var(--border);
    position: relative;
    overflow: hidden;
}

.vital-card-icon {
    font-size: 2rem;
    margin-bottom: 0.4rem;
}

.vital-label {
    font-size: 0.7rem;
    font-weight: 700;
    text-transform: uppercase;
    color: var(--text-sec);
}

.vital-value {
    font-family: 'Nunito', sans-serif;
    font-size: 2rem;
    font-weight: 900;
    color: var(--text);
}

.vital-unit {
    font-size: 0.8rem;
    color: var(--text-sec);
}

.vital-badge {
    display: inline-block;
    padding: 0.18rem 0.6rem;
    border-radius: 20px;
    font-size: 0.68rem;
    font-weight: 700;
    margin-top: 0.35rem;
}

.badge-normal  { background: #E8F5ED; color: #3A8F5A; }
.badge-warning { background: #FEF8E7; color: #C07800; }
.badge-danger  { background: #FDECEC; color: #C03030; }

.sec-head {
    font-family: 'Nunito', sans-serif;
    font-size: 1.15rem;
    font-weight: 800;
    color: var(--text);
    margin: 1.4rem 0 0.8rem 0;
}

.live-pill {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    background: #F0FDF4;
    color: #16A34A;
    border: 1px solid #BBF7D0;
    padding: 0.3rem 0.8rem;
    border-radius: 20px;
    font-size: 0.72rem;
    font-weight: 700;
}

.pulse-dot {
    width: 7px;
    height: 7px;
    background: #16A34A;
    border-radius: 50%;
    display: inline-block;
    animation: blink 1.4s infinite;
}

@keyframes blink {
    0%,100% { opacity:1; transform:scale(1) }
    50% { opacity:0.4; transform:scale(1.4) }
}

.stTabs [data-baseweb="tab-list"] {
    gap: 6px;
    background: #F3F4F6;
    border-radius: 14px;
    padding: 5px;
    border: 1px solid var(--border);
}

.stTabs [data-baseweb="tab"] {
    border-radius: 10px;
    padding: 0.45rem 1.1rem;
    font-weight: 700;
}

.stTabs [aria-selected="true"] {
    background: var(--teal) !important;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

# ─── MOCK DATA ─────────────────────────────────────────────────────────────────
def gen_vitals(days=14):
    dates = [datetime.now() - timedelta(days=i, hours=random.randint(0,10)) for i in range(days)]
    dates.reverse()

    return pd.DataFrame({
        "datetime": dates,
        "temperature": [round(random.uniform(36.2, 38.6), 1) for _ in range(days)],
        "heart_rate": [random.randint(60, 112) for _ in range(days)],
        "spo2": [random.randint(93, 100) for _ in range(days)],
        "bp_sys": [random.randint(110, 148) for _ in range(days)],
        "bp_dia": [random.randint(70, 95) for _ in range(days)],
    })

vdf = gen_vitals()
latest = vdf.iloc[-1]

# ─── STATUS FUNCTIONS ─────────────────────────────────────────────────────────
def get_status(value, low, high):
    if low <= value <= high:
        return "Normal"
    elif value > high:
        return "Warning"
    else:
        return "danger"

temp_s = get_status(latest['temperature'], 36.1, 37.2)
hr_s   = get_status(latest['heart_rate'], 60, 100)
spo2_s = get_status(latest['spo2'], 95, 100)
bp_s   = get_status(latest['bp_sys'], 90, 120)

# ─── VITAL CARD ────────────────────────────────────────────────────────────────
def vc(icon, label, val, unit, status):

    badge_cls = {
        "Normal": "badge-normal",
        "Warning": "badge-warning",
        "danger": "badge-danger"
    }.get(status, "badge-normal")

    return f"""
    <div class="vital-card">
      <div class="vital-card-icon">{icon}</div>

      <div class="vital-label">{label}</div>

      <div class="vital-value">
        {val}
        <span class="vital-unit">{unit}</span>
      </div>

      <div>
        <span class="vital-badge {badge_cls}">
          {status}
        </span>
      </div>
    </div>
    """

# ─── FIXED CHART FUNCTION ─────────────────────────────────────────────────────
def warm_chart(df, col, color, title,
               ymin=None,
               ymax=None,
               hlines=[]):

    # HEX → RGBA converter
    def hex_to_rgba(hex_color, alpha=0.15):

        hex_color = hex_color.lstrip('#')

        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)

        return f'rgba({r},{g},{b},{alpha})'

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df['datetime'],
        y=df[col],

        mode='lines+markers',

        line=dict(
            color=color,
            width=2.5
        ),

        marker=dict(
            size=5,
            color=color
        ),

        fill='tozeroy',

        # FINAL FIX
        fillcolor=hex_to_rgba(color, 0.15)
    ))

    # Reference lines
    for val, lbl, lcolor in hlines:

        fig.add_hline(
            y=val,

            line_dash="dot",

            line_color=lcolor,

            annotation_text=lbl,

            annotation_font_size=10
        )

    fig.update_layout(

        title=dict(
            text=title,

            font=dict(
                family='Nunito',
                size=13,
                color='#2D2D2D'
            )
        ),

        height=260,

        plot_bgcolor='#FFFFFF',
        paper_bgcolor='white',

        margin=dict(
            l=10,
            r=10,
            t=40,
            b=10
        ),

        font=dict(
            family='Lato'
        ),

        showlegend=False,

        xaxis=dict(
            showgrid=False
        ),

        yaxis=dict(
            gridcolor='#F5EFE6',

            # FIXED RANGE CONDITION
            range=[ymin, ymax]
            if ymin is not None and ymax is not None
            else None
        )
    )

    return fig

# ─── NAVBAR ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="nav-wrap">
  <div>
    <div class="nav-logo">🌿 Nash · Patient Portal</div>
    <div class="nav-sub">Your Health. Your Control.</div>
  </div>

  <div class="nav-user">
    👤 Arjun Krishnan
  </div>
</div>
""", unsafe_allow_html=True)

# ─── TABS ──────────────────────────────────────────────────────────────────────
tab1, tab2 = st.tabs([
    "🏠 Home",
    "📡 My Vitals"
])

# ─── TAB 1 ────────────────────────────────────────────────────────────────────
with tab1:

    st.markdown(
        '<div class="live-pill"><span class="pulse-dot"></span> NASH ROBOT ACTIVE</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sec-head">📡 Latest Vitals</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(
            vc("🌡️", "Temperature",
               latest['temperature'],
               "°C",
               temp_s),
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            vc("💓", "Heart Rate",
               int(latest['heart_rate']),
               "bpm",
               hr_s),
            unsafe_allow_html=True
        )

    with c3:
        st.markdown(
            vc("🫁", "SpO₂",
               int(latest['spo2']),
               "%",
               spo2_s),
            unsafe_allow_html=True
        )

    with c4:
        st.markdown(
            vc("🩺", "Blood Pressure",
               f"{int(latest['bp_sys'])}/{int(latest['bp_dia'])}",
               "mmHg",
               bp_s),
            unsafe_allow_html=True
        )

# ─── TAB 2 ────────────────────────────────────────────────────────────────────
with tab2:

    st.markdown(
        '<div class="sec-head">📊 14-Day History Charts</div>',
        unsafe_allow_html=True
    )

    ch1, ch2 = st.columns(2)

    with ch1:

        st.plotly_chart(
            warm_chart(
                vdf,
                'heart_rate',
                '#E8837A',
                '💓 Heart Rate (bpm)',

                hlines=[
                    (100, 'Max Normal', '#F0A500'),
                    (60, 'Min Normal', '#5DB075')
                ]
            ),

            use_container_width=True
        )

    with ch2:

        st.plotly_chart(
            warm_chart(
                vdf,
                'temperature',
                '#F5A67D',
                '🌡️ Temperature (°C)',

                hlines=[
                    (37.2, 'Fever Threshold', '#E05C5C')
                ]
            ),

            use_container_width=True
        )

    ch3, ch4 = st.columns(2)

    with ch3:

        st.plotly_chart(
            warm_chart(
                vdf,
                'spo2',
                '#4EADA8',
                '🫁 SpO₂ (%)',

                ymin=88,
                ymax=102,

                hlines=[
                    (95, 'Min Normal', '#F0A500')
                ]
            ),

            use_container_width=True
        )

    with ch4:

        fig_bp = go.Figure()

        fig_bp.add_trace(go.Scatter(
            x=vdf['datetime'],
            y=vdf['bp_sys'],

            mode='lines+markers',

            name='Systolic',

            line=dict(
                color='#E8837A',
                width=2.5
            ),

            marker=dict(size=5)
        ))

        fig_bp.add_trace(go.Scatter(
            x=vdf['datetime'],
            y=vdf['bp_dia'],

            mode='lines+markers',

            name='Diastolic',

            line=dict(
                color='#4EADA8',
                width=2.5
            ),

            marker=dict(size=5)
        ))

        fig_bp.add_hline(
            y=120,
            line_dash="dot",
            line_color="#F0A500",
            annotation_text="Target"
        )

        fig_bp.update_layout(

            title=dict(
                text='🩺 Blood Pressure (mmHg)',

                font=dict(
                    family='Nunito',
                    size=13,
                    color='#2D2D2D'
                )
            ),

            height=260,

            plot_bgcolor='#FFFFFF',
            paper_bgcolor='white',

            margin=dict(
                l=10,
                r=10,
                t=40,
                b=10
            ),

            font=dict(
                family='Lato'
            ),

            xaxis=dict(
                showgrid=False
            ),

            yaxis=dict(
                gridcolor='#F5EFE6'
            ),

            legend=dict(
                orientation='h'
            )
        )

        st.plotly_chart(
            fig_bp,
            use_container_width=True
        )

    # ─── TABLE ────────────────────────────────────────────────────────────────
    st.markdown(
        '<div class="sec-head">🗂️ Scan History Log</div>',
        unsafe_allow_html=True
    )

    disp = vdf.copy()

    disp['datetime'] = disp['datetime'].dt.strftime(
        "%d %b %Y  %I:%M %p"
    )

    disp.columns = [
        "Date & Time",
        "Temp (°C)",
        "Heart Rate",
        "SpO₂ (%)",
        "BP Sys",
        "BP Dia"
    ]

    st.dataframe(
        disp.iloc[::-1].reset_index(drop=True),
        use_container_width=True,
        height=260
    )

# ─── FOOTER ───────────────────────────────────────────────────────────────────
st.markdown("""
<div style="
text-align:center;
padding:1.5rem 0 0.5rem 0;
font-size:0.72rem;
color:#7A7A8C;
border-top:1px solid #EDE8E1;
margin-top:2rem;
">

🌿 Nash Patient Portal · Built with ❤️ using Streamlit

</div>
""", unsafe_allow_html=True)
