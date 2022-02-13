rm -r -f runs/
rm -r -f outputs/
python training/train.py 

echo "Test training score"
cat test_training/eval_results.txt

echo "Flores eval score"
cat eval_training_flores//eval_results.txt

