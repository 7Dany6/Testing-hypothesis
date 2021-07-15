"""
The first Oscar winners got their prizes in 1929.
We have data concerning 100 women and 100 men as well.
We are going to use t-test in order to find out whether differences between age of women and men statistically reliable.
Average age of men is 45, standard deviation = 9
Average age of women if 34, standard deviation = 10
Our null hypothesis goes like this: average population age of women = average population age of men
Alternative hypothesis follows: average population mean of women != average population mean of men
"""
import math
import numpy as np
import scipy.stats as st

average_men = 45
sd_men = 9

average_women = 34
sd_women = 10

number_of_people = 100
alpha = 0.95

se = math.sqrt((sd_men**2 / number_of_people + sd_women**2 / number_of_people))
t = (average_men - average_women) / se

df = number_of_people + number_of_people - 2

# providing two-sided test
p_value = np.abs(st.t.ppf((1 - alpha) / 2, df))

print(f'p-value of {alpha*100}% confidence interval is {p_value}, whereas t is {t}')

if t > p_value:
    print('Reject null hypothesis!')
else:
    print('Accept null hypothesis!')

"""
Finally, we accept our alternative hypothesis which means that 'average population age of women != average population age of men'
"""