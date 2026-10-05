# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///
## Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# COMMAND ----------

# MAGIC %md
# MAGIC ##Tests for Customer Table
# MAGIC

# COMMAND ----------

##Data Ingestion for Customers table

customers=spark.table("shop_performance.shop.customers").toPandas()
display(customers)

# COMMAND ----------

##Checking the information of the table
customers.info()

# COMMAND ----------

## Printing the Column list for this dataset
print(customers.columns.tolist())

# COMMAND ----------

##Checking for duplicates 
customers.duplicated().sum()

# COMMAND ----------

##Checking for Unique values
print(customers["CustomerID"].value_counts(dropna=False))

# COMMAND ----------

##Checking for null values
print(customers.isnull().sum())

# COMMAND ----------

##Checking for minimum, maximum, and average
age_numeric = pd.to_numeric(customers["Age"], errors="coerce")
print(age_numeric.min())
print(age_numeric.max())
print(age_numeric.mean())

# COMMAND ----------

## Replacing the Null Age values with Average age
customers['Age'] = pd.to_numeric(customers['Age'], errors='coerce')
mean_age = round(customers['Age'].mean(),0)
customers['Age'] = customers['Age'].fillna(mean_age)


# COMMAND ----------

##Checking the values
customers["City"].value_counts()

# COMMAND ----------

##Replacing the Null Cities with "Unknown"
customers["City"] = customers["City"].fillna("Unknown")

# COMMAND ----------

##Changing the names of the City to One name
customers["City"] = customers["City"].str.title()


# COMMAND ----------

##Changing the name of the City
customers["City"] = customers["City"].str.strip().str.title()
customers["City"] = customers["City"].replace("Mashad", "Mashhad")

# COMMAND ----------

## Ensuring that the dates are well structured and removing Null dates with modal date
customers["SignupDate"] = pd.to_datetime(customers["SignupDate"], errors="coerce")
customers["SignupDate"] = customers["SignupDate"].fillna(customers["SignupDate"].mode())


# COMMAND ----------

##Replacing the Null CustomerSegment with "Unknown"
customers["CustomerSegment"] = customers["CustomerSegment"].fillna("Unknown")

# COMMAND ----------

print(customers.describe(include="all"))

# COMMAND ----------

# MAGIC %md
# MAGIC ##Tests for Order Table

# COMMAND ----------

##Data Ingestion for Orders table

orders=spark.table("shop_performance.shop.orders")
orders=orders.toPandas()
display(orders)

# COMMAND ----------

##Check the orders table information
orders.info()

# COMMAND ----------

##Checking for duplicates 
orders.duplicated().sum()

# COMMAND ----------

## Removing Duplicates on the Orders Table
orders = orders.drop_duplicates()

# COMMAND ----------

print(orders.describe(include="all"))

# COMMAND ----------

## Printing the Column list for this dataset
print(orders.columns.tolist())

# COMMAND ----------

## Unique customers
print("Unique Customers:", orders["CustomerID"].nunique())

## Unique products
print("Unique Products:", orders["ProductID"].nunique())

# COMMAND ----------

##Checking the Min and Max of the data points Quantity and Discount values
orders["Quantity"] = pd.to_numeric(orders["Quantity"], errors="coerce")
orders["Discount"] = pd.to_numeric(orders["Discount"], errors="coerce")
print(orders["Quantity"].min(), orders["Quantity"].max())
print(orders["Discount"].min(), orders["Discount"].max())


# COMMAND ----------

print(orders.isnull().sum())

# COMMAND ----------

##Repalcing the Blank spaces with a mean value in the Discount column and Ensuring there are no errors
orders["Discount"] = pd.to_numeric(orders["Discount"], errors="coerce")
orders["Discount"] = orders["Discount"].fillna(orders["Discount"].mean())

# COMMAND ----------

