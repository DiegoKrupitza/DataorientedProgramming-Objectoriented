#!/usr/bin/env python3
# encoding=utf-8
"""
This is the template for the first exercise of data oriented programming
paradigms (semester 2018W).

Before you start, please read this and all other comments in this file.

In order to receive a valid grade, you must rename this file from
"exercise_1.py" to "%s_exercise_1.py" % student_id. If you don't have a student
id, please use your name and replace all spaces with underscores.

You must use Python version 3 (3.6+ recommended). It is recommended to install
Anaconda or Miniconda. You can develop everything using Jupyter notebooks, the
submission must be given in this Python file however.

The code will be evaluated based on unit tests. Every passing test gives a
point. These unit tests will not be public. However, in order to be able to
test your code and verify that the submission works, simply run this script
and a couple of tests will run. If you're stuck with at any of the `assert`
statements, simple deactivate them and continue working.

The submission will be executed on a Unix system in order to record your
answers for Task 4 and 5, so it is important to check that your submission
executes without any errors before submitting it. For the submission, only
this (renamed) file needs to be uploaded to TUWEL. Submission deadline is
23.11.2018 23:55.

"""

# the only imports allowed are those contained in Python's standard library and
# numpy
import datetime
from functools import partial
import os
import timeit
import unittest
import csv
import math
import time

import numpy as np

"""
The goal of this exercise is to compare different programming paradigms and
techniques to read in data, pre-process it (e.g. handle missing values) and
aggregate it as described.

The scenario for this exercise is providing an aggregated view to weather
observations (temperature, humidity) gathered in Vienna from 2012 to 2016.

The data to be used can be found in the subdirectory named 'data'. If you
develop your submission on Windows, please make sure that you don't use any
backslashes in the file names, because the submission won't run on Unix
systems. Either use normal slashes, or use the functions provided in the
os.path module. If you stick with the provided function templates, you should
be fine.

"""


"""
Task 1:

Provide an object-oriented programming approach by completing the class
template and implementing the methods accordingly. Instructions can be found
in the class' and method's own docstrings.

"""


class WeatherObservation(object):
	"""
	Class containing all temperature and humidity fields as contained in the
	CSV files.

	The individual values should be accessible as instance variables or
	attributes, they must be named exactly as the columns of the CSV files.

	All values should be stored as floats. Missing values should be represented
	by 'None'.

	For simplicity, this class can also be used for aggregation of values
	(although the names of the variables/attributes are not really meaningful
	anymore then).

	You are free to write your own classes for aggregation of values (on a
	weekly, monthly, yearly basis) though. This might be beneficial to win the
	chocolate challenge (see Task 4 below). If you do so, please implement
	them as classes inheriting from this class and use the same attribute /
	eariable names.

	"""
	# TODO: your changes here

	def __init__(self, month=None, day=None, temp_dailyMin=None, temp_minGround=None, temp_dailyMean=None, temp_dailyMax=None, temp_7h=None, temp_14h=None, temp_19h=None, hum_dailyMean=None, hum_7h=None, hum_14h=None, hum_19h=None):
		self.month = month
		self.day = day
		self.temp_dailyMin = temp_dailyMin
		self.temp_minGround = temp_minGround
		self.temp_dailyMean = temp_dailyMean
		self.temp_dailyMax = temp_dailyMax
		self.temp_7h = temp_7h
		self.temp_14h = temp_14h
		self.temp_19h = temp_19h
		self.hum_dailyMean = hum_dailyMean
		self.hum_7h = hum_7h
		self.hum_14h = hum_14h
		self.hum_19h = hum_19h


