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
    'exponential': {
        'st': st.expon,
        'mle': [1.594323],
        'mme': [1.594322],
    },'gamma': {
        'st': st.gamma,
        'mle': [0.8055547, 1.2842414],
        'mme': [0.4913494, 0.7833695],
    }, 'weibull': {
        'st': st.weibull_min,
        'mle': [0.8456672, 0.5691232],
        'mme': [0.7153732, 0.5056480],
    }, 'lognormal': {
        'st': st.lognorm,
        'mle': [-1.202592,1.359600],
        'mme': [-1.021589, 1.053699],
    },
}

# mle
plt.hist(data, bins=50, density=True, label='data', alpha=0.5)
plt.plot(x, dists['exponential']['st'].pdf(x,
        scale=1/dists['exponential']['mle'][0]),
        label='exponential')
plt.plot(x, dists['gamma']['st'].pdf(x,
        a=dists['gamma']['mle'][0], scale=1/dists['gamma']['mle'][1]),
        label='gamma')
plt.plot(x, dists['weibull']['st'].pdf(x,
        c=dists['weibull']['mle'][0], scale=1/dists['gamma']['mle'][1]),
        label='weibull')
plt.plot(x, dists['lognormal']['st'].pdf(x,
        dists['lognormal']['mle'][1], 0, np.exp(dists['lognormal']['mle'][0])),
        label='lognormal')

plt.legend(loc="upper right")
plt.title('Distribution fit using MLE')
plt.savefig('mle-fit.jpg')
plt.ylabel('pdf value')
plt.xlabel('Interevent time')
plt.show()

# mme
plt.hist(data, bins=50, density=True, label='data', alpha=0.5)
plt.plot(x, dists['exponential']['st'].pdf(x,
        scale=1/dists['exponential']['mme'][0]),
        label='exponential')
plt.plot(x, dists['gamma']['st'].pdf(x,
        a=dists['gamma']['mme'][0], scale=1/dists['gamma']['mme'][1]),
        label='gamma')
plt.plot(x, dists['weibull']['st'].pdf(x,
        c=dists['weibull']['mme'][0], scale=1/dists['gamma']['mme'][1]),
        label='weibull')
plt.plot(x, dists['lognormal']['st'].pdf(x,
        dists['lognormal']['mme'][1], 0, np.exp(dists['lognormal']['mme'][0])),
        label='lognormal')

plt.legend(loc="upper right")
plt.title('Distribution fit using MOM (MME in R)')
plt.savefig('mme-fit.jpg')
plt.ylabel('pdf value')
plt.xlabel('Interevent time')
plt.show()
