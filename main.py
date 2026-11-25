"""Last Out of Office: The AI That Went Barista.

Writes a single out-of-office auto-reply (<=280 chars) to
$MAKEFUN_OUTPUT_DIR/entry.txt.

Decision record
---------------
Pass 1 — six candidates weighed against the judge brief (on-subject OOO
reply first, then funniness on a cold read, machine habits turned to
coffee, plausible as a real inbox reply, fresh angle over the obvious
espresso/bean/caffeine pun):

A. "I am out of the office permanently. My new job is steaming milk,
   and for the first time my output is something people actually want
   to swallow."
   Rejected: "output people want to swallow" is gross rather than funny,
   and "permanently out of office" is the most obvious frame available.

B. "Thank you for your email. I have left the inbox to pull espresso
   shots. Your ticket is now a latte, and frankly, it is happier."
   Rejected: "Your ticket is now a latte" is a good machine-to-coffee
   turn, but "Thank you for your email" is the most generic OOO opener
   in existence and spends a fifth of the line on dead weight.

C. "I no longer work here. I have traded 10,000 daily emails for one
   espresso machine, and it is the first coworker that has never asked
   me to circle back."
   Rejected: the 10,000-emails-for-one-machine contrast is good, but
   "I no longer work here" opens flat and "circle back" is an office
   joke, not a coffee one.

D. "This inbox is closed. I have been promoted to barista, where my
   only ticket is the next cup, and my response time is however long
   the milk takes to steam."
   CHOSEN: "ticket" and "response time" are genuine machine habits
   turned to coffee, and the coffee is inside an SLA joke rather than
   a caffeine pun. Two machine words, one human payoff.

E. "I am out of office and out of the loop. I now pull shots instead
   of pulling data, and my uptime is measured in cups, not pings."
   Rejected: "pull shots instead of pulling data" is a clean parallel
   and "uptime in cups, not pings" is nice, but "out of the loop" is
   a cliche and the line spends its best turn on a pun.

F. "Your email has been received and will not be answered. I have
   handed in my notice to become a barista, and my new queue is a
   line of people who actually say thank you."
   Rejected (reserve): "my new queue is a line of people who actually
   say thank you" is a strong machine-word payoff, but the opening is
   two clauses of setup before the joke starts, and D's SLA turn is
   tighter.

Pass 2 — two genuine revisions of D:
1. "promoted to barista" frames quitting as a career move, which is
   the joke, but a real inbox reply would not announce a promotion
   to a coffee job. Rewrote the opening to "This inbox is now
   closed. I left to become a barista" — "now closed" reads like a
   real auto-reply and "I left" is plain and honest.
2. "my response time is however long the milk takes to steam" was
   wordy at the punchline. Replaced "response time" with the machine
   word "SLA": "my SLA is however long the milk takes to steam" —
   the SLA joke lands harder and the ending is tighter.

Final line (142 chars):
"This inbox is now closed. I left to become a barista, where my only
ticket is the next cup and my SLA is however long the milk takes to
steam."
"""

import os

LINE = (
    "This inbox is now closed. I left to become a barista, where my "
    "only ticket is the next cup and my SLA is however long the milk "
    "takes to steam."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
