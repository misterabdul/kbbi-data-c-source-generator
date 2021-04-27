MAIN := main.py

PYTHON ?= python
CFLAGS ?= -Wall -Wextra

SRCDIR := src

all: $(SRCDIR)/$(MAIN)
	@$(PYTHON) $(SRCDIR)/$(MAIN)
	@$(CC) -c ./out/kbbi_data.c -o ./out/kbbi_data.o
	@$(RM) ./out/kbbi_data.c

clean:
	@$(RM) -rf ./out/kbbi_*

.PHONY: all
