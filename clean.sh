cat cet6.json| grep -E -v '}|{'  | awk -F ':' '{print $1}' | sed 's/\"//g' | sed 's/\ //g' > p_cet6.txt
cat toefl.txt | awk '{print $1}' > p_toefl.txt

