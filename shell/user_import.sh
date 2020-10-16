#!/bin/bash

path_file="/scripts/python/"
file="data.txt"
full_file="$path_file$file"

while read line
	do
	funcao=$(echo "$line" | awk -F' ' '{print $1}' | tr -d '"')
	if [ "$funcao" == "ADD" ]; then 
		nome=$(echo "$line" | awk -F',' '{print $1}' | tr -d '"' | cut -d' ' -f2-)
		login=$(echo "$line" | awk -F',' '{print $2}' | tr -d '"' | tr -d ' ')
		passwd=$(echo "$line" | awk -F',' '{print $3}' | tr -d '"' | tr -d ' ')
		sudo useradd -c "$nome" -m "$login" -p $(openssl passwd -1 "$passwd") 2>/dev/null
		echo "Usuário $login foi criado com sucesso!"
	elif [ "$funcao" == "DISABLE" ]; then
		login=$(echo "$line" | awk -F' ' '{print $2}' | tr -d '"')
		sudo userdel -rf "$login" 2>/dev/null
		echo "Usuário $login foi desativado com sucesso!"
	fi
done <"$full_file"

data_hoje=`date +%Y%m%d`
mv "$full_file" "${path_file}${data_hoje}.bak"
