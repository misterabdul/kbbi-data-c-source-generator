MAIN := main.py

PYTHON ?= python
CFLAGS ?= -Wall -Wextra
SFLAGS ?=

SRCDIR := src

all: $(SRCDIR)/$(MAIN)
	@$(PYTHON) $(SRCDIR)/$(MAIN)
	@$(CC) -c ./out/kbbi_data.c -o ./out/kbbi_data.o $(CFLAGS) $(SFLAGS)
	@$(RM) ./out/kbbi_data.c

clean:
	@$(RM) -rf ./out/kbbi_*

.PHONY: all
