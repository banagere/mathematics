import numpy as np

# # Q1
# stock_a = [0.03, 0.015, -0.015, 0.02, 0.02]
# stock_b = [0.07, 0.01, -0.03, 0.025, 0.01]
# stock_c = [-0.05, 0.02, -0.015, 0.01, -0.02]

# stock_returns = np.array([stock_a, stock_b, stock_c])

# print(stock_returns)


# # Q2
# stock_weights = np.array([0.2, 0.5, 0.3])

# portfolio_returns = np.dot(stock_weights, stock_returns) # order matters

# print(f"\n Portfolio Returns: {portfolio_returns}")

# # Q3
# correlation_matrix = np.corrcoef(stock_returns)
# print("\nCorrelation Matrix:\n", correlation_matrix)

# # Checking if stock_a and stock_b are linearly dependent
# k = stock_returns[0] / stock_returns[1]  # Element-wise division
# collinear = np.allclose(k, k[0])  # Are all ratios equal?

# if collinear:
#     print("\nStock A and Stock B are collinear.")
# else:
#     print("\nStock A and Stock B are NOT collinear.")

    
    
# # Q4
# # Nearly collinear stock returns (small noise added)
# stock_a = np.array([0.03, 0.015, -0.015, 0.02, 0.02])
# stock_b = 2 * stock_a + np.array([0, 0.0001, -0.0002, 0.0001, 0])  # Slight noise
# # stock_b = 2 * stock_a

# # Compute element-wise ratio
# k = stock_a / stock_b

# tolerance = 0.01  # Allow 1% variation
# collinear = np.all(np.abs(k - k[0]) < tolerance)

# print("\nk values:", k)
# print("\nAre Stock A and Stock B collinear?", collinear)




# Q5
# Simulated stock returns (Stock B has slight noise)
stock_a = np.array([0.03, 0.015, -0.015, 0.02, 0.02, 0.025, -0.01, 0.015, 0.005, 0.02])
stock_b = 2 * stock_a + np.array([0, 0.0001, -0.0002, 0.0001, 0, 0.0003, -0.0005, 0.0002, -0.0001, 0.0001])  

# Compute k values (element-wise ratio)
k = stock_a / stock_b

# Set a tolerance threshold for small noise
tolerance = 0.005  

# Identify days where k deviates too much from its median value
median_k = np.median(k)
divergence_days = np.where(np.abs(k - median_k) > tolerance)[0]

print("\nk values:", k)
print("\nMedian k:", median_k)
print("\nDivergence days (potential mean reversion opportunities):", divergence_days)
