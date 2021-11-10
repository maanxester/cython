build:
	easycython fib_cy.py


clean:
	@echo "Fazendo a limpeza"
	rm -rf __pycache__
	rm -f prof*
	rm -f *.so
	rm -f *.html
	rm -rf build
