# https://forums.fast.ai/t/tips-for-building-large-image-datasets/26688
googleimagesdownload -k "tesla" -s medium -l 500 -o data/train -i tesla -cd chromedriver
googleimagesdownload -k "cars" -s medium -l 500 -o data/train -i others -cd chromedriver
