# SimpleEDA
SimpleEDA is a wrapper around Pandas for Exploratory Data Analysis(EDA).You can perform Initial EDA with just 3 or 4 lines of code. SimpleEDA can perform basic EDA operations with less code and less hassle.

## Installation
You can install SimpleEDA via pip. Write this command in terminal and voila, you have installed SimpleEDA.
        pip install SimpleEDA
        
It will auto install dependencies and you don't need to worry about anything.

# Functions
SimpleEDA class has 8 functions that you can use. 

## Function 1 SimpleEDA.summary()
Summary function is the main function of SimpleEDA. DataFrame is the input and it does not return anything but prints the output.
In output you get Statistical summary of DataFrame like mean, median etc. Then you will get DataFrame rows and columns, null value count,
column types in numeric and categorical class, unique value count and duplicate rows information.

## Function 2 SimpleEDA.gua_hist_num()
Graphical univariate analysis function accepts a DataFrame as input and plots histograms of each numeric column. This may take time based
on number of columns and rows. It accepts only numerical columns. Don't worry, we can get numeric columns from your DataFrame.


