verify:
	python3 tools/verify_fo4_constraint_isolation.py
	python3 -m pytest -q
	git diff --check
