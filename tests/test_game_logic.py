from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


def test_new_game_bug_string_secret():
    # app.py passes secret as str() on even attempts (line 144).
    # The old check_guess fell back to string comparison in that case,
    # so check_guess(9, "10") returned "Too High" instead of "Too Low"
    # because "9" > "1" alphabetically. That wrong outcome could leave
    # the game in a broken state requiring a New Game reset.
    outcome, _ = check_guess(9, "10")
    assert outcome == "Too Low"

    outcome, _ = check_guess(15, "10")
    assert outcome == "Too High"

    outcome, _ = check_guess(10, "10")
    assert outcome == "Win"
