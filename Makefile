all:
	python main.py

clean:
	rm -r *.pyc
install:
	cp dist/Lazy-IOTA /usr/local/bin/