grep "\.\|," tgt.txt  | grep '.\{230\}' > catalan_train.txt
wc -l catalan_train.txt

