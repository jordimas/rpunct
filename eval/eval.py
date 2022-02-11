from simpletransformers.ner import NERModel

'''
def train_model():
    """
    Trains simpletransformers model
    """
    # Create a NERModel
    model = NERModel("bert", "bert-base-uncased",
                     args={"overwrite_output_dir": True,
                           "num_train_epochs": 3,
                           "max_seq_length": 512,
                           "lazy_loading": True},
                     labels=VALID_LABELS)

    # # Train the model
    steps, tr_details = model.train_model('rpunct_train_set.txt')
'''

if __name__ == "__main__":
    print(f"Evaluation")

    VALID_LABELS = ['OU', 'OO', '.O', '!O', ',O', '.U', '!U', ',U', ':O', ';O', ':U', "'O", '-O', '?O', '?U']
    #valid_labels = ['OU', 'OO', '.O', '!O', ',O', '.U', '!U', ',U', ':O', ';O', ':U', "'O", '-O', '?O', '?U']
    model = NERModel("bert", "outputs/", labels=VALID_LABELS,
                          args={"silent": True, "max_seq_length": 512})


    result = model.eval_model("rpunct_test_set.txt", output_dir = "eval_model/")
    print(f"result: {result}")

    with open('eval-results.txt', 'w') as fp:
        fp.write(result)

