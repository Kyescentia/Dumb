from customUtils import generate_random_number, read_guess, win_or_lose, record_game, print_records

# Simulate the gameplay of a coin flipping game
def flip_coin_game():
    while True:
        answer = generate_random_number()
        guess = read_guess()
        if guess == 0:
            break
        result = win_or_lose(answer, guess)
        record_game(answer, guess, result)

    print("\nThank you for playing coin-flipping game!\n")
    print_records()


flip_coin_game()