# Earthquake-Interevent-Time-Analysis
Preparation files and guidelines:
1. Earthquake interevent time analysis helps up to assess earthquake hazards of a seismic region. Several probability distributions are used for this purpose. Before we proceed, let us first understand a few basic concepts about earthquakes. Visit https://earthquake.usgs.gov/education/ for details.
2. What is an earthquake? Is Indonesia prone to earthquakes? What do you mean by earthquake prediction? Is earthquake prediction same as earthquake forecasting? Find at https://www.usgs.gov/faqs/can-you- predict-earthquakes?qt-news_science_products=0#qt-news_science_products
3. Now let us collect previous earthquakes for the Sumatra and adjacent regions. For this, visit http://www.isc.ac.uk/iscbulletin/search/catalogue/, in ISC Bulletin  CSV formatted catalogue  rectangular search region, latitude -10 to 10 deg N, longitude 90-110 deg E  time period 1900.01.01 to 2020.10.20  additional parameters, depth 0-200 km, magnitude 6-10, magnitude type ‘any’, magnitude author ISC output event catalogue. Thus you get a list of earthquakes that occurred in the region after 1900.
4. In order to remove the dependent events, such as foreshocks, aftershocks and seismic clusters, let us apply a dynamic window-based spatio-temporal filtering algorithm as: Search radius r  exp   1.024  0.804 M   15, and time window t  exp   2.870  1.235 M   60. If there is any event falling within the search radius and/or within the time window, we remove that event. In this way, we find a catalog of i.i.d events. The interevent times of the declustered catalog can be obtained by subtracting the occurrence time from the next occurrence time. For example, if two events occurred on April 04, 1905 and August 20, 1908, then the difference of these dates will be the interevent time. You can express the interevent times in day or year, as per your choice.
6. Having the list of interevent times, now we are ready for modeling using various probability distributions, such as exponential, gamma, Weibull, and lognormal.
7. Use MLE and MoM parameter estimations to obtain the estimated parameters.
8. Now in order to prioritize the candidate probability distributions, let us apply two tests: AIC and K-S.
9. You may use inbuilt tool of R, MATLAB, or any other software to fit interevent time data to different probability models.
10. Now, having done the above steps, how can you forecast earthquakes? See https://www.tandfonline.com/doi/full/10.1080/19475705.2018.1466730 for reference.
