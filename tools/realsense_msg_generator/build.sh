#/bin/bash

if [ -d 'build' ]; then
	rm -r build/*;
else
	mkdir build;
fi

cd build;
cmake ../;
make -j8;
if [ -d '../output' ]; then
	rm -r ../output/*;
else
	mkdir ../output;
fi

cp -a 'devel/include/realsense_msgs' ../output/cpp;
cp -a 'devel/lib/python2.7/dist-packages/realsense_msgs' ../output/python;
