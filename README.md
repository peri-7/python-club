# Python Club — ιστοσελίδα μαθημάτων

Στατική ιστοσελίδα με το υλικό του ομίλου, φτιαγμένη με
[MkDocs](https://www.mkdocs.org/) + [Material](https://squidfunk.github.io/mkdocs-material/).

## Προεπισκόπηση στον υπολογιστή σου

```bash
conda activate python-club
mkdocs serve
```

Άνοιξε το <http://127.0.0.1:8000>. Η σελίδα ανανεώνεται μόνη της σε κάθε αλλαγή.

> Δουλεύει **χωρίς internet** — χρήσιμο αν πέσει το δίκτυο του σχολείου.

## Δομή

```
docs/
├── index.md                     ανακατεύθυνση στους Αρχάριους (δεν είναι καρτέλα)
├── beginners/                   ΚΑΡΤΕΛΑ 1 — Αρχάριοι
│   ├── index.md
│   ├── theory/
│   │   ├── index.md             λίστα μαθημάτων θεωρίας
│   │   ├── lesson-01.md         η σελίδα του μαθήματος
│   │   └── lesson-01.pdf        το εκτυπώσιμο PDF του ίδιου μαθήματος
│   └── exercises/               ίδια δομή
└── advanced/                    ΚΑΡΤΕΛΑ 2 — Προχωρημένοι
    └── ...
```

Κάθε PDF κάθεται **δίπλα** στη σελίδα του, με το ίδιο όνομα. Έτσι ο σύνδεσμος
μέσα στη σελίδα είναι απλά `lesson-01.pdf`.

## Πώς προσθέτω νέο μάθημα

1. Φτιάξε το `docs/beginners/theory/lesson-02.md`.
2. Βάλε δίπλα του το `lesson-02.pdf`.
3. Πρόσθεσε μία γραμμή στο `nav:` του `mkdocs.yml`.
4. Πρόσθεσε τον σύνδεσμο στο `docs/beginners/theory/index.md`.

## Χρήσιμα μοτίβα

````markdown
[:material-file-pdf-box: Εκτυπώσιμο PDF](lesson-02.pdf){ .md-button }

==υπογράμμιση με μαρκαδόρο==

!!! warning "Προσοχή"
    Κείμενο προειδοποίησης.

??? success "Λύση"
    ```python
    print("κρυφή μέχρι να την πατήσει ο μαθητής")
    ```
````

## Ανέβασμα στο internet (GitHub Pages)

```bash
git init && git add . && git commit -m "αρχική έκδοση"
# φτιάξε ένα repo στο GitHub και σύνδεσέ το, μετά:
mkdocs gh-deploy
```

Μετά το πρώτο ανέβασμα, συμπλήρωσε το `site_url:` στο `mkdocs.yml`.
# python-club
