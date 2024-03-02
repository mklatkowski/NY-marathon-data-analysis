import pandas as pd
import matplotlib.pyplot as plt
import datetime
import random

pd.set_option("display.max_rows", None)
data = pd.read_csv('cleared_runners_data.csv')

#zebranie danych o liczbie biegaczy w zależności od parametru
age_counts = data['Age'].value_counts().sort_index()
sex_counts = data['Sex'].value_counts().sort_index()
country_counts = data['Country'].value_counts().sort_values(ascending=True)

#zebranie danych o wynikach biegaczy w zależności od parametru
data['Time'] = pd.to_timedelta(data['Result']).dt.total_seconds()
avg_result_by_age = data.groupby('Age')['Time'].mean()

avg_result_by_country = data.groupby('Country')['Time'].mean()
avg_result_by_country = avg_result_by_country.sort_values()

avg_result_by_sex = data.groupby('Sex')['Time'].mean()

def number_by_age():
    plt.figure(figsize=(20, 6))
    plt.bar(age_counts.index, age_counts.values)
    plt.xlabel('Wiek')
    plt.ylabel('Ilość osób')
    plt.title('Ilość osób w danym wieku')
    plt.xticks(age_counts.index)

def number_by_sex():
    plt.figure(figsize=(5, 6))
    plt.bar(sex_counts.index, sex_counts.values)
    plt.xlabel('Płeć')
    plt.ylabel('Ilość osób')
    plt.title('Ilość osób w danej płci')
    plt.xticks(sex_counts.index)

def number_by_country():
    plt.figure(figsize=(60, 6))
    plt.yscale('log')
    plt.bar(country_counts.index, country_counts.values)
    plt.xlabel('Narodowość')
    plt.ylabel('Ilość osób')
    plt.title('Ilość osób w danej narodowości')
    plt.xticks(country_counts.index, rotation=90)

def result_by_age():
    plt.figure(figsize=(10, 6))
    plt.bar(avg_result_by_age.index, avg_result_by_age.values)
    plt.xlabel('Wiek')
    plt.ylabel('Średni wynik')
    plt.title('Średni wynik biegu w zależności od wieku')
    plt.xticks(rotation=45)
    plt.grid(True)

def result_by_country():
    plt.figure(figsize=(80, 6))
    plt.bar(avg_result_by_country.index, avg_result_by_country.values)
    plt.xlabel('Narodowość')
    plt.ylabel('Średni wynik')
    plt.title('Średni wynik biegu w zależności od narodowości')
    plt.xticks(rotation=45)
    plt.grid(True)

def result_by_sex():
    plt.figure(figsize=(6, 6))
    plt.bar(avg_result_by_sex.index, avg_result_by_sex.values)
    plt.xlabel('Płeć')
    plt.ylabel('Średni wynik')
    plt.title('Średni wynik biegu w zależności od płci')
    plt.xticks(rotation=45)
    plt.grid(True)


if __name__ == '__main__':
    number_by_country()
    number_by_age()
    number_by_sex()
    result_by_country()
    result_by_age()
    result_by_sex()
    plt.show()