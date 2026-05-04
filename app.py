import streamlit as st
import pandas as pd
import pickle

# =========================
# PAGE SETUP
# =========================
st.set_page_config(
    page_title="Gaurav’s Score Prediction Model",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# CUSTOM CSS
# =========================
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #0f172a 0%, #111827 50%, #1f2937 100%);
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .title-box {
        background: rgba(255,255,255,0.06);
        border: 1px solid rgba(255,255,255,0.12);
        padding: 1.2rem 1.4rem;
        border-radius: 22px;
        box-shadow: 0 8px 30px rgba(0,0,0,0.18);
        backdrop-filter: blur(10px);
    }
    .glass-card {
        background: rgba(255,255,255,0.06);
        border: 1px solid rgba(255,255,255,0.12);
        padding: 1rem 1.1rem;
        border-radius: 18px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.16);
        backdrop-filter: blur(10px);
    }
    .metric-label {
        font-size: 0.9rem;
        color: #cbd5e1;
        margin-bottom: 0.25rem;
    }
    .metric-value {
        font-size: 1.8rem;
        font-weight: 800;
        color: white;
        line-height: 1.1;
    }
    .metric-sub {
        font-size: 0.85rem;
        color: #94a3b8;
    }
    .small-note {
        color: #cbd5e1;
        font-size: 0.92rem;
    }
    .section-box {
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.10);
        border-radius: 18px;
        padding: 1rem 1rem;
        margin-bottom: 1rem;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        background: rgba(255,255,255,0.06);
        border-radius: 14px;
        padding: 10px 16px;
    }
    .stTabs [aria-selected="true"] {
        background: rgba(59,130,246,0.25) !important;
        border: 1px solid rgba(59,130,246,0.5) !important;
    }
    div[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f172a 0%, #111827 100%);
    }
</style>
""", unsafe_allow_html=True)

# =========================
# LOAD MODEL + COLUMNS
# =========================
@st.cache_resource
def load_assets():
    model = pickle.load(open("model.pkl", "rb"))
    columns = pickle.load(open("columns.pkl", "rb"))
    return model, columns

model, columns = load_assets()

# =========================
# MAPPINGS FOR HUMAN-FRIENDLY INPUTS
# =========================
famsize_map = {
    "3 or fewer family members (LE3)": "LE3",
    "More than 3 family members (GT3)": "GT3"
}

pstatus_map = {
    "Parents living together (T)": "T",
    "Parents living apart (A)": "A"
}

yesno_map = {
    "No": "no",
    "Yes": "yes"
}

sex_options = {
    "Female": "F",
    "Male": "M"
}

address_options = {
    "Rural area": "R",
    "Urban area": "U"
}

job_options = {
    "At home / no job": "at_home",
    "Health sector": "health",
    "Services / office / govt work": "services",
    "Teacher": "teacher",
    "Other": "other"
}

health_options = {
    "Very unhealthy": 1,
    "Unhealthy": 2,
    "Okay / average": 3,
    "Healthy": 4,
    "Very healthy": 5
}

alcohol_options = {
    "Never": 1,
    "Very low": 2,
    "Moderate": 3,
    "High": 4,
    "Very high": 5
}

# =========================
# SIDEBAR
# =========================
with st.sidebar:
    st.markdown("## 🎓 About this model")
    st.write("This app predicts a student’s final grade (**G3**) and estimated CGPA using personal, academic, and lifestyle inputs.")
    st.markdown("---")
    st.markdown("### What the model expects")
    st.write("- Honest inputs")
    st.write("- Realistic values")
    st.write("- Best used as an estimate, not a final truth")
    st.markdown("---")
    st.caption("Model: Random Forest Regressor")
    st.caption("Saved files: model.pkl, columns.pkl")

# =========================
# HEADER
# =========================
st.markdown("""
<div class="title-box">
    <h1 style="margin:0; color:white;">🎓 Gaurav’s Score Prediction Model</h1>
    <p style="margin:0.4rem 0 0 0; color:#cbd5e1;">
        Predict final grade (G3), percentage, and estimated CGPA from student data.
    </p>
