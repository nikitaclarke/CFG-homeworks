**Q1. How does Object Oriented Programming differ from Procedural Oriented Programming?**

Object Oriented Programming (OOP) differs from Procedural Oriented Programming (POP). OOP is a programming model which uses objects. Whereas, POP calls upon procedures.

Some of the key features of OOP include Polymorphism, where multiple objects can share the same name, but serve different functionalities. Inheritance which allows for child classes that inherit attributes and methods from the parent class. Encapsulation which allows for more secure implementation, by containing the class or object with their methods. Additionally, abstraction allows classes to keep certain data attributes private, which can keep the program more secure.

In comparison, the key features of POP include predefined functions, which are functions that are used from an external library or from the programming language. Local variables which means a method can only work within the code it is defined, and doesn’t affect the global state. In contrast, global variables are another key feature which are able to be accessed from anywhere within the program.

OOP is the most popular out of the two, and has a number of advantages over POP:
-   OOP is faster and easier to execute
-   OOP provides a clear structure for the programs.
-   The code is able to follow the DRY (Don’t Repeat Yourself) concept, meaning the code is easier to maintain and modify.
-   OOP is easier to create applications with less code and quicker execution.
-   The code is reusable due to the use of classes and objects.
-   The maintenance of the code is easier and doesn’t affect existing objects.
  
In comparison, there are also some advantages of using POP:
-   POP offers a simple and straightforward way to code.
-   It is easier to track the program flow with POP.
-   POP is useful for general-purpose programming
-   The code is able to be strongly structured.

In OOP, objects contain attributes and methods, which form the data included. The most popular use of OOP is class-based, where the objects are instances of classes. In comparison, POP calls upon procedures such as routines, subroutines and functions which contain a sequence of instructions to be carried out. The ideology behind POP is that the code should follow a narrative to serve the purpose of the program.

The main difference between the two is how they divide a program, OOP divides into smaller objects to do this, and POP divides into smaller procedures or functions. Another difference is that objects within OOP contain both data and functions, whereas POP contains procedures/functions that act onto the data. Some other differences include.

-   OOP uses a bottom-up approach, whereas POP uses a top-down approach
-   Inheritance is supported within OOP, whereas it is not in POP.
-   Encapsulation is supported within OOP, whereas it is not in POP
-   Polymorphism is supported within OOP, whereas it is not in POP.
-   The code can be reused using OOP, but cannot using POP.
-   OOP can be used to solve big problems, but POP is not suitable.
-   Adding new data and functions is easy using OOP, but it is not using POP.

In conclusion, there are many differences between OOP and POP, and advantages to using both depending on the purpose of the program. However, for large programs and big problem solving, it would be difficult to use POP solely. It is also worth noting that OOP is the most popular out of the two.

**Q2. What's polymorphism in OOP?**

Polymorphism is a key feature of Object-Oriented Programming (OOP). Polymorphism is the use of a single entity such as a method, operator or object that represents different types in different scenarios.

Polymorphism within OOP can be used while creating class methods, and allows for different classes to have methods with the same name. By doing this, the object can be disregarded and the methods can be called. An example of this is below, I have created two classes Rabbit and Horse, which both have the same method names introduction() and make_sound(). The classes were joined or linked together in any way, but polymorphism makes it possible to call the methods from both classes.

    class Rabbit:  
    def __init__(self, name, age):  
        self.name = name  
        self.age = age  
  
    def introduction(self):  
        print(f"I am a rabbit. My name is {self.name} and I am {self.age}")  
  
    def make_sound(self):  
        print("Squeak") 

	class Horse:  
    def __init__(self, name, age):  
        self.name = name  
        self.age = age  
  
    def introduction(self):  
        print(f"I am a horse. My name is {self.name} 		and I am {self.age}")  
  
    def make_sound(self):  
        print("Neighhhhh")  

	rabbit1 = Rabbit('Barney', 3)  
	horse1 = Horse("Elsa", 7)  
  
	for animal in (rabbit1, horse1):  
    animal.make_sound()  
    animal.introduction()  
    animal.make_sound()

	# Output:
	# Squeak
	# I am a rabbit. My name is Barney and I am 3
	# Squeak
	# Neighhhhh
	# I am a horse. My name is Elsa and I am 7
	# Neighhhhh

