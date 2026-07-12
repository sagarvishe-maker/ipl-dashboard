# ================= IMPORTS =================

import streamlit as st
import pandas as pd
import plotly.express as px
import os

# ================= PAGE CONFIG =================

st.set_page_config(
    page_title="IPL Dashboard",
    page_icon="🏏",
    layout="wide"
)

# ================= LOAD DATA =================

df = pd.read_csv(
    "ipl_data.csv.gz",
    compression="gzip",
    low_memory=False
)

# ================= CLEAN SEASON =================

df['season'] = df['season'].astype(str)

df['season'] = df['season'].replace({
    '2007/08': '2008',
    '2009/10': '2010',
    '2020/21': '2020'
})

df = df[df['season'] != '2026']

# ================= FIX TEAM SPELLING =================

df['batting_team'] = df['batting_team'].replace({
    'Royal Challengers Bangaluru': 'Royal Challengers Bengaluru',
    'Royal Challengers Bengalore': 'Royal Challengers Bangalore'
})

df['bowling_team'] = df['bowling_team'].replace({
    'Royal Challengers Bangaluru': 'Royal Challengers Bengaluru',
    'Royal Challengers Bengalore': 'Royal Challengers Bangalore'
})

df['match_won_by'] = df['match_won_by'].replace({
    'Royal Challengers Bangaluru': 'Royal Challengers Bengaluru',
    'Royal Challengers Bengalore': 'Royal Challengers Bangalore'
})

# ================= IPL NAMES =================

ipl_name = {
    '2008':'DLF IPL',
    '2009':'DLF IPL',
    '2010':'DLF IPL',
    '2011':'IPL',
    '2012':'IPL',
    '2013':'Pepsi IPL',
    '2014':'Pepsi IPL',
    '2015':'Pepsi IPL',
    '2016':'Vivo IPL',
    '2017':'Vivo IPL',
    '2018':'Vivo IPL',
    '2019':'Vivo IPL',
    '2020':'Dream11 IPL',
    '2021':'Vivo IPL',
    '2022':'TATA IPL',
    '2023':'TATA IPL',
    '2024':'TATA IPL',
    '2025':'TATA IPL'
}

# ================= TEAM LOGOS =================

teams_logos = {

    "Chennai Super Kings":
    "team logos/Chennai Super Kings.png",

    "Mumbai Indians":
    "team logos/Mumbai Indians.png",

    "Royal Challengers Bangalore":
    "team logos/Royal Challengers Bangalore.png",

    "Royal Challengers Bengaluru":
    "team logos/Royal Challengers Bengaluru.png",

    "Kolkata Knight Riders":
    "team logos/Kolkata Knight Riders.png",

    "Delhi Capitals":
    "team logos/Delhi Capitals.png",

    "Punjab Kings":
    "team logos/Punjab Kings.png",

    "Rajasthan Royals":
    "team logos/Rajasthan Royals.png",

    "Sunrisers Hyderabad":
    "team logos/Sunrisers Hyderabad.png",

    "Gujarat Titans":
    "team logos/Gujarat Titans.png",

    "Lucknow Super Giants":
    "team logos/Lucknow Super Giants.png",

    "Delhi Daredevils":
    "team logos/Delhi Daredevils.png",

    "Kings XI Punjab":
    "team logos/Kings XI Punjab.png",

    "Deccan Chargers":
    "team logos/Deccan Chargers.png",

    "Gujarat Lions":
    "team logos/Gujarat Lions.png",

    "Kochi Tuskers Kerala":
    "team logos/Kochi Tuskers Kerala.png",

    "Pune Warriors":
    "team logos/Pune Warriors.png",

    "Pune Warriors India":
    "team logos/Pune Warriors.png",

    "Rising Pune Supergiant":
    "team logos/Rising Pune Supergiant.png",

    "Rising Pune Supergiants":
    "team logos/Rising Pune Supergiants.png"
}

# ================= SAFE LOGO FUNCTION =================

def show_logo(team_name, width=120):

    if team_name in teams_logos:

        logo_path = teams_logos[team_name]

        if os.path.exists(logo_path):
            pass

            # st.image(
            #     logo_path,
            #     width=width
            # )

# ================= COLORS =================

ipl_colors = [
    "#60a5fa",
    "#facc15",
    "#f97316",
    "#a855f7",
    "#22c55e",
    "#ef4444",
    "#14b8a6"
]

