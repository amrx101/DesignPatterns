BUILDER DESIGN PATTERN

- Used when we have to  create a product that has either
    - Lots of components
    - Lost of configurations
    - Client may want a granular customisation of these components

Main Classes
1. Product : This is the product class which has setters for all the components.
2. BuilderInterface: This is an ABC which list all abc methods  required to build the product. 
3. ConcreteBuilder: This implements BuilderInterface.
4. Director: This is the bridge between client and the entire mechanism.


Mechanism:

1. Create Product class.
   1. All components are properties
   2. All properties have setter
2. Create BuilderInterface(ABC)
   1. In the init, instantiate Product() and have a getter for it
   2. Declare an abc method for each component of Product.
3. Concrete Builder:
   1. Implement each abc method od BuilderInterface.
4. Director:
   1. Has Concrete Builder as an attribute
   2. Calls self.concrete_builder.build()
   3. ConcreteBuilder attr is settable, so client can use just 1 Director object to create different type of Product

