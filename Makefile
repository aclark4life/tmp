test:
	check-manifest
	flake8 *.py
#	pyroma
	python setup.py test
