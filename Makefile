

all:
	xelatex main
	bibtex main
	makeglossaries main
	xelatex main
	xelatex main

pdf:
	make all

clean:
	rm main.synctex.gz main.aux main.out main.bcf main.run.xml main.toc main.lof main.lot main.pdf main.log main.blg main.bbl main.dvi main-blx.bib main.acn  main.acr  main.alg  main.glg  main.glo  main.gls  main.ist
