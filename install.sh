PROJECT_ROOT=$(echo pwd)

python3 -m venv .
python3 -m pip --upgrade pip
python3 -m pip install -r requirements.txt

ln -s font lib/python3.8/site-packages/fpdf/font

echo "All set up!"