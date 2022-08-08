FROM image_base

RUN python3 -m pip install jupyterlab

WORKDIR /notebook

CMD jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root --NotebookApp.token=

