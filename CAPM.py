def capm(expected_market_return, risk_free_rate, beta):
    return risk_free_rate + beta * (expected_market_return - risk_free_rate)


# Example inputs
expected_market_return = 0.15  # Market return
risk_free_rate = 0.05  # Risk-free rate
beta = 1.8  # Beta of the stock

expected_return = capm(expected_market_return, risk_free_rate, beta)
print(f"Expected Return: {expected_return * 100:.2f}%")


