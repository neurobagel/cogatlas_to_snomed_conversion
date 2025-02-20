# Makefile

.PHONY: fetch process loop

fetch:
	python src/fetch_data.py

process: 
	python src/process_data.py

vocab_map.json:
	python src/map_data.py

loop:
	for i in {1..5}; do echo "Iteration $$i"; done

replace:
	python src/replace_in_dictionary.py