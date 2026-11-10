# JavaScript Basics — για όσους ήδη ξέρουν Python

[:material-file-pdf-box: Εκτυπώσιμο PDF](javascript-vs-python.pdf){ .md-button }

## Πού τρέχει η JavaScript

Η Python συνήθως τρέχει σε ένα παράθυρο τερματικού. Η JS τρέχει σε ένα web
browser και αλλάζει την HTML (δηλαδή τον κώδικα της ιστοσελίδας) σε πραγματικό
χρόνο.

!!! info ""
    Γι' αυτό η JavaScript είναι η γλώσσα των ιστοσελίδων: ό,τι κουνιέται,
    αλλάζει ή απαντάει όταν πατάς κάτι σε μια σελίδα, συνήθως είναι JS.

## Τερματισμός εντολών

Στην Python, μια εντολή ολοκληρώνεται όταν πατάμε “Enter” και μεταβαίνουμε στην
κάτω γραμμή.

Στη JS, οι εντολές χωρίζονται μεταξύ τους με `;`

<div class="grid" markdown>

```python title="Python"
age = 12
color = "red"
```

```js title="JavaScript"
let age = 12;
let color = "red";
```

</div>

Επειδή οι εντολές χωρίζονται με `;` και όχι με αλλαγή γραμμής, στη JS μπορούμε
να γράψουμε και δύο εντολές στην ίδια γραμμή — αλλά είναι πιο ευανάγνωστο να
μένει μία εντολή ανά γραμμή.

## Οργάνωση εντολών

Για να ομαδοποιήσουμε εντολές στην Python (π.χ. τις εντολές που θέλουμε να
επαναλαμβάνονται εντός ενός for loop) χρησιμοποιούμε indentation (enter + tab).

Στη JS, γράφουμε τον κώδικα εντός `{ }`

<div class="grid" markdown>

```python title="Python"
if score > 10:
    score = 0
    print("You won!")
```

```js title="JavaScript"
if (score > 10) {
    score = 0;
    console.log("You won!");
}
```

</div>

!!! info ""
    Στη JS η συνθήκη μπαίνει πάντα μέσα σε παρενθέσεις `( )`, και δεν υπάρχει η
    άνω-κάτω τελεία `:` της Python. Η εσοχή δεν είναι υποχρεωτική — τη βάζουμε
    όμως για να διαβάζεται ο κώδικας.

??? tip "Ψάξε μόνος σου"
    - [MDN — if...else](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else)
    - [MDN — block statement `{ }`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/block)

## Ορισμός μεταβλητών

Όταν ορίζουμε μια μεταβλητή στη JavaScript, πρέπει να δηλώνουμε αν σκοπεύουμε να
μεταβάλουμε την τιμή της στη συνέχεια του προγράμματος.

| Λέξη | Σημασία |
|------|---------|
| `const` | Η τιμή της μεταβλητής δεν πρέπει να αλλάξει. |
| `let` | Επιτρέπονται νέες αναθέσεις. |

```js title="JavaScript"
const age = 12;
age = 13;        // ERROR
```

!!! warning "Προσοχή"
    Αυτό που απαγορεύεται είναι η νέα ανάθεση. Αν έχουμε μια λίστα, επιτρέπεται
    να αλλάξουμε το περιεχόμενό της, με μεθόδους επεξεργασίας λιστών.

```js title="JavaScript"
const enemies = ["goblin", "orc"];
enemies.push("troll");    // επιτρέπεται: αλλάζουμε το περιεχόμενο
enemies = ["dragon"];     // ERROR: νέα ανάθεση
```

!!! info ""
    Στην Python δεν δηλώνουμε τίποτα: γράφουμε απλώς `age = 12`. Στη JS πρέπει
    πάντα να διαλέξουμε `const` ή `let`. Κανόνας: ξεκίνα με `const` και βάλε
    `let` μόνο αν όντως χρειάζεται να αλλάξει η τιμή.

??? tip "Ψάξε μόνος σου"
    - [MDN — const](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const)
    - [MDN — let](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)

## Έξοδος

Για να εμφανίσουμε ένα μήνυμα στο τερματικό χρησιμοποιούμε την εντολή
`console.log()` αντί για `print()`

<div class="grid" markdown>

```python title="Python"
print("hello world")
```

```js title="JavaScript"
console.log("hello world");
```

</div>

Το τερματικό αλλάζει ανάλογα με την εφαρμογή. Αν τρέχουμε μια εφαρμογή στο
browser, για να δούμε την έξοδο κάνουμε inspect και πηγαίνουμε στο tab console.

| Λειτουργικό | Συντόμευση για inspect |
|-------------|------------------------|
| Windows / Linux | ++ctrl+shift+i++ |
| Mac | ++cmd+option+i++ |

