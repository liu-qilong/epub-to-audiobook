# the first argument is the file name without extension
file=$1

./epub2md.sh $file

echo "convert md > epub"
pandoc -s temp/$file.md -o temp/$file"_"clean.epub