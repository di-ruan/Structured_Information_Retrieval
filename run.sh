#!/bin/bash
# The BASH script to execute the python query.
# The default "./run.sh" will run as "./run.sh -key test -t infobox -q bill gates"
# Adding any of "-key", "-t", and "-q" can modify the default values
# An additional "-v" for debugging

API_KEY="test"
MODE=infobox
QUERY="bill gates"
IN_QUERY=n
SOURCE=interact
FILE=
VERBOSE=n

function test_and_add_query
{
	if [ "$IN_QUERY" = "y" ]; then
		QUERY="$QUERY $1"
	else
		echo "Unknown format"
	fi
}

if [ ! "$1" = "" ]; then
	while [ "$1" != "" ]; do
		case $1 in
			-key )
				IN_QUERY=n
				shift
				API_KEY=$1
				;;
			-t )
				if [ ! "$SOURCE" = "file" ]; then
					SOURCE=normal
				fi
				IN_QUERY=n
				shift
				MODE=$1
				;;
			-q )
				SOURCE=normal
				IN_QUERY=y
				shift
				QUERY=$1
				;;
			-v )
				IN_QUERY=n
				VERBOSE=y
				;;
			-f )
				SOURCE=file
				IN_QUERY=n
				shift
				FILE=$1
				;;
			* )
				test_and_add_query $1
		esac
		shift
	done
fi

if [ "$VERBOSE" = "y" ]; then
	echo "API key: $API_KEY"
	echo "source: $SOURCE"
	echo "mode: $MODE"
	echo "query: $QUERY"
	echo "file: $FILE"
fi

if [ "$SOURCE" = "normal" ]; then
	python main.py $API_KEY $SOURCE $MODE $QUERY
elif [ "$SOURCE" = "file" ]; then
	python main.py $API_KEY $SOURCE $MODE $FILE
else
	python main.py $API_KEY interact
fi
