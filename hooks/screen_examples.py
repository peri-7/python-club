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
     - ένα «Παράδειγμα εξόδου» δεν έχει καμία είσοδο χρήστη σημειωμένη·
  2. στο HTML μετατρέπει το {{...}} σε <span class="screen-in">...</span>.
"""

import logging
import re

log = logging.getLogger("mkdocs.hooks.screen_examples")

FENCE = re.compile(r"^(?P<indent>[ \t]*)```(?P<info>[^`\n]*)$")
TITLE = re.compile(r'title="([^"]*)"')
OUTPUT_TITLE = re.compile(r"έξοδ|εξόδ|Αποτέλεσμα", re.IGNORECASE)
NEEDS_INPUT_TITLE = re.compile(r"Παράδειγμα εξόδου|χρήστης")

# Το Pygments δεν ξέρει γλώσσα «screen», οπότε θα έχανε την κλάση. Γι' αυτό το
# ```screen title="..." γίνεται ```{.text .screen title="..."} πριν το Markdown.
SCREEN_FENCE = re.compile(r"^([ \t]*)```screen(?:[ \t]+(.*))?$", re.MULTILINE)
SCREEN_BLOCK = re.compile(
    r'(<div class="language-text screen highlight">.*?</code>)', re.DOTALL
)
INPUT = re.compile(r"\{\{(.*?)\}\}")


def _blocks(markdown):
    """Δίνει (γραμμή, info, περιεχόμενο) για κάθε fenced μπλοκ."""
    lines = markdown.split("\n")
    i = 0
    while i < len(lines):
        m = FENCE.match(lines[i])
        if m and m.group("info").strip():
            start, indent, info = i, m.group("indent"), m.group("info").strip()
            body = []
            i += 1
            while i < len(lines) and lines[i].strip() != "```":
                body.append(lines[i][len(indent):])
                i += 1
            yield start + 1, info, "\n".join(body)
        i += 1


def on_page_markdown(markdown, page, **kwargs):
    src = page.file.src_uri
    for line, info, body in _blocks(markdown):
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
        if NEEDS_INPUT_TITLE.search(title) and "{{" not in body:
            log.warning(
                f'{src}:{line}: "{title}" χωρίς είσοδο χρήστη — σημείωσε ό,τι '
                "πληκτρολογεί ο χρήστης με {{ }}"
            )
    return SCREEN_FENCE.sub(
        lambda m: f"{m.group(1)}```{{.text .screen {m.group(2) or ''}}}", markdown
    )


def on_page_content(html, **kwargs):
    return SCREEN_BLOCK.sub(
        lambda m: INPUT.sub(r'<span class="screen-in">\1</span>', m.group(1)), html
    )
