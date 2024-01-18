# the first argument is the file name without extension
file=$1

# the second argument is the clean flag
isclean=$2
isclean=${isclean:-false}

# convert epub to md
echo "convert epub > md"
pandoc -s temp/$file.epub -o temp/$file.md

# format cleasing
echo "format cleansing"
python format_clean.py temp/$file.md $isclean