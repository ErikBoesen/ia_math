all: ia
ia:
	latexmk -pdf -pdflatex="pdflatex -interaction=nonstopmode --shell-escape" ia.tex -f
clean:
	rm -fv *.{aux,bbl,blg,log,out,pdf,synctex.gz,pyg,fls,fdb_latexmk,toc}
