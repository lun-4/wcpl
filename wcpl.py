#!/usr/bin/env python3

import sys
argv = sys.argv

WCPL_VERSION = '0.0.1'
WCPL_BUILD = 1

def wcpl(data, env):
	compiled = []
	env['_head'] = ''

	for line in data.split('\n'):
		if len(line) < 1:
			continue
		cmd = line[0]
		commands = line.split(' ')
		if commands[0] == 'm':
			meta_type = commands[1]
			meta_command = (''.join(commands[2:])).split('=')
			meta_var = meta_command[0]
			meta_val = meta_command[1]

			print(meta_command)
			if meta_type == 's':
				# read string
				meta_val = meta_val[1:-1]
				env['meta'][meta_var] = meta_val

			env['_head'] += '<meta %s=%s>' % (meta_var, meta_val)
		if commands[0] == 't':
			compiled.append("%s" % ''.join(commands[1:]))

	res = ''

	res += '<head>\n %s \n</head>\n' % ''.join(env['_head'])
	res += '\n<body>\n %s \n</body>' % '\n'.join(compiled)

	return '<html>\n%s\n</html>' % res

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
			print(wcpl(f.read(), env))

if __name__ == '__main__':
	main()