class WeatherObservationsObjectOriented(object):
	"""
	A generic class representing all weather observations.

	All weather observations must be collected in a dictionary named
	`observations`. The key for the individual items are `datetime` instances.
	The items are instances of `WeatherObservation`.

	This class provides some methods to display the (aggregated) weather
	observations for a specific, day, week, month, and year.

	As an aggregation function the arithmetic mean should be used.
	Missing values should be omitted during aggregation.

	"""
	def __init__(self):
		self.observations = {}

	def load_data(self, filename):
		"""
		This method must load all data from the filename given and populate
		the object's variables.

		Parameters
		----------
		filename : str
						File containing the weather observations in CSV format.

		"""
		with open(filename) as csvfile:
			fieldReader = csv.reader(csvfile, delimiter=',', quotechar='"')
			next(fieldReader)  # kipping the first line with the descriptions
			for row in fieldReader:
				year = filename[filename.index("_")+1:filename.index(".")]
				day = row[2]
				month = row[1]
				date = "{}.{}.{}".format(day, month, year) # format day.month.year
				#print("Reading information from Date {}".format(date))
				col = [float(x) if x != '' else None for x in row]
				self.observations[date] = WeatherObservation( month, day, col[3], col[4], col[5], col[6], col[7], col[8], col[9], col[10], col[11], col[12], col[13])

	def day(self, date):
		"""
		Display the weather observations for this specific day.
		If no observation is available, return 'None'.

		Parameters
		----------
		date : datetime instance
						Date for which the weather observations should be given.

		Returns
		-------
		observation : WeatherObservation instance
						Weather observation for that day.

		"""
		# DONETODO: your changes here
		observation = None
		dateConverted = "{}.{}.{}".format(date.day, date.month, date.year)
		for k in self.observations.keys():
			if k == dateConverted:
				observation = self.observations[k]
		return observation

	def calcMeanFromSet(self, aggrateObservations):
		observation = None
		# calculation the mean for every field
		lenght = len(aggrateObservations)
		if lenght != 0:
			# temp_dailyMin
			temp_dailyMin = sum(a.temp_dailyMin if a.temp_dailyMin != None else 0 for a in aggrateObservations) / \
				len(list(filter(lambda x: x.temp_dailyMin != None, aggrateObservations)))
			# temp_minGround
			temp_minGround = sum(a.temp_minGround if a.temp_minGround != None else 0 for a in aggrateObservations) / \
				len(list(filter(lambda x: x.temp_minGround != None, aggrateObservations)))
			# temp_dailyMean
			temp_dailyMean = sum(a.temp_dailyMean if a.temp_dailyMean != None else 0 for a in aggrateObservations) / \
				len(list(filter(lambda x: x.temp_dailyMean != None, aggrateObservations)))
			# temp_dailyMax
			temp_dailyMax = sum(a.temp_dailyMax if a.temp_dailyMax != None else 0 for a in aggrateObservations) / \
				len(list(filter(lambda x: x.temp_dailyMax != None, aggrateObservations)))
			# temp_7h
			temp_7h = sum(a.temp_7h if a.temp_7h != None else 0 for a in aggrateObservations) / \
				len(list(filter(lambda x: x.temp_7h != None, aggrateObservations)))
			# temp_14h
			temp_14h = sum(a.temp_14h if a.temp_14h != None else 0 for a in aggrateObservations) / \
				len(list(filter(lambda x: x.temp_14h != None, aggrateObservations)))
			# temp_19h
			temp_19h = sum(a.temp_19h if a.temp_19h != None else 0 for a in aggrateObservations) / \
				len(list(filter(lambda x: x.temp_19h != None, aggrateObservations)))
			# hum_dailyMean
			hum_dailyMean = sum(a.hum_dailyMean if a.hum_dailyMean != None else 0 for a in aggrateObservations) / \
				len(list(filter(lambda x: x.hum_dailyMean != None, aggrateObservations)))
			# hum_7h
			hum_7h = sum(a.hum_7h if a.hum_7h != None else 0 for a in aggrateObservations) / \
				len(list(filter(lambda x: x.hum_7h != None, aggrateObservations)))
			# hum_14h
			hum_14h = sum(a.hum_14h if a.hum_14h != None else 0 for a in aggrateObservations) / \
				len(list(filter(lambda x: x.hum_14h != None, aggrateObservations)))
			# hum_19h
			hum_19h = sum(a.hum_19h if a.hum_19h != None else 0 for a in aggrateObservations) / \
				len(list(filter(lambda x: x.hum_19h != None, aggrateObservations)))

			observation = WeatherObservation(-1, -1, temp_dailyMin, temp_minGround, temp_dailyMean,
											 temp_dailyMax, temp_7h, temp_14h, temp_19h, hum_dailyMean, hum_7h, hum_14h, hum_19h)

		return observation

	def week(self, date):
		"""
		Display the aggregated weather observations for this specific week.
		According to the ISO standard, a week is defined to start on Monday.
		If no observations are available to be aggregated, return 'None'.

		Parameters
		----------
		date : datetime instance
						Date for which the different values should be aggregated.

		Returns
		-------
		week_average : WeatherObservation instance
						Weather observations aggregated by week.

		"""
		observation = None
		week = date.isocalendar()[1]
		aggrateObservations = []
		
		# collection all the Observations with the given month
		for k in self.observations.keys():
			datefromDictionary = datetime.datetime.strptime(k, "%d.%m.%Y")
			if datefromDictionary.isocalendar()[1] == week:
				aggrateObservations.append(self.observations[k])

		# calculation the mean for every field
		return self.calcMeanFromSet(aggrateObservations)

	def month(self, date):
		"""
		Display the aggregated weather observations for this specific month.
		If no observations are available to be aggregated, return 'None'.

		Parameters
		----------
		date : datetime instance
						Date for which the different values should be aggregated.

		Returns
		-------
		month_average : WeatherObservation instance
						Weather observations aggregated by month.

		"""
		aggrateObservations = []
		month = date.month
		# collection all the Observations with the given month
		for k in self.observations.keys():
			datefromDictionary = datetime.datetime.strptime(k, "%d.%m.%Y")
			if datefromDictionary.month == month:
				aggrateObservations.append(self.observations[k])

		# calculation the mean for every field
		return self.calcMeanFromSet(aggrateObservations)

	def year(self, date):
		"""
		Display the aggregated weather observations for this specific year.
		If no observations are available to be aggregated, return 'None'.

		Parameters
		----------
		date : datetime instance
						Date for which the different values should be aggregated.

		Returns
		-------
		year_average : WeatherObservation instance
						Weather observations aggregated by year.

		"""
		aggrateObservations = []
		year = date.year
		# collection all the Observations with the given month
		for k in self.observations.keys():
			datefromDictionary = datetime.datetime.strptime(k, "%d.%m.%Y")
			if datefromDictionary.year == year:
				aggrateObservations.append(self.observations[k])

		# calculation the mean for every field
		return self.calcMeanFromSet(aggrateObservations)


