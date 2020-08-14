 """The __init__.py file makes Python treat directories containing it as modules. Furthermore, 
 this is the first file to be loaded in a module,
 so it can be used to execute code that has to be run each time a module is loaded,
 or specify the submodules to be exported.

 PyMySQL is a pure-Python MySQL client library.

 """
import pymysql
pymysql.version_info = (1, 3, 13, "final", 0)
pymysql.install_as_MySQLdb()
