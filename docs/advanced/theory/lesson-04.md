# Θεωρία: Οι βιβλιοθήκες time και random

[:material-file-pdf-box: Εκτυπώσιμο PDF](lesson-04.pdf){ .md-button }

## Βιβλιοθήκες (libraries)

Βιβλιοθήκη ονομάζεται μια συλλογή έτοιμου κώδικα (κυρίως συναρτήσεων) της Python.

Για να τις εισάγουμε στα προγράμματά μας, γράφουμε `import` και μετά το όνομα
της βιβλιοθήκης.

```python
import time
import random
```

Για να χρησιμοποιήσουμε κάποια συνάρτηση μιας βιβλιοθήκης, γράφουμε πρώτα το
όνομα της βιβλιοθήκης, βάζουμε μια τελεία και καλούμε τη συνάρτηση.

```python
time.sleep()
```

!!! note "Σημείωση"
    Το `import` το γράφουμε **μία φορά**, στην αρχή του προγράμματος.

??? tip "Ψάξε μόνος σου"
    [docs.python.org — Modules (tutorial)](https://docs.python.org/3/tutorial/modules.html)

## Η βιβλιοθήκη time

Time ονομάζεται η βιβλιοθήκη που εισάγει χρόνο στα προγράμματά μας. Έχει δύο
βασικές συναρτήσεις.

### `time.time()`

Επιστρέφει τον αριθμό δευτερολέπτων που έχει περάσει από τις 12 τα μεσάνυχτα,
την 1η Ιανουαρίου του 1970! (δεν κάνω πλάκα…)

```python
start = time.time()

for i in range(10000000):
    x = 5
    x = x + 10

end = time.time()

program_time_in_seconds = end - start
```

Το παραπάνω πρόγραμμα μετράει τον αριθμό των δευτερολέπτων που χρειάστηκε το
`for` loop.

### `time.sleep()`

Παγώνει το πρόγραμμα για τον αριθμό δευτερολέπτων που ζητήσαμε.

```python
x = 0

while True:
    time.sleep(1)
    x = x + 1
    if x >= 100:
        break
```

Το παραπάνω πρόγραμμα μετράει 100 δευτερόλεπτα και μετά τερματίζει.

??? tip "Ψάξε μόνος σου"
    - [docs.python.org — `time.time()`](https://docs.python.org/3/library/time.html#time.time)
    - [docs.python.org — `time.sleep()`](https://docs.python.org/3/library/time.html#time.sleep)

## Η βιβλιοθήκη random

Random ονομάζεται η βιβλιοθήκη που εισάγει τυχαιότητα στα προγράμματά μας.
Ακολουθούν οι βασικότερες συναρτήσεις της.

### `random.randint(a, b)`

Επιστρέφει έναν τυχαίο ακέραιο από `a` ως `b`, με πιθανότητα 1/(b-a+1).

```python
die = random.randint(1, 6)   #ρίψη δίκαιου ζαριού
```

### `random.random()`

Επιστρέφει έναν τυχαίο δεκαδικό αριθμό από το 0.0 έως το 1.0, αλλά όχι το 1.0.

```python
probability = random.random()

if (probability < 0.2):
    print("low chance of happening")
```

### `random.uniform(a, b)`

Επιστρέφει έναν τυχαίο δεκαδικό αριθμό από το `a` ως το `b`.

```python
probability = random.uniform(0.0, 1.0)

if (probability == 1.0):
    print("It will definitely happen")
```

### `random.choice()`

Επιστρέφει ένα τυχαίο στοιχείο μιας λίστας.

```python
coin = random.choice(["heads", "tails"])
```

### `random.shuffle()`

Ανακατεύει τυχαία τη σειρά των στοιχείων μιας λίστας.

```python
cards = ["ace", "king", "queen", "jack"]

random.shuffle(cards)
print(cards)
```

```screen title="Έξοδος"
['queen', 'ace', 'king', 'jack']
```

??? tip "Ψάξε μόνος σου"
    - [docs.python.org — `random.randint()`](https://docs.python.org/3/library/random.html#random.randint)
    - [docs.python.org — `random.random()`](https://docs.python.org/3/library/random.html#random.random)
    - [docs.python.org — `random.uniform()`](https://docs.python.org/3/library/random.html#random.uniform)
    - [docs.python.org — `random.choice()`](https://docs.python.org/3/library/random.html#random.choice)
    - [docs.python.org — `random.shuffle()`](https://docs.python.org/3/library/random.html#random.shuffle)
