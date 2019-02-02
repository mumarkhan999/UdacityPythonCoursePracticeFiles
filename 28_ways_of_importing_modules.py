"""
We can import modules by two ways

First way:

import calendar

but in this way you have to call methods of calendar like this

calendar.month( ... )

Second Way:

from calendar import *

so now you will call method with out the name of module

month( ... )


You should use the first way when you have imported 2 or more modules
and they have methods with same name

e.g.

pow( ... ) is also built in
as well as in math module
math.pow( ... )

Use second way when your method is not present in any other imported module

"""
