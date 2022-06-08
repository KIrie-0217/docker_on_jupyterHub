FROM jupyter/scipy-notebook
USER root

# apt update
RUN apt update 

# timezoneの設定
RUN apt install -y tzdata
RUN ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime
ENV TZ=Asia/Tokyo

RUN apt autoremove
RUN apt clean
RUN rm -r /var/lib/apt/lists/*

#  計算機関連
RUN pip install --no-cache-dir optuna keras

# jupyter拡張
RUN pip install --no-cache-dir jupyterlab_code_formatter jupyterlab-git lckr-jupyterlab-variableinspector jupyterlab_widgets ipywidgets import-ipynb jupyterlab-language-pack-ja-JP


# サンプルコード
RUN git clone https://github.com/zhiyzuo/python-tutorial.git work



CMD ["jupyterhub-singleuser", "--allow-root"]
