DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

cd $DIR/data && wget https://github.com/wizyoung/YOLOv3_TensorFlow/releases/download/v1.0/yolo_tf_weights.zip -O temp.zip; 
cd $DIR/data && unzip temp.zip; 
cd $DIR/data && rm temp.zip
