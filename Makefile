build:
	easycython fib_cy.py
	easycython *.pyx


clean:
	@echo "Fazendo a limpeza"
	rm -rf __pycache__
	rm -f prof*
	rm -f *.so
	rm -f *.html
	rm -rf build
	rm -f *.c
