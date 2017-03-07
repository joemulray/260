PYTHON = python
VIEWER = more

.PHONY: run view clean


run: prob1


prob1: prob1.py
	$(PYTHON) prob1.py


test: prob1.py
	$(PYTHON) prob1.py < $(file)

view: prob1.py
	$(VIEWER) prob1.py


clean: 
	-rm *.pyc