##Repalcing the Blank spaces with a mean value in the Quantity column and Ensuring there are no errors
orders["Quantity"] = pd.to_numeric(orders["Quantity"], errors="coerce")
orders["Quantity"] = orders["Quantity"].fillna(orders["Quantity"].mean())

# COMMAND ----------

##Replacing Null payment methods with Unknown
orders["PaymentMethod"] = orders["PaymentMethod"].fillna("Unknown")

# COMMAND ----------

## Ensuring there dates are well structured and replaced Null dates with Modal dates
orders["OrderDate"] = pd.to_datetime(orders["OrderDate"], errors="coerce")
orders["OrderDate"] = orders["OrderDate"].fillna(orders["OrderDate"].mode())

# COMMAND ----------

print(orders.describe(include="all"))

# COMMAND ----------

# MAGIC %md
# MAGIC ##----------------------------------------------------------------------------------------------------------

# COMMAND ----------

# MAGIC %md
# MAGIC ##Tests For Payments Table

# COMMAND ----------

##Data Ingestion for Payments Table

payments=spark.table("shop_performance.shop.payments")
payments=payments.toPandas()
display(payments)

# COMMAND ----------

payments.info()

# COMMAND ----------

##Checking for payments duplicates
payments.duplicated().sum()

# COMMAND ----------

##Checking for Null values 
print(payments.isnull().sum())

# COMMAND ----------

## Ensuring there dates are well structured and replaced Null dates with Modal dates
payments["PaymentDate"] = pd.to_datetime(payments["PaymentDate"], errors="coerce")
payments["PaymentDate"] = payments["PaymentDate"].fillna(payments["PaymentDate"].mode())

# COMMAND ----------

##Reviewing the statistics of the data
print(payments.describe(include="all"))

# COMMAND ----------

# MAGIC %md
# MAGIC ##Tests For Products Table

# COMMAND ----------

##Data Ingestion for Products Table

products=spark.table("shop_performance.shop.products")
products=products.toPandas()
display(products)

# COMMAND ----------

products.info()

# COMMAND ----------

##Checking for products duplicates
products.duplicated().sum()

# COMMAND ----------

##Reviewing the Null Values on Products Table
print(products.isnull().sum())

# COMMAND ----------

# DBTITLE 1,Cell 47
##Correcting the Numeric Errors and using Mean to Replace Nulls even though they are not there
products["UnitPrice"] = pd.to_numeric(products["UnitPrice"], errors="coerce")
products["UnitPrice"] = products["UnitPrice"].fillna(products["UnitPrice"].mean())

# COMMAND ----------

##Chekcing the Min and Max 
print(products["UnitPrice"].min(), products["UnitPrice"].max())

# COMMAND ----------

##Reviewing the statistics of the data
print(products.describe(include="all"))

# COMMAND ----------

# MAGIC %md
# MAGIC ##----------------------------------------------------

# COMMAND ----------

# MAGIC %md
# MAGIC ##Consolidated Code from Customers, Orders, Payments and Products

# COMMAND ----------

data = orders.merge(
    products,
    on="ProductID",
    how="left"
)

data = data.merge(
    customers,
    on="CustomerID",
    how="left"
)

payment_status = payments.groupby("OrderID")["PaymentStatus"].first().reset_index()

data = data.merge(
    payment_status,
    on="OrderID",
    how="left"
)
display(data)

# COMMAND ----------



# COMMAND ----------

##Calculate Revenue using the Quantity, Unitprice and the Discount 
data["Revenue"] = (
    data["Quantity"]
    * data["UnitPrice"]
    * (1 - data["Discount"])
)

# COMMAND ----------

##Excluding the revenue on orders that were returned or canceled by customers
revenue_data = data[
    ~data["Status"].str.lower().isin(["cancelled", "canceled", "returned"])
].copy()

# COMMAND ----------

