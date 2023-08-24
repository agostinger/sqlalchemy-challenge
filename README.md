# sqlalchemy-challenge
Climate Analysis on Honolulu, Hawaii for travel planning. To help with trip planning, 
decided to do a climate analysis about the area. Performed the following analysis.

Part 1: Analyze and Explore the Climate Data:

In this section, used Python and SQLAlchemy to do a basic climate analysis and data 
exploration of the climate database. Specifically, used SQLAlchemy ORM queries, Pandas,
and Matplotlib. 

Precipitation Analysis:
1. Find the most recent date in the dataset. The most recent date was August 23, 2017.

2. Using that date, pulled the previous 12 months of precipitation data by querying the previous 12 months of data. Selected only dates and precipitation data and loaded the query results into a Pandas DataFrame. Sorted the DataFrame values by "date" and plotted the results in a bar graph as displayed in the climate.ipynb file. 

Based on the analysis and graph, the months with the most preciptation are in fall and spring (Months September and April/May) and also the month of February.

Station Analysis:

1. Designed a query to calculate the total number of stations in the dataset and grouped to find the most-active stations by listing them in descending order. To do so, completed the following steps:
        The station id with the greatest number of observations is Station USC005199281 with 2772 observations.

2. Designed a query that calculated the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query (Station USC005199281).

Plotted the results as a histogram, as shown on the climate.ipynb file. As displayed on the histogram plot, temperatures between 75-77 degrees are the most frequent observation.

Part 2: Design Climate App
After completing the initial analysis, designed a Flask API based on the queries developed. To do so, used Flask to create routes as follows:

    1. / 
        Start at the homepage.
        Listed all the available routes below.

    2. /api/v1.0/precipitation

        Convert the query results from precipitation analysis above (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.

            Returned the JSON representation of your dictionary.

    3. /api/v1.0/stations

        Return a JSON list of stations from the dataset.
    4./api/v1.0/tobs

        Query the dates and temperature observations of the most-active station for the previous year of data.

        Return a JSON list of temperature observations for the previous year.

    5./api/v1.0/<start> and /api/v1.0/<start>/<end>

        Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.

        For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.

        For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.
        
        
