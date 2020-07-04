#!/usr/bin/env python
# coding: utf-8

# In[95]:


import numpy as np
import string
import operator
import re
import pandas as pd
from scipy import stats
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.linear_model import Lasso, LogisticRegression
from sklearn.feature_selection import SelectFromModel
from sklearn.preprocessing import StandardScaler


# In[128]:



class SimpleEDA():
    '''This class contains all EDA operations you can perform using SimpleEDA.
    '''
    
    def __init__(self, df):
        self.df = df

    
    def summary(self):
        '''
        Lemmatization function accepts a string and return the lemmatized version of that input string.
        This function uses Spacy.
        Input
        ----------
        type : str
            The self argument is used as input and it accepts a string.
        Return
        ----------
        type : str
            returns a lemmatized string,
        '''
        rows, cols =self.shape
        w = list(self.dtypes)
        column = list(self.columns)
        types = {}
        a = list(self.duplicated(subset=None, keep='first'))
        dup_count = a.count(True)
        dup_indices = []
        for i in range(len(a)):
            if a[i] == True:
                dup_indices.append(i)
        duplicateRows = self[self.duplicated()]
        for i in range(len(w)):
            type_check = str(w[i])
            col = str(column[i])
            if 'int' in type_check or 'float' in type_check:
                ty= 'numeric'
            else:
                ty = 'Categorical'
            types[col] = ty
        types = pd.Series(types)
        summary = ("""
\033[1m DataFrame Statistical Summary:\033[0m \n\n {}
\033[1m DataFrame Summmary: \033[0m \n\n Number of Rows: {}\n Number of Columns: {}\n\n
\033[1m Null value count \033[0m \n{}
\033[1m Columns DataTypes:\033[0m \n\n {}\n
\033[1m Unique values count:\033[0m \n\n {}
\033[1m Total Duplicate rows found:\033[0m \n\n {}
\033[1m Duplicate rows indices:\033[0m \n\n {}""".format(self.describe(),rows, cols,self.isnull().sum(),types,self.nunique(), dup_count, dup_indices))
        print(summary)

        if (duplicateRows.shape)[0] != 0:
            print("If you want to print Duplicate rows, Please write yes.")
            dup_a = input()
            if dup_a=='yes':
                print(duplicateRows)
            
    def gua_hist_num(self):
        new_self= self.select_dtypes(include=['int64', 'float64'])
        if len(list(new_self.columns)) < 5:
            new_self.hist(figsize=(10, 10), bins=50, xlabelsize=8, ylabelsize=8, )
        else:
            new_self.hist(figsize=(16, 20), bins=50, xlabelsize=8, ylabelsize=8)
            
    def gua_bar_cat(self):
        new_self= self.select_dtypes(include='object')
        if new_self.empty==False:
            column = list(new_self.columns)
            for c in column:
                selfs = dict(new_self[c].value_counts())
                self_vals = list(selfs.values())
                if len(self_vals)<  30:
                    self_k= list(selfs.keys())
                    plt.figure(figsize=(6,4))
                    plt.bar(self_k, self_vals)
                    plt.title(c)
                    xlocs, xlabs = plt.xticks()
                    xlocs=[i for i in range(0,len(self_k))]
                    xlabs=[i for i in range(0,len(self_k))]
                    for i, v in enumerate(self_vals):
                        plt.text(xlocs[i], v, str(v))
                    plt.show()
                else:
                    print("Too many values in the the graph makes ticks overlapping. We will set large figure size and horizontal Bar graph. Each graph may differ in looks due to difference data size and it may take some moments. If you want to proceed, write yes")
                    ans = input()
                    if ans=='yes':
                        self_k= list(selfs.keys())
                        bina = np.arange(len(self_k))  
                        plt.figure(figsize=(10,150))
                        plt.barh(self_k, self_vals, height=0.8)
                        plt.ylim([0,bina.size])
                        plt.title(c)
                        plt.yticks(bina, self_k)
                        for index, value in enumerate(self_vals):
                            plt.text(value, index, str(value))
                        plt.show()
        else:
            print("No categorical Columns found")
    def corr_columns(self, thresh=0.90):
        corr_matrix = self.corr().abs()
        upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(np.bool))
        to_drop = [column for column in upper.columns if any(upper[column] > thresh)]
        return to_drop
    
    def find_outliers(self, method='z-score', thresh=3):
        new_self= self.select_dtypes(include=['int64', 'float64'])
        if method=='iqr':
            Q1 = new_self.quantile(0.25)
            Q3 = new_self.quantile(0.75)
            IQR = Q3 - Q1
            iqr_df = (new_self < (Q1 - 1.5 * IQR)) | (new_self > (Q3 + 1.5 * IQR))
            return np.where(iqr_df == True)
        else:
            z = np.abs(stats.zscore(new_self))
            return np.where(z > thresh)
        
    def plot_boxplot(self):
        new_self= self.select_dtypes(include=['int64', 'float64'])
        column = list(new_self.columns)
        for c in column:
            fig, axs = plt.subplots(ncols=1)
            sns.boxplot(x=new_self[c])
            
    def plot_scatterplots(self, target):
        new_self= self.select_dtypes(include=['int64', 'float64'])
        column = list(new_self.columns)
        for c in column:
            fig, axs = plt.subplots(ncols=1)
            sns.scatterplot(x=new_self[c], y=new_self[target])
    
    def feature_selection(self, target):
        new_self= self.select_dtypes(include=['int64', 'float64'])
        scaler = StandardScaler()
        scaler.fit(new_self.fillna(0))
        sel_ = SelectFromModel(LogisticRegression(C=1, penalty='l2'))
        sel_.fit(scaler.transform(new_self.fillna(0)), new_self[target])
        selected_feat = new_self.columns[(sel_.get_support())]
        removed_feats = new_self.columns[(sel_.estimator_.coef_ == 0).ravel().tolist()]
        a = list(removed_feats)
        a.append(target)
        cols = new_self.columns
        imt_feats = [x for x in cols if x not in a]
        print("We have found these features to be important:", imt_feats)


# In[129]:


# In[86]:





# In[ ]:

