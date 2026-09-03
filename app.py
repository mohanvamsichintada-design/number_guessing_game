import streamlit as st
import random

st.title("🎯 Number Guessing Game")

st.write("Welcome to my Python Number Guessing Game!")

# -------------------------------
# Choose difficulty
# -------------------------------

level = st.selectbox(
    "Choose your difficulty level:",
    ["EASY", "MEDIUM", "HARD"]
)

# -------------------------------
# Set range and attempts
# -------------------------------

if level == "EASY":
    b = 50
    max_attempts = 4

elif level == "MEDIUM":
    b = 100
    max_attempts = 7

else:
    b = 500
    max_attempts = 10

# -------------------------------
# Detect difficulty change
# -------------------------------

if "previous_level" not in st.session_state:
    st.session_state.previous_level = level

if level != st.session_state.previous_level:

    st.session_state.guess = random.randint(1, b)
    st.session_state.attempt = 0
    st.session_state.game_over = False
    st.session_state.previous_level = level

# -------------------------------
# Initialize game values
# -------------------------------

if "guess" not in st.session_state:
    st.session_state.guess = random.randint(1, b)

if "attempt" not in st.session_state:
    st.session_state.attempt = 0

if "game_over" not in st.session_state:
    st.session_state.game_over = False

# -------------------------------
# Display game information
# -------------------------------

st.info(f"🔢 Guess a number between 1 and {b}")
st.write("🎯 Attempts:", st.session_state.attempt, "/", max_attempts)

# -------------------------------
# Start New Game
# -------------------------------

if st.button("🎮 Start New Game", key="new_game"):

    st.session_state.guess = random.randint(1, b)
    st.session_state.attempt = 0
    st.session_state.game_over = False

    st.success("🎮 New game started!")

# -------------------------------
# Player's guess
# -------------------------------

user_guess = st.number_input(
    "Enter your expected number:",
    min_value=1,
    max_value=b,
    step=1
)

# -------------------------------
# Check Guess
# -------------------------------

if st.button("🎯 Guess", key="guess_button"):

    if st.session_state.game_over:

        st.warning("The game is over! Start a new game.")

    else:

        st.session_state.attempt += 1

        st.write(
            "Attempt",
            st.session_state.attempt,
            "out of",
            max_attempts
        )

        # -------------------------------
        # Your original LOW / HIGH logic
        # -------------------------------

        if user_guess < st.session_state.guess:

            st.warning("⬆️ Too low! Try a higher number.")

        elif user_guess > st.session_state.guess:

            st.warning("⬇️ Too high! Try a lower number.")

        else:

            st.success(
                "🎉 CONGRATULATIONS! "
                "Your expectation is correct!"
            )

            st.session_state.game_over = True

        # -------------------------------
        # Game Over
        # -------------------------------

        if st.session_state.attempt >= max_attempts:

            if user_guess != st.session_state.guess:

                st.error("❌ You are out of chances!")
                st.warning("Try Again")
                st.error("GAME OVER")

                st.session_state.game_over = True

if st.session_state.game_over:

    if st.button("🔄 Play Again", key="play_again"):

        st.session_state.guess = random.randint(1, b)
        st.session_state.attempt = 0
        st.session_state.game_over = False

        st.rerun()