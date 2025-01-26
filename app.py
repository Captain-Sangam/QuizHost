import streamlit as st
from PIL import Image

class QuizHost:
    def __init__(self):
        if 'step' not in st.session_state:
            st.session_state.step = 0
        
        # Set page config to wide mode
        st.set_page_config(layout="wide", page_title="QuizHost")
        
        if 'teams' not in st.session_state:
            st.session_state.teams = []
        if 'scores' not in st.session_state:
            st.session_state.scores = []
        if 'score_history' not in st.session_state:
            st.session_state.score_history = []
        if 'correct_points' not in st.session_state:
            st.session_state.correct_points = 10
        if 'pass_points' not in st.session_state:
            st.session_state.pass_points = 5
        if 'company_name' not in st.session_state:
            st.session_state.company_name = ''
        if 'logo' not in st.session_state:
            st.session_state.logo = None

    def team_setup(self):
        st.header("Team Setup")
        num_teams = st.number_input("Number of Teams", min_value=1, max_value=10, value=2)
        
        # Clear existing teams if number changes
        if len(st.session_state.teams) != num_teams:
            st.session_state.teams = [''] * num_teams
            st.session_state.scores = [0] * num_teams

        for i in range(num_teams):
            st.session_state.teams[i] = st.text_input(f"Team {i+1} Name", 
                                                      value=st.session_state.teams[i] or f"Team {i+1}")
        
        if st.button("Next: Score Settings", type='primary'):
            st.session_state.step = 1
            st.experimental_rerun()

    def score_settings(self):
        st.header("Score Settings")
        st.session_state.correct_points = st.number_input(
            "Points for Correct Answer", 
            min_value=0, 
            value=st.session_state.correct_points
        )
        st.session_state.pass_points = st.number_input(
            "Points for Passed Question", 
            min_value=0, 
            value=st.session_state.pass_points
        )
        
        cols = st.columns(2)
        with cols[0]:
            if st.button("Previous: Team Setup"):
                st.session_state.step = 0
                st.experimental_rerun()
        
        with cols[1]:
            if st.button("Next: Branding", type='primary'):
                st.session_state.step = 2
                st.experimental_rerun()

    def branding(self):
        st.header("Branding")
        st.session_state.company_name = st.text_input(
            "Company Name", 
            value=st.session_state.company_name
        )
        
        uploaded_logo = st.file_uploader("Upload Company Logo", type=['png', 'jpg', 'jpeg'])
        
        if uploaded_logo is not None:
            st.session_state.logo = uploaded_logo
            logo = Image.open(uploaded_logo)
            st.image(logo, caption='Uploaded Logo', width=200)
        
        cols = st.columns(2)
        with cols[0]:
            if st.button("Previous: Score Settings"):
                st.session_state.step = 1
                st.experimental_rerun()
        
        with cols[1]:
            if st.button("Next: Scoreboard", type='primary'):
                st.session_state.step = 3
                st.experimental_rerun()

    def scoreboard(self):
        # Company name and logo side by side
        if st.session_state.company_name or st.session_state.logo:
            col1, col2 = st.columns([3, 1])
            with col1:
                if st.session_state.company_name:
                    st.header(st.session_state.company_name)
            with col2:
                if st.session_state.logo:
                    logo = Image.open(st.session_state.logo)
                    st.image(logo, width=100)

        # Scoreboard
        st.header("Scoreboard")
        # Use container for full width and add gap between columns
        with st.container():
            cols = st.columns([1] * len(st.session_state.teams), gap="large")
            
            for i, (team, score) in enumerate(zip(st.session_state.teams, st.session_state.scores)):
                with cols[i]:
                    st.metric(team, score)

                    for _ in range(3):
                        st.markdown('##')
                    
                    if st.button(f"Correct", key=f"correct_{i}", type='secondary',use_container_width=True):
                        st.session_state.score_history.append(
                            (i, st.session_state.scores[i], 'correct')
                        )
                        st.session_state.scores[i] += st.session_state.correct_points
                        st.experimental_rerun()
                    
                    if st.button(f"Pass", key=f"pass_{i}", type='secondary',use_container_width=True):
                        st.session_state.score_history.append(
                            (i, st.session_state.scores[i], 'pass')
                        )
                        st.session_state.scores[i] += st.session_state.pass_points
                        st.experimental_rerun()

        # Undo button
        for _ in range(3):
            st.markdown('##')
        if st.button("Undo" , use_container_width=True, type='primary') and st.session_state.score_history:
            last_action = st.session_state.score_history.pop()
            team_index, previous_score, _ = last_action
            st.session_state.scores[team_index] = previous_score
            st.experimental_rerun()

        # Back button in a corner
        for _ in range(3):
            st.markdown('##')
        if st.button("Edit Config", use_container_width=True):
            st.session_state.step = 2
            st.experimental_rerun()

    def main(self):
        # Step-by-step navigation
        if st.session_state.step == 0:
            self.team_setup()
        elif st.session_state.step == 1:
            self.score_settings()
        elif st.session_state.step == 2:
            self.branding()
        elif st.session_state.step == 3:
            self.scoreboard()

def main():
    quiz_app = QuizHost()
    quiz_app.main()
    st.markdown(
        """
        <div style='position: fixed; bottom: 0; left: 0; width: 100%; text-align: center; padding: 10px; color: grey;'>
            <p style='margin: 5px;'>QuizHost - A Streamlit-based Quiz Management System @ 2025</p>    
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<div style='margin-bottom: 120px;'></div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()