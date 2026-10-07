# Θεωρία: Λίστες στην Python

[:material-file-pdf-box: Εκτυπώσιμο PDF](lesson-03.pdf){ .md-button }

## Εισαγωγή στις λίστες

Οι λίστες (lists) αποτελούν τύπο δεδομένων της Python. Αντιστοιχίζουν μια σειρά
δεδομένων σε μια μεταβλητή.

Όταν ορίζουμε μια λίστα, βάζουμε τα δεδομένα σε αγκύλες και τα χωρίζουμε με
κόμματα.

```python
my_list = ["yes", "no", "maybe"]
```

Τα δεδομένα εντός μιας λίστας μπορεί να ανήκουν σε οποιοδήποτε τύπο.

```python
random_list = ["pancakes", 8988676767, 9.44, False]
```

Ορίζουμε μια **κενή λίστα**, δηλαδή μια λίστα που δεν περιέχει στοιχεία, με
αγκύλες `[]`.

```python
my_empty_list = []
```

??? tip "Ψάξε μόνος σου"
    [docs.python.org — Lists (tutorial)](https://docs.python.org/3/tutorial/introduction.html#lists)

## Μέγεθος της λίστας (length)

Ο αριθμός των στοιχείων μίας λίστας είναι το μέγεθός της. Μπορούμε να
υπολογίσουμε αυτόν τον αριθμό χρησιμοποιώντας τη συνάρτηση `len()`.

```python
fruit_basket = ["apple", "banana", "cherry"]
print(len(fruit_basket))
```

```screen title="Έξοδος"
3
```

??? tip "Ψάξε μόνος σου"
    [docs.python.org — `len()`](https://docs.python.org/3/library/functions.html#len)

## Προσπέλαση στοιχείων (indexing)

Μπορούμε να έχουμε πρόσβαση στα στοιχεία μίας λίστας χρησιμοποιώντας δείκτες
(indexes) μαζί με το όνομα της λίστας.

Οι δείκτες είναι απλά ένα νούμερο που μας δείχνει τη θέση του στοιχείου στη
λίστα. Η αρίθμηση αυτή ξεκινάει από το 0, όχι από το 1. Ας δούμε αναλυτικά τη
λίστα `fruit_basket = ["apple", "banana", "cherry"]`:

| Index    | 0         | 1          | 2          |
|----------|-----------|------------|------------|
| Στοιχείο | `"apple"` | `"banana"` | `"cherry"` |

!!! warning "Προσοχή"
    Η αρίθμηση ξεκινά από το **μηδέν**!

Αυτό που βλέπουμε ως δεύτερο στοιχείο στη λίστα έχει index 1, το τρίτο 2 κλπ,
δηλαδή ένα μικρότερο από αυτό που αυθόρμητα θα σκεφτόμασταν. Άρα για να έχουμε
πρόσβαση στα στοιχεία της λίστας γράφουμε το όνομα της λίστας και τον δείκτη σε
αγκύλες:

- `"apple"` → `fruit_basket[0]`
- `"banana"` → `fruit_basket[1]`
- `"cherry"` → `fruit_basket[2]`

```python
random_list = ["pancakes", 8988676767, 9.44, False]

print(random_list)
print(random_list[0])

my_favorite_number = random_list[2]
print(my_favorite_number)
```

```screen title="Έξοδος"
['pancakes', 8988676767, 9.44, False]
pancakes
9.44
```

### Αρνητικοί δείκτες

Μπορούμε να χρησιμοποιήσουμε αρνητικούς δείκτες για να προσπελάσουμε τα
στοιχεία της λίστας από το τέλος προς την αρχή:

| Index    | -3        | -2         | -1         |
|----------|-----------|------------|------------|
| Στοιχείο | `"apple"` | `"banana"` | `"cherry"` |

- `"cherry"` → `fruit_basket[-1]` — 1ο στοιχείο από το τέλος
- `"banana"` → `fruit_basket[-2]` — 2ο στοιχείο από το τέλος
- `"apple"` → `fruit_basket[-3]` — 3ο στοιχείο από το τέλος

```python
random_list = ["pancakes", 8988676767, 9.44, False]
print(random_list[-2])
```

```screen title="Έξοδος"
9.44
```

??? tip "Ψάξε μόνος σου"
    [docs.python.org — Common Sequence Operations](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations)
    (δες τις γραμμές `s[i]` και τη σημείωση για αρνητικούς δείκτες)

## Προσπέλαση τμήματος (slicing)

Μπορούμε να έχουμε πρόσβαση σε ολόκληρο τμήμα της λίστας χρησιμοποιώντας τους
δείκτες.

### Σύνταξη

```python
my_list[start:end:step]
```

- `start`: από ποια θέση ξεκινάμε
- `end`: έως ποια θέση — **δεν** συμπεριλαμβάνεται στην υπολίστα που
  επιστρέφεται!
- `step`: πόσα βήματα κάνουμε για το επόμενο στοιχείο

Αν παραλείψουμε κάποιο από αυτά, παίρνει προεπιλεγμένη τιμή:

- Αν αφήσουμε το `start` κενό → ξεκινάει από την αρχή της λίστας.
- Αν αφήσουμε το `end` κενό → φτάνει έως το τέλος.
- Αν αφήσουμε και τα δύο κενά, `my_list[:]` → παίρνουμε ολόκληρη τη λίστα.
- Αν αφήσουμε το `step` κενό → παίρνει την τιμή 1, δηλαδή επιστρέφει
  συνεχόμενα στοιχεία.
- Μπορούμε επίσης να χρησιμοποιούμε αρνητικούς δείκτες (π.χ. `-1`, `-2`) για
  να μετράμε από το τέλος.

### Παραδείγματα

Σε όλα τα παραδείγματα χρησιμοποιούμε τη λίστα `nums = [1, 2, 3, 4, 5, 6]`:

| Index    | 0 | 1 | 2 | 3 | 4 | 5 |
|----------|---|---|---|---|---|---|
| Στοιχείο | 1 | 2 | 3 | 4 | 5 | 6 |

**Παράδειγμα 1 — Από θέση `start` έως `end`**

```python
nums = [1, 2, 3, 4, 5, 6]
print(nums[2:5])    # από τη θέση 2 έως πριν τη θέση 5 (2 : 5 : _)
```

```screen title="Έξοδος"
[3, 4, 5]
```

!!! info ""
    Ενώ επιλέξαμε `end=5`, το στοιχείο στη θέση 5 (`nums[5]` → `6`) δεν
    επιστρέφεται. Το τελευταίο στοιχείο που επιστρέφεται είναι αυτό στη θέση 4
    (`nums[4]` → `5`). Το `end` λέει έως ποια θέση, αλλά η ίδια αυτή η θέση δεν
    επιστρέφεται· φτάνουμε μέχρι την προηγούμενη. Εδώ πήραμε τις θέσεις 2, 3, 4.

**Παράδειγμα 2 — Από την αρχή έως θέση `end`**

```python
nums = [1, 2, 3, 4, 5, 6]
print(nums[:4])    # παραλείψαμε αρχή και step (_ : 4 : _)
```

```screen title="Έξοδος"
[1, 2, 3, 4]
```

Επιστρέφουμε από τη θέση 0 έως και τη θέση 3.

**Παράδειγμα 3 — Από θέση `start` έως το τέλος**

```python
nums = [1, 2, 3, 4, 5, 6]
print(nums[3:])    # παραλείψαμε τέλος και step (3 : _ : _)
```

```screen title="Έξοδος"
[4, 5, 6]
```

Πήραμε τις θέσεις 3, 4, 5.

**Παράδειγμα 4 — Χρήση `step` (βήμα)**

```python
nums = [1, 2, 3, 4, 5, 6]
print(nums[::2])    # από αρχή έως τέλος παίρνω κάθε 2ο στοιχείο
```

```screen title="Έξοδος"
[1, 3, 5]
```

Πήραμε τις θέσεις 0, 2, 4.

**Παράδειγμα 5 — Αρνητικοί δείκτες**

```python
nums = [1, 2, 3, 4, 5, 6]
print(nums[-3:-1])    # από το 3ο από το τέλος έως πριν το τελευταίο
```

```screen title="Έξοδος"
[4, 5]
```

!!! info ""
    Πήραμε τις θέσεις -3 και -2. Και με αρνητικούς δείκτες, δεν επιστρέφεται η
    θέση `end` (-1, το τελευταίο στοιχείο), αλλά μέχρι μία θέση πριν από αυτήν
    (-2).

**Παράδειγμα 6 — Αντιστροφή λίστας με slicing**

```python
nums = [1, 2, 3, 4, 5, 6]
print(nums[::-1])    # (_ : _ : -1)
```

```screen title="Έξοδος"
[6, 5, 4, 3, 2, 1]
```

!!! info ""
    Με αρνητικό `step` κάνουμε τα ίδια βήματα με το αντίστοιχο θετικό (εδώ 1),
    απλά ξεκινώντας από το τέλος της λίστας: θέσεις -1, -2, -3, -4, -5, -6.

??? tip "Ψάξε μόνος σου"
    [docs.python.org — Common Sequence Operations](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations)
    (δες τις γραμμές `s[i:j]` και `s[i:j:k]`)

## Έλεγχος αν ένα στοιχείο υπάρχει στη λίστα

Μπορούμε να χρησιμοποιήσουμε το keyword `in` για να ελέγξουμε εάν κάποιο
συγκεκριμένο στοιχείο περιέχεται σε μια λίστα.

```python
fruit_basket = ["apple", "banana", "cherry"]
if "apple" in fruit_basket:
    print("Yes, 'apple' is in the fruits list")
```

```screen title="Έξοδος"
Yes, 'apple' is in the fruits list
```

!!! info ""
    Με το keyword `in` δημιουργούμε μια συνθήκη που μπορούμε να τοποθετήσουμε
    μέσα σε ένα `if`.

??? tip "Ψάξε μόνος σου"
    [docs.python.org — Membership test operations](https://docs.python.org/3/reference/expressions.html#membership-test-operations)

## Αλλαγή στοιχείων μιας λίστας

Στις λίστες μπορούμε να τροποποιήσουμε στοιχεία, χρησιμοποιώντας το index του
στοιχείου και τον τελεστή της ανάθεσης (`=`).

```python
fruit_basket = ["apple", "banana", "cherry"]
fruit_basket[1] = "strawberry"    # "banana" → "strawberry"

print(fruit_basket)
```

```screen title="Έξοδος"
['apple', 'strawberry', 'cherry']
```

Μπορούμε επίσης να αλλάξουμε περισσότερα από ένα στοιχεία ταυτόχρονα,
χρησιμοποιώντας slicing.

| Index    | 0         | 1          | 2          | 3          | 4        | 5         |
|----------|-----------|------------|------------|------------|----------|-----------|
| Στοιχείο | `"apple"` | `"banana"` | `"cherry"` | `"orange"` | `"kiwi"` | `"mango"` |

```python
fruit_basket = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
fruit_basket[1:3] = ["strawberry", "watermelon"]    # αλλαγή των στοιχείων 1 έως 3 (1, 2)

print(fruit_basket)
```

```screen title="Έξοδος"
['apple', 'strawberry', 'watermelon', 'orange', 'kiwi', 'mango']
```

!!! warning "Προσοχή"
    Τα νέα στοιχεία `"strawberry"` και `"watermelon"` τα δίνουμε σε μορφή
    λίστας: `["strawberry", "watermelon"]`.

### Όταν το διάστημα είναι μικρότερο από τα νέα στοιχεία

```python
fruit_basket = ["apple", "banana", "cherry"]
fruit_basket[1:2] = ["strawberry", "watermelon"]

print(fruit_basket)
```

```screen title="Έξοδος"
['apple', 'strawberry', 'watermelon', 'cherry']
```

Δίνουμε διάστημα ενός στοιχείου στη λίστα (θέση 1) και 2 νέα στοιχεία. Η Python
στη θέση που ορίσαμε (θέση 1) θα κάνει την αλλαγή `"banana"` → `"strawberry"`
και ύστερα θα προσθέσει το στοιχείο που περισσεύει, `"watermelon"` (νέο!). Τα
στοιχεία που ήταν εκτός του διαστήματος αλλαγής θα μετακινηθούν αντίστοιχα,
αλλά δεν θα αλλάξουν: το `"cherry"` από τη θέση 2 πάει στη θέση 3.

### Όταν το διάστημα είναι μεγαλύτερο από τα νέα στοιχεία

```python
fruit_basket = ["apple", "banana", "cherry"]
fruit_basket[1:3] = ["watermelon"]

print(fruit_basket)
```

```screen title="Έξοδος"
['apple', 'watermelon']
```

Δίνουμε διάστημα δύο στοιχείων στη λίστα (θέσεις 1 και 2) και 1 νέο στοιχείο.
Η Python θα διαγράψει τα στοιχεία για τα οποία δεν έχουμε ορίσει νέα τιμή.
Συγκεκριμένα, στη θέση 1 θα κάνει την αλλαγή `"banana"` → `"watermelon"`, αφού
υπάρχει νέα τιμή, και ύστερα θα διαγράψει το στοιχείο στη θέση 2, για το οποίο
δεν έχουμε νέα τιμή.

`['apple', 'banana', 'cherry']` ➡ `['apple', 'watermelon']`

??? tip "Ψάξε μόνος σου"
    [docs.python.org — Mutable Sequence Types](https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types)
    (δες τις γραμμές `s[i] = x` και `s[i:j] = t`)

## Εισαγωγή νέων στοιχείων σε λίστα

### `append()`

Χρησιμοποιείται για να προσθέσουμε ένα νέο στοιχείο **στο τέλος** της λίστας.

```python
fruit_basket.append(new_item)
```

Μέσα στην παρένθεση βάζουμε το νέο στοιχείο που θέλουμε να προστεθεί.

```python
fruit_basket = ["apple", "banana", "cherry"]
fruit_basket.append("orange")

print(fruit_basket)
```

```screen title="Έξοδος"
['apple', 'banana', 'cherry', 'orange']
```

!!! warning "Προσοχή"
    Δεν μπορούμε να χρησιμοποιήσουμε την `append()` για να προσθέσουμε
    παραπάνω από ένα στοιχείο στη λίστα. Το
    `fruit_basket.append("orange", "lemon")` δίνει `TypeError`.

### `insert()`

Χρησιμοποιείται για να προσθέσουμε ένα νέο στοιχείο **σε συγκεκριμένη θέση**
(index).

```python
fruit_basket.insert(index, new_item)
```

Μέσα στην παρένθεση δίνουμε δύο ορίσματα: πρώτο το index στο οποίο θα προστεθεί
το νέο στοιχείο και δεύτερο το νέο στοιχείο.

```python
fruit_basket = ["apple", "banana", "cherry"]
fruit_basket.insert(1, "orange")

print(fruit_basket)
```

```screen title="Έξοδος"
['apple', 'orange', 'banana', 'cherry']
```

Το `"orange"` μπήκε στη θέση 1 και τα επόμενα στοιχεία μετακινήθηκαν μία θέση
δεξιά.

!!! warning "Προσοχή"
    Ούτε η `insert()` προσθέτει παραπάνω από ένα στοιχείο. Το
    `fruit_basket.insert(1, "orange", "lemon")` δίνει `TypeError`.

### `extend()`

Η `extend()` χρησιμοποιείται όταν θέλουμε να προσθέσουμε **πολλά** στοιχεία σε
μια λίστα με μία μόνο κίνηση. Πρακτικά, κάνει `append` κάθε στοιχείο από μια
άλλη λίστα.

```python
fruit_basket.extend(new_list)
```

Μέσα στην παρένθεση βάζουμε τη νέα λίστα που θέλουμε να προστεθεί.

```python
fruit_basket = ["apple", "banana", "cherry"]
newlist = ["mango", "pineapple", "papaya"]
fruit_basket.extend(newlist)

print(fruit_basket)
```

```screen title="Έξοδος"
['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']
```

Το ίδιο ακριβώς μπορούμε να κάνουμε χρησιμοποιώντας τον τελεστή `+` για να
προσθέσουμε δύο λίστες.

```python
fruit_basket = ["apple", "banana", "cherry"]
newlist = ["mango", "pineapple", "papaya"]
updatedlist = fruit_basket + newlist

print(updatedlist)
```

```screen title="Έξοδος"
['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']
```

??? tip "Ψάξε μόνος σου"
    [docs.python.org — More on Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
    (`append`, `extend`, `insert` και όλες οι υπόλοιπες μέθοδοι των λιστών)

## Διαγραφή στοιχείων από λίστα

### `remove()`

Η μέθοδος `remove()` αφαιρεί το πρώτο στοιχείο της λίστας που έχει την τιμή
που της δίνουμε.

```python
fruit_basket.remove(item)
```

Μέσα στην παρένθεση βάζουμε το στοιχείο που θέλουμε να διαγραφεί.

```python
fruit_basket = ["apple", "banana", "cherry"]
fruit_basket.remove("banana")

print(fruit_basket)
```

```screen title="Έξοδος"
['apple', 'cherry']
```

!!! info ""
    Αν υπάρχουν πολλές εμφανίσεις του ίδιου στοιχείου, η `remove()` αφαιρεί
    μόνο την πρώτη.

```python
fruit_basket = ["apple", "banana", "cherry", "banana", "kiwi"]
fruit_basket.remove("banana")

print(fruit_basket)
```

```screen title="Έξοδος"
['apple', 'cherry', 'banana', 'kiwi']
```

Το 2ο `"banana"` παρέμεινε στην τελική λίστα.

### `pop()`

Η μέθοδος `pop()` αφαιρεί το στοιχείο στη θέση (index) που της δίνουμε.

```python
fruit_basket.pop(index)
```

Μέσα στην παρένθεση βάζουμε το index του στοιχείου που θέλουμε να διαγραφεί.

```python
fruit_basket = ["apple", "banana", "cherry"]
fruit_basket.pop(1)    # διαγραφή του fruit_basket[1]

print(fruit_basket)
```

```screen title="Έξοδος"
['apple', 'cherry']
```

!!! info ""
    Αν δεν δώσουμε index, η `pop()` αφαιρεί το **τελευταίο** στοιχείο της
    λίστας.

```python
fruit_basket = ["apple", "banana", "cherry"]
fruit_basket.pop()

print(fruit_basket)
```

```screen title="Έξοδος"
['apple', 'banana']
```

### `del`

Το keyword `del` μπορεί να χρησιμοποιηθεί για να διαγράψει ένα στοιχείο σε
συγκεκριμένη θέση ή ακόμη και ολόκληρη τη λίστα.

```python
del fruit_basket[index]    # διαγραφή ενός στοιχείου της λίστας
del fruit_basket           # διαγραφή όλης της λίστας
```

```python
fruit_basket = ["apple", "banana", "cherry"]
del fruit_basket[0]    # διαγραφή του fruit_basket[0]

print(fruit_basket)
```

```screen title="Έξοδος"
['banana', 'cherry']
```

### `clear()`

Η μέθοδος `clear()` αδειάζει τη λίστα, αφήνοντάς την κενή, αλλά **χωρίς** να
τη διαγράψει. Δηλαδή, σε αντίθεση με την εντολή `del`, μετά το `clear()`
μπορούμε να προσθέσουμε νέα στοιχεία στη λίστα (π.χ. με `append()`).

```python
fruit_basket.clear()
```

```python
fruit_basket = ["apple", "banana", "cherry"]
fruit_basket.clear()

print(fruit_basket)
```

```screen title="Έξοδος"
[]
```

Η λίστα εξακολουθεί να υπάρχει, αλλά δεν έχει πια περιεχόμενο.

??? tip "Ψάξε μόνος σου"
    - [docs.python.org — More on Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
      (`remove`, `pop`, `clear`)
    - [docs.python.org — The `del` statement](https://docs.python.org/3/tutorial/datastructures.html#the-del-statement)

## Αντιγραφή λίστας

Δεν μπορούμε να αντιγράψουμε το περιεχόμενο της λίστας `fruit_basket` στην
`fruit_basket2` γράφοντας:

```python
fruit_basket2 = fruit_basket
```

Με αυτή τη γραμμή **δεν** δημιουργούμε νέα λίστα. Αντίθετα, δημιουργούμε ένα
δεύτερο όνομα (reference) που δείχνει στην ίδια λίστα στη μνήμη. Αυτό σημαίνει
ότι:

- οι δύο μεταβλητές δείχνουν στο ίδιο αντικείμενο,
- οποιαδήποτε αλλαγή κάνουμε στη μία λίστα θα εμφανιστεί και στην άλλη,
- οι λίστες δεν είναι πλέον ανεξάρτητες μεταξύ τους.

Αυτό συνήθως δεν είναι επιθυμητό, γιατί θέλουμε η κάθε λίστα να μπορεί να
αλλάζει χωρίς να επηρεάζει την άλλη. Για να αντιγράψουμε το περιεχόμενο μιας
λίστας χρησιμοποιούμε τη μέθοδο `copy()`.

```python
newlist = oldlist.copy()
```

```python
fruit_basket = ["apple", "banana", "cherry"]
fruit_basket2 = fruit_basket.copy()
print(fruit_basket2)
```

```screen title="Έξοδος"
['apple', 'banana', 'cherry']
```

??? tip "Ψάξε μόνος σου"
    [docs.python.org — More on Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
    (`list.copy()`)

## Επανάληψη (loop) μέσα από μια λίστα

Η επανάληψη είναι πολύ χρήσιμη όταν θέλουμε να επεξεργαστούμε ή να εμφανίσουμε
κάθε στοιχείο της λίστας.

### Loop με `for` — εμφάνιση στοιχείων ένα προς ένα

Μπορούμε να χρησιμοποιήσουμε `for` loop για να προσπελάσουμε τα στοιχεία μιας
λίστας.

```python
fruit_basket = ["apple", "banana", "cherry"]
for x in fruit_basket:
    print(x)
```

```screen title="Έξοδος"
apple
banana
cherry
```

Αυτό, όπως βλέπουμε, εμφανίζει κάθε στοιχείο της λίστας σε ξεχωριστή γραμμή.
Μπορούμε την παραπάνω εντολή να τη γράψουμε σε μια γραμμή ως εξής:

```python
fruit_basket = ["apple", "banana", "cherry"]
[print(x) for x in fruit_basket]
```

```screen title="Έξοδος"
apple
banana
cherry
```

### Loop με δείκτες (index numbers)

Μπορούμε να κάνουμε το ίδιο πράγμα χρησιμοποιώντας τα indexes της λίστας για να
προσπελάσουμε τα στοιχεία της. Θα χρησιμοποιήσουμε τις συναρτήσεις `range()`
και `len()`.

```python
fruit_basket = ["apple", "banana", "cherry"]
for i in range(len(fruit_basket)):
    print(fruit_basket[i])
```

```screen title="Έξοδος"
apple
banana
cherry
```

Στην ουσία εδώ κάνουμε προσπέλαση με indexes, π.χ. `print(fruit_basket[0])`.
Για να βρούμε πόσες επαναλήψεις θα εκτελέσουμε, βάζουμε μέσα στο `range()` τη
συνάρτηση `len()`. Άρα το `range(len(fruit_basket))` θα δώσει τιμές από το `0`
έως και το `len(fruit_basket) - 1`, που είναι όλα τα indexes της λίστας. Έτσι
την προσπελαύνουμε ολόκληρη.

### Loop με `while`

Αντίστοιχα, για την προσπέλαση μιας λίστας μέσω indexes μπορούμε να
χρησιμοποιήσουμε `while` loop.

```python
fruit_basket = ["apple", "banana", "cherry"]
i = 0
while i < len(fruit_basket):
    print(fruit_basket[i])
    i = i + 1   # αύξηση του index, αλλιώς θα έχουμε infinite loop
```

```screen title="Έξοδος"
apple
banana
cherry
```

Το `while` σε αυτή την περίπτωση κάνει το ίδιο πράγμα με το `for`, αλλά μας
δίνει περισσότερο έλεγχο.

??? tip "Ψάξε μόνος σου"
    - [docs.python.org — `for` statements](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
    - [docs.python.org — The `range()` function](https://docs.python.org/3/tutorial/controlflow.html#the-range-function)

## Ταξινόμηση λίστας

Η Python μας επιτρέπει να ταξινομούμε (να βάζουμε σε σειρά) τα στοιχεία μιας
λίστας πολύ εύκολα, χρησιμοποιώντας τη μέθοδο `sort()`. Η ταξινόμηση γίνεται
αλφαβητικά για λέξεις (strings) και αριθμητικά για αριθμούς.

!!! info "Υπενθύμιση"
    **Αύξουσα σειρά ταξινόμησης:** Τα στοιχεία διατάσσονται από το μικρότερο
    στο μεγαλύτερο, δηλαδή κάθε επόμενο στοιχείο είναι μεγαλύτερο ή ίσο από το
    προηγούμενό του.

    item1 < item2 < item3 < item4 < item5 < item6, π.χ. 2 3 6 9 17 22 33

    **Φθίνουσα σειρά ταξινόμησης:** Τα στοιχεία διατάσσονται από το μεγαλύτερο
    στο μικρότερο, δηλαδή κάθε επόμενο στοιχείο είναι μικρότερο ή ίσο από το
    προηγούμενό του.

    item1 > item2 > item3 > item4 > item5 > item6, π.χ. 33 22 17 9 6 3 2

### `sort()` — αύξουσα σειρά (προεπιλογή)

Η μέθοδος `sort()` ταξινομεί τη λίστα από το μικρότερο προς το μεγαλύτερο (ή
αλφαβητικά, από το Α → Ω).

**Παράδειγμα — αλφαβητική ταξινόμηση**

```python
fruit_basket = ["orange", "mango", "kiwi", "pineapple", "banana"]
fruit_basket.sort()
print(fruit_basket)
```

```screen title="Έξοδος"
['banana', 'kiwi', 'mango', 'orange', 'pineapple']
```

**Παράδειγμα — αριθμητική ταξινόμηση**

```python
mylist = [100, 50, 65, 82, 23]
mylist.sort()
print(mylist)
```

```screen title="Έξοδος"
[23, 50, 65, 82, 100]
```

### `sort(reverse = True)` — φθίνουσα σειρά

Για να ταξινομήσουμε τη λίστα αντίστροφα (μεγαλύτερο → μικρότερο),
χρησιμοποιούμε το όρισμα `reverse = True`.

**Παράδειγμα — αλφαβητικά**

```python
fruit_basket = ["orange", "mango", "kiwi", "pineapple", "banana"]
fruit_basket.sort(reverse = True)
print(fruit_basket)
```

```screen title="Έξοδος"
['pineapple', 'orange', 'mango', 'kiwi', 'banana']
```

**Παράδειγμα — αριθμητικά**

```python
mylist = [100, 50, 65, 82, 23]
mylist.sort(reverse = True)
print(mylist)
```

```screen title="Έξοδος"
[100, 82, 65, 50, 23]
```

??? tip "Ψάξε μόνος σου"
    - [docs.python.org — `list.sort()`](https://docs.python.org/3/library/stdtypes.html#list.sort)
    - [docs.python.org — Sorting Techniques](https://docs.python.org/3/howto/sorting.html)

## Μπορούμε να χειριζόμαστε strings ως λίστες!

Πολλά από όσα κάνουμε με τις λίστες δουλεύουν και στα strings. Έστω
`word = "PYTHON"`:

| Κώδικας | Αποτέλεσμα |
|---------|------------|
| `print(word[0])` | `P` |
| `print(word[-1])` | `N` |
| `word_length = len(word)` | `word_length = 6` |
| `print(word[0:2])` | `PY` |

```python
word = "PYTHON"
for letter in word:
    print(letter)
```

```screen title="Έξοδος"
P
Y
T
H
O
N
```

```python
word = "PYTHON"
for i in range(len(word)):
    print(word[i])
```

```screen title="Έξοδος"
P
Y
T
H
O
N
```

!!! warning "Προσοχή"
    Το `word[0] = "C"` **δεν επιτρέπεται**: δεν μπορούμε να αλλάξουμε γράμμα σε
    ένα string (δίνει `TypeError`). Πρέπει να φτιάξουμε νέο string.

??? tip "Ψάξε μόνος σου"
    [docs.python.org — Text (tutorial)](https://docs.python.org/3/tutorial/introduction.html#text)

## Extras — πώς τοποθετώ input σε λίστα

Πολύ συχνά θέλουμε ο χρήστης να δώσει πολλά στοιχεία (αριθμούς ή λέξεις) μέσα
σε μία γραμμή, χωρισμένα με κενά. Η Python μας επιτρέπει να τα μετατρέψουμε
εύκολα σε λίστα χρησιμοποιώντας τη μέθοδο `split()`.

### 1. Διάβασμα λίστας από τον χρήστη (λέξεις ή strings)

```python
fruits = input("Δώσε φρούτα χωρισμένα με κενό: ").split()
print(fruits)
```

Αν ο χρήστης γράψει `apple banana cherry`:

```screen title="Έξοδος"
Δώσε φρούτα χωρισμένα με κενό: {{apple banana cherry}}
['apple', 'banana', 'cherry']
```

!!! info ""
    Η μέθοδος `split()` «σπάει» το κείμενο σε λίστα χρησιμοποιώντας τα κενά.

### 2. Διάβασμα λίστας αριθμών

Όταν θέλουμε αριθμούς, πρέπει πρώτα να τους «σπάσουμε» με `split()` και μετά να
τους μετατρέψουμε σε ακέραιους (`int`):

```python
numbers = input("Δώσε αριθμούς χωρισμένους με κενό: ").split()
numbers = [int(x) for x in numbers]
```

Τι κάνει η γραμμή `[int(x) for x in numbers]`;

- περνάει κάθε στοιχείο `x` της λίστας,
- το μετατρέπει σε αριθμό `int`,
- και φτιάχνει νέα λίστα με τους αριθμούς.

### Γενικός κανόνας

Για λέξεις:

```python
mylist = input("Δώσε στοιχεία: ").split()
```

Για αριθμούς:

```python
mylist = input("Δώσε αριθμούς: ").split()
mylist = [int(x) for x in mylist]
```

??? tip "Ψάξε μόνος σου"
    - [docs.python.org — `str.split()`](https://docs.python.org/3/library/stdtypes.html#str.split)
    - [docs.python.org — List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
