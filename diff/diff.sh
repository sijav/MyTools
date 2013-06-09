dir1=old/
dir2=new/
IFS=$'\n'
rm -rf diff
mkdir -p diff/"${dir1}"
rm -rf diff/"${dir1}"
cp -r "${dir1}" diff/"${dir1}"
for file in $(grep -Ilsr -m 1 '.' "$dir1"); do
	diff "$file" "${file/${dir1}/${dir2}}" > diff/"$file" 
done
find diff/ -empty -type f -delete
find diff/ -name *.png -type f -delete
find diff/ -name *.jpg -type f -delete
find diff/ -name *.arsc -type f -delete
find diff/ -empty -type d -delete
