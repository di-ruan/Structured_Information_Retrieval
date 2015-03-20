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


c) Usage

    To run our program, We provide three options:
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
