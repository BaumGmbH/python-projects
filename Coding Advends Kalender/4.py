def conver_euros(euros):
    coins = {
        2: "2.00€",
        1: "1.00€",
        0.5: "0.50€",
        0.2: "0.20€",
        0.1: "0.10€",
        0.05: "0.05€",
        0.02: "0.02€",
        0.01: "0.01€"
    }

    result = {
        2: 0,
        1: 0,
        0.5: 0,
        0.2: 0,
        0.1: 0,
        0.05: 0,
        0.02: 0,
        0.01: 0
    }

    for coin in coins.keys():
        while euros - coin >= 0:
            result[coin] += 1
            euros -= coin

    # Print Result

    for coin in result.keys():
        print(str(result[coin]) + " x " + coins[coin])

conver_euros(float(input("Please enter a amount of euros: ")))

