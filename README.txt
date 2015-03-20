COMS E6111 Advanced Database Systems - Project 2

a) Group members

    Di Ruan (dr2763)
    Jie-Gang Kuang (jk3735)


b) File list

    run.sh
    main.py
    Analyser.py
    Answer.py
    Display.py
    Search.py
    README.txt
    transcript_Bill_Gates.txt
    transcript_Robert_Downey_Jr.txt
    transcript_Jackson.txt
    transcript_NFL.txt
    transcript_NBA.txt
    transcript_NY_Knicks.txt
    transcript_Miami_Heat.txt
    transcript_who_created_Google.txt
    transcript_who_created_Lord_Of_the_Rings.txt
    transcript_who_created_Microsoft.txt
    transcript_who_created_Romeo_and_Juliet.txt


c) Usage

    To run our program, We provide the same three options as the reference program:
    1.  ./run.sh -key <Freebase API key> -q <query> -t <infobox|question>
    2.  ./run.sh -key <Freebase API key> -f <files of queries> -t <infobox|question>
    3.  ./run.sh -key <Freebase API key>


d) Design

    This project consists of two parts:

        run.sh is the script to invoke the program.
        main.py is the entry of the program.
        Search.py contains the part for interacting with freebase API.
        Analyser.py analyses the result for part1.
        Answer.py analyses the result for part2.
        Display.py is the part for displaying the data in table format.



e) Freebase API Key: AIzaSyBgfj3L8cqcu6OEd21JkQcHhBQJA6jUOXo
   requests per second per user: 10


f) Additional Information
