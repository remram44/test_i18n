#!/bin/sh

DIR=$(dirname $0)/..

exec xgettext \
    --language=Python \
    --keyword=_ \
    --keyword=_n:1,2 \
    --output=$DIR/po/test_i18n.pot \
    $(find $DIR/test_i18n -name '*.py')
