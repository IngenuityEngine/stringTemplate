import os
import sys
from expects import *
import datetime

import pathman
pathman.addRelativePath(__file__, '../..')
import tryout
import arkUtil

import stringTemplate

class test(tryout.TestSuite):
	title = 'test/test_stringTemplate.py'

	def basics(self):
		template = 'Sup {name}, welcome to {place}'
		data = {'name': 'Robocop', 'place':'Mars'}
		result = stringTemplate.expand(template, data)
		expect(result).to(equal('Sup Robocop, welcome to Mars'))

	def dates(self):
		date = datetime.datetime.now()
		day = arkUtil.pad(date.day, 2)
		month = arkUtil.pad(date.month, 2)
		shortYear = arkUtil.pad(date.year % 100, 2)
		fullYear = str(date.year)

		testString = 'it is now ' + day + ' of ' + month + ' of ' + fullYear
		templateString = 'it is now {dd} of {mm} of {yyyy}'
		expect(stringTemplate.expand(templateString))\
			.to(equal(testString))

		templateString = '{yy} is short for {yyyy}'
		testString = shortYear + ' is short for '+ fullYear
		expect(stringTemplate.expand(templateString))\
			.to(equal(testString))
		testString = '{dd}'
		expect(len(stringTemplate.expand(testString)))\
			.to(equal(2))
		testString = '{mm}'
		expect(len(stringTemplate.expand(testString)))\
			.to(equal(2))
		testString = '{yy}'
		expect(len(stringTemplate.expand(testString)))\
			.to(equal(2))
		testString = '{yyyy}'
		expect(len(stringTemplate.expand(testString)))\
			.to(equal(4))

if __name__ == '__main__':
	tryout.run(test)
