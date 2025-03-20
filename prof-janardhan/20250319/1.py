import numpy as np

# question 1
stock_a_weight = 0.6
stock_b_weight = 0.4

stock_a_returns = 0.02
stock_b_returns = -0.01

weight = np.array([stock_a_weight, stock_b_weight])
returns = np.array([stock_a_returns, stock_b_returns])

portfolio_return = np.dot(weight, returns)

# print(weight)
# print(returns)
print(f"Question 1: {portfolio_return:.2%}")



# question 2
r_1 = np.array([0.02, -0.01, 0.015])
r_2 = np.array([0.03, 0.00, -0.005])

w_1 = 0.5
w_2 = 1 - w_1

ret = w_1 * r_1 + w_2 * r_2

print(f"Question 2: {ret}")

# question 3
w1 = np.array([0.5, 0.3, 0.2])
w2 = np.array([0.6, 0.2, 0.2])

alpha = 0.5
beta = 1 - alpha

new_portfolio = alpha * w1 + beta * w2

if np.isclose(new_portfolio.sum(), 1):
    print(f"Question 3: {new_portfolio}")
else:
    print("Weights do not sum to 1, adjust alpha and beta!")    
