# Optimizing E-commerce Product Page Layout Through A/B Test Analysis: Impact on Add-to-Cart Rate

## Overview

This project analyzes A/B testing data to determine the most effective e-commerce product page layout for maximizing add-to-cart rates.  The analysis involves statistical comparisons of key metrics between different layout variations (A and B) to identify statistically significant differences and inform data-driven optimization strategies.  The results are presented through both console output and visualizations.

## Technologies Used

* Python 3
* Pandas
* Matplotlib
* Seaborn

## How to Run

1. **Install Dependencies:** Navigate to the project directory in your terminal and install the required Python libraries using pip:

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Analysis:** Execute the main script using:

   ```bash
   python main.py
   ```

   Ensure that your data file (assumed to be named `ab_test_data.csv` and located in the same directory) is correctly formatted with relevant columns (e.g., layout variation, add-to-cart events, total views).  Adjust file paths within `main.py` if necessary.

## Example Output

The script will produce the following outputs:

* **Console Output:**  A summary of the A/B test results, including key metrics like conversion rates (add-to-cart rate), confidence intervals, and statistical significance tests (e.g., p-values). This will indicate which layout variation (A or B) performed better.

* **Visualization(s):**  A plot (e.g., `add_to_cart_comparison.png`) visualizing the add-to-cart rates for both layout variations, potentially including error bars to represent confidence intervals, allowing for a clear visual comparison of performance.  This will aid in understanding the magnitude of the difference between the variations.


## Data

The analysis requires a CSV file named `ab_test_data.csv` in the root directory.  This file should contain at least the following columns:

* `layout`:  Indicates the layout variation (A or B).
* `add_to_cart`:  Number of add-to-cart events for each observation.
* `total_views`: Total number of views for each observation.


This structure provides a basic framework for running the analysis.  Further details on specific statistical tests and data preprocessing can be found within the code itself.