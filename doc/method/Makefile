TEX	= pdflatex
BIBTEX  = bibtex

SOURCES = signal.tex

all : signal.pdf

signal.pdf : $(SOURCES)
	$(TEX) signal
	$(BIBTEX) signal
	$(TEX) signal
	$(TEX) signal
clean :
	rm -f *aux *out *log *dvi *bbl *blg *toc signal.pdf