"""
Task 2:

Provide an data-oriented programming approach and complete the class template
and implement the methods accordingly. Only Python's own mechanisms
(i.e. lists, dictionaries, tuples) should be used. Numpy is not allowed.

Please consider the exemplary access patterns of Task 4 when designing your
data-oriented approach.

"""


class WeatherObservationsDataOriented(object):
	"""
	A generic class representing all weather observations.

	All weather observations should be stored in a data-oriented fashion. It
	is up to you on how the data is organised. Only Python's own mechanisms
	(i.e. lists, dictionaries, tuples) should be used. Numpy is not allowed.

	All methods of `WeatherObservationsObjectOriented` class must be
	implemented with the same calling signature as for the object oriented
	example above. They should also return `WeatherObservation` instances.

	As before, as an aggregation function the arithmetic mean should be used.
	Missing values should be handled as 'None' and omitted during aggregation.

	"""

	"""
	 I'm working wiht an array wich represents a  matrix with nxn
	 every row represents a dataentry
	 [
		[DATE,TEM_DAILYMIN,...],
		[DATE,TEM_DAILYMIN,...]
	 ]

	"""
	def __init__(self):
		self.observations = []
		self.index_list = [] # due to the fact that i'm using a simple list and not a dictionary i might have to use a serperate list for my indizes that the best solution for that case

	def load_data(self, filename):
		"""
		This method must load all data from the filename given and populate
		the object's variables.

		Parameters
		----------
		filename : str
						File containing the weather observations in CSV format.

		"""
		# TODO: your changes here
		with open(filename) as csvfile:
			fieldReader = csv.reader(csvfile, delimiter=',', quotechar='"')
			next(fieldReader)  # kipping the first line with the descriptions
			year = filename[filename.index("_")+1:filename.index(".")]
			if year not in self.index_list:
				self.index_list.append(year)
				for row in fieldReader:
					day = row[2]
					month = row[1]
					date = "{}.{}.{}".format(day, month, year) # format day.month.year
					col = [float(x) if x != '' else None for x in row]
					matrixRow = [date, month, day, col[3], col[4], col[5], col[6], col[7], col[8], col[9], col[10], col[11], col[12], col[13]]
					self.observations.append(matrixRow)

	def calcMeanFromSet(self,aggregateRows):
		observation = None
		lenght = len(aggregateRows)
		if lenght != 0:
			# temp_dailyMin
			temp_dailyMin = sum(a[3] if a[3] != None else 0 for a in aggregateRows) / len(list(filter(lambda x: x[3] != None, aggregateRows)))
			# temp_minGround
			temp_minGround = sum(a[4] if a[4] != None else 0 for a in aggregateRows) / len(list(filter(lambda x: x[4] != None, aggregateRows)))
			# temp_dailyMean
			temp_dailyMean = sum(a[5] if a[5] != None else 0 for a in aggregateRows) / len(list(filter(lambda x: x[5] != None, aggregateRows)))
			# temp_dailyMax
			temp_dailyMax = sum(a[6] if a[6] != None else 0 for a in aggregateRows) / len(list(filter(lambda x: x[6] != None, aggregateRows)))
			# temp_7h
			temp_7h = sum(a[7] if a[7] != None else 0 for a in aggregateRows) / len(list(filter(lambda x: x[7] != None, aggregateRows)))
			# temp_14h
			temp_14h = sum(a[8] if a[8] != None else 0 for a in aggregateRows) / len(list(filter(lambda x: x[8] != None, aggregateRows)))
			# temp_19h
			temp_19h = sum(a[9] if a[9] != None else 0 for a in aggregateRows) / len(list(filter(lambda x: x[9] != None, aggregateRows)))
			# hum_dailyMean
			hum_dailyMean = sum(a[10] if a[10] != None else 0 for a in aggregateRows) / len(list(filter(lambda x: x[10] != None, aggregateRows)))
			# hum_7h
			hum_7h = sum(a[11] if a[11] != None else 0 for a in aggregateRows) / len(list(filter(lambda x: x[11] != None, aggregateRows)))
			# hum_14h
			hum_14h = sum(a[12] if a[12] != None else 0 for a in aggregateRows) / len(list(filter(lambda x: x[12] != None, aggregateRows)))
			# hum_19h
			hum_19h = sum(a[13] if a[13] != None else 0 for a in aggregateRows) / len(list(filter(lambda x: x[13] != None, aggregateRows)))

			observation = WeatherObservation(-1, -1, temp_dailyMin, temp_minGround, temp_dailyMean, temp_dailyMax, temp_7h, temp_14h, temp_19h, hum_dailyMean, hum_7h, hum_14h, hum_19h)

		return observation

	def day(self, date):
		"""
		Display the weather observations for this specific day.
		If no observation is available, return 'None'.

		Parameters
		----------
		date : datetime instance
						Date for which the weather observations should be given.

		Returns
		-------
		observation : WeatherObservation instance
						Weather observation for that day.

		"""
		# TODO: your changes here
		observation = None
		dateConverted = "{}.{}.{}".format(date.day, date.month, date.year)
		for row in self.observations:
			if row[0] == dateConverted:
				observation = WeatherObservation(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13])
		return observation

	def week(self, date):
		"""
		Display the aggregated weather observations for this specific week.
		According to the ISO standard, a week is defined to start on Monday.
		If no observations are available to be aggregated, return 'None'.

		Parameters
		----------
		date : datetime instance
						Date for which the different values should be aggregated.

		Returns
		-------
		week_average : WeatherObservation instance
						Weather observations aggregated by week.

		"""
		# TODO: your changes here
		aggregateRows = []
		week = date.isocalendar()[1]
		for row in self.observations:
			datefromRow = datetime.datetime.strptime(row[0], "%d.%m.%Y")
			if datefromRow.isocalendar()[1] == week:
				aggregateRows.append(row)

		# It seems to be that all the None valls should not count -> the reason why i have to have such a complicated len with filter
		# calc
		return self.calcMeanFromSet(aggregateRows);

	def month(self, date):
		"""
		Display the aggregated weather observations for this specific month.
		If no observations are available to be aggregated, return 'None'.

		Parameters
		----------
		date : datetime instance
						Date for which the different values should be aggregated.

		Returns
		-------
		month_average : WeatherObservation instance
						Weather observations aggregated by month.

		"""
		# TODO: your changes here

		# Finds the rows that are have the matching month for further operations
		aggregateRows = []
		month = date.month
		
		for row in self.observations:
			datefromRow = datetime.datetime.strptime(row[0], "%d.%m.%Y")
			if datefromRow.month == month:
				aggregateRows.append(row)

		# It seems to be that all the None valls should not count -> the reason why i have to have such a complicated len with filter
		# calc
		return self.calcMeanFromSet(aggregateRows);

	def year(self, date):
		"""
		Display the aggregated weather observations for this specific year.
		If no observations are available to be aggregated, return 'None'.

		Parameters
		----------
		date : datetime instance
						Date for which the different values should be aggregated.

		Returns
		-------
		year_average : WeatherObservation instance
						Weather observations aggregated by year.

		"""
		# TODO: your changes here
		aggregateRows = []
		year = date.year
		for row in self.observations:
			datefromRow = datetime.datetime.strptime(row[0], "%d.%m.%Y")
			if datefromRow.year == year:
				aggregateRows.append(row)

		# It seems to be that all the None valls should not count -> the reason why i have to have such a complicated len with filter
		# calc
		return self.calcMeanFromSet(aggregateRows);


