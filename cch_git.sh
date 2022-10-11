#!/bin/bash

# 현재 branch로 푸쉬
git config --global push.default current

dt=$(date +'%Y%m%d_%s')
res="git status"

git add .

$res

# if [ "${res}"==*"modified:"* ]; then
#     echo 'warning'
# else
#     exit
# fi

echo '* Enter the commit message *'
read commit_message

git commit -m $commit_message

git push

$res

echo success upload
