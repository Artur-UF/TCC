
Main: *.tex
	rm -f diss.pdf
	pdflatex Main
	bibtex Main
	pdflatex Main
	pdflatex Main
	mv Main.pdf diss.pdf

clean:
	rm -f *.log *.aux *.toc *.lot *.lof *.bbl *.blg img/*-converted-to.pdf fig/*-converted-to.pdf

