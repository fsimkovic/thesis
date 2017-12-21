

all:
	xelatex main
	bibtex main
	makeglossaries main
	xelatex main
	xelatex main

clean:
	rm main.aux main.out main.bcf main.run.xml main.toc main.lof main.lot main.pdf main.log main.blg main.bbl main.dvi main-blx.bib
