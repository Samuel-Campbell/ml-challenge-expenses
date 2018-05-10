from sklearn.pipeline import Pipeline
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.preprocessing import StandardScaler
from data_extraction.data_extractor import Parser
from sklearn.metrics import precision_recall_fscore_support


class Classifier:
    def __init__(self):
        self.input_dimensions = 0
        self.model = None

    def train(self):
        x_train, y_train = Parser().post_process_data(Parser.training_data_file)
        x_test, y_test = Parser().post_process_data(Parser.validation_data_file)
        self.input_dimensions = len(x_train[0])
        clf = KerasClassifier(
            build_fn=self._nn_architecture, epochs=300, verbose=0)
        scaler = StandardScaler()
        self.model = Classifier._create_pipeline(scaler, clf)
        self.model.fit(x_train, y_train)
        self.test(x_test, y_test)

    def _nn_architecture(self):
        model = Sequential()
        model.add(Dense(self.input_dimensions, input_dim=self.input_dimensions,
                        kernel_initializer='normal', activation='relu'))
        model.add(Dense(11, kernel_initializer='normal', activation='relu'))
        model.add(Dense(1, kernel_initializer='normal', activation='sigmoid'))
        model.compile(loss='binary_crossentropy', optimizer='adam')
        return model

    @staticmethod
    def _create_pipeline(scaler, regressor):
        estimators = []
        estimators.append(('standardize', scaler))
        estimators.append(('mlp', regressor))
        return Pipeline(estimators)

    def test(self, x_test, y_test):
        y_predict = self.model.predict(x_test)
        sum = 0
        for i in range(len(y_predict)):
            if y_predict[i] == y_test[i]:
                sum += 1
        accuracy = sum * 100.0 / len(y_test)
        (precision, recall, f1, _) = precision_recall_fscore_support(y_test, y_predict)
        print('Test accuracy: {}%'.format(accuracy))
        print('Precision: {}'.format(precision))
        print('Recall: {}'.format(recall))
        print('F1: {}\n'.format(f1))