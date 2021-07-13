MAIN := main.py

PYTHON ?= python
CFLAGS ?= -Wall -Wextra
SFLAGS ?=

SRCDIR := src

all: $(SRCDIR)/$(MAIN)
	@$(PYTHON) $(SRCDIR)/$(MAIN)

clean:
	@$(RM) -rf ./out/*

.PHONY: all
