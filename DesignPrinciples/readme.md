- KISS 
  - Viljum forðast needless complexity, þurfum við pattern ?
- YAGNI
  - Ekki bæta við functionality fyrr en þú þarft það !
  - Requirements breytast
- Rule of Three
  - Við viljum býða með abstraction þangað til við erum komin með 3 dæmi
  - (3 er ekki harðsett regla)
- DRY (Dont repeat yourself)
  - Mótsögn við Rule of three (hugsa fyrst um rule of three)
  - Minka endurtekt, einangra það sem er sameiginlegt frá öðrum
- Knuth's Optimization Principle
  - Kemur inn á KISS (svipað)
  - Hugsa um læsileika fyrst
  - Ekki optimize fyrr en við þurfum þess. 
- Strive for loosely coupled design
  - Componentar tala sem minnst við hvern annan, (tala saman í gegnum interface)
  - vita eins lítið um hvort annað o
- Law of Demeter
  - Viljum tala við nánustu vini okkar
  - A friend of a friend is a stranger
  - stuðlar að loose coupling
- Program to an interface not an implementation
  - Fókusa hvað klasi geri, ekki hvernig
  - Nota explicit eða implicit interface
  - stuplar að loose couping
- Composition vs Inheritance
  - Inheritance
    - parent og child mikið kúplað saman
    - breytingar á parent gæti leitt til breytingar á chield
    - Erfitt að gera breytingar
  - Composition 
    - auðvelt að skipta út hlutum sem þarf, færri klasa
- SOLID principles
  - Single Responsibility Principle (SRP)
    - Við viljum hjúpa breytingar svo ákveðinn kóði breytist saman (Það er ein ástæða til að kóði breytist)
  - Open-Closed Principle (OCP)
    - Við viljum bæta við virkni með nýjum kóða en ekki breyta honum
    - Sjá Code
  - Liskov Substitution Principle (LSP)
    - objects of a superclass should be replaceable with objects of its subclasses without breaking the application
  - Interface Segregation Principle (ISP)
    - Clientar dependa á það sem þeir þurfa en ekki (Not implemented)
    - Amazon og dropbox dependa á 1 interface, dropbox útfærir ekki 2 virknir
    - laga brjóta interface upp í 2 fleiri interface og dropbox erfir bara það sem hann vantar en amazon erfir allt
  - Dependency Inversion Principle (DIP)
    - Við viljum ekki að high level componantar dependi á low level componenta
    - Við viljum að high level component eigi abstraction og low level dependi á þá
    - svipuð hugmynd og event driven
    - Oft í Onion Architecture
- 