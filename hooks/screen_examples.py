"""Χρωματισμός παραδειγμάτων εξόδου: ό,τι τυπώνει ο υπολογιστής vs ό,τι πληκτρολογεί ο χρήστης.

Γράφουμε κάθε μπλοκ εξόδου προγράμματος ως ```screen, και ό,τι πληκτρολογεί ο χρήστης
ανάμεσα σε {{ }}:

    ```screen title="Παράδειγμα εξόδου"
    λεπτά;{{75}}
    1 : 15
    ```

Το hook:
  1. ελέγχει το Markdown και βγάζει warning (άρα το `mkdocs build --strict` αποτυγχάνει) όταν
     - ένα μπλοκ εξόδου (title με «έξοδ»/«εξόδ»/«Αποτέλεσμα») δεν είναι ```screen,
     - ένα ```screen έχει ασύζευκτα {{ / }},
     - ένα ```screen δεν έχει κανένα {{ }}, ενώ θα έπρεπε. «Θα έπρεπε» σημαίνει:
       αν ακολουθεί αμέσως ένα ```python, ο κώδικας εκείνος καλεί input(·
       αλλιώς, ο τίτλος του ή το κείμενο της ενότητας (από την τελευταία
       επικεφαλίδα) μιλάει για χρήστη/είσοδο.
       Αν ένα τέτοιο μπλοκ πράγματι δεν έχει είσοδο, γράψε ```screen no-input.
  2. στο HTML μετατρέπει το {{...}} σε <span class="screen-in">...</span>.
"""

import logging
import re

log = logging.getLogger("mkdocs.hooks.screen_examples")

FENCE = re.compile(r"^(?P<indent>[ \t]*)```(?P<info>[^`\n]*)$")
TITLE = re.compile(r'title="([^"]*)"')
OUTPUT_TITLE = re.compile(r"έξοδ|εξόδ|Αποτέλεσμα", re.IGNORECASE)
NEEDS_INPUT = re.compile(r"Παράδειγμα εξόδου|χρήστ|είσοδ|input\(", re.IGNORECASE)
HEADING = re.compile(r"^#{1,6} ")

# Το Pygments δεν ξέρει γλώσσα «screen», οπότε θα έχανε την κλάση. Γι' αυτό το
# ```screen title="..." γίνεται ```{.text .screen title="..."} πριν το Markdown.
SCREEN_FENCE = re.compile(r"^([ \t]*)```screen(?:[ \t]+(.*))?$", re.MULTILINE)
SCREEN_BLOCK = re.compile(
    r'(<div class="language-text screen highlight">.*?</code>)', re.DOTALL
)
INPUT = re.compile(r"\{\{(.*?)\}\}")


def _blocks(markdown):
    """Δίνει (γραμμή, info, περιεχόμενο, κείμενο ενότητας, προηγούμενο μπλοκ) για
    κάθε fenced μπλοκ. Το προηγούμενο μπλοκ είναι (info, περιεχόμενο) αν απέχει
    μόνο κενές γραμμές, αλλιώς None."""
    prev, prev_end = None, -2
    lines = markdown.split("\n")
    section = []
    i = 0
    while i < len(lines):
        if HEADING.match(lines[i]):
            section = []
        section.append(lines[i])
        m = FENCE.match(lines[i])
        if m and m.group("info").strip():
            start, indent, info = i, m.group("indent"), m.group("info").strip()
            body = []
            i += 1
            while i < len(lines) and lines[i].strip() != "```":
                body.append(lines[i][len(indent):])
                i += 1
            adjacent = prev if all(not l.strip() for l in lines[prev_end + 1:start]) else None
            yield start + 1, info, "\n".join(body), "\n".join(section[:-1]), adjacent
            prev, prev_end = (info, "\n".join(body)), i
        i += 1


def on_page_markdown(markdown, page, **kwargs):
    src = page.file.src_uri
    for line, info, body, section, prev in _blocks(markdown):
        lang = info.split()[0] if not info.startswith("title=") else ""
        tm = TITLE.search(info)
        title = tm.group(1) if tm else ""

        if lang != "screen":
            if lang in ("", "text") and OUTPUT_TITLE.search(title):
                log.warning(
                    f'{src}:{line}: μπλοκ εξόδου "{title}" πρέπει να γραφτεί ως ```screen '
                    "(η είσοδος του χρήστη μέσα σε {{ }})"
                )
            continue

        if body.count("{{") != body.count("}}"):
            log.warning(f"{src}:{line}: ```screen με ασύζευκτα {{{{ / }}}}")
        if prev and prev[0].split()[0] == "python":
            needs_input = "input(" in prev[1]
        else:
            needs_input = bool(NEEDS_INPUT.search(title + "\n" + section))
        if "{{" not in body and "no-input" not in info.split() and needs_input:
            log.warning(
                f'{src}:{line}: "{title}" χωρίς είσοδο χρήστη, ενώ η ενότητα μιλάει '
                "για χρήστη/είσοδο — σημείωσε ό,τι πληκτρολογεί ο χρήστης με {{ }} "
                "(ή γράψε ```screen no-input αν πράγματι δεν υπάρχει)"
            )
    return SCREEN_FENCE.sub(
        lambda m: f"{m.group(1)}```{{.text .screen {_attrs(m.group(2))}}}", markdown
    )


def _attrs(info):
    return " ".join(w for w in (info or "").split(" ") if w != "no-input")


def on_page_content(html, **kwargs):
    return SCREEN_BLOCK.sub(
        lambda m: INPUT.sub(r'<span class="screen-in">\1</span>', m.group(1)), html
    )