"""
Task 3:

Provide an data-oriented programming approach and complete the class template
and implement the methods accordingly. This time in addition to Python's own
mechanisms, Numpy is explicitly allowed and should be used.

As in Task 2, consider the exemplary access patterns of Task 4 when designing
your approach.

"""


class WeatherObservationsDataOrientedNumpy(object):
	"""
	A generic class representing all weather observations.

	All weather observations should be collected in a data-oriented fashion
	and numpy should be used to store the data.

	All methods of `WeatherObservationsObjectOriented` class must be
	implemented and must have the same calling signature as for the object
	oriented example above, but should return numpy arrays instead.

	The columns of the returned numpy arrays should have the same ordering
	as in the CSV files and contain only the weather observations.

	As an aggregation function the arithmetic mean should be used.
	Missing values should be handled as NaN (not a number; np.nan) and omitted
	during aggregation.

	"""
	def __init__(self):
		self.observations = np.array([None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],dtype = np.float)
		self.index_list = []

	def load_data(self, filename):
		"""
		This method must load all data from the filename given and populate
		the object's variables.

		Parameters
		----------
		filename : str
						File containing the weather observations in CSV format.

		"""
		with open(filename) as csvfile:
			fieldReader = csv.reader(csvfile, delimiter=',', quotechar='"')
			next(fieldReader)  # kipping the first line with the descriptions
			year = filename[filename.index("_")+1:filename.index(".")]
			if year not in self.index_list:
				self.index_list.append(year)
				for row in fieldReader:
					day = row[2]
					month = row[1]
					date = "{}.{}.{}".format(day, month, year) # format day.month.year
					week = datetime.datetime.strptime(date, "%d.%m.%Y").isocalendar()[1]
					#print("Reading information from Date {}".format(date))
					row = [x if x != "" else None for x in row ]
					matrixRow = np.array([[week, day, month, year, row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13]]],dtype = np.float)
					self.observations = np.vstack((self.observations,matrixRow))	
					
					
	def day(self, date):
		day = date.day
		month = date.month
		year = date.year
		result = self.observations[self.observations[:,1] == float(day) ]
		result = result[result[:,2] == float(month)]
		result = result[result[:,3] == float(year)]
		return np.nanmean(result,axis=0)[4:]

	def week(self, date):
		week = date.isocalendar()[1]
		result = self.observations[self.observations[:,0] == float(week) ]
		return np.nanmean(result,axis=0)[4:]

	def month(self, date):
		month = date.month
		result = self.observations[self.observations[:,2] == float(month) ]
		return np.nanmean(result,axis=0)[4:]
		
	def year(self, date):
		year = date.year
		result = self.observations[self.observations[:,3] == float(year) ]
		return np.nanmean(result,axis=0)[4:]




