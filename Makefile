

pdf:
	xelatex main
	bibtex main
	makeglossaries main
	xelatex main
	xelatex main

docx:
	pandoc main.tex -o main.docx --bibliography=library.bib -S --csl=static/angewandte-chemie.csl

clean:
	rm main.equ main.glsdefs main.synctex.gz main.aux main.out main.bcf main.run.xml main.toc main.lof main.lot main.log main.blg main.bbl main.dvi main-blx.bib main.acn  main.acr  main.alg  main.glg  main.glo  main.gls  main.ist
