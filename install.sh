PROJECT_ROOT=$(pwd)

python3 -m venv .
source bin/activate
python3 -m pip install -r requirements.txt

ln -s $PROJECT_ROOT/font $PROJECT_ROOT/lib/python3.8/site-packages/fpdf/font

echo "All set up!"
