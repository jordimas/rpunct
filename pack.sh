OUTDIR=dist/

rm -r -f $OUTDIR
mkdir -p $OUTDIR/outputs
cp outputs/. $OUTDIR/outputs
cp rpunct/punctuate.py $OUTDIR
cp tests/* $OUTDIR
cp inference/*.py $OUTDIR
pushd $OUTDIR && zip ../rpunct-ca.zip -r * && popd
