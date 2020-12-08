echo 0
export FLASK_APP=ping_violence_detection.py
echo 1
export LC_ALL=C.UTF-8
echo 2
export LANG=C.UTF-8
echo 3
flask run --host=0.0.0.0 --port=3000

