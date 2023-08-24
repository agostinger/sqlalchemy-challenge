# Import the dependencies.
import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Welcome to the Climate App for Honolulu<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start>YYYY-MM-DD<br/>"
        f"/api/v1.0/<start>YYYY-MM-DD/<end>YYYY-MM-DD"
    )
@app.route("/api/v1.0/precipitation")

def precipitation():

    """Return a list of dates and percipitation values from 2016-2017"""
# Query to retrieve the last 12 months of precipitation data.
# Starting from the most recent data point in the database.
    end_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]

# Calculate the date one year from the last date in data set.
    query_date = dt.datetime.strptime(end_date, "%Y-%m-%d") - dt.timedelta(days=365)

# Perform a query to retrieve the data and precipitation scores
    results = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= "2016-08-23").all()

# Create a dictionary with date as key and prcp as value.
    precipitation_analysis = {}
    for date, prcp in results:
        precipitation_analysis[date] = prcp

    return jsonify(precipitation_analysis)

@app.route("/api/v1.0/stations")
def stations():

    """Return a list of all station names"""
    # Query all stations
    results = session.query(Station.station).all()

    # Convert list of tuples into normal list
    all_stations = list(np.ravel(results))

    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")

def temperature():

    """Return a list of dates and temperatures values from 2016-2017"""
# Query to retrieve the last 12 months of temperature data.
# Starting from the most recent data point in the database.
    end_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]

# Calculate the date one year from the last date in data set.
    query_date = dt.datetime.strptime(end_date, "%Y-%m-%d") - dt.timedelta(days=365)

# Perform a query to retrieve the data and temp scores
    results = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.station == "USC00519281").\
        filter(Measurement.date >= query_date).all()

# Create a dictionary with date as key and temp as value.
    temperature_analysis = {}
    for date, temp in results:
        temperature_analysis[date] = temp

    return jsonify(temperature_analysis)

@app.route("/api/v1.0/<start>")

def avg_temps(start):

 # Convert the start_date parameter to a datetime object
    start = dt.datetime.strptime(start, "%Y-%m-%d").date()

    # Query the database for temp data from start to the end date of the data
    results = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.date >= start).all()

    # Calculate min, max, and average temperatures
    temp = [result.tobs for result in results]
    if temp:
        min_temp = min(temp)
        max_temp = max(temp)
        avg_temp = sum(temp) / len(temp)
        return jsonify({"Minimum Temperature": min_temp, "Max Temperature": max_temp,
                         "Average Temperature": avg_temp})
    else:
        return jsonify({"error": f"The date specified {start} was not found."}), 404

@app.route("/api/v1.0/<start>/<end>")

def state_end_avg(start, end):

 # Convert the start_date parameter to a datetime object
    start= dt.datetime.strptime(start, "%Y-%m-%d").date()
    end = dt.datetime.strptime(end, "%Y-%m-%d").date()

    # Query the database for temp data from start to the end date of the data
    results = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.date >= start, Measurement.date <= end).all()

    # Calculate min, max, and average temperatures
    temp = [result.tobs for result in results]
    if temp:
        min_temp = min(temp)
        max_temp = max(temp)
        avg_temp = sum(temp) / len(temp)
        return jsonify({"Minimum Temperature": min_temp, "Max Temperature": max_temp,
                         "Average Temperature": avg_temp})
    else:
        return jsonify({"error": f"The dates specified {start} and/or {end} was not found."}), 404


# Define main behavior
if __name__ == '__main__':
    app.run(debug=True)
