cd temp

# create the list of mp3 files to combine
touch mp3_ls.txt
> mp3_ls.txt

for f in test-*.mp3
do
    echo "file '$f'" >> mp3_ls.txt
done

# combine mp3 files
ffmpeg -f concat -safe 0 -i mp3_ls.txt -c copy output.mp3