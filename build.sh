quip version $1
quip clean --macfilesonly
python setup.py sdist bdist_wheel
pip uninstall uac-api
pip install --upgrade --find-links=./dist/ --pre uac-api
a=$PWD
cd ..
python -c "import uac_api; print(uac_api.__version__)"
cd $a