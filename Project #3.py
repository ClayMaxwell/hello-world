Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print ("Your name is", name)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    print ("Your name is", name)
NameError: name 'name' is not defined
>>> name = ("Pistole Pete")
>>> print ("Your name is", name)
Your name is Pistole Pete
>>> 