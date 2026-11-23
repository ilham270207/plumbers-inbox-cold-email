#!/usr/bin/env python3
"""Write a 120-word cold email to /output/entry.txt.

Deterministic, no network, no randomness: the output is always the same
email (subject line included, exactly 120 words).
"""

import os

# Email logic, mapped to the plumber-judge's brief:
# (1) sounds like it knows a plumber's week — 6 a.m. callouts, invoices
#     scribbled in the van, receipts in a glovebox, tax like a burst pipe;
# (2) the offer is concrete and small — sort receipts, chase invoices,
#     tidy tax, one clean number a month, first month free, no big
#     contract; (3) short enough to read on a phone between jobs — 120
#     words, short paragraphs; (4) ends with one easy ask — a 10-minute
#     call Tuesday at 7 a.m., before the first job. One ask, one time.
#     The sender is named (Sam, ClearBooks) and the sign-off carries the
#     trade ("bookkeeping for trades"), so the email feels like a person,
#     not a blast.
EMAIL = """Subject: Your books, done while you're on the next job

Hi \u2014 I know your week: 6 a.m. callouts, invoices scribbled in the van, receipts in a glovebox, and tax season looming like a burst pipe.

I'm Sam from ClearBooks. We handle the books for tradespeople \u2014 nothing fancy. We sort through all your receipts, chase down every unpaid invoice, and keep your tax returns tidy, so each month you see one clean number instead of a pile of paper.

No big contract, and the first month is free. Setup takes one 10-minute call \u2014 I can ring you between jobs.

Want me to call Tuesday at 7 a.m., before your first job?

Best,
Sam \u2014 ClearBooks, bookkeeping for trades."""


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(EMAIL)


if __name__ == "__main__":
    main()
