
This project is to be done individually.

Do not show your code to anyone, or look at anyone else's.

You may discuss general concepts following the empty hands rules.

In this project you will write 9 classes as shown in:
![Barnyard Inheritance Diagram](img/BarnyardInheritance.png)

The classes are to be defined in the `src` folder using the following file and class names:
* `farm_animal.py` : `FarmAnimal`
  * All farm animals have constructor that has a single age (in years) instance attribute  (use `self.age` as the name)
  * All farm animals have a `str` conversion method that prints the class type and age; you can do this with only a single `str` method in the `FarmAnimal` or you can override as needed.
  * All farm animals have a `make_sound` method that returns a string
    * The method in `FarmAnimal` should just return an empty string
  * All farm animals have an equal method that returns true if the objects are the same class and the same age
  
* `winged_animal.py` : `WingedAnimal`
  * Winged animals are FarmAnimals that make a `flap, flap` sound

* `ruminant.py` : `Ruminant`
  * https://en.wikipedia.org/wiki/Ruminant
  * Ruminants make a `burp` sound

* `duck.py` : `Duck`
  * `Duck`s are `WingedAnimal`s that add a `quack, quack` sound
    * e.g. `flap, flap - quack, quack`

* `chicken.py` : `Chicken`
  * `Chicken`s are `WingedAnimal`s that add a `cluck, cluck` sound

* `goat.py` : `Goat`
  * `Goat`s are `Ruminant`s that add a `baaah` sound

* `cow.py` : `Cow`
  * `Cow`s are `Ruminant`s that make either (your choice) of two sounds:
    * They add `moo` to the `burp`, or
    * They say `Eat mor chikin!` without the `burp` (these are civilized cows)

* `hen.py` : `Hen`
  * `Hen`s are `Chicken`s that add a `squawk!` sound when laying eggs
    * e.g. `flap, flap - cluck, cluck - squawk!`

* `rooster.py` : `Rooster`
  * `Rooster`s are `Chicken`s that add a `cock-a-doodle doo` to WingedAnimal sound
    * e.g. `flap, flap - cock-a-doodle doo!`

These class definitions are repetitive but don't require a lot of code, and even less
if you properly use inheritance. 

In addition to the classes, define `barnyard.py` script (not class) with the following methods:
* `get_barnyard()` method
  * returns a `list` of `FarmAnimals` containing:
    * At least 1 of each "leaf" types in the inheritance tree (i.e., Hen, Rooster, Duck, Cow, Goat)
    * At least 4 hens with the following ages (0.25, 0.6, 1.0, 8)
    * At least 3 roosters with the following ages (0.25, 0.6, 1.0)
    * Thus, the list must contain at least 10 items
    * Keep the list reasonable with no more the 100 items
    * Contains only `FarmAnimal` instances
    * I suggest using `random.shuffle` to shuffle your list in place so the animals are in no particular order for testing other methods
    
* `listen(barnyard_list)` method
  * Given a list, return a new list containing the associated sounds they make (one item per animal)
  * If the list contains something other than a FarmAnimal, just ignore that item 
    * Do not let the program crash, but I don't care how you protect this 
    
* `get_roosters(barnyard_list)` method
  * Given list, return a new list containing only `Rooster`s
  * It is possible to do this in one line using a list comprehension
    * But you do NOT have to do it that "Pythonic" way 

* `get_layers(barnyard_list)` method
  * Given a list of `FarmAnimal`s, return a new list containing `Hen`s that are between the ages of 0.5 and 7.0 years inclusive
  * The list may contain other animals, so `isinstance` is your friend
  * It is possible to do this in one line using a list comprehension
    * But you do NOT have to do it that "Pythonic" way 

## Usage
<pre>
cow = Cow(3.5)
print(cow)
print(cow.make_sound())
barnyard = [cow] # A list with one cow
</pre>

shows:
<pre>
Cow : 3.5
burp - moo
</pre>

## Look at the provided unit tests for more details!

## Submission

* Code must be pushed to Gitlab and graded on WebCat.
* Your WebCat grade counts, so make sure your code is properly graded by the due date
* Due 12-April at 11:59PM
