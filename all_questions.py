# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = No
    answers["(b)"] = No
    answers["(c)"] = Yes
    answers["(d)"] = Yes

    # explain-string: explanation in english prose
    answers["(a) explain"] = "the case which is home owner=yes and marital status=single will trigger two rules"
    answers["(b) explain"] = "home owner=no,marital status=divorced annual income=high,currently employed=yes, cannot trigger any rules"
    answers["(c) explain"] = "for the case which is home owner=yes, marital status=divorced, annual income=medium,currently employed=yes will trigger different rules and have different results"
    answers["(d) explain"] = "home owner=no,marital status=divorced annual income=high,currently employed=yes this one should be a default class"

    return answers


# -----------------------------------------------------------
def question2():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = None
    answers["(b)"] = None
    answers["(c)"] = None
    answers["(d)"] = None

    # explain_string: explanation in english prose
    answers["(a) explain"] = None
    answers["(b) explain"] = None
    answers["(c) explain"] = None
    answers["(d) explain"] = None

    return answers
# -----------------------------------------------------------
def question3():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = No
    answers["(b)"] = No
    answers["(c)"] = Yes

    # explain-string: explanation in english prose
    answers["(a) example"] = "the pigeon will trigger two rules"
    answers["(b) example"] = "the cold blood and givebirth case will not trigger any rules, for example leopard"
    answers["(c) example"] = "the pigeon will trigger two rules and get two different results"

    return answers
# -----------------------------------------------------------
def question7():
    answers = {}

    # bool: True/False
    answers["(a)"] = False
    answers["(b)"] = True
    answers["(c)"] = False
    answers["(d)"] = False

    # explain_string: explanation in english prose
    answers["(a) explain"] = "in back-propagation, it will use the later layer's information to calculate the former layer"
    answers["(b) explain"] = "after a ann model is built and used on a test set, it will calculate in a forward, which means that the activation in the former layer will be weighted and used as the input in the later layer"
    answers["(c) explain"] = "the vanish gradient problem means that the gradients of the loss function are influenced by the input value and become very small, it will cause the change of the weight of the layers become very small"
    answers["(d) explain"] = "if all of the case can be classified correctly, the loss function will be zero, but the loss function and the activation functions still have gradients, it will not be zero "

    return answers

# -----------------------------------------------------------
def question8():
    answers = {}

    # float
    answers["(a) P(X_1=1)"] = 0.65
    answers["(a) P(X_2=1)"] = 0.41
    answers["(a) P(X_1=1,X_2=1)"] = 0.28

    # string: "dependent" or "independent"
    answers["(a) Relationship between X_1 and X_2"] = "dependent"

    # string: "yes" or "no"
    answers["(b) X_1 and X_2 conditionally independent given the class?"] = yes

    # float
    answers["(c) P(X_1=1 | +)"] = 0.8
    answers["(c) P(X_1=1 | -)"] = 0.5
    answers["(c) P(X_2=1 | +)"] = 0.5
    answers["(c) P(X_2=1 | -)"] = 0.32
    answers["(c) P(X_3=1 | +)"] = 0.4
    answers["(c) P(X_3=1 | -)"] = 0.16

    # For each row give the class predicted by the model after training using Naive Bayes
    # String: either '+' or '-'
    answers["(d) Row 1"] = +
    answers["(d) Row 2"] = -
    answers["(d) Row 3"] = -
    answers["(d) Row 4"] = -

    # float between 0 and 1
    answers["(d) Training error rate"] = 0.35

    return answers

# --------------------------------------------------------
def question9():
    answers = {}

    # int
    answers["(a) K"] = 1
    answers["(b) K"] = 5

    # explain_string
    answers["(a) explain"] = "the two kinds of data points are definitely separated, so we just need k=1 to find the label of the data point nearby the target to classify it"
    answers["(b) explain"] = "the two kinds of data points have some overlaps, but k=50 is not necessary, because it will contain too much points which may generate error and increase the calculation costs"

    return answers

# --------------------------------------------------------
def question10():
    answers = {}

    # float
    answers["(a) P(A=1|+)"] = 0.6
    answers["(a) P(B=1|+)"] = 0.4
    answers["(a) P(C=1|+)"] = 0.8
    answers["(a) P(A=1|-)"] = 0.4
    answers["(a) P(B=1|-)"] = 0.4
    answers["(a) P(C=1|-)"] = 0.2

    # type: explanatory string
    answers["(a) P(A=1|+) explain your answer"] = "there are 3 A=1 in the positive set, there are 5 positive cases and 5 negative cases in the whole dataset"
  
    # type: float
    # note: R is the sample (A=1,B=1,C=1)
    answers["(b) P(+|R)"] = 0.857  # WRONG
    answers["(b) P(R|+)"] = 0.192
    answers["(b) P(R|-)"] = 0.032

    # string, '+' or '-'
    answers["(b) class label"] = +

    # explain_string
    answers["(b) Explain your reasoning"] = "we can get the different conditinal probabilities for different value of ABC, and we have the prior probabilities which are 0.5 for+ 0.5 for -, then we use the formula to calclulate the p(R|+) and p(R|-), then we can get the p(+|R) and p(-|R), which one is bigger, the label wil be that"
  
    # float
    answers["(c) P(A=1)"] = 0.5
    answers["(c) P(B=1)"] = 0.4
    answers["(c) P(A=1,B=1)"] = 0.2

    # type: string, 'yes' or 'no'
    answers["(c) A independent of B?"] = yes
  
    # type: float
    answers["(d) P(A=1)"] = 0.5
    answers["(d) P(B=0)"] = 0.6
    answers["(d) P(A=1,B=0)"] = 0.3

    # type: string: 'yes' or 'no'
    answers["(d) A independent of B?"] = yes
  
    # type: float
    answers["(e) P(A=1,B=1|+)"] = 0.2
    answers["(e) P(A=1|+)"] = 0.6
    answers["(e) P(B=1|+)"] = 0.4

    # type: string: 'yes' or 'no'
    answers["(e) A independent of B given class +?"] = no

    # type: explanatory string
    answers["(e) A and B conditionally independent given class +, explain"] =  "P(A=1,B=1|+)not equal to P(A=1|+)*P(B=1|+) "
  
    return answers
# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