"""
Task 4:

Compare the runtime of the different implementations.
Use the timeit module or other appropriate methods.
Average the runtime of 3 runs with 3 different dates.

Record the timing for every step separately and compare them afterwards.

Steps to be performed for each implementation method (Task 1 - 3):

1) load all data from the CSV files into the respective object
2) for a specific date, return all weather observations for that day
3) aggregate all temperature values for the week this day belongs to
4) aggregate all humidity values for the month this day belongs to
5) aggregate the 'temp_dailyMean' values for the year this day belongs to

After performing these 5 steps, you should have 5 timings for each
implementation method. Compare them and put your written evaluation into the
return statement of the `solution_task_4()` function. The answer should not
exceed 250 words.

Please use the provided function templates. You are free to time the steps
given above in any way you think is appropriate.

There will be a chocolate challenge for this exercise. The fastest solution for
each implementation method (Task 1 - 3) wins some chocolate. To qualify for the
challenge, not all implementations must be provided, but correct values must
be computed of course. The access patterns to the data are similar to the 5
steps outlined above.

"""


def load_all_data(observations):
	"""
	Load all data files for the given observation object.

	Parameters
	----------
	observations : WeatherObservations*** instance.
					Initialised WeatherObservations*** object.

	Returns
	-------
	observations :
					Same observations object with all data loaded.

	"""
	# load all data
	observations.load_data('data/weather_2012.csv')
	observations.load_data('data/weather_2013.csv')
	observations.load_data('data/weather_2014.csv')
	observations.load_data('data/weather_2015.csv')
	observations.load_data('data/weather_2016.csv')
	# return observations
	return observations


