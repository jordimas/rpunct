from simpletransformers.ner import NERModel


if __name__ == "__main__":
    print(f"Evaluation")

    VALID_LABELS = ['OU', 'OO', '.O', '!O', ',O', '.U', '!U', ',U', ':O', ';O', ':U', "'O", '-O', '?O', '?U']
    model = NERModel("bert", "outputs/", labels=VALID_LABELS, args={"silent": True, "max_seq_length": 512})


    result, model_outputs, pred_list = model.eval_model("rpunct_test_set.txt", output_dir = "eval-localmodel/")

#    model = NERModel("bert", "felflare/bert-restore-punctuation", labels=VALID_LABELS,
#                          args={"silent": True, "max_seq_length": 512})


 #   result = model.eval_model("rpunct_test_set.txt", output_dir = "eval-hf/")
    
    #print(f"result: {result}")

#    with open('eval-results.txt', 'w') as fp:
#        fp.write(result)

