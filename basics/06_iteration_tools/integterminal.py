# 06_iteration_tools> python
# Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> f=open('script.py')
# >>> f.readline()
# 'import time\n'
# >>> 
# >>> f.readline()
# 'print("I am here.")\n'
# >>> f.readline()
# 'username="Pranjal"\n'
# >>> f.readline()
# 'print(username)'
# >>> f.readline()
# ''
# >>> f.readline()
# ''   

# --------------****-----------

# using __next__()
# chaay aur python\06_iteration_tools> python
# Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> f=open('script.py')
# >>> f.__next__()
# 'import time\n'
# >>> f.__next__()
# 'print("I am here.")\n'
# >>> f.__next__()
# 'username="Pranjal"\n'
# >>> f.__next__()
# 'print(username)\n'
# >>> f.__next__()
# '\n'
# >>> f.__next__()
# Traceback (most recent call last):
#   File "<python-input-6>", line 1, in <module>
#     f.__next__()
#     ~~~~~~~~~~^^
# StopIteration
# >>>

# --------------*********------------

# \06_iteration_tools> python
# Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> for line in open('script.py'):
# ...     print(line)
# ... 
# import time

# print("I am here.")

# username="Pranjal"

# print(username)







# >>> 



# ---------*****------------
# >>> f=open('script.py')
# >>> while True:
# ...     line=f.readline()
# ...     if not line: 
# ...         break
# ...     print(line, end='')
# ... 
# import time
# print("I am here.")
# username="Pranjal"
# print(username)



# >>> 