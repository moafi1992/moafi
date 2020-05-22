from django.test import TestCase

# Create your tests here
mylist=(1,2,3)
mylist[0]=0
for x in mylist:
    print(x)