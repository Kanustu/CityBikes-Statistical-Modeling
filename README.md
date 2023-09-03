# Final-Project-Statistical-Modelling-with-Python

## Project/Goals
To conduct statistical analysis on data collected from multiple sources, applying the knowledge acquired from the LHL Statistical Modeling with Python course.

## Process
### Connecting to and attaining the necessary data from the Citybikes API
I began by delving into the Citybikes API, seeking to understand how to make API calls effectively. I selected Los Angeles, California, as the focal point of my data collection efforts. My objective was to obtain comprehensive information about bike stations, including their geographical coordinates (longitude and latitude) and the number of available bikes at each station. I then parsed the acquired data into a structured dataframe for further analysis and insights.

### Connecting to and attaining the necessary data from the Yelp and Foursquare API's
I began by exploring the documentation for both the Foursquare and Yelp APIs. This step allowed me to gain a understanding of how to write the API calls effectively and access the information these platforms had to offer. Using the longitude and latitude coordinates of each bike station, I formulated API requests to extract the metrics that I deemed valuable from both Foursquare and Yelp. Once the API calls were executed successfully, I parsed the returned data, organizing it into dedicated dataframes for each platform. This approach laid the foundation for analysis and insights, enabling me to leverage the power of both Foursquare and Yelp data for my project's objectives.

### Joining the data from all sources
With the individual datasets i needed, I began the merging of the information from Citybikes, Yelp, and Foursquare into a unified and comprehensive dataframe. This integration allowed for a full view of the data, enabling me to attempt draw meaningful insights. Subsequently, I delved into exploratory data analysis (EDA), leveraging the power of data visualization to gain a deeper understanding of the relationships, patterns, and trends within the dataset.

I then created an SQLite3 database. To optimize data organization, I made the decision to divide the larger dataset into three distinct tables within the database. This approach enhanced data integrity and will allow for easier access and retrieval if needed for further analysis and modeling.

### Creation and interpretation of a Regression model
In pursuit of uncovering the relationship between the availability of bikes and various location metrics within the proximity of each bike station, I constructed a regression model using the powerful capabilities of statsmodels. This model aimed to shed light on how these metrics collectively influenced the number of free bikes at a given station.

However, the initial model delivered a somewhat disappointing R-squared value of just 0.010, signifying that it could account for only 1% of the variance observed in the 'free_bikes' variable. Adding to the complexity, there were notable red flags in the form of high p-values associated with the 'popularity' and 'rating' variables, indicating that they failed to reach the desired level of statistical significance. In light of these findings, it became evident that the next step entailed a refinement of the model. This process would involve the removal of variables with elevated p-values, an endeavor aimed at achieving a more robust and accurate fit.

The subsequent iteration of the model brought about a change. While the R-squared value remained at 0.010, indicative of the persistent challenge in explaining variability, the once-high p-values for the variables had now descended below the widely accepted significance threshold of <0.05. This transformation suggested that the refined model was better equipped to attempt to explain the relationship between the location metrics and the availability of free bikes, paving the way for more analysis.

## Results
In the context of this specific scenario, the Foursquare API emerged as the primary data source, offering a more robust and actionable dataset. Notably, Foursquare boasted a more precise rating system, which added depth to the analysis. One observation was the disparity in the quantity of data retrieved, with Foursquare yielding a threefold increase in the number of locations compared to Yelp. This abundance of data enhanced the potential for uncovering meaningful insights.

However, despite that data and the refinement of the regression model, the outcome presented a challenge. The final regression model, while built upon the dataset from Foursquare, appeared to yield statistically insignificant results. With an R-squared value of merely 0.010, the model could account for a mere 1% of the variability observed in the availability of bikes. This outcome underscored the multifaceted nature of the factors influencing bike availability, suggesting that other unaccounted-for variables or external factors may play a substantial role in the observed variations. This realization posed questions and opportunities for further exploration and refinement of the analysis.

## Challenges 
The process of selecting the needed metrics from both the Foursquare and Yelp APIs was a critical step in shaping the approach. It involved careful consideration of which data points would be most relevant to the project objectives. For instance, in the case of Foursquare, metrics such as location ratings, popularity, and review counts were deemed crucial in painting a comprehensive picture of the locales surrounding bike stations.

Additionally, dealing with incompatible data formats and values was an essential aspect of data preprocessing. This included harmonizing rating values, converting them from a 5-point system (as used by Yelp) to a 10-point system (as used by Foursquare). Handling missing or null values was equally important, with strategies such as replacing them with the median values of their respective columns, ensuring data completeness and integrity. These decisions and data transformations were integral to preparing a cohesive and consistent dataset, setting the stage for analysis and modeling.

## Future Goals
While the project has yielded some insights, there were a couple of aspects that I would have loved to explore further. Firstly, it would have been insightful to make multiple API requests to Citybikes over an extended period, spanning at least a few weeks. My hypothesis is that factors such as the time of day and the difference from weekdays to weekends could significantly influence the number of available bikes at different bike stations. This analysis could have unveiled patterns and trends, providing a better understanding of bike availability dynamics.

Secondly, I had a strong inclination to incorporate weather data into the analysis. Given that bike riding is inherently an outdoor activity, it's reasonable to assume that weather conditions play a pivotal role in the utilization of bike stations. By integrating data from a weather API or similar source, I could have explored the correlation between weather variables (such as temperature, precipitation, and wind) and bike availability. This addition would have enriched the analysis by accounting for external factors that undoubtedly impact the usage of bike-sharing systems, offering a more comprehensive view.