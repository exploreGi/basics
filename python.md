## DataType
1. In Python, data type of the variables is determined dynamically at run time. Based on the value that is assigned to the variable python assigns the appropriate data type.This is done using a programming paradigm called duck typing.Duck Typing focuses on teh behaviour of the object rather than its specific type.Python looks at how you use the variable and the operations you perform on it to infer its data type.
1. All data types in python are object types and have associated class.

## Collections
In-built data structure , List, Set, Dictionary

## List
1. Mutable, defined in [ ], requirement has changing values, cannot be used as key in a dictionary

## Tuple
1. Immutable, defined in ( );read only list; maintains insertion order;allows duplicates;can add different types; can be used as key in dictionary
2. Can covert a list to  tuple using tuple() fucntion

## Set
1. Does not allow duplicates; defined in { }
1. SET object does not allowing indexing
1. SET object does not slicing or repetition
1. can perform update[ a,b ] and remove

## FrozenSet
can be used on a set using frozenset() function; once used, cannot do update or remove on the set

| Methods | Constructors |
| ----------------- | ---------------|
| any name          | __init__ |
| called when it is invoked | automatically when the class is instantiated |
| any number of times | once per object |
| business logic | initialise and declare variables |

## Encapsulation 

IN python, private fields are not completely hidden.They can be accessed using name mangling
Encapsulation is the process binding the methods and data/fields together so that only those methods can access that data.