Another example of Polymorphism within OOP is Method Overriding. This is used alongside inheritance. The parent class can be overridden, by redefining certain methods and attributes specifically to the child class. In my example below, polymorphism works to override the max_speed() method and uses the one that is defined in the child class (Car). In comparison, show() was not overridden by the Car class so it is taken from the Vehicle class.

	class Vehicle:  
  
    def __init__(self, name, color, price):  
        self.name = name  
        self.color = color  
        self.price = price  
  
    def show(self):  
        print('Details:', self.name, self.color, self.price)  
  
    def max_speed(self):  
        print('Vehicle max speed is 200')  
  
  
	class Car(Vehicle):  
    def max_speed(self):  
        print('Car max speed is 500')  
  
  
	Car Object  
	car = Car('Tesla', 'Pink', 100000)  
	car.show()  
	car.max_speed()

	# Output:
	# Details: Tesla Pink 100000
	# Car max speed is 500

Another example of Polymorphism is Method Overloading, which is calling the same method that has different parameters. However, this will raise a TypeError within Python as it is not supported.

**Q3. What's inheritance in OOP?**

Within OOP, inheritance allows the child classes to inherit attributes and methods from the parent class. The parent class can also be referred to as base class or superclass. The child class can be referred to as a derived class or subclass. In order to create a child class, the parent class is added as a parameter when creating the class. For example, if we had a parent class of Animal and wanted to create a child class of Dog, it would look like this: Dog(Animal).

An example of single inheritance is below, where the Parent class has a name attribute, and an introduction() method. The child class Employee uses inheritance so the Employee class inherits the introduction() method from the Person class. By doing this, we are able to call the introduction() method within the Employee class. This is an example of single inheritance because the Employee class inherits from one parent class.

	class Person:  
    def __init__(self, name):  
        self.name = name  
  
    def introduction(self):  
        return f"Hi, it's {self.name}"  
  
  
	class Employee(Person):  
    def __init__(self, name, job_title):  
        self.name = name  
        self.job_title = job_title  
  
  
	employee = Employee('Nikita', 'Software Engineer')  
	print(employee.introduction())

	# Output:
	# Hi, it's Nikita

Additionally, Python has a super() function that will make the child class inherit all the methods and properties from its parent class. By using this, the parent element does not have to be named within the __init__ function.

Inheritance is useful as there are attributes and functions that can apply to a whole class. This prevents repetition, and allows shared functions. The parent class can contain universal attributes and functions. It is also useful as you are still able to customise these classes if necessary.

There are five forms of Inheritance within OOP:

-   Single Inheritance where the child class inherits from one parent class.
-   Multiple Inheritance where the features of multiple parent classes are inherited into the child class.
-   Multilevel Inheritance where a new child class inherits from a parent and a child class.
-   Hierarchical Inheritance where more than one child class is created from a single parent class.
-   Hybrid Inheritance occurs when there are multiple types of the above inheritances.

**Q4. If you had to make a program that could vote for the top three funniest people in the office, how would you do that? How would you make it possible to vote on those people?**

In order to make this program, I would use Python, SQL, and Flask and follow the below steps:

-   Create a database within MySQL with a column for the names of the staff members, first column, second column and third column. I would then populate the MYSQL database with all of the names of the staff members within the office.
-   Build the backend within Python by connecting to the MYSQL Database that has been built with the staff members details.
-   Connect Flask to Python in order to have an interface for people to vote.
-   Create a GET request to pull the names of the staff members, and the corresponding 1,2,3. Create HTML/CSS to display this next to each staff member's name.
-   Create a POST request that will update the votes within the MYSQL database when the votes are made.
-   The program will need a user interface, to allow the user to log in and cast their vote. A function will need to be created where the user’s name cannot match the name they are voting for, meaning that people cannot vote for themselves.
-   A function will need to be created allowing the user to only vote once per one, two and three.
-   Create a set time that the vote will end, and allow no more POST requests to the database.
-   Once the vote ends, a function to tally up the votes within the MySQL Database and rank the highest votes for first, second and third. Counter could be utitlised for this.
-   Create a HTML/CSS to reveal the winners once the vote has ended.

The website would look something like the below with a list of all staff members. The staff members are then able to vote for the person they think is funniest, the second person and the third person:

