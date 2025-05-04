#Task C
# Set seed for reproducibility
np.random.seed(8583)

# Store results
bootstrap_means = []
bootstrap_stds = []
bootstrap_98th = []

# Creating 500 samples of size 150
for _ in range(500):
    sample = df.sample(n=150, replace=True)
    bp = sample['BloodPressure']
    bootstrap_means.append(bp.mean())
    bootstrap_stds.append(bp.std())
    bootstrap_98th.append(np.percentile(bp, 98))
  
#Calculating Population statistics
population_mean = df['BloodPressure'].mean()
population_std = df['BloodPressure'].std()
population_98th = np.percentile(df['BloodPressure'], 98)

# Calculating Bootstrap Averages
bootstrap_mean_average = np.mean(bootstrap_means)
bootstrap_std_average = np.mean(bootstrap_stds)
bootstrap_98th_average = np.mean(bootstrap_98th)

# Summary DataFrame
bp_compare = pd.DataFrame({
    'Statistic': ['Mean', 'Standard Deviation', '98th Percentile'],
    'Population': [population_mean, population_std, population_98th],
    'Bootstrap Average': [bootstrap_mean_average, bootstrap_std_average, bootstrap_98th_average]
})

print(bp_compare)
# Visualization
#comparing statistics of Population and bootstrap averages of blood pressure
bp_melted = bp_compare.melt(id_vars='Statistic', var_name='Source', value_name='Value')

# Barplot
plt.figure(figsize=(10, 6))
sns.barplot(data=bp_melted, x='Statistic', y='Value', hue='Source')
plt.title('BloodPressure: Population vs Bootstrap (500 Samples of 150)')
plt.ylabel('Value')
plt.tight_layout()
plt.show()

