#!/bin/bash
# The BASH script to execute the python query.
# The default "./run.sh" will run as "./run.sh -key test -t infobox -q bill gates"
# Adding any of "-key", "-t", and "-q" can modify the default values
# An additional "-v" for debugging

API_KEY="test"
MODE=infobox
QUERY="bill gates"
IN_QUERY=n
VERBOSE=n

function test_and_add_query
{
	if [ "$IN_QUERY" = "y" ]; then
		QUERY="$QUERY $1"
	else
		echo "Unknown format"
	fi
}

if [ "$1" = "" ]; then
	echo "Default test"
else
	while [ "$1" != "" ]; do
		case $1 in
			-key )
				IN_QUERY=n
				shift
				API_KEY=$1
				;;
			-t )
				IN_QUERY=n
				shift
				MODE=$1
				;;
			-q )
				IN_QUERY=y
				shift
				QUERY=$1
				;;
			-v )
				VERBOSE=y
				;;
			* )
				test_and_add_query $1
		esac
		shift
	done
fi

if [ "$VERBOSE" = "y" ]; then
	echo "API key: $API_KEY"
	echo "mode: $MODE"
	echo "query: $QUERY"
fi

python main.py $API_KEY $MODE $QUERY