# ================= DARK THEME =================

st.markdown("""
<style>

[data-testid="stAppViewContainer"]{
    background:#070b1a;
    color:white;
}

section[data-testid="stSidebar"]{
    background:#111827;
}

h1,h2,h3,h4,h5,h6,p,label{
    color:white !important;
}

div[data-testid="stMetric"]{
    background:linear-gradient(145deg,#111827,#1f2937);
    border:1px solid #374151;
    padding:10px;
    border-radius:14px;
}

</style>
""", unsafe_allow_html=True)

# ================= HEADER =================

col1, col2 = st.columns([1,5])

with col1:

    # st.image(
    #     "logos/ipl.jpeg",
    #     width=110
    # )

with col2:

    st.markdown("""
    <h1 style='color:#60a5fa;'>
   🏏 IPL DASHBOARD
    </h1>

    <h4 style='color:gray;'>
    IPL Data Analysis 2008 - 2025
    </h4>
    """, unsafe_allow_html=True)

st.markdown("---")

# ================= FILTERS =================

f1, f2, f3, f4 = st.columns(4)

season_order = [
    '2008','2009','2010','2011',
    '2012','2013','2014','2015',
    '2016','2017','2018','2019',
    '2020','2021','2022','2023',
    '2024','2025'
]

with f1:

    selected_season = st.selectbox(
        "📅 Season",
        ["All"] + season_order
    )

with f2:

    teams = sorted(
        df['batting_team'].dropna().unique()
    )

    selected_team = st.selectbox(
        "🏏 Team",
        ["All"] + list(teams)
    )

with f3:

    players = sorted(
        df['batter'].dropna().unique()
    )

    selected_player = st.selectbox(
        "👤 Player",
        ["All"] + list(players)
    )

with f4:

    venues = sorted(
        df['venue'].dropna().unique()
    )

    selected_venue = st.selectbox(
        "🏟️ Venue",
        ["All Venues"] + list(venues)
    )

# ================= FILTER LOGIC =================

filtered_df = df.copy()

if selected_season != "All":

    filtered_df = filtered_df[
        filtered_df['season'] == selected_season
    ]

if selected_venue != "All Venues":

    filtered_df = filtered_df[
        filtered_df['venue'] == selected_venue
    ]

if selected_team != "All":

    filtered_df = filtered_df[
        (filtered_df['batting_team'] == selected_team) |
        (filtered_df['bowling_team'] == selected_team)
    ]

if selected_player != "All":

    filtered_df = filtered_df[
        (filtered_df['batter'] == selected_player) |
        (filtered_df['bowler'] == selected_player)
    ]

# ================= IPL INFO =================

if selected_season != "All":

    st.markdown(f"""
    <div style="
    background:#111827;
    padding:18px;
    border-radius:15px;
    text-align:center;
    border:1px solid #374151;
    margin-bottom:25px;
    ">

    <h2 style='color:#60a5fa;'>
    🏏 {ipl_name.get(selected_season,'IPL')}-{selected_season}
    </h2>


    </div>
    """, unsafe_allow_html=True)

# ================= WINNER SECTION =================

if selected_season != "All":

    winner = df[
        df['season'] == selected_season
    ]['match_won_by'].dropna()

    if not winner.empty:

        winner_team = winner.mode()[0]

        w1, w2 = st.columns([3,0.8])

        with w1:

            st.markdown(f"""
            <div style="
            background:linear-gradient(145deg,#111827,#1f2937);
            padding:20px;
            border-radius:20px;
            border:1px solid #374151;
            margin-bottom:15px;
            text-align:center;
            ">

            <h2 style="
            color:#facc15;
            margin-bottom:10px;
            font-size:30px;
            ">
            🏆 Winner Team
            </h2>

            <h1 style="
            color:#60a5fa;
            font-size:42px;
            ">
            {winner_team}
            </h1>

            </div>
            """, unsafe_allow_html=True)

        with w2:

            show_logo(
                winner_team,
                200
            )

st.markdown("---")

# ================= KPIs =================

k1,k2,k3,k4 = st.columns(4)

k1.metric("🏏 Matches", filtered_df['match_id'].nunique())
k2.metric("🔥 Runs", int(filtered_df['runs_batter'].sum()))
k3.metric("🎯 Wickets", int(filtered_df['wicket_kind'].notna().sum()))
k4.metric("👥 Teams", filtered_df['batting_team'].nunique())

