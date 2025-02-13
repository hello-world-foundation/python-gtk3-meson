#!/bin/bash

if ! command -v xgettext &> /dev/null
then
	echo "xgettext could not be found."
	echo "you can install the package with 'apt install gettext' command on debian."
	exit
fi


echo "updating pot file"
xgettext -o po/example.pot --from-code="utf-8" \
    `find example -type f -iname "*.py"` \
    `find example -type f -iname "*.ui"`

for lang in $(cat po/LINGUAS); do
	if [[ -f po/$lang.po ]]; then
		echo "updating $lang.po"
		msgmerge -o po/$lang.po po/$lang.po po/example.pot
	else
		echo "creating $lang.po"
		cp po/example.pot po/$lang.po
	fi
done