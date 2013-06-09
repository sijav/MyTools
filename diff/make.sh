dir1=old/
dir2=new/
IFS=$'\n'
rm -rf make
mkdir -p make/"${dir1}"
rm -rf make/"${dir1}"
cp -r diff make
for file in $(grep -Ilsr -m 1 '.' diff/"${dir1}" ); do
	cp -f "${dir2}""${file}" make/"${file}"
done
