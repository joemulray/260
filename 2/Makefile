PYTHON = python
VIEWER = less

.PHONY: clean run view

run: problem1 problem2 problem3

problem1 : problem1.py
	@chmod +x problem1.py
	$(PYTHON) problem1.py
	

problem2 : problem2.py
	@chmod +x problem2.py
	$(PYTHON) problem2.py


problem3 : problem3.py
	@chmod +x problem3.py
	$(PYTHON) problem3.py

view : problem1.py problem2.py problem3.py

	$(VIEWER) problem1.py
	$(VIEWER) problem2.py
	$(VIEWER) problem3.py
 
clean :
	- \rm $(outFile) > /dev/null 2>&1
	- \rm *.pyc > /dev/null 2>&1

