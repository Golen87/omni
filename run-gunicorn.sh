cd /root/omni/

python3 -m pipenv run \
    gunicorn \
    -c conf/gunicorn_config.py \
    --workers 1 \
    omni.wsgi:application
