

pdf:
	xelatex main
	bibtex main
	makeglossaries main
	xelatex main
	xelatex main

docx:
	pandoc main.tex -S -o main.docx

clean:
	rm main.edu main.glsdefs main.synctex.gz main.aux main.out main.bcf main.run.xml main.toc main.lof main.lot main.log main.blg main.bbl main.dvi main-blx.bib main.acn  main.acr  main.alg  main.glg  main.glo  main.gls  main.ist
