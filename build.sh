quip version $1
quip clean --macfilesonly
python setup.py sdist bdist_wheel
pip uninstall uac-api
pip install --upgrade --find-links=./dist/ --pre uac-api
a=$PWD
cd ..
python -c "import uacapi; print(uacapi.__version__)"
cd $a