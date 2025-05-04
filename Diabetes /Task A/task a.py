#Task A
# i) Set seed for reproducibility
np.random.seed(8583)

# Taking a random sample of 25 from total population
sample_25 = df.sample(n=25, random_state=8583)
# ii) Calculating mean and highest of glucose values from sample 25 and total population
print(f"Mean of Glucose in Sample 25: {sample_25['Glucose'].mean()}")
print(f"Max of Glucose in Sample 25: {sample_25['Glucose'].max()}")
print(f"Mean of Glucose in Population: {df['Glucose'].mean()}")
print(f"Max of Glucose in Population: {df['Glucose'].max()}")
# Create a summary table
glucose_summary_table = {
    'Diabetes Dataset': ['Population', 'Sample (n=25)'],
    'Mean Glucose': [df['Glucose'].mean(), sample_25['Glucose'].mean()],
    'Max Glucose': [df['Glucose'].max(), sample_25['Glucose'].max()]
}

glucose_df = pd.DataFrame(glucose_summary_table)
glucose_df.set_index('Diabetes Dataset', inplace=True)
print(glucose_df)
# iii)Visualization
plt.figure(figsize=(12, 5))

# Mean Glucose
plt.subplot(1, 2, 1)
sns.barplot(data=glucose_df, x='Diabetes Dataset', y='Mean Glucose', palette='Blues_d')
plt.title('Mean Glucose Comparison')
plt.ylabel('Mean Glucose Level')

# Max Glucose
plt.subplot(1, 2, 2)
sns.barplot(data=glucose_df, x='Diabetes Dataset', y='Max Glucose', palette='Oranges_d')
plt.title('Max Glucose Comparison')
plt.ylabel('Max Glucose Level')

plt.tight_layout()
plt.savefig("glucose_sample_vs_population.png")
plt.show()