**![](https://lh6.googleusercontent.com/Exo5eBeZPiOO62B3vRC1oyR19ltXTgshqGB6dZcDMth1qGc2FFm9NZtQ-x7XYwBGiQf-GrX_VHqFgJQv9c3udg5twkZE7GDjRpwoNBzL94HKo3LTrXpSprlkrbZskYAxsR-tjLP3UEa6LDT-cVEOyXs)**

**Q5. What's the software development cycle?**

The Software Development Cycle explains how software is delivered in a series of different stages beginning with the planning and ending with the deployment of the software. The software development cycle consists of six stages: Planning and Requirement Analysis, Requirements, Design, Implement Software, Testing and Deployment.

*Stage 1. Planning and Requirement Analysis*

The requirement analysis is performed by the senior members within the team, and includes input from the customer, sales department, market surveys and subject matter experts. The information sourced from the requirement analysis is used to plan the project approach and to conduct a product feasibility study. Quality assurance and risk analysis is also conducted within this stage. In addition to this, resource allocation, capacity planning, project scheduling, cost estimation and provisioning are all taken into account during the planning stage. Once this stage is complete, there should be project plans, schedules, cost estimations and procurement requirements.

*Stage 2. Requirements*

In the requirements phase, the business must communicate with the software team to explain their requirements for the new development. These requirements are gathered from stakeholders and Subject Matter Experts (SMEs). The Development team and Product Managers discuss with the SMEs the processes that need to be developed or enhanced by the software team. Once this stage is complete, the output is a Waterfall project which lists all of the requirements within the project. Otherwise, an agile method would produce a backlog of tasks that are required to be actioned.

*Stage 3. Design*

Following the requirements, the software team and developers can look at designing the project/software. This process follows established patterns of application architecture and software development. Proven design patterns are used to keep consistency. The design phase may also include rapid prototyping in order to compare solutions to find the best design fit. Once this stage is complete, there will be a design document that has the chosen patterns and components that have been selected, and code that has been produced during the rapid prototyping which can be used as a starting point.

*Stage 4. Implement Software*

This phase involves producing the software. There are different ways that this may be conducted depending on the methodology. If Agile methodology is being used, this phase will be conducted in sprints. If Waterfall is being used, it will be conducted as a single block. Producing the software should be done as quickly as possible, and contact should be kept with the stakeholders to discuss the expectations that are being met. Once this stage is complete, there will be testable and functional software developed.

*Stage 5. Testing*

This phase is important, as quality software could not be produced without testing occurring. A number of tests are necessary during this phase, such as code quality, unit testing, integration testing, performance testing and security testing. These texts are usually automated to ensure that they run regularly and are always completed. The software has to reach the quality standards defined in the Software Requirement Specification. Once this stage is complete. There will be tested functional software that is ready for the next stage, deployment.

*Stage 6. Deployment*

The deployment phase is usually an automated phase. Sometimes, this phase is almost invisible and software is deployed as soon as it is ready to be. However, sometimes it does involve some manual approvals. It is recommended that deployment is fully automated in a continuous deployment model, such as Application Release Automation (ARA). Once this stage is complete, the working software will be released.

**Q6. What's the difference between agile and waterfall?**
Waterfall and Agile are two different methodologies used in the Software Development Life Cycle (SDLC). Waterfall is a sequential approach, meaning that the team works through each phase once the phase before has been completed. Waterfall divides the SDLC into distinct phases (requirements gathering, analysis and design, coding and unit testing, system and deployment). Within waterfall, each phase has to be signed off. In comparison, Agile is a team-based approach which encourages continuous development and testing as they are concurrent. Agile defines time-boxed phases called sprints, and allows for more communication between customers, developers, project managers. Within agile, if the work item hasn’t been completed, it will be recorded and the backlog will be adjusted, and the team will then move onto the next task or sprint.

There are key differences between the two:
-   Waterfall is sequential, whereas agile is a continuous iteration
-   Agile is known for flexibility, whereas waterfall is structured
-   Agile performs testing concurrently, whereas in waterfall, testing comes after the build phase.
-   Agile allows for change in requirements, whereas waterfall does not allow to change the requirements once project development has started.   
-   Phases may appear more than once within agile, but they will only be completed once in waterfall.
-   Project details can be adjusted within agile, but not in waterfall.
  
There are different advantages for using Waterfall or Agile. Some advantages for Waterfall include.
-   It is an easy methodology to manage as there is specific outputs from each phase.
-   Waterfall works well for smaller size projects where requirements are easily understood.
-   Waterfall produces faster delivery of a project.
-   The process and results are well documented

Whereas, there are also some limitations to the Waterfall methodology:
-   It is not ideal for a large project
-   If the requirements aren’t clear, it can be less effective
-   It is difficult to make any changes to previous phase.
-   There is no testing during development, which could end up creating problems in the testing phase.

In comparison, some advantages to Agile include:
-   Agile is focused on the client process. It ensures that the client is involved during every stage.
-   Agile teams are motivated and self-organised which can arguably produce a better result
-   Agile ensures the quality is maintained.
-   Agile allows for the client and team to know exactly what has been completed, and what hasn’t.

There are also some limitations to Agile:
-   It is not ideal for small projects.
-   It requires an expert to make important decisions.
-   There is an extra cost to use the Agile methodology.
-   The project can easily not stay on track.
  
Overall, there are many differences between the two and it can depend on the project which methodology is best to use.

**Q7. What is a reduced function used for?**

The reduce() function within Python allows a list to be reduced in a concise way. The reduce() function is not a built-in function,, and has to be imported from the functools module. The reduced function is the mathematical technique of folding or reduction. The reduced function has two required arguments, function and iterable.

The reduced function is used to reduce an iterable into a single cumulative value. To do this, it works by:
-   Applying a function to the first and the second element of an iterable.
-   Storing the result
-   Applying the function to the third element and the result
-   Continues the process until there are no values left

	    from functools import reduce  
		numbers = [1, 2, 3, 4]  
		total = reduce(lambda a, b: a + b, numbers)  
		print(total)

In the code example above, the reduce function is working by doing the below:
-   Applying the function to the first and second element: 1+2 = 3
-   Storing the result (3)
-   Applying the function to the third element and the stored result: 3+3 = 6
-   Storing the result (6)
-   Applying the function to the fourth element and the stored result: 6+4 = 10
-   There are no values left.
-   We then get the output of 10.

You can also use the reduce function to multiply:

    from functools import reduce  
	numbers = [1, 2, 3, 4]  
	result = reduce(lambda x, y: x * y, numbers)  
	print(result)

Again this works in a similar way:

-   Applying the function to the first and second element: 1*2 = 2
-   Storing the result (2)
-   Applying the function to the third element and the stored result: 2 * 3 = 6
-   Storing the result (6)
-   Applying the function to the fourth element and the stored result: 6 * 4 = 24
-   There are no values left.
-   We then get the output of 24

The reduced function can also be used to find the min/max in an iterable as per the below example:

    from functools import reduce  
	numbers = [5, 1000, 15, 7000, 4]  
	greatest = reduce(max, numbers)  
	print(greatest)

In addition to the uses shown in my examples, the reduce() function can also be used to check if all values are true. Although there are many uses of the reduce function, it is usually not the most optimal way of carrying out a function, as it calls the function many times, which can lead to slow and inefficient code.

**Q8. How does merge sort work?**

Merge sort is one of the most popular divide and conquer sorting algorithms, meaning it is divided into subgroups recursively until the solution is easy to solve. The solution is then combined. Merge sort has a O(n* log(n)) running time, which is the optimal running time.

Merge sort can be used to sort the values in any traversable data. Merge sort works by:
-   Splitting the data in half
-   Calling merge sort on each half to sort them recursively  
-   Merge both sorted halves into one sorted dataset

The algorithm works by moving from top to bottom, dividing the data into smaller and smaller parts until there are only separate elements. Then it moves back up the data to sort, and then combining.

An example would be:
-   An array of 2651743:
-   This would be split in half to 2651 and 743   
-   2651 would then be further divided into 26 and 51
-   743 would then be further divided into 74 and 3
-   26 would be divided to 2 and 6, 51 would be divided to 5 and 1
-   74 would be divided to 7 and 4, 3 would be left untouched.
-   Subgroups now all contain one element
-   The merge will then start:
-   Compare 2 and 6 and sort these - 2 and 6 will be saved.
-   5 and 1 would be compared - 1 and 5 will be saved.
-   7 and 4 would be compared - 4 and 7 will be saved.
-   3 is left untouched.
-   26 and 15 will then be compared (by the left element) and will be saved as 1 2 5 6
-   47 and 3 will be compared and will be saved as 3 4 7
-   There will be one last merge set - 1256 and 347. This will get the output 1234567

An example of Merge Sort in Python code is:

    def merge_sort(array):  
    if len(array) > 1:  
        left_array = array[:len(array)//2]  
        right_array = array[len(array)//2:]  
  
        merge_sort(left_array)  
        merge_sort(right_array)  
  
        left_array_index = 0  
	  right_array_index = 0  
	  merged_array_index = 0  
  
	  while left_array_index < len(left_array) and 	right_array_index < len(right_array):  
            if left_array[left_array_index] < right_array[right_array_index]:  
                array[merged_array_index] = left_array[left_array_index]  
                left_array_index += 1  
	  else:  
                array[merged_array_index] = right_array[right_array_index]  
                right_array_index += 1  
	  merged_array_index += 1  
  
	  while left_array_index < len(left_array):  
            array[merged_array_index] = left_array[left_array_index]  
            left_array_index += 1  
	  merged_array_index += 1  
  
	  while right_array_index < len(right_array):  
            array[merged_array_index] = right_array[right_array_index]  
            right_array_index += 1  
	  merged_array_index += 1  
  
  
	array_test = [2, 6, 5, 1, 7, 4, 3]  
  
	merge_sort(array_test)  
	print(array_test)
	
	# Output: [1, 2, 3, 4, 5, 6, 7]

**Q9. Generators - Generator functions allow you to declare a function that behaves like an iterator, i.e. it can be used in a for loop. What is the use case?**

Generators allow developers to make an iterator in a fast, easy and clean way. This is beneficial as iterators save memory space by using lazy evaluation which is useful for large datasets.

Generators have an improved memory performance by using the yield statement, which saves the state of the function. Therefore, the next time the function is called, the execution will continue from where it was left, with the same variable values before yielding. With generators, multiple yield statements can exist within a function without terminating the function as opposed to a single return statement.

Some use cases of generators include:
-   it does not hold entire data in the memory, as it yields one data at a time, whereas iterators load the entire dataset and iterates through the process. This is another example of how the performance is efficient.
-   Generators can be used to create a processing pipeline by creating a stack of generators, which improves readability and scalability of the code.
-   When the data is time bound, there is no reason to store the data for a long period of time.
-   When using large data, it would be impractical to store the data.
-   When it is likely that only a portion of the data will ever be needed
-   Easily scalable up to any amount of data

We can also use Generator Expressions, which works in the same way as a list comprehension but is surrounded by ().

**Q.10 Decorators - A page for useful (or potentially abusive?) decorator ideas. What is the return type of the decorator?**

Python decorators allow a function to be “wrapped” with another function. This is useful for code reuse and readability. The return type of a decorator is an object. Decorators allow the way the function behaves to change, without changing the code. An example of a very simple decorator is below:

Using the example below, @my_decorator now becomes a function that is able to use the hello object, and return something different to the interpreter. The decorator can also remove the function, or return something that is not a function.

    @my_decorator
	def  hello():
	print('hello')

Looking at the example above, @my_decorator now becomes a function that is able to use the hello object, and return something different to the interpreter. The decorator can also remove the function, or return something that is not a function. However, in most cases, the object our decorator returns mimics the function that was decorated.

Another example is below. In this example, we created the function remove_butter, and the function make_cake. We decorated the make_cake function with the remove_butter function, which returns the modified make_cake function by removing the butter from the cake recipe, leaving with an output of:

	Here is a cake made using:
	- flour
	- sugar
	- strawberries

    def remove_butter(cake_recipe):  
    def cake_recipe_without_butter(ingredients):  
        ingredients.remove('butter')  
        cake_recipe(ingredients)  
    return cake_recipe_without_butter  
  
	@remove_butter  
	def make_cake(ingredients):  
    print("Here is a cake made using: ")  
    for ingredient in ingredients:  
        print(f"- {ingredient}")  
  
	make_cake(['flour', 'sugar', 'butter', 'strawberries'])

We could also use multiple decorators, as seen in the example below where @swap_butter_for_margarine and @swap_sugar_for_sweetener has been used. This modifies the return of the make_cake function leading to an Output of:
	 
	 # Output:
	 Here is a cake made using: 
	- flour
	- strawberries
	- margarine
	- sweetener

	# Code:
    def swap_butter_for_margarine(cake_recipe):  
    def cake_recipe_with_margarine_instead_of_butter(ingredients):  
        if 'butter' in ingredients:  
            ingredients.remove('butter')  
            ingredients.append('margarine')  
        cake_recipe(ingredients)  
    return cake_recipe_with_margarine_instead_of_butter  
  
	def swap_sugar_for_sweetener(cake_recipe):  
    def cake_recipe_with_sweetener_instead_of_sugar(ingredients):  
        if 'sugar' in ingredients:  
            ingredients.remove('sugar')  
            ingredients.append('sweetener')  
        cake_recipe(ingredients)  
    return cake_recipe_with_sweetener_instead_of_sugar  
  
	@swap_butter_for_margarine  
	@swap_sugar_for_sweetener  
	def make_cake(ingredients):  
    print("Here is a cake made using: ")  
    for ingredient in ingredients:  
        print(f"- {ingredient}")  
  
	make_cake(['flour', 'sugar', 'butter', 'strawberries'])

Decorators can be potentially abusive, as the principle of least surprise may not be adhered to due to the fact that potentially anything could be assigned as a decorator. A decorated function is expected to be called in the same way as if it wasn’t decorated. If it isn’t, it may lead to the code not being readable, and be harder to debug.