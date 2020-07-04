# SimpleEDA
SimpleEDA is a wrapper around Pandas for Exploratory Data Analysis(EDA).You can perform Initial EDA with just 3 or 4 lines of code. SimpleEDA can perform basic EDA operations with less code and less hassle.

## Installation
You can install SimpleEDA via pip. Write this command in terminal and voila, you have installed SimpleEDA.

        pip install SimpleEDA
        
It will auto install dependencies and you don't need to worry about anything.

# Functions
SimpleEDA class has 8 functions that you can use. 

### Function 1 SimpleEDA.summary()
Summary function is the main function of SimpleEDA. DataFrame is the input and it does not return anything but prints the output.
In output you get Statistical summary of DataFrame like mean, median etc. Then you will get DataFrame rows and columns, null value count,
column types in numeric and categorical class, unique value count and duplicate rows information.

### Function 2 SimpleEDA.gua_hist_num()
Graphical univariate analysis function accepts a DataFrame as input and plots histograms of each numeric column. This may take time based on number of columns and rows. It accepts only numerical columns. Don't worry, we can get numeric columns from your DataFrame.

### Function 3 SimpleEDA.gua_bar_cat()
Graphical univariate analysis function accepts a DataFrame as input and plots bar charts of each categorical column. This may take time based on number of columns and rows. It accepts only categorical columns. Don't worry, we can get categorical columns from your DataFrame.

### Function 4 SimpleEDA.corr_columns()
Correlation columns accepts DataFrame and a threshhold. It returns a list of highly correlated columns based on your threshhold.

### Function 5 SimpleEDA.find_outliers()
Find outliers function accepts DataFrame, a string for method argument(default: z-score, accepts iqr also) and a int for thresh argument. If you have provided iqr, you don't need to pass thresh. Return 2 numpy arrays, first one gives you rows and second one gives you column. For example array([23]) array([3]) means 23rd row is outlier on basis of 3rd column value. e.g [23][3]

### Function 6 SimpleEDA.plot_boxplot()
Plot Boxplot function accepts DataFrame and plot boxplot for each column. This may take time based on number of columns and rows. It accepts only numerical columns. Don't worry, we can get numerical columns from your DataFrame.

### Function 7 SimpleEDA.plot_scatterplots()
Plot scatterplot function accepts DataFrame and plot scatterplot for each column. Accepts a string containing a target column name. This may take time based on number of columns and rows. It accepts only numerical columns. Don't worry, we can get numerical columns from your DataFrame.

### Function 8 SimpleEDA.feature_selection()
This function selected important features from input DataFrame. Accepts DataFrame and a target column. This may take time based on number of columns and rows. It accepts only numerical columns. Don't worry, we can get numerical columns from your DataFrame.

# About Author
Hi there, My name is Muhammad Shahid and I am working as Data Scientist in Five Rivers Technologies. I have done BSCS from COMSATS University Islamabad and MSCS from NUCES FAST Islamabad. I have expertise in Data Science, Machine Learning(ML) and Natural Language Processing(NLP). If you have any query about this project, you may reach me at chshahidhamdam@gmail.com
