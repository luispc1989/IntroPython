# Import librarie
import pandas as pd

# Load Kiva's Loans Dataset
df = pd.read_csv(r"C:\Users\Luís Pinto Coelho\Desktop\Introdução ao Python\Assignment3\kiva_loans.csv")

# Inspection of the data
print("First 5 rows of the dataset:\n", df.head(), "\n\nDataset Information:")
df.info()

# Requirement 1: Select rows using string methods and numerical conditions
# Example: Select Loans for 'Agriculture' sector in the 'Philippines' with Loan amount > 1000
filtered_df = df.query("country == 'Philippines' and sector == 'Agriculture' and loan_amount > 1000")[['id', 'loan_amount', 'activity', 'sector', 'country']]
print("\nFiltered rows (Agriculture, Philippines, loan > 1000):\n", filtered_df.head())

# Requirment 2: Sort table using one or more columns
# Example: Sort the data by 'Loan_amount' in descending order
print("\nTop 5 loans sorted by 'loan_amount' in descending order:\n", df[['country', 'sector', 'loan_amount']].sort_values(by='loan_amount', ascending=False).head())

# Requirment 3: Group and aggregate rows using "groupby"
# Example: Group by 'country' and calculate total and average loan amount 
country_loan_summary = df.groupby('country', as_index=False).agg(total_loan_amount=('loan_amount', 'sum'), average_loan_amount=('loan_amount', 'mean'), loan_count=('loan_amount', 'count'))
print("\nLoan summary by country (total, average, count):\n", country_loan_summary.head(6).set_index(pd.Index(range(1, len(country_loan_summary.head(6)) + 1))))

# Requirement 4: Create a new variable with "apply" and "Lambda"
# Example: Categorize loans into 'Small', 'Medium', and 'Large' based on 'Loan_amount'
df['loan_size_category'] = df['loan_amount'].apply(lambda x: 'Small' if x < 500 else 'Medium' if x < 2000 else 'Large')
print("\nLoan size categories (first 5 rows):\n", df[['loan_amount', 'loan_size_category']].head(5).set_index(pd.Index(range(1, len(df.head(5)) + 1))))

# Save the transformed DataFrame as a new CSV in UTF-8 format with comma separator
output_path = r"C:\Users\Luís Pinto Coelho\Desktop\Introdução ao Python\Assignment3\kiva_loans_analysis.csv"
with open(output_path, 'w', encoding='utf-8') as file:
    file.write('sep=,\n')  # Escreve a linha separadora no início
    df.to_csv(file, index=False, encoding='utf-8', sep=',')  # Salva o DataFrame no arquivo
print(f"\nTransformed DataFrame successfully saved to: {output_path}")
