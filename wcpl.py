#!/usr/bin/env python3

WCPL_VERSION = '0.0.1'
WCPL_BUILD = 1

def wcpl(data, env):
	compiled = []

	for line in data.split('\n'):
		cmd = line[0]
		commands = line.split(' ')
		if commands[0] == 'm':
			meta_type = commands[1]
			if meta_type == 's':
				


	return '<html>%s</html>' % ''.join(compiled)

def main():
	if len(argv) > 1:
		fname = argv[1]
		result = ""
		env = {
			"meta": {
				"charset": "utf-8",
				#"title": "default"
			},
			"wcpl": {
				"version": WCPL_VERSION,
				"build": WCPL_BUILD,
			}
		}
		with open(fname, 'r') as f:
			wcpl(f.read(), env)

if __name__ == '__main__':
	main()