??? tip "Ψάξε μόνος σου"
    [MDN — console.log()](https://developer.mozilla.org/en-US/docs/Web/API/console/log_static)

## String interpolation για “custom” prints

Περικλείουμε το string σε backticks `` `...` `` και εισάγουμε τις μεταβλητές σε
`${..}`

<div class="grid" markdown>

```python title="Python"
error = "index error"
message = f"program exited with {error}"
```

```js title="JavaScript"
const error = "index error";
const message = `program exited with ${error}`;
```

</div>

Και στις δύο γλώσσες το αποτέλεσμα είναι το ίδιο:

```screen title="Αποτέλεσμα"
program exited with index error
```

!!! info ""
    Τα backticks `` ` `` είναι διαφορετικό σύμβολο από τα απλά εισαγωγικά. Σε
    ελληνικό πληκτρολόγιο βρίσκονται συνήθως στο πλήκτρο αριστερά από το `1`.

??? tip "Ψάξε μόνος σου"
    [MDN — Template literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals)

## Έλεγχος ισότητας

Γενικά, γίνεται με `===` αντί για `==` όπως στην Python. Αντίστοιχα, το
«διάφορο» γράφεται `!==` αντί για `!=`

| Σημασία | Python | JavaScript |
|---------|--------|------------|
| ίσο με | `==` | `===` |
| διάφορο από | `!=` | `!==` |

Το `==` της JS κάνει αυτόματες μετατροπές τύπου (type casting) πριν συγκρίνει,
που συχνά δεν είναι αυτές που περιμένουμε.

```js title="JavaScript"
console.log("5" == 5);     // true  - μετατρέπει το "5" σε αριθμό
console.log("5" === 5);    // false - string και αριθμός δεν είναι το ίδιο
```

!!! warning "Κανόνας"
    Στη JavaScript χρησιμοποιούμε πάντα `===` και `!==`

!!! quote "Fun fact"
    Την πρώτη φορά που είδα `===` στην JS γραμμένο από συνεργάτη μου, νόμιζα ότι
    ήταν bug και το άλλαξα σε `==` καταστρέφοντας το πρόγραμμα…

??? tip "Ψάξε μόνος σου"
    [MDN — Strict equality (===)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Strict_equality)

## Συναρτήσεις

<div class="grid" markdown>

```python title="Python"
def add(a, b):
    return a + b
```

```js title="JavaScript"
function add(a, b) {
    return a + b;
}
```

</div>

Η κλήση είναι ίδια και στις δύο γλώσσες:

<div class="grid" markdown>

```python title="Python"
result = add(3, 2)
```

```js title="JavaScript"
const result = add(3, 2);
```

</div>

??? tip "Ψάξε μόνος σου"
    [MDN — function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function)

## Arrow Functions (ΠΡΟΧΩΡΗΜΕΝΟ!)

Οι arrow functions είναι ένας πιο σύντομος τρόπος να γράψουμε μια συνάρτηση.
Συνήθως τις αποθηκεύουμε σε μια `const` μεταβλητή, αλλά μπορούν να γραφτούν και
κατευθείαν μέσα σε μια άλλη εντολή — θα το δούμε στους πίνακες παρακάτω. Οι AI
coding agents τις χρησιμοποιούν συνέχεια…

```js title="JavaScript"
const multiply = (a, b) => {
    return a * b;
};
```

ή αν έχουμε μόνο μια γραμμή κώδικα και δε χρειάζεται ομαδοποίηση:

```js title="JavaScript"
const multiply = (a, b) => a * b;
```

!!! quote ""
    Σκεφτείτε την σαν τον ορισμό μιας συνάρτησης στα μαθηματικά.

Καλείται κανονικά ως συνάρτηση:

```js title="JavaScript"
const result = multiply(3, 2);
```

??? tip "Ψάξε μόνος σου"
    [MDN — Arrow function expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)

## Δομή object (αντίστοιχη του python Dictionary)

<div class="grid" markdown>

```python title="Python"
person = {"name": "Alex", "age": 50}

print(person["age"])
```

```js title="JavaScript"
const person = { name: "Alex", age: 50 };

console.log(person.age);
```

</div>

```screen title="Αποτέλεσμα"
50
```

!!! info ""
    Δύο διαφορές: στη JS τα ονόματα των κλειδιών γράφονται **χωρίς
    εισαγωγικά**, και τα διαβάζουμε με **τελεία** (`person.age`) αντί για
    αγκύλες.

??? tip "Ψάξε μόνος σου"
    [MDN — Working with objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects)

## Επανάληψη σε πίνακες (for loops)

Το ακριβές αντίστοιχο του `for x in lista:` της Python είναι το `for ... of` της
JS.

<div class="grid" markdown>

```python title="Python"
enemies = ["goblin", "orc", "troll"]

for enemy in enemies:
    print(enemy)
```

```js title="JavaScript"
const enemies = ["goblin", "orc", "troll"];

for (const enemy of enemies) {
    console.log(enemy);
}
```

</div>

```screen title="Αποτέλεσμα"
goblin
orc
troll
```

### Μέθοδοι πίνακα: forEach

Στη JS συναντάμε πολύ συχνά και έναν δεύτερο τρόπο: τη μέθοδο `forEach()`, στην
οποία δίνουμε μια arrow function. Δεν είναι for loop — είναι μέθοδος του πίνακα
— αλλά κάνει την ίδια δουλειά.

```js title="JavaScript"
const enemies = ["goblin", "orc", "troll"];

enemies.forEach(enemy => {
    console.log(enemy);
});
```

```screen title="Αποτέλεσμα"
goblin
orc
troll
```

!!! info ""
    Εδώ βλέπουμε μια arrow function που **δεν** αποθηκεύεται σε μεταβλητή:
    γράφεται κατευθείαν μέσα στην `forEach`. Η μεταβλητή `enemy` παίρνει κάθε
    φορά το επόμενο στοιχείο του πίνακα, ακριβώς όπως στο `for ... of`.

??? tip "Ψάξε μόνος σου"
    - [MDN — for...of](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of)
    - [MDN — Array.prototype.forEach()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach)
