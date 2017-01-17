#Joseph Mulray HW1,
#January 17 2017
#Makefile to compile hello.py

PYTHON = python
VIEWER = more

.PHONY: clean run view

run :  hello.py
	@chmod +x hello.py
	$(PYTHON) hello.py

view : hello.py
	$(VIEWER) hello.py 

clean :
	@\rm *.pyc