def time_steps(observations, date):
	"""
	Example function to time the individual steps.

	In order to actually time these steps, functionality needs to be
	implemented.

	Parameters
	----------
	observations : WeatherObservations*** instance.
					Initialised WeatherObservations*** object.
	date : datetime instance
					Date for which the different values should be aggregated.

	Returns
	-------
	timings : tuple
					Times required to load data, report values for day, week, month and
					year, respectively.

	Notes
	-----
	This function will not be used for grading. The timing will be determined
	externally.

	"""
	# TODO: your changes here
	# load all data
	time_load = 0
	for i in range(3):
		start_load = time.process_time()
		
		load_all_data(observations)
		
		end_load = time.process_time()
		time_load += (end_load - start_load)
	time_load = time_load / 3
	#print("Time load:",time_load)
	
	# retrieve (aggregated) values for day, week, month and year
	time_day = 0
	for i in range(3):
		start_day = time.process_time()
		
		observations.day(date)
		
		end_day = time.process_time()
		time_day += (end_day - start_day)
	time_day = time_day / 3
	#print("Time day:",time_day)

	time_week = 0
	for i in range(3):
		start_week = time.process_time()
		 
		observations.week(date)
		
		end_week = time.process_time()
		time_week += (end_week - start_week)
	time_week = time_week / 3
	#print("Time week:",time_week)

	time_month = 0
	for i in range(3):
		start_month = time.process_time()
		
		observations.month(date)
		
		end_month = time.process_time()
		time_month += (end_month - start_month)
	time_month = time_month / 3
	#print("Time month:",time_month)


	time_year = 0
	for i in range(3):
		start_year = time.process_time()
		
		observations.year(date)
		
		end_year = time.process_time()
		time_year += (end_year - start_year)
	time_year = time_year / 3
	#print("Time year:",time_year)

	# return the recorded timings
	return time_load, time_day, time_week, time_month, time_year


def evaluate():
	"""
	Example function to compare the individual implementations.

	"""

	# TODO: your changes here
	# object oriented
	#print("Objectoriented")
	obs_oo = WeatherObservationsObjectOriented()
	times_oo = time_steps(obs_oo, datetime.date(2012, 1, 1))

	# data oriented
	#print("\nDataoriented")
	obs_do = WeatherObservationsDataOriented()
	times_do = time_steps(obs_do, datetime.date(2012, 1, 1))

	# data oriented w/ numpy
	#print("\nNumpy")
	obs_np = WeatherObservationsDataOrientedNumpy()
	times_np = time_steps(obs_np, datetime.date(2012, 1, 1))
	
	
	# compare timings
	return times_oo, times_do, times_np


def solution_task_4():
	"""
	Return your solution for Task 4.

	"""
	evaluate()
	# TODO: your changes here
	return '''
	For the measuring of the time I used the time module for python. The reason is that there were some problems with parameters using the timeit implementation.
	According to the measurements the Dataoriented Approach (without Numpy) is the fastest one for loading the date and a few miliseconds numpy slower. That's obvious because numpy is not designed for single element operations, it's designed to work on enormous datasets which are already preloaded.
	Therefore the numpy (and also the Dataoriented) approach are a lot slower doing single element operations than the objectoriented one.
	On the other side numpy is in finding the mean for a certain month, week and year the fastest, because in thoose scenarios the way its working is at its best. 
	Among the data oriented and object oriented approach is nearly no differences. Sometimes the object oriented is 0.002 seconds faster and sometimes the other way around
	All in all it's safe to say that numpy isn't that fast loading the data, but it can work really fast on aggregated Data. On the other hand it is better to use objects for single element operations
	'''


"""
Task 5:

Describe in your own words how the implementations of Task 2 and 3 could have
been improved further and what is needed (or missing) in order to do so.
If you implemented them already in an improved fashion, please specify in your
answer how you did so. Your answer should not exceed 250 words.

"""


