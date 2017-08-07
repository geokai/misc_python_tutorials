### Circus Dogs

This directory contains my own first class script after completing oop tutorials by
[Richard White](https://www.youtube.com/user/rwhite5279/featured):

[**Intro To Object-Oriented Programming In Python (parts 1 & 2)**](https://www.youtube.com/watch?v=wYYzteRKU7U "Richard White")


__CircusDogs Class__

The class is based on a ficticious circus dog troupe.
A dog object can be instanciated with passing 'name' and a 'breed' instance variables,
an empty 'tricks' list is created and also a counter which is internally initially set
to zero.
This class inherits from the python 'object' class.

'get\_' methods provide a means to return the name and breed of the dog.
An 'add\_trick' method appends a trick (string) to the tricks list.

__Tricks Counter__

There are three implementations of the tricks counter (see branches):

1. a counter not contained within the instance, that is incremented via an
independent enumerate function of the trick list within the 'num\_of\_tricks'
method.  The counter quantity in is not stored but calculated at each call.

1. a counter variable contained within each instance which is incremented with each
add\_trick method call but has no programatic connection with the tricks list.

1. a counter variable contained within each instance which is incremented with each
add\_trick method call from within the add method via an enumerate function of
the trick list

I will research further into which would be the better counter method to use.


__Overriding method__

The object superclass \_\_str\_\_ method is overridden to provide a more useful output
of instance state.
