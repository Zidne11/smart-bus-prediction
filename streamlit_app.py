import streamlit as st

# -----------------------------
# Smart Bus Prediction App
# -----------------------------

st.set_page_config(
    page_title="Smart Bus Prediction",
    page_icon="🚌",
    layout="wide"
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@500;600;700;800&display=swap');

    :root {
        --ink: #172c3b;
        --muted: #617381;
        --teal: #087f78;
        --teal-dark: #05645f;
        --paper: #f4f8f7;
        --line: #dce8e5;
    }
    .stApp {
        background: radial-gradient(ellipse at 85% 2%, #dcefeb 0, transparent 35%),
                    linear-gradient(180deg, #f7faf9 0%, #eef5f3 100%);
        color: var(--ink);
        font-family: 'DM Sans', sans-serif;
    }
    .block-container {
        max-width: 1160px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }
    h1, h2, h3, [data-testid="stMetricLabel"] {
        font-family: 'Manrope', sans-serif;
        color: var(--ink);
    }
    .hero {
        position: relative;
        overflow: hidden;
        padding: 2.2rem 2.4rem;
        margin: 0 0 1.5rem;
        border: 1px solid #d7e9e5;
        border-radius: 14px;
        background: linear-gradient(115deg, #ffffff 0%, #e8f5f1 68%, #d9efea 100%);
        box-shadow: 0 12px 32px rgba(26, 64, 68, .07);
    }
    .hero:after {
        content: 'BUS';
        position: absolute;
        right: 2rem;
        bottom: -2.6rem;
        color: rgba(8, 127, 120, .07);
        font: 800 9rem/1 'Manrope', sans-serif;
        letter-spacing: 0;
        pointer-events: none;
    }
    .hero-kicker, .section-kicker {
        color: var(--teal-dark);
        font-size: .76rem;
        font-weight: 700;
        letter-spacing: .08em;
        text-transform: uppercase;
    }
    .hero h1 {
        max-width: 720px;
        margin: .55rem 0 .4rem;
        font-size: clamp(1.8rem, 4vw, 2.65rem);
        line-height: 1.15;
    }
    .hero p { max-width: 640px; margin: 0; color: var(--muted); font-size: 1rem; }
    .section-title { margin: 1.8rem 0 .2rem; font-size: 1.45rem; }
    .section-copy { margin: 0 0 1rem; color: var(--muted); }
    [data-testid="stVerticalBlockBorderWrapper"] {
        border-color: var(--line);
        border-radius: 10px;
        background: rgba(255, 255, 255, .84);
        box-shadow: 0 5px 18px rgba(26, 64, 68, .045);
    }
    [data-testid="stWidgetLabel"] label { color: #294451; font-weight: 600; }
    div[data-baseweb="select"] > div, div[data-baseweb="input"] > div {
        border-color: #cddbd8;
        border-radius: 7px;
        background-color: #fff;
    }
    div[data-testid="stSlider"] [data-baseweb="slider"] { padding-top: .35rem; }
    .stButton > button {
        min-height: 3.35rem;
        border: 0;
        border-radius: 8px;
        background: linear-gradient(100deg, var(--teal-dark), #0a9187);
        color: #fff;
        font-family: 'Manrope', sans-serif;
        font-size: 1.08rem;
        font-weight: 700;
        box-shadow: 0 8px 18px rgba(8, 127, 120, .2);
        transition: transform .15s ease, box-shadow .15s ease;
    }
    .stButton > button:hover {
        border: 0;
        color: #fff;
        transform: translateY(-1px);
        box-shadow: 0 11px 22px rgba(8, 127, 120, .28);
    }
    .result-label { margin: .35rem 0 .8rem; color: var(--muted); }
    .result-card {
        height: 100%;
        min-height: 154px;
        padding: 1.2rem 1.35rem;
        border: 1px solid var(--line);
        border-radius: 10px;
        background: #fff;
        box-shadow: 0 7px 22px rgba(26, 64, 68, .06);
    }
    .result-card .label { color: var(--muted); font-size: .88rem; font-weight: 600; }
    .result-card .value {
        margin: .45rem 0 .25rem;
        color: var(--ink);
        font: 800 2rem/1.2 'Manrope', sans-serif;
    }
    .result-card .detail { color: var(--muted); font-size: .88rem; }
    .density-pill {
        display: inline-block;
        margin-top: .5rem;
        padding: .32rem .7rem;
        border: 1px solid;
        border-radius: 99px;
        font-size: .84rem;
        font-weight: 700;
    }
    .density-low { color: #176c49; border-color: #a9d9bf; background: #eaf7ef; }
    .density-medium { color: #85600d; border-color: #ead18a; background: #fff8df; }
    .density-high { color: #a43e35; border-color: #efb8b1; background: #fff0ee; }
    .context-line {
        margin-top: .85rem;
        padding: .8rem 1rem;
        border-left: 3px solid #18a096;
        border-radius: 3px;
        background: #e7f4f1;
        color: #35545c;
        font-size: .92rem;
    }
    .info-panel {
        height: 100%;
        padding: 1.2rem 1.3rem;
        border-top: 3px solid #0a9187;
        border-radius: 4px 4px 8px 8px;
        background: rgba(255, 255, 255, .82);
    }
    .info-panel h3 { margin: 0 0 .45rem; font-size: 1.02rem; }
    .info-panel p { margin: 0; color: var(--muted); font-size: .92rem; line-height: 1.55; }
    @media (max-width: 640px) {
        .block-container { padding: 1rem 1rem 2rem; }
        .hero { padding: 1.5rem 1.25rem; }
        .hero:after { right: .6rem; font-size: 6rem; }
        .hero h1 { font-size: 1.8rem; }
        .result-card { min-height: 132px; }
    }
    </style>
    <div class="hero">
      <div class="hero-kicker">Smart transit · Live planning</div>
      <h1>Smart Bus Arrival &amp; Passenger Density</h1>
      <p>বাস কখন আসবে এবং কতজন যাত্রী থাকতে পারে তা সহজেই অনুমান করুন।</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="section-kicker">Journey details</div><h2 class="section-title">Plan your trip</h2><p class="section-copy">বাসের বর্তমান পরিস্থিতি অনুযায়ী তথ্য নির্বাচন করুন।</p>', unsafe_allow_html=True)

input_columns = st.columns(3, gap="medium")
with input_columns[0]:
    with st.container(border=True):
        st.markdown("**🚌 Route & schedule**")
        route = st.selectbox(
            "Bus Route",
            ["Route 1", "Route 2", "Route 3", "Route 4", "Route 5"]
        )
        day = st.selectbox(
            "📅 Day",
            ["Saturday", "Sunday", "Monday", "Tuesday",
             "Wednesday", "Thursday", "Friday"]
        )
        time = st.slider(
            "🕐 Time",
            min_value=0,
            max_value=23,
            value=8
        )

with input_columns[1]:
    with st.container(border=True):
        st.markdown("**🚦 Road conditions**")
        traffic = st.selectbox(
            "Traffic",
            ["Low", "Medium", "High"]
        )
        weather = st.selectbox(
            "🌦️ Weather",
            ["Sunny", "Cloudy", "Rainy"]
        )
        st.markdown("*Traffic and weather help describe current conditions.*")

with input_columns[2]:
    with st.container(border=True):
        st.markdown("**👥 Passenger count**")
        passengers = st.number_input(
            "Current Passenger Count",
            min_value=0,
            max_value=200,
            value=30
        )
        st.markdown("*Enter the number of passengers currently on board.*")

# Prediction button
if st.button("🔮 Predict arrival", use_container_width=True):
    # Demo prediction logic
    # পরে আপনার trained ML model এখানে যুক্ত করা হবে
    if traffic == "High":
        arrival_time = 15
    elif traffic == "Medium":
        arrival_time = 10
    else:
        arrival_time = 5

    if passengers < 30:
        density = "Low"
    elif passengers < 80:
        density = "Medium"
    else:
        density = "High"

    density_class = f"density-{density.lower()}"
    st.markdown(
        f"""
        <div class="section-kicker" style="margin-top:1.8rem">Your estimate</div>
        <h2 class="section-title">Prediction result</h2>
        <p class="result-label">An estimate based on the details you entered.</p>
        <div class="result-card">
          <div class="label">⏱️ Estimated arrival</div>
          <div class="value">{arrival_time} <span style="font-size:1rem;font-weight:600">min</span></div>
          <div class="detail">Estimated time until the bus arrives</div>
        </div>
        <div class="result-card" style="margin-top:.8rem">
          <div class="label">👥 Passenger density</div>
          <div><span class="density-pill {density_class}">{density}</span></div>
          <div class="detail" style="margin-top:.55rem">Based on {passengers} current passengers</div>
        </div>
        <div class="context-line">Route: {route} &nbsp;·&nbsp; Day: {day} &nbsp;·&nbsp; Time: {time}:00</div>
        """,
        unsafe_allow_html=True,
    )

st.markdown('<div class="section-kicker" style="margin-top:2.5rem">A clearer commute</div><h2 class="section-title">How It Works</h2>', unsafe_allow_html=True)
how_columns = st.columns(3, gap="medium")
with how_columns[0]:
    st.markdown('<div class="info-panel"><h3>01 · Add trip details</h3><p>Select the route, day, and time you want to check.</p></div>', unsafe_allow_html=True)
with how_columns[1]:
    st.markdown('<div class="info-panel"><h3>02 · Describe conditions</h3><p>Choose current traffic, weather, and passenger count.</p></div>', unsafe_allow_html=True)
with how_columns[2]:
    st.markdown('<div class="info-panel"><h3>03 · Get an estimate</h3><p>See the estimated arrival time and expected passenger density.</p></div>', unsafe_allow_html=True)

st.markdown('<div class="section-kicker" style="margin-top:2.5rem">About this project</div><h2 class="section-title">About Smart Bus</h2>', unsafe_allow_html=True)
st.markdown(
    '<div class="info-panel"><p>Smart Bus helps passengers plan with a quick estimate of bus arrival time and onboard density. This demo uses the selected traffic level and passenger count to generate its prediction.</p></div>',
    unsafe_allow_html=True,
)
