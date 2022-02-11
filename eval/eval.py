from simpletransformers.ner import NERModel

if __name__ == "__main__":
    print(f"Evaluation")

    valid_labels = ['OU', 'OO', '.O', '!O', ',O', '.U', '!U', ',U', ':O', ';O', ':U', "'O", '-O', '?O', '?U']
    model = NERModel("bert", "outputs/", labels=valid_labels,
                          args={"silent": True, "max_seq_length": 512})


    result = model.eval_model("rpunct_test_set.txt", output_dir = "eval_model/")
    print(f"result: {result}")