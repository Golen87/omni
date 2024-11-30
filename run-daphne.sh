cd /root/omni/

python3 -m pipenv run \
    daphne \
    -b 0.0.0.0 -p 8008 \
    omni.asgi:application
