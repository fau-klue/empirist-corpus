#!/bin/bash

total=$(grep -Pvc '^<.+>$' ../empirist.vrt)
train=$(xsltproc extract_train.xsl ../empirist.vrt | grep -Pvc '^<.+>$')
train_cmc=$(xsltproc extract_train_cmc.xsl ../empirist.vrt | grep -Pvc '^<.+>$')
train_web=$(xsltproc extract_train_web.xsl ../empirist.vrt | grep -Pvc '^<.+>$')
test=$(xsltproc extract_test.xsl ../empirist.vrt | grep -Pvc '^<.+>$')
test_cmc=$(xsltproc extract_test_cmc.xsl ../empirist.vrt | grep -Pvc '^<.+>$')
test_web=$(xsltproc extract_test_web.xsl ../empirist.vrt | grep -Pvc '^<.+>$')

cmc=$(($train_cmc + $test_cmc))
web=$(($train_web + $test_web))

echo "|          |   CMC |   Web | Total |
|----------+-------+-------+-------|
| Training |  $train_cmc |  $train_web | $train |
| Test     |  $test_cmc |  $test_web | $test |
|----------+-------+-------+-------|
| Total    | $cmc | $web | $total |"
