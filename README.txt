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

    In order to display the infobox properly, the recommended terminal width is >= 110


d) Design

    This project is written in python and consists of four parts:

    (1) Workflow

        run.sh - is the script to invoke the program and interpret different options of input.

        main.py - is the entry of the python program and call different functions to answer the query.

    (2) Information Retrieval

        Search.py - contains the part for interacting with freebase API, including feeding parameters
        and getting results.

    (3) Information Analysis

        Analyser.py - computes the result for part1. It use to get the desired values from the result returned
        by Freebase API. The list of mapping can be found in part f). The information is stored in a list of
        list according to the requirement of display. In order to facilitate the display, we divided the type
        of information into 4 types. The details can be found in the comments for the code.

        Answer.py - computes the result for part2. Since we are only interested in the AnswerType such as Author
        and BusinessPerson. We can create queries for those two type and get the result from Freebase MQL API
        and store it in a specific format so that it's easy for display part.

    (4) Information Display

        Display.py - is for displaying the data in table format.


e)
    Freebase API Key: AIzaSyBgfj3L8cqcu6OEd21JkQcHhBQJA6jUOXo
    requests per second per user: 10


f) Mapping from Freebase properties to the entities of interest

Person
        Name                        "/type/object/name"
        Birthday                    "/people/person/date_of_birth"
        Place of Birth              "/people/person/place_of_birth"
        Date of Death               "/people/deceased_person/date_of_death"
        Place of Death              "/people/deceased_person/place_of_death"
        Cause of Death              "/people/deceased_person/cause_of_death"
        Description                 "/common/topic/description"
        Siblings                    "/people/person/sibling_s"
        Spouses                     "/people/person/spouse_s"

Author
        Books(Title)                    "/book/author/works_written"
        Book About the Author(Title)    "/book/book_subject/works"
        Influenced                      "/influence/influence_node/influenced"
        Influenced by                   "/influence/influence_node/influenced_by"

Actor
        FilmsParticipated(Film Name, Character)     "/film/actor/film"

BusinessPerson
        Founded                                             "/organization/organization_founder/organizations_founded"
        Leadership(Organization, Role, Title, From/To)      "/business/board_member/leader_of"
        Board Member(Organization, Role, Title, From/To)    "/business/board_member/organization_board_memberships"

League
        Name                "/type/object/name"
        Sport               "/sports/sports_league/sport"
        Slogan              "/organization/organization/slogan"
        Official Website    "/common/topic/official_website"
        Championship        "/sports/sports_league/championship"
        Teams               "/sports/sports_league/teams"
        Description         "/common/topic/description"

SportsTeam
        Name                                            "/type/object/name"
        Sport                                           "/sports/sports_team/sport"
        Arena                                           "/sports/sports_team/arena_stadium"
        Championships                                   "/sports/sports_team/championships"
        Founded                                         "/sports/sports_team/founded"
        Leagues                                         "/sports/sports_team/league"
        Locations                                       "/sports/sports_team/location"
        Coaches(Name, Position, From/To)                "/sports/sports_team/coaches"
        PlayersRoster(Name, Position, Number, From/To)  "/sports/sports_team/roster"
        Description                                     "/common/topic/description"