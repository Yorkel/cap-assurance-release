PYTHON ?= python3

.PHONY: reproduce verify test checksums all
reproduce:
	$(PYTHON) tools/reproduce.py
verify:
	$(PYTHON) tools/verify.py
checksums:
	$(PYTHON) tools/checksums.py
test:
	$(PYTHON) -m unittest discover -s tests -v
all: reproduce verify test checksums
