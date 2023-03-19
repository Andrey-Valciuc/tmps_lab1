# TMPS Laboratorul 1
#### Realizat:  Valciuc Andrei TI-204
## Sarcina: Elaborarea unui proiect care respectă cele 5 principii SOLID
## Realizarea sarcinii:


##1.Single Responsibility Principle (SRP):
Clasele Rectangle, Circle, Square și Triangle au fiecare o singură responsabilitate, care este să calculeze aria figurilor respective. Iată un exemplu al clasei Rectangle care își implementează singura responsabilitate:

```
class Rectangle(IShape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        return self.length * self.breadth
```
##2.Open/Closed Principle (OCP):
Proiectul este deschis pentru extindere, dar închis pentru modificare. Forme noi pot fi adăugate prin crearea unei noi clase care implementează interfața IShape fără a o modifica. Spre exemplu mai jos putem observa adăugarea unei figuri noi:

```
class Pentagon(IShape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return 1.720477 * self.side * self.side
```

##3.Liskov Substitution Principle (LSP):
Fiecare clasă de formă poate fi înlocuită cu interfața de bază IShape, fără a afecta corectitudinea programului. Iată un exemplu de program care utilizează interfața IShape pentru a calcula aria unui obiect Circle:
```
class Circle(IShape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius * self.radius


shape = Circle(radius)
area_calculator = AreaCalculator()
area = area_calculator.calculate_area(shape)
```

##4.Interface Segregation Principle (ISP):
ISP spune că interfețele ar trebui să fie specializate, astfel încât modulele să nu fie forțate să implementeze metode pe care nu le folosesc sau nu au nevoie de ele. În acest cod, interfața IShape conține doar o metodă, calculate_area(), care este necesară pentru a calcula aria formei. Această interfață este implementată de toate clasele de forme 

```
class IShape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
```

##5.Dependency Inversion Principle (DIP):
Proiectul respectă acest principiu depinzând de abstracții (interfața IShape) mai mult decât de implementări concrete (clasele de figuri).În această secvență de cod, clasa abstractă IShape reprezintă o abstracție și definește o metodă abstractă calculate_area(). Această clasă este folosită ca și tipul de date pentru parametrul shape din metoda calculate_area() a clasei AreaCalculator. Deoarece IShape este o abstracție, AreaCalculator depinde de aceasta în loc să depindă de implementările concrete ale figurilor. Prin urmare AreaCalculator este dependent de o abstracție și nu de implementări concrete

```
class IShape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class AreaCalculator:
    def calculate_area(self, shape: IShape):
        return shape.calculate_area()

```





