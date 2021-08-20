PREFIX ?= /usr

all:
	@echo RUN \'make install\' to install warper

install:
	@install -Dm755 warper $(DESTDIR)$(PREFIX)/bin/warper

uninstall:
	@rm -f $(DESTDIR)$(PREFIX)/bin/warper

