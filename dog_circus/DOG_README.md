## Circus Dogs

This directory contains my first class script after completing oop tutorials by
[Richard White](https://www.youtube.com/user/rwhite5279/featured):

[**Intro To Object-Oriented Programming In Python (parts 1 & 2)**](https://www.youtube.com/watch?v=wYYzteRKU7U)


### CircusDogs Class

The class is based on a ficticious circus dog troupe.
A dog object can be instanciated with passing a 'name' and a 'breed',
an empty 'tricks' list is created and also a counter which is internally set
to zero.
This class inherits from the python 'object' class.

'Get' methods provide a means to return the name and breed of the dog.
An 'add\_trick' method appends a trick (string) to the tricks list.

### Tricks Counter

There are three implementations of the tricks counter (branches):

- a counter not contained within the instance, that is incremented via an
independent enumerate function of the trick list within the 'num\_of\_tricks'
method.  The counter quantity in is not stored but calculated at each call.

- a counter variable contained within each instance which is incremented with each
add\_trick method call but has no programatic connection with the tricks list.

- a counter variable contained within each instance which is incremented with each
add\_trick method call from within the add method via an enumerate function of
the trick list

I will research further into the better counter method to use.
