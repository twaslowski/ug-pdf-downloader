PROJECT_ROOT=$(echo pwd)

python3 -m venv .
source bin/activate
python3 -m pip install -r requirements.txt

ln -s font lib/python3.8/site-packages/fpdf/font

echo "All set up!"
