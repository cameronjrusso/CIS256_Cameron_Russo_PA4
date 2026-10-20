# Cameron Russo
# CIS256 Fall 2026
# Programming Assignment 4

import guess_the_word as game


def test_random_word_is_in_list():
    # Every selected word should be one we included in the game.
    for _ in range(20):
        assert game.choose_word() in game.WORDS


def test_correct_guess():
    # The letter a is in banana.
    assert game.check_guess("banana", "a") is True


def test_incorrect_guess():
    # The letter z is not in banana.
    assert game.check_guess("banana", "z") is False


def test_repeated_letters_are_all_shown():
    # One guess of a should reveal all three a's.
    assert game.display_word("banana", {"a"}) == "_ a _ a _ a"


def test_letters_can_be_guessed_in_any_order():
    # Both b and n should show up, regardless of which was guessed first.
    assert game.display_word("banana", {"n", "b"}) == "b _ n _ n _"


def test_player_can_win(monkeypatch, capsys):
    # Pick a known word so the test does not depend on randomness.
    monkeypatch.setattr(game, "choose_word", lambda: "banana")
    answers = iter(["n", "b", "a"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(answers))

    game.play_game()

    output = capsys.readouterr().out
    assert "Congratulations!" in output
    assert "banana" in output


def test_player_can_run_out_of_attempts(monkeypatch, capsys):
    # Six wrong guesses should end the game.
    monkeypatch.setattr(game, "choose_word", lambda: "banana")
    answers = iter(["c", "d", "e", "f", "g", "h"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(answers))

    game.play_game()

    output = capsys.readouterr().out
    assert "Game over!" in output
    assert "banana" in output


def test_invalid_and_repeated_guesses(monkeypatch, capsys):
    # Invalid input and a repeated letter should not use up a turn.
    monkeypatch.setattr(game, "choose_word", lambda: "banana")
    answers = iter(["12", "b", "b", "n", "a"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(answers))

    game.play_game()

    output = capsys.readouterr().out
    assert "Please enter just one letter." in output
    assert "You already guessed that letter." in output
    assert "Congratulations!" in output
