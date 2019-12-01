# Simple script to perform youtube searches based on video content (captions)

## Instructions

1. You have to create a directory with the name TOKEN_{your Google API token}. Like this: `mkdir ./TOKEN_IJHEO2J3KjkOEWIJKEKklj323`

2. Usage: `python sic.py [--viewcount] <"search scope"> <maxresults> <"multiple strings" "like" "this">`
    >using `--viewcount` it sorts video results by view count.

3. Example:

```
$ python sic.py "trump press conference" 10 "immigration"
Found 10 videos.
No occurrences found on video WATCH: President Trump SURPRISE Oval Office News Conference by FOX 10 Phoenix (1/10)
No occurrences found on video President Trump holds press conference after UN meetings in New York | ABC News by ABC News (2/10)
Found occurrence for "immigration" at President Trump holds press conference today at Mar-a-Lago, live stream (jZqt5rDI8XI) -> https://youtu.be/jZqt5rDI8XI?t=367
Found occurrence for "immigration" at President Trump holds press conference today at Mar-a-Lago, live stream (jZqt5rDI8XI) -> https://youtu.be/jZqt5rDI8XI?t=427
Found occurrence for "immigration" at President Trump holds press conference today at Mar-a-Lago, live stream (jZqt5rDI8XI) -> https://youtu.be/jZqt5rDI8XI?t=585
Found occurrence for "immigration" at President Trump holds press conference today at Mar-a-Lago, live stream (jZqt5rDI8XI) -> https://youtu.be/jZqt5rDI8XI?t=1137
Found 4 occurrences at President Trump holds press conference today at Mar-a-Lago, live stream (jZqt5rDI8XI) -> https://youtu.be/jZqt5rDI8XI
No occurrences found on video President Trump Participates in a Joint Press Conference with the Prime Minister of Japan by The White House (4/10)
No occurrences found on video President Trump Holds a Joint Press Conference with the President of the Republic of Korea by The White House (5/10)
No occurrences found on video Watch Live: Trump Delivers Remarks After El Paso And Dayton Weekend Shootings | NBC News by NBC News (6/10)
No occurrences found on video Watch Donald Trump's full press conference in New York by CBS News (7/10)
Found occurrence for "immigration" at Full 'Squad' Press Conference In Response To President Donald Trump’s Attacks | MTP Daily | MSNBC (NF2A4KndU-g) -> https://youtu.be/NF2A4KndU-g?t=452
Found 1 occurrences at Full 'Squad' Press Conference In Response To President Donald Trump’s Attacks | MTP Daily | MSNBC (NF2A4KndU-g) -> https://youtu.be/NF2A4KndU-g
No occurrences found on video President Trump Participates in a Press Conference by The White House (9/10)
Found occurrence for "immigration" at Watch Now: President Donald Trump's full press conference after Midterm Elections results (-67ZrVAX58A) -> https://youtu.be/-67ZrVAX58A?t=2089
Found occurrence for "immigration" at Watch Now: President Donald Trump's full press conference after Midterm Elections results (-67ZrVAX58A) -> https://youtu.be/-67ZrVAX58A?t=4676
Found occurrence for "immigration" at Watch Now: President Donald Trump's full press conference after Midterm Elections results (-67ZrVAX58A) -> https://youtu.be/-67ZrVAX58A?t=4681
Found occurrence for "immigration" at Watch Now: President Donald Trump's full press conference after Midterm Elections results (-67ZrVAX58A) -> https://youtu.be/-67ZrVAX58A?t=4730
Found occurrence for "immigration" at Watch Now: President Donald Trump's full press conference after Midterm Elections results (-67ZrVAX58A) -> https://youtu.be/-67ZrVAX58A?t=5148
Found 5 occurrences at Watch Now: President Donald Trump's full press conference after Midterm Elections results (-67ZrVAX58A) -> https://youtu.be/-67ZrVAX58A

```