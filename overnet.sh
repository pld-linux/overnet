#!/bin/sh
if [ ! -d $HOME/ed2k ]; then
	mkdir $HOME/ed2k
fi
cp /usr/bin/overnet $HOME/ed2k/overnet
echo ""
echo "Done... It's now installed at $HOME/ed2k/ :)"
echo ""
echo "Please set \"path to local core\" to $HOME/ed2k/overnet"
echo ""

