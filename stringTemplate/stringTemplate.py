import datetime

import pathman
pathman.addRelativePath(__file__, '../..')
import arkUtil

# expand takes in a string and replaces patterns like {dd}
# with information.
# specialFunction allows a specific class to augment stringTemplate's
# functionality with class-specific replacment possibilities. See server/scripts/osOperations realPath
# method for a case of this in practice.
def expand(string, replacements={}):

	bracketedComponents = arkUtil \
		.getRegexMatches(string, '{.*?\}')

	if not len(bracketedComponents):
		return string

	for component in bracketedComponents:
		replacement = component[1:-1]
		if replacement.upper() in ['DD', 'MM', 'YY', 'YYYY']:
			replacement = getDateComponent(replacement)
		elif replacement in replacements:
			replacement = replacements[replacement]

		string = string.replace(component, replacement)

	return string

def getDateComponent(pattern):
	def datePad(dateComponent):
		return arkUtil.pad(dateComponent, 2)

	date = datetime.datetime.now()
	pattern = pattern.upper()

	if pattern == 'DD':
		return datePad(date.day)
	elif pattern == 'MM':
		return datePad(date.month)
	elif pattern == 'YY':
		return datePad(date.year % 100)
	elif pattern == 'YYYY':
		return str(date.year)
