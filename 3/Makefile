PYTHON = python
VIEWER = more

.PHONY : run view clean

run: prob1 prob2 prob3


prob1: prob1.py
	$(PYTHON) prob1.py $(arg)

prob2: prob2.py
	$(PYTHON) prob2.py $(arg)

prob3: prob3.py
	$(PYTHON) prob3.py

view: prob1.py prob2.py prob3.py
	$(VIEWER) prob1.py
	$(VIEWER) prob2.py
	$(VIEWER) prob3.py

clean: 
	- \rm $(outFile) > /dev/null 2>&1
	- \rm *.pyc > /dev/null 2>&1
