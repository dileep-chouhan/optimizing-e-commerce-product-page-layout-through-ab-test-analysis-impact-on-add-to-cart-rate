import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
# --- 1. Synthetic Data Generation ---
np.random.seed(42) # for reproducibility
# Number of users in each group
n_users = 1000
# Simulate A/B test data
data = {
    'group': ['A'] * n_users + ['B'] * n_users,
    'add_to_cart': np.concatenate([
        np.random.binomial(1, 0.15, n_users),  # Group A: 15% add-to-cart rate
        np.random.binomial(1, 0.20, n_users)   # Group B: 20% add-to-cart rate
    ])
}
df = pd.DataFrame(data)
# --- 2. Data Cleaning and Preparation ---
# (In a real-world scenario, this would involve handling missing values, outliers, etc.)
# For this synthetic data, no cleaning is needed.
# --- 3. Analysis ---
# Calculate add-to-cart rates for each group
group_a_rate = df[df['group'] == 'A']['add_to_cart'].mean()
group_b_rate = df[df['group'] == 'B']['add_to_cart'].mean()
# Perform a two-proportion z-test
z_stat, p_value = stats.proportions_ztest(
    [df[df['group'] == 'A']['add_to_cart'].sum(), df[df['group'] == 'B']['add_to_cart'].sum()],
    [n_users, n_users]
)
print(f"Group A Add-to-Cart Rate: {group_a_rate:.4f}")
print(f"Group B Add-to-Cart Rate: {group_b_rate:.4f}")
print(f"Z-statistic: {z_stat:.2f}")
print(f"P-value: {p_value:.3f}")
# Interpret the results
alpha = 0.05
if p_value < alpha:
    print("There is a statistically significant difference between the groups.")
    if group_b_rate > group_a_rate:
        print("Group B (new layout) performs better.")
    else:
        print("Group A (original layout) performs better.")
else:
    print("There is no statistically significant difference between the groups.")
# --- 4. Visualization ---
plt.figure(figsize=(8, 6))
plt.bar(['Group A', 'Group B'], [group_a_rate, group_b_rate], color=['skyblue', 'coral'])
plt.ylabel('Add-to-Cart Rate')
plt.title('A/B Test Results: Add-to-Cart Rates')
plt.ylim(0, 0.25) # set y-axis limit for better visualization
plt.text(0, group_a_rate + 0.01, f'{group_a_rate:.2%}', ha='center')
plt.text(1, group_b_rate + 0.01, f'{group_b_rate:.2%}', ha='center')
# Save the plot
output_filename = 'ab_test_results.png'
plt.savefig(output_filename)
print(f"Plot saved to {output_filename}")