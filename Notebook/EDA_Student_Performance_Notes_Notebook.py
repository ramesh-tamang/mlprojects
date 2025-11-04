"""
EDA_Student_Performance_Notes_Notebook.py

Copy-friendly Jupyter Notebook style Python file for Student Performance EDA.

Contents:
- Structured notes in Markdown cells
- Example EDA code with plots (histograms, boxplots, correlations)
- Helper functions to save notes or run example EDA

Usage:
- Copy this into a Jupyter notebook (.ipynb) or run as a Python script in VS Code/Jupyter.
"""

NOTES = r"""
# Student Performance — EDA Notebook

## 1. Purpose
Explore student performance dataset to find patterns and factors influencing academic outcomes.

## 2. Example Dataset Columns
- `student_id`, `gender`, `age`, `parental_education`, `lunch`, `test_preparation`, `math_score`, `reading_score`, `writing_score`, `attendance_rate`

## 3. EDA Steps
1. Load and inspect data
2. Clean missing values / duplicates
3. Descriptive statistics
4. Visualizations: histograms, boxplots, bar charts, scatterplots, heatmaps
5. Grouped summaries and pivot tables
6. Optional statistical tests
7. Feature engineering: average_score, score_category, pass/fail
8. Quick modeling preparation checklist
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('whitegrid')

# Helper functions
def save_notes_md(filename='EDA_Student_Performance_Notes.md'):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(NOTES)
    print(f"Saved notes to {filename}")

def example_eda(csv_path='data/stud.csv'):
    df = pd.read_csv(csv_path)
    print('--- Head ---')
    print(df.head())
    print('\n--- Info ---')
    print(df.info())

    # Derived column
    df['average_score'] = df[['math_score','reading_score','writing_score']].mean(axis=1)

    # Histogram
    plt.figure(figsize=(8,4))
    sns.histplot(df['average_score'], kde=True, bins=20, color='skyblue')
    plt.title('Average Score Distribution')
    plt.xlabel('Average Score')
    plt.show()

    # Boxplot by gender
    plt.figure(figsize=(8,4))
    sns.boxplot(x='gender', y='average_score', data=df, palette='Set2')
    plt.title('Average Score by Gender')
    plt.show()

    # Correlation heatmap
    numeric_cols = df.select_dtypes(include='number')
    plt.figure(figsize=(6,5))
    sns.heatmap(df[numeric_cols].corr(), annot=True, fmt='.2f', cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.show()

    # Grouped summary by test preparation
    summary = df.groupby('test_preparation')[['math_score','reading_score','writing_score','average_score']].mean()
    print('\n--- Grouped Summary by Test Preparation ---')
    print(summary)

    return df

if __name__ == '__main__':
    save_notes_md()
    print('\nRun example_eda("data/stud.csv") to see EDA plots.')
