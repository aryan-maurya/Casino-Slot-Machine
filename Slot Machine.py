import random

MAX_LINES = 3
MAX_BET = 2000
MIN_BET = 10
ROWS = 3
COLS = 3

symbol_count = {"🍌": 2, "💲": 4, "🃏": 6, "🍭": 8}

symbol_value = {"💲": 5, "🃏": 4, "🍭": 3, "🍌": 2}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_spin(rows,cols,symbols):
    all_symbols = []
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


def deposit():
    while True:
        amount = input("What amount would you like to deposit? ₹ ")
        if amount.isdigit():
            amount = int(amount)
            if amount >= 100:
                break
            else:
                print("Minimum deposit amout is ₹100.")
        else:
            print("Please enter a valid amount.")

    return amount


def get_lines():
    while True:
        lines = input("Enter the number of rows you want to bet on (1- "+str(MAX_LINES)+ ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter number of rows in given range.")
        else:
            print("Please enter a number.")

    return lines


def get_bet():
    while True:
        amount = input("What amount would you like to bet on each row? : ₹ ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount should be between ₹{MIN_BET} - ₹{MAX_BET}.")
        else:
            print("Please enter a valid amount.")

    return amount


def spin(balance):
    lines = get_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough balance to bet that amount, your current balance is ₹{balance}.")
        else:
            break

    print(f"You're betting ₹{bet} on {lines} lines. Total bet is equal to: ₹{total_bet}")

    slots = get_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ₹{winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ₹{balance}.")
        ans = input("Press enter to play, (q to quit).")
        if ans == "q":
            break
        balance += spin(balance)

    print(f"You're left with ₹{balance}.")

main()
