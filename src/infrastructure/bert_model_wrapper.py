class BertModelWrapper:

    def __init__(self, bert_model):
        self.bert_model = bert_model

    def _from_normal_input_to_bert_input_dict(self, normal_input):
        joined_user_inputs = "".join(normal_input["user_input"])
        return [{
            "paragraphs": [{
                "context":
                joined_user_inputs,
                "qas": [{
                    "answers": [],
                    "id": "",
                    "is_impossible": False,
                    "question": normal_input["question"]
                }]
            }],
            "title":
            ""
        }]

    def _from_bert_output_to_normal_output(self, all_nbest_json):
        return [(y['probability'], y['text'])
                for y in [x[1] for x in all_nbest_json.items()][0]]

    @staticmethod
    def question_schema(user_input, question):
        return {"user_input": user_input, "question": question}

    def transform(self, X):
        user_input, question = X
        normal_input = BertModelWrapper.question_schema(user_input, question)
        transformed_input = self._from_normal_input_to_bert_input_dict(
            normal_input)
        _, all_nbest_json, _ = self.bert_model.transform(transformed_input)
        transformed_output = self._from_bert_output_to_normal_output(
            all_nbest_json)
        return transformed_output