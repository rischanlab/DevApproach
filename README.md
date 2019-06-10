# DevApproach
Find the most interesting views from all possible views of data set using deviation based approach (i.e., distance) between the probability distribution of target view and the probability distribution of reference view.

###

Data set : https://archive.ics.uci.edu/ml/datasets/student+performance


###

How to use this code? 

1. Download student data set from link above
2. import the data set to PostgreSQL engine 
3. See `config.py` file and update with your setting
4. See `student.py` comment unwanted attributes depends on your need
5. Run `main.py`
6. Input your target query (e.g., want_continue_study='Yes')
7. Input your reference query (e.g., want_continue_study='No' or leave it blank if you want whole data as your reference)
8. See the result on your prompt (depends on how many k on your setting)
10. it also generate result as results.xlsx

###
If you want to run comparison of all attributes as the target query vs. whole data set as the reference, you can make a list of all attributes, modify `devapproach.py` query function (e.g., query2) and do looping. For instance, example in Windows: 

Create dot bat file and do looping: `C:\Anaconda\python.exe C:\Users\XXX\DevApproach\main.py want_continue_study='Yes'%*`

