####################
#
#   explore.py
#   ----------
#   
#   Description:
#       Provides functions for visualizing key findings and performing
#       statistical tests to validate analysis conclusions.
#
#   Fields:
#       None
#
#   Functions:
#       distribution_of_customer_churn(df)
#       visualize_churn_rate_versus_contract_type(df)
#       visualize_churn_rate_versus_payment_type(df)
#       visualize_monthly_charges_versus_tenure(df)
#       statistical_tests()
#
####################

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from util.stats_util import *

def distribution_of_customer_churn(df: pd.core.frame.DataFrame) -> None:
    '''
        Display a histogram visualizing the distribution of churn in
        Telco customer dataset.

        Parameters
        ----------
        df: DataFrame
            The expected argument is a pandas dataframe containing the
            Telco customer dataset.
    '''

    sns.histplot(df.churn)
    plt.title('Customers that churn make up roughly a quarter of the customer population')
    plt.show()

def visualize_churn_rate_versus_contract_type(df: pd.core.frame.DataFrame) -> None:
    '''
        Display a histogram visualizing the distribution of customers
        who have churned and those that haven't versus the contract
        type.

        Parameters
        ----------
        df: DataFrame
            The expected argument is a pandas dataframe containing the
            Telco customer dataset.
    '''

    churned = df[df.churn == 'Yes']
    not_churned = df[df.churn == 'No']

    sns.histplot(data = not_churned.contract_type, label = 'Not Churned', color = 'green')
    sns.histplot(data = churned.contract_type, label = 'Churned', color = 'red')
    plt.title('Most customers that are churning are on the month-to-month contract')
    plt.legend()
    plt.show()

def visualize_churn_rate_versus_payment_type(df: pd.core.frame.DataFrame) -> None:
    '''
        Display a histogram visualizing the distribution of customers
        who have churned and those that haven't versus the payment
        type.

        Parameters
        ----------
        df: DataFrame
            The expected argument is a pandas dataframe containing the
            Telco customer dataset.
    '''

    churned = df[df.churn == 'Yes']
    not_churned = df[df.churn == 'No']

    sns.histplot(data = not_churned.payment_type, label = 'Not Churned', color = 'green')
    sns.histplot(data = churned.payment_type, label = 'Churned', color = 'red')
    plt.title('Most customers that are churning use the electronic check payment method')
    plt.xticks(rotation = 30)
    plt.legend()
    plt.show()

def visualize_monthly_charges_versus_tenure(df: pd.core.frame.DataFrame) -> None:
    '''
        Display a histogram visualizing the distribution of monthly charges
        for customers who have churned and have tenure less than or equal to
        24 months. Additionally the percentage of customers who have churned
        that are in this group is displayed.

        Parameters
        ----------
        df: DataFrame
            The expected argument is a pandas dataframe containing the
            Telco customer dataset.
    '''

    churn_customers = df[df.churn == 'Yes']
    print(f'tenure less than or equal to 24, percentage of churn pop.: {(churn_customers.tenure <= 24).mean():.2%}')

    sns.histplot(data = churn_customers[churn_customers.tenure <= 24], x = 'monthly_charges')
    plt.title('Customers with 2 years or less of tenure that have churned')
    plt.show()

def statistical_tests():
    pass