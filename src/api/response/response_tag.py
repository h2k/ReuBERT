from enum import Enum


class ResponseTag(Enum):
    GREETING_TAG = (0, "ReuBERT[greeting]:~$ {}")
    GOODBYE_TAG = (1, "ReuBERT[goodbye]:~$ {}")
    ENTER_INFORMATION_TAG = (2, "You[enter information]:~$ ")
    GATHER_INFORMATION_TAG = (3, "ReuBERT[gather information]:~$ {}")
    ENTER_QUESTION_TAG = (4, "You[enter question]:~$ ")
    ANSWER_QUESTION_TAG = (5, "ReuBERT[answer question]:~$ {}")

    def __str__(self):
        return self.value[1]
