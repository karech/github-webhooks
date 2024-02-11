pip freeze -q -r requirements.txt | sed '/freeze/,$ d' >requirements-prod.txt
pip freeze -q -r requirements-test.txt | sed '/freeze/,$ d' >requirements-test-prod.txt