k5,k6,k7,k8 = st.columns(4)

k5.metric("📅 Seasons", filtered_df['season'].nunique())
k6.metric("4️⃣ Fours", int((filtered_df['runs_batter'] == 4).sum()))
k7.metric("6️⃣ Sixes", int((filtered_df['runs_batter'] == 6).sum()))
k8.metric("🏟️ Venues", filtered_df['venue'].nunique())

st.markdown("---")

# ================= PLAYER DETAILS =================

if selected_player != "All":

    player_df = filtered_df[
        (filtered_df['batter'] == selected_player) |
        (filtered_df['bowler'] == selected_player)
    ]

    # ================= PLAYER + TEAM NAME =================

    if selected_season != "All":

        # ✅ Batter team first
        batter_teams = player_df[
            player_df['batter'] == selected_player
        ]['batting_team']

        # ✅ Bowler team second
        bowler_teams = player_df[
            player_df['bowler'] == selected_player
        ]['bowling_team']

        # ✅ Merge unique teams
        player_teams = pd.concat([
            batter_teams,
            bowler_teams
        ]).dropna().unique()

        team_text = ", ".join(player_teams)

        heading_text = f"{selected_player} ({team_text})"

    else:

        heading_text = selected_player

    # ================= HEADER =================

    st.markdown(f"""
    <div style="
    background:linear-gradient(145deg,#111827,#1f2937);
    padding:15px;
    border-radius:18px;
    border:1px solid #374151;
    margin-bottom:20px;
    text-align:center;
    ">

    <h2 style="color:#60a5fa;">
    👤 Player Details
    </h2>

    <h3 style="
    color:#facc15;
    margin-top:10px;
    ">
    {heading_text}
    </h3>

    </div>
    """, unsafe_allow_html=True)

    # ================= METRICS =================

    p1,p2,p3,p4 = st.columns(4)

    p1.metric("🔥 Runs", int(player_df['runs_batter'].sum()))
    p2.metric("🎯 Wickets", int(player_df['wicket_kind'].count()))
    p3.metric("🏏 Matches", player_df['match_id'].nunique())
    p4.metric("🏟️ Venues", player_df['venue'].nunique())

    st.markdown("---")

# ================= TEAM DETAILS =================

if selected_team != "All":

    td1, td2 = st.columns([5,1])

    with td1:

        st.markdown("""
        <div style="
        background:linear-gradient(145deg,#111827,#1f2937);
        padding:15px;
        border-radius:18px;
        border:1px solid #374151;
        margin:15px 0;
        text-align:center;
        ">

        <h2 style="color:#60a5fa;">
        🏏 Team Details
        </h2>

        </div>
        """, unsafe_allow_html=True)

    with td2:

        show_logo(selected_team, 140)

    team_df = filtered_df.copy()

    t1,t2,t3,t4 = st.columns(4)

    t1.metric("🏏 Matches", team_df['match_id'].nunique())
    t2.metric("🔥 Runs", int(team_df['runs_batter'].sum()))
    t3.metric("🎯 Wickets", int(team_df['wicket_kind'].notna().sum()))
    t4.metric("📅 Seasons", team_df['season'].nunique())

    st.markdown("---")


# ================= DATA =================

top_teams = filtered_df.groupby(
    'batting_team'
).size().reset_index(
    name='matches'
).sort_values(
    'matches',
    ascending=False
).head(5)

top_batsmen = filtered_df.groupby(
    'batter'
)['runs_batter'].sum().reset_index().sort_values(
    'runs_batter',
    ascending=False
).head(5)

top_bowlers = filtered_df.groupby(
    'bowler'
)['wicket_kind'].count().reset_index(
    name='wickets'
).sort_values(
    'wickets',
    ascending=False
).head(5)

toss_data = filtered_df.groupby(
    'toss_decision'
).size().reset_index(name='count')

wins = filtered_df['match_won_by'].value_counts().reset_index()
wins.columns = ['team', 'wins']

matches = filtered_df['batting_team'].value_counts().reset_index()
matches.columns = ['team', 'matches']

team_result = pd.merge(
    matches,
    wins,
    on='team',
    how='left'
).fillna(0)

team_result['losses'] = (
    team_result['matches'] - team_result['wins']
)

