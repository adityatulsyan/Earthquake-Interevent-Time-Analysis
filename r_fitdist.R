library(fitdistrplus)
library(jsonlite)

data = as.matrix(interevent_time.csv)[,2];

res = fitdist(data, "exp", method = "mme");

summary(res)

capture.output(summary(res), file = "fit_op/exp_res.txt")
# 
# plot(res)
# 
# ans = ks.test(data, "pexp", rate = 0.6892658)
# 
# capture.output(ans, file = "ks/exp_ks.txt")