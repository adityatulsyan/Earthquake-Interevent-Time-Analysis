#install.packages("fitdistrplus", repo="http://cran.rstudio.com/");
#install.packages("actuar", repo="http://cran.rstudio.com/");

library(fitdistrplus)
library(actuar)

intervent <- read.csv("interevent_time.csv");
data = as.matrix(intervent)[,2];

method <- "mme";

print("Processing the exponential distribution")
res = fitdist(data, "exp", method = method);
summary(res)
print("1234:")
capture.output(summary(res), file = "results/exp_res.txt")
ans = ks.test(data, "pexp", res[["estimate"]])
capture.output(ans, file = "results/exp_ks.txt")

print("Processing the gamma distribution")
res = fitdist(data, "gamma", method = method);
summary(res)
capture.output(summary(res), file = "results/gamma_res.txt")
ans = ks.test(data, "pgamma", res[["estimate"]])
capture.output(ans, file = "results/gamma_ks.txt")

print("Processing the weibull distribution")
memp <- function(x, order) mean(x^order)
res = fitdist(data, "weibull", method = method, order = c(1,2), memp=memp);
summary(res)
capture.output(summary(res), file = "results/weibull_res.txt")
ans = ks.test(data, "pweibull", res[["estimate"]])
capture.output(ans, file = "results/weibull_ks.txt")

print("Processing the lognormal distribution")
res = fitdist(data, "lnorm", method = method);
summary(res)
capture.output(summary(res), file = "results/lognormal_res.txt")
ans = ks.test(data, "plnorm", res[["estimate"]])
capture.output(ans, file = "results/lognormal_ks.txt")
