import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as st
from distfit import distfit
import numpy as np
from pprint import pprint

data = pd.read_csv('interevent_time.csv', names=['index', 'interevent_time'], skiprows=1)
data = data['interevent_time']
y, x = np.histogram(data, bins=50, density=True)
x = (x + np.roll(x, -1))[:-1] / 2.0

dists = {
    'exponential': st.expon,
    'gamma': st.gamma,
    'weibull': st.weibull_min,
    'lognormal': st.lognorm
}

plt.hist(data, bins=50, density=True, label='data')
for i, (name, dist) in enumerate(dists.items()):
    args = dist.fit(y)
    prob = st.kstest(y, dist.cdf, args)
    pprint(f'For {name}: MLE parameters = {args} and K-S test results = {prob}')
# Get line for each distribution (and scale to match observed data)
    pdf_fitted = dist.pdf(x, *args[:-2], loc=args[-2], scale=args[-1])

    # Add the line to the plot
    plt.plot(x, pdf_fitted, label=f'{name} ({prob[-1]})')

plt.legend(loc='upper left')
plt.show()