##Conducting date function accroding to day name, month name, and year
revenue_data["OrderDate"] = pd.to_datetime(revenue_data["OrderDate"])
revenue_data["Year"] = revenue_data["OrderDate"].dt.year
revenue_data["Month"] = revenue_data["OrderDate"].dt.month
revenue_data["YearMonth"] = revenue_data["OrderDate"].dt.to_period("M")

# COMMAND ----------

total_revenue = revenue_data["Revenue"].sum()

total_orders = revenue_data["OrderID"].nunique()

average_order_value = total_revenue / total_orders

# COMMAND ----------

monthly_revenue = (
    revenue_data
    .groupby("YearMonth")["Revenue"]
    .sum()
    .reset_index()
)

# COMMAND ----------

##Monthly Revenue growth
monthly_revenue["Growth"] = (
    monthly_revenue["Revenue"].pct_change() * 100
)

# COMMAND ----------

## Ensuring that the dates are well structured and removing Null dates with modal date
data["SignupDate"] = pd.to_datetime(data["SignupDate"], errors="coerce")
data["SignupDate"] = data["SignupDate"].fillna(data["SignupDate"].mode())

# COMMAND ----------

## Ensuring that the dates are well structured and removing Null dates with modal date
data["OrderDate"] = pd.to_datetime(data["OrderDate"], errors="coerce")
data["OrderDate"] = data["OrderDate"].fillna(data["OrderDate"].mode())

# COMMAND ----------

## Replacing the Null Age values with Average age
data['Age'] = pd.to_numeric(data['Age'], errors='coerce')
mean_age = round(data['Age'].mean(),0)
data['Age'] = data['Age'].fillna(mean_age)

# COMMAND ----------

##Replacing the Null CustomerSegment with "Unknown"
data["CustomerSegment"] = data["CustomerSegment"].fillna("Unknown")

# COMMAND ----------

##Replacing the Null Cities with "Unknown"
data["City"] = data["City"].fillna("Unknown")

# COMMAND ----------

##Conducting the date Functions
data["SignupDate"] = pd.to_datetime(data["SignupDate"])

data["Month"] = data["SignupDate"].dt.month_name()
data["Day"] = data["SignupDate"].dt.day_name()
data["Year"] = data["SignupDate"].dt.year

# COMMAND ----------

##Conducting the IF statement to categorize age groups
age_numeric = pd.to_numeric(customers["Age"], errors="coerce")
def age_group(age):
    if age <= 19:
        return "Teenagers"
    elif age <= 35:
        return "Youth"
    elif age <= 64:
        return "Adults"
    else:
        return "Pensioners"

data["Age_Group"] = pd.to_numeric(data["Age"], errors="coerce").apply(age_group)

# COMMAND ----------

##Categorizing the UnitPrices
def price_category(price):
    if price < 35:
        return "Cheaper"
    elif price < 65:
        return "Cheap"
    elif price <= 120:
        return "Pricey"
    else:
        return "Expensive"

data["Price_Category"] = data["UnitPrice"].apply(price_category)

# COMMAND ----------

##Categorizing the Quantity 
def quantity_category(quantity):
    if quantity <= 1:
        return "Low Quantity"
    elif quantity <= 3:
        return "Medium Quantity"
    elif quantity <= 5:
        return "High Quantity"
    else:
        return "Too Much"

data["Quantity_Category"] = data["Quantity"].apply(quantity_category)

# COMMAND ----------

##Categorizing the Revenue by Worst to great
def revenue_category(revenue):
    if revenue <= 0:
        return "Worst Revenue"
    elif revenue <= 100:
        return "Bad Revenue"
    elif revenue <= 200:
        return "Good Revenue"
    elif revenue <= 500:
        return "Great Revenue"
    elif revenue <= 1300:
        return "Best Revenue"
    else:
        return "Above"
        
data["Revenue_Category"] = data["Revenue"].apply(revenue_category)


# COMMAND ----------

##Displaying the Final Data
display(data)

# COMMAND ----------

data.info()