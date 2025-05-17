import pandas as pd
# Load dataset
df= pd.read_csv('owid-covid-data.csv')
# Check columns
print(df.columns)
# Preview rows
print(df.head())
#Identify missing values
print(df.isnull().sum())

# Data Cleaning
# Filter countries of interest
countries_of_interests=['USA','India','Kenya', 'South Africa']
# Drop rows with missing data
df = df.dropna(subset=['continent','date','new_cases','new_deaths'])
# Convert date column to datetime
df['date']=pd.to_datetime(df['date'])
# Handle numeric missing values
# ...existing code...

# Handle missing numeric values with interpolation
numeric_values = ['new_cases', 'new_deaths', 'total_cases', 'total_deaths', 'total_vaccinations']
for col in numeric_values:
    if col in df.columns:
        df[col] = df[col].interpolate(method='linear')

# Exploratory Data Analysis (EDA)
# Plot total cases over time for selected countries.
import matplotlib.pyplot as plt
import seaborn as sns

selected_countries= ['USA','Kenya','India','South Africa']
plt.figure(figsize=(11, 8))
for country in selected_countries:
    country_data=df[df['location']==country]
    plt.plot(country_data['date'],country_data['total_cases'], label=country)

    plt.title('Total COVID19 Cases over Time')
    plt.xlabel('Date')
    plt.ylabel('Total Cases')
    plt.legend()
    plt.show()
    plt.tight_layout()

# Total deaths over time
plt.figure(figsize=(11, 6))
for country in selected_countries:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['total_deaths'], label=country)
    plt.title('Total Death Cases over Time')
    plt.xlabel('Date')
    plt.ylabel('Total Deaths')
    plt.legend()
    plt.show()
    plt.tight_layout()

# Compare daily new cases between countries.
    plt.title('Daily New COVID19 Cases over Time')
    plt.xlabel('Date')
    plt.ylabel('Daily New Cases')
    plt.legend()
    plt.show()
    plt.tight_layout()

    # Calculate death rates
    df['death_rate']= df['total_deaths'] / df['total_cases']

# Visualizations(Bar charts)
# Bar chart: Top 10 countries by total cases (latest date)
latest_date = df['date'].max()
latest_data = df[df['date'] == latest_date]
top_countries = latest_data.groupby('location')['total_cases'].max().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x=top_countries.values, y=top_countries.index, palette='viridis')
plt.title('Top 10 Countries by Total COVID-19 Cases (Latest Date)')
plt.xlabel('Total Cases')
plt.ylabel('Country')
plt.tight_layout()
plt.show()

# Visualizing Vaccination Progress
plt.figure(figsize=(11, 8))
for country in selected_countries:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['total_vaccinations'], label=country)
    
plt.title('COVID-19 Vaccination Cases over Time')
plt.xlabel('Date')
plt.ylabel('Total Vaccinations')
plt.legend()
plt.show()
plt.tight_layout()

#Compare % vaccinated population.
plt.figure(figsize=(11, 8))
for country in selected_countries:
    country_data = df[df['location'] == country]
    if 'people_vaccinated_per_hundred' in country_data.columns:
        plt.plot(country_data['date'], country_data['people_vaccinated_per_hundred'], label=country)

plt.title('Percentage of Population Vaccinated Over Time')
plt.xlabel('Date')
plt.ylabel('% Vaccinated (per hundred)')
plt.legend()
plt.tight_layout()
plt.show()

# Optional: Pie chart for vaccinated vs. unvaccinated (latest date, selected country)
country = 'USA'  #Change as needed
latest_country_data = df[(df['location'] == country) & (df['date'] == df['date'].max())]
if not latest_country_data.empty and 'people_vaccinated_per_hundred' in latest_country_data.columns:
    vaccinated = latest_country_data['people_vaccinated_per_hundred'].values[0]
    unvaccinated = 100 - vaccinated
    plt.figure(figsize=(6, 6))
    plt.pie([vaccinated, unvaccinated], labels=['Vaccinated', 'Unvaccinated'], autopct='%1.1f%%', colors=['Blue', 'Green'])
    plt.title(f'Vaccinated vs. Unvaccinated in {country} (Latest Date)')
    plt.show()

    