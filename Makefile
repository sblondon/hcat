
package:
	python setup.py sdist

clean:
	rm -rf dist hcat.egg-info
	rm man/*.gz