def solution_task_5():
	"""
	Return your solution for Task 5.

	"""
	# TODO: your changes here
	return '''
	Object oriented is for single element operations in its best state because of the dictionary (which contains as key a given date) it as fast and simple as possible.
	For the calculation of the mean for every field for a given month, week, year is already quite sophisticated, because I'm saving the data in an object with the given date and month. So accessing the iterating the data, for example for a given year, it can be done easily.
	The only difference between the Object oriented approach and the self written data oriented is only that one uses objects and the other one is based on matrixes and that instead of using a dictionary I'm using a list in Task 2. So to keep the data consistent and avoid redundancy in the dataset I implemented an additional list which contains all the indices.

	The only way to improve both the tasks is to pre-calculate the week and store it as an additional field in an object or as an additional column in a matrix. But this will affect the speed of the loading process. That is the reason why i did not implemented it.  
	Another potential, but sadly impossible way to improve the data oriented approach would be if it could be possible to slice arrays like with numpy. Sadly, that's not possible so the only efficient way is to iterate over the list.
	'''


"""
The code below is for testing purposes only.

"""


def test():
	"""
	This function checks for the correctness of the submission.

	You are free to comment `assert` statements as you like in order to make
	this function pass. However, grading will be performed based on unit tests
	and not on this function.

	"""
	# Task 1: object-oriented
	obs = WeatherObservationsObjectOriented()
	assert isinstance(obs.observations, dict)
	obs.load_data('data/weather_2012.csv')
	# single day
	day = obs.day(datetime.date(2012, 1, 1))
	assert isinstance(day, WeatherObservation)
	assert day.hum_dailyMean == 98
	# monthly average
	month = obs.month(datetime.date(2012, 10, 1))
	assert isinstance(month, WeatherObservation)
	assert np.allclose(month.temp_dailyMin, 6.9387, atol=1e-3)
	# load all years
	obs = load_all_data(obs)
	assert len(obs.observations) == 1827

	# Task 2: data-oriented
	obs = WeatherObservationsDataOriented()
	obs.load_data('data/weather_2012.csv')
	# single day
	day = obs.day(datetime.date(2012, 1, 1))
	assert isinstance(day, WeatherObservation)
	assert day.hum_dailyMean == 98
	# monthly average
	month = obs.month(datetime.date(2012, 1, 2))
	assert isinstance(month, WeatherObservation)
	assert np.allclose(month.temp_dailyMin, 0.67)
	# load all years
	obs = load_all_data(obs)
	assert len(obs.observations) == 1827

	# Task 3: data-oriented with numpy
	obs = WeatherObservationsDataOrientedNumpy()
	obs.load_data('data/weather_2012.csv')
	# single day (hum_dailyMean should be 4th to last column)
	day = obs.day(datetime.date(2012, 1, 1))
	assert isinstance(day, np.ndarray)
	assert day[-4] == 98
	# monthly average (temp_dailyMin should be first column)
	month = obs.month(datetime.date(2012, 1, 2))
	assert np.allclose(month[0], 0.67)
	# yearly average
	year = obs.year(datetime.date(2012, 1, 2))
	assert np.allclose(year[0], 7.5, atol=1e-3)


"""
Do not modify the code below, otherwise your submission may not be graded
correctly.

"""


def run():
	# parse student ID
	filename = os.path.basename(__file__)
	student_id = filename[:-14]
	# record Task 4 & 5 answers to an file
	task_4 = solution_task_4()
	task_5 = solution_task_5()
	if len(task_4.split()) > 250:
		print('WARNING: Please shorten your answer for Task 4 to 250 words.')
	if len(task_5.split()) > 250:
		print('WARNING: Please shorten your answer for Task 5 to 250 words.')
	with open('%s.txt' % student_id, 'w') as f:
		f.write('Student: %s\n\n' % student_id)
		f.write('Answer Task 4:\n' + task_4 + '\n')
		f.write('Answer Task 5:\n' + task_5 + '\n')
	print('OK: Your submission ran successfully and was recorded for your '
		  'student id / name: "%s". Please check that this is correct. Your '
		  'solution for Task 4 and 5 can be found in the generated file '
		  '"%s.txt".' % (student_id, student_id))


if __name__ == '__main__':
	run()
	try:
		test()
	except AssertionError:
		print('ERROR: basic tests are not passing!')
	else:
		print('OK: basic tests are passing.')
