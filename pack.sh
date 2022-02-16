OUTDIR=dist/

rm -r -f $OUTDIR
rm -f rpunct-ca.zip
mkdir -p $OUTDIR/outputs
cp outputs/*.bin $OUTDIR/outputs
cp outputs/*.json $OUTDIR/outputs
cp rpunct/punctuate.py $OUTDIR
cp inference/*.py $OUTDIR
pushd $OUTDIR && zip ../rpunct-ca.zip -r * && popd
