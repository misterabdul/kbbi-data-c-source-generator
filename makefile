MAIN := main.py

CFLAGS := -Wall -Wextra

SRCDIR := src

all: $(SRCDIR)/$(MAIN)
	@python $(SRCDIR)/$(MAIN)
	@$(CC) -c ./out/kbbi_data.c -o ./out/kbbi_data.o
	@rm ./out/kbbi_data.c

clean:
	@rm -rf ./out/kbbi_*

.PHONY: all
