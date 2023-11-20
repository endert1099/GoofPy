# GoofPy
A library for creating objects and game sims in Python, more things coming soon

## Currently supports:
- Pygame
- GameObjects
- Players
- Games

## Docs:
- `goof` class:
Takes ID(int) and meta(any)
  ```
  import goofpy
  
  obj = goofpy.goof(0, "TestMeta")
  
  ```
  Class functions:
  `getID()`, `getMeta()`, and `setMeta(value)`, are properties of any `goof` class, self-explanatory
  The below are not part of the `goof` class but relate to it.
  `getObjectByClass(class)` returns all instances of a certain class
  `getMetaById(id)` is self-explanatory
  `compareMeta(originalID, newID)` gets the meta of the object based on id, returns `True` if the 2 are equal
  `getObjsWithMeta(meta)` returns all objects with a particular meta value

- `GameObject` class:
Takes an ID, x, y, z, data, type, can take zIndex
  ```
  import goofpy

  obj = goofpy.goof(0, "TestMeta")
  gObj = goofpy.GameObject(obj.goofid, 
  ```
- `Creator` class:
Takes no parameters
  ```
  import goofpy

  c = goofpy.Creator()
  ```
  Class functions:
  `givePosition2D(obj: goof, x, y, zIndex) 