</div>
""", unsafe_allow_html=True)

st.write("")

# =========================
# FORM
# =========================
with st.form("student_form"):
    tab1, tab2, tab3, tab4 = st.tabs([
        "👤 Basic Info",
        "📚 Academic Info",
        "🌱 Lifestyle Info",
        "🍺 Health & Alcohol"
    ])

    with tab1:
        st.markdown("#### Student profile")
        c1, c2, c3 = st.columns(3)

        with c1:
            age = st.number_input("Age", min_value=15, max_value=25, value=18, step=1)
            sex_label = st.selectbox("Gender", list(sex_options.keys()))
            address_label = st.selectbox("Location", list(address_options.keys()))

        with c2:
            famsize_label = st.selectbox(
                "Family size",
                list(famsize_map.keys()),
                help="LE3 means 3 or fewer family members. GT3 means more than 3 family members."
            )
            pstatus_label = st.selectbox(
                "Parents’ living status",
                list(pstatus_map.keys()),
                help="T means together. A means apart."
            )
            traveltime = st.slider(
                "Travel time to school",
                1, 4, 2,
                help="1 = very short travel time, 4 = very long travel time."
            )

        with c3:
            Medu = st.slider(
                "Mother’s education level",
                0, 4, 2,
                help="0 = no schooling, 4 = higher education."
            )
            Fedu = st.slider(
                "Father’s education level",
                0, 4, 2,
                help="0 = no schooling, 4 = higher education."
            )

    with tab2:
        st.markdown("#### Academic background")
        a1, a2, a3 = st.columns(3)

        with a1:
            studytime = st.slider(
                "Study time per week",
                1, 4, 2,
                help="1 = very low study time, 4 = very high study time."
            )
            failures = st.slider(
                "Past academic failures",
                0, 3, 0,
                help="Number of previous class failures."
            )
            absences = st.number_input(
                "Absences",
                min_value=0, max_value=100, value=5, step=1,
                help="Total number of school days missed."
            )

        with a2:
            schoolsup_label = st.selectbox("Extra school support", list(yesno_map.keys()))
            famsup_label = st.selectbox("Family academic support", list(yesno_map.keys()))
            paid_label = st.selectbox("Paid extra classes", list(yesno_map.keys()))

        with a3:
            Mjob_label = st.selectbox("Mother’s job", list(job_options.keys()))
            Fjob_label = st.selectbox("Father’s job", list(job_options.keys()))

    with tab3:
        st.markdown("#### Daily life and social pattern")
        l1, l2, l3 = st.columns(3)

        with l1:
            activities_label = st.selectbox("Extra activities", list(yesno_map.keys()))
            nursery_label = st.selectbox("Nursery school attended", list(yesno_map.keys()))
            higher_label = st.selectbox("Wants higher education", list(yesno_map.keys()))

        with l2:
            internet_label = st.selectbox("Internet access at home", list(yesno_map.keys()))
            romantic_label = st.selectbox("Currently in a romantic relationship", list(yesno_map.keys()))
            famrel = st.slider(
                "Family relationship quality",
                1, 5, 4,
                help="1 = very poor relationship, 5 = very strong relationship."
            )

        with l3:
            freetime = st.slider(
                "Free time after school",
                1, 5, 3,
                help="1 = very little free time, 5 = lots of free time."
            )
            goout = st.slider(
                "Going out with friends",
                1, 5, 3,
                help="1 = stays in mostly, 5 = goes out very often."
            )

    with tab4:
        st.markdown("#### Health and alcohol section")

        st.info(
           
            "Choose the option that best matches the student’s real situation."
        )

        h1, h2, h3 = st.columns(3)

        with h1:
            health_label = st.selectbox(
                "Health condition",
                list(health_options.keys()),
                help="1 = very unhealthy, 5 = very healthy."
            )
            st.caption("Degree of membership: poor health → unhealthy, average → okay, good → healthy.")

        with h2:
            Dalc_label = st.selectbox(
                "Weekday alcohol usage",
                list(alcohol_options.keys()),
                help="1 = never, 5 = very high use on weekdays."
            )
            st.caption("Degree of membership: low use → low risk, high use → high risk.")

        with h3:
            Walc_label = st.selectbox(
                "Weekend alcohol usage",
                list(alcohol_options.keys()),
                help="1 = never, 5 = very high use on weekends."
            )
            st.caption("Degree of membership: low use → low risk, high use → high risk.")

    submitted = st.form_submit_button("🚀 Predict Performance")

# =========================
# PREDICTION
# =========================
if submitted:
    # map user-friendly labels to model values
    sex = sex_options[sex_label]
    address = address_options[address_label]
    famsize = famsize_map[famsize_label]
    Pstatus = pstatus_map[pstatus_label]
    schoolsup = yesno_map[schoolsup_label]
    famsup = yesno_map[famsup_label]
    paid = yesno_map[paid_label]
    activities = yesno_map[activities_label]
    nursery = yesno_map[nursery_label]
    higher = yesno_map[higher_label]
    internet = yesno_map[internet_label]
    romantic = yesno_map[romantic_label]
    Mjob = job_options[Mjob_label]
    Fjob = job_options[Fjob_label]
    health = health_options[health_label]
    Dalc = alcohol_options[Dalc_label]
    Walc = alcohol_options[Walc_label]

    user_df = pd.DataFrame([{
        "age": age,
        "sex": sex,
        "address": address,
        "famsize": famsize,
        "Pstatus": Pstatus,
        "Medu": Medu,
        "Fedu": Fedu,
        "Mjob": Mjob,
        "Fjob": Fjob,
        "traveltime": traveltime,
        "studytime": studytime,
        "failures": failures,
        "schoolsup": schoolsup,
        "famsup": famsup,
        "paid": paid,
        "activities": activities,
        "nursery": nursery,
        "higher": higher,
        "internet": internet,
        "romantic": romantic,
        "famrel": famrel,
        "freetime": freetime,
        "goout": goout,
        "Dalc": Dalc,
        "Walc": Walc,
        "health": health,
        "absences": absences
    }])

    user_df = pd.get_dummies(user_df, drop_first=True)
    user_df = user_df.reindex(columns=columns, fill_value=0)

    pred_g3 = float(model.predict(user_df)[0])
    pred_g3 = max(0, min(20, pred_g3))

    percentage = (pred_g3 / 20) * 100
    cgpa = percentage / 9.5

    if pred_g3 >= 15:
        status = "Excellent 🔥"
    elif pred_g3 >= 12:
        status = "Good ✅"
    elif pred_g3 >= 10:
        status = "Pass ⚠️"
    else:
        status = "At Risk ❌"

    st.markdown("---")
    st.subheader("📊 Prediction Result")

    m1, m2, m3, m4 = st.columns(4)

    with m1:
        st.markdown(f"""
        <div class="glass-card">
            <div class="metric-label">Predicted G3</div>
            <div class="metric-value">{pred_g3:.2f}</div>
            <div class="metric-sub">Out of 20</div>
        </div>
        """, unsafe_allow_html=True)

    with m2:
        st.markdown(f"""
        <div class="glass-card">
            <div class="metric-label">Percentage</div>
            <div class="metric-value">{percentage:.2f}%</div>
            <div class="metric-sub">Converted from G3</div>
        </div>
        """, unsafe_allow_html=True)

    with m3:
        st.markdown(f"""
        <div class="glass-card">
            <div class="metric-label">Estimated CGPA</div>
            <div class="metric-value">{cgpa:.2f}</div>
            <div class="metric-sub">Approximate value</div>
        </div>
        """, unsafe_allow_html=True)

    with m4:
        st.markdown(f"""
        <div class="glass-card">
            <div class="metric-label">Status</div>
            <div class="metric-value">{status}</div>
            <div class="metric-sub">Prediction outcome</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.progress(pred_g3 / 20)

    st.markdown("### 🧠 Observation for the user")

    if pred_g3 >= 15:
        st.success("The model predicts strong academic performance. This suggests good study habits, strong consistency, and healthier lifestyle signals.")
    elif pred_g3 >= 12:
        st.info("The model predicts decent performance. The student is likely in a safe academic zone.")
    elif pred_g3 >= 10:
        st.warning("The model predicts borderline performance. Small improvements in study time, attendance, and discipline may raise the score.")
    else:
        st.error("The model predicts weak performance. This may indicate low study time, more absences, weaker support, or risky lifestyle patterns.")

    suggestions = []
    if studytime <= 2:
        suggestions.append("Increase study time.")
    if absences >= 10:
        suggestions.append("Reduce absences.")
    if failures >= 1:
        suggestions.append("Work on weak subjects and avoid repeat failures.")
    if goout >= 4:
        suggestions.append("Balance social time with study time.")
    if Dalc >= 3 or Walc >= 3:
        suggestions.append("Reduce alcohol usage for better academic focus.")
    if higher == "no":
        suggestions.append("Set a stronger goal for higher education.")
    if health <= 2:
        suggestions.append("Improve health habits like sleep, diet, and routine.")

    if suggestions:
        st.markdown("### 💡 Suggestions")
        for s in suggestions:
            st.write(f"- {s}")

    with st.expander("🔍 Encoded input preview"):
        st.dataframe(user_df, use_container_width=True)