# ================= CHARTS =================

fig1 = px.bar(
    top_teams,
    x='batting_team',
    y='matches',
    text='matches',
    color='batting_team',
    color_discrete_sequence=ipl_colors,
    title="🏆 Top Teams"
)

fig2 = px.bar(
    top_batsmen,
    x='batter',
    y='runs_batter',
    text='runs_batter',
    color='runs_batter',
    color_continuous_scale="Oranges",
    title="🟧 Orange Cap"
)

fig3 = px.bar(
    top_bowlers,
    x='bowler',
    y='wickets',
    text='wickets',
    color='wickets',
    color_continuous_scale="Purples",
    title="🟪 Purple Cap"
)

fig5 = px.pie(
    toss_data,
    names='toss_decision',
    values='count',
    hole=0.5,
    title="🪙 Toss Decision"
)

fig6 = px.bar(
    team_result.head(5),
    x='team',
    y=['wins','losses'],
    barmode='group',
    title="✅ Team Win & Loss"
)

# ================= GRAPH STYLE =================

for fig in [fig1,fig2,fig3,fig5,fig6]:

    fig.update_layout(
        paper_bgcolor='#111827',
        plot_bgcolor='#0b1220',
        font_color='white',
        height=240,
        margin=dict(l=10,r=10,t=40,b=10)
    )

# ================= GRAPH LAYOUT =================

r1,r2,r3 = st.columns(3)

with r1:
    st.plotly_chart(fig2, use_container_width=True)

with r2:
    st.plotly_chart(fig3, use_container_width=True)

with r3:
    st.plotly_chart(fig5, use_container_width=True)

r4,r5 = st.columns(2)

with r4:
    st.plotly_chart(fig1, use_container_width=True)

with r5:
    st.plotly_chart(fig6, use_container_width=True)



#  # ================= PLAYING XI (ONLY FOR PLAYER/TEAM VIEW) =================

# # ❌ Hide if Season = All
# if selected_season != "All":

#     st.markdown("---")

#     st.markdown("""
#     <h2 style='text-align:center;color:#60a5fa;'>
#     🏏 Playing XI
#     </h2>
#     """, unsafe_allow_html=True)

#     # ---------------- BATTERS ----------------
#     batters = filtered_df.groupby('batter').agg(
#         runs=('runs_batter', 'sum'),
#         matches=('match_id', 'nunique')
#     ).reset_index().rename(columns={'batter': 'player'})

#     # ---------------- BOWLERS ----------------
#     bowlers = filtered_df.groupby('bowler').agg(
#         wickets=('wicket_kind', 'count'),
#         matches=('match_id', 'nunique')
#     ).reset_index().rename(columns={'bowler': 'player'})

#     # ---------------- MERGE ----------------
#     players = pd.merge(batters, bowlers, on='player', how='outer').fillna(0)

#     # ---------------- FIX MATCHES (IMPORTANT) ----------------
#     players['matches'] = players[['matches_x', 'matches_y']].max(axis=1)
#     players = players.drop(columns=['matches_x', 'matches_y'], errors='ignore')

#     # ---------------- ROLE LOGIC ----------------
#     def assign_role(r):
#         if r['wickets'] >= 15 and r['runs'] < 250:
#             return "⚾ Bowler"
#         elif r['runs'] >= 400 and r['wickets'] >= 8:
#             return "🔄 All-Rounder"
#         else:
#             return "🏏 Batsman"

#     players['Role'] = players.apply(assign_role, axis=1)

#     # ---------------- IMPACT SCORE ----------------
#     players['impact'] = players['runs'] + (players['wickets'] * 25)

#     # ---------------- TOP 11 ----------------
#     top11 = players.sort_values('impact', ascending=False).head(11)

#     # ---------------- ROLE ORDER ----------------
#     role_order = {
#         "🏏 Batsman": 1,
#         "🔄 All-Rounder": 2,
#         "⚾ Bowler": 3
#     }

#     top11['order'] = top11['Role'].map(role_order)

#     top11 = top11.sort_values(
#         by=['order', 'impact'],
#         ascending=[True, False]
#     )

#     # ---------------- FINAL TABLE (Role REMOVED) ----------------
#     st.dataframe(
#         top11[['player', 'runs', 'wickets', 'matches']],
#         use_container_width=True,
#         hide_index=True
#     )