def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty.

    The game has three levels (Easy, Medium, Hard).  "Medium" corresponds to
    the original "Normal" level and uses 1–100.  Hard is intentionally
    broader.  This helper is used by the Streamlit app as well as the unit
    tests.
    """
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Medium":
        return 1, 100
    if difficulty == "Hard":
        return 1, 200
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an integer guess.

    Returns
    -------
    ok : bool
        Whether parsing succeeded.
    guess_int : int | None
        The parsed value (rounded if given a float).
    error_message : str | None
        An error message suitable for display, or ``None`` on success.
    """
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare ``guess`` to ``secret``.

    Returns a tuple ``(outcome, message)``.  ``outcome`` is a short string used
    internally (and by the score updater) such as ``"Win"`` or
    ``"Too High"``.  ``message`` is a human-friendly hint that can safely be
    displayed to the player.
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        if guess > secret:
            return "Too High", "📉 Go LOWER!"
        else:
            return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        g = str(guess)
        if g == str(secret):
            return "Win", "🎉 Correct!"
        if g > str(secret):
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on ``outcome`` and ``attempt_number``.

    The rules mirror those in the Streamlit app: winning gives more points the
    earlier it happens, a wrong guess penalizes the player, and alternating
    mistakes sometimes grant a small bonus for guessing on the right side of
    the secret.
    """
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
