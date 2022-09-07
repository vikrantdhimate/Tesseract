# Tesseract

1. install libraries
    sudo apt-get install libtool libjpeg-dev libtiff-dev libpng-dev

2. Python installation
    wget https://www.python.org/ftp/python/3.7.11/Python-3.7.11.tgz  
    tar xzf Python-3.7.11.tgz 
    cd Python-3.7.11 
    ./configure --enable-optimizations 
    make altinstall 

3. Leptonica installation
    wget https://src.fedoraproject.org/lookaside/extras/leptonica/leptonica-1.73.tar.gz/092cea2e568cada79fff178820397922/leptonica-1.73.tar.gz
    tar xzvf leptonica-1.73.tar.gz
    cd leptonica-1.73
    ./configure
    make
    sudo make install

4. Tesseract installtion
    wget https://github.com/tesseract-ocr/tesseract/archive/3.04.01.tar.gz
    mv 3.04.01.tar.gz tesseract-3.04.01.tar.gz
    tar xzvf tesseract-3.04.01.tar.gz
    cd tesseract-3.04.01/
    ./autogen.sh
    ./configure
    make
    sudo make install
    sudo ldconfig
 
 5. Train Data
    wget https://github.com/tesseract-ocr/tessdata/raw/main/eng.traineddata
    cp eng.traineddata /usr/local/share/tessdata/eng.traineddata
    export TESSDATA_PREFIX="/usr/local/share"

6. pytesseract installation
    python3.8 -m pip install pytesseract
