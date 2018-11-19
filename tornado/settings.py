import tornado
from tornado.options import define, options

define("debug", default=True, help="debug mode")
if options.debug:
    print('DEBUG IS ON')
define("port", default=8888, help="run on the given port", type=int)
tornado.options.parse_command_line()


