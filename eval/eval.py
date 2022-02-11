from simpletransformers.ner import NERModel

if __name__ == "__main__":
    print(f"Evaluation")

    self.model = NERModel("bert", "felflare/bert-restore-punctuation", labels=self.valid_labels,
                          args={"silent": True, "max_seq_length": 512})


    model.eval_model(rpunct_test_set.txt, output_dir = "eval_model/")
