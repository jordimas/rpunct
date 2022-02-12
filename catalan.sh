grep "\.\|," tgt.txt  | grep '.\{100\}' > catalan.txt
wc -l catalan.txt

