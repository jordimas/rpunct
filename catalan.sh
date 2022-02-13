grep "\.\|," tgt.txt  | grep '.\{230\}' > catalan.txt
wc -l catalan.txt
cp catalan.txt yelp_polarity_reviews_train.txt
