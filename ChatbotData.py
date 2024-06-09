import pandas as pd
import Levenshtein

class SimpleChatBotLevenshtein:
    def __init__(self, filepath):
        self.questions, self.answers = self.load_data(filepath)

    def load_data(self, filepath):
        data = pd.read_csv(filepath)
        questions = data['Q'].tolist()
        answers = data['A'].tolist()
        return questions, answers

    def levenshtein_distance(self, s1, s2):
        return Levenshtein.distance(s1, s2)

    def find_best_answer(self, input_sentence):
        min_distance = float('inf')
        best_match_index = -1

        for i, question in enumerate(self.questions):
            distance = self.levenshtein_distance(input_sentence, question)
            if distance < min_distance:
                min_distance = distance
                best_match_index = i

        return self.answers[best_match_index]

# 데이터 파일의 경로를 지정합니다.
filepath = 'ChatbotData.csv'

# 챗봇 객체를 생성합니다.
chatbot = SimpleChatBotLevenshtein(filepath)

# '종료'라는 입력이 나올 때까지 사용자의 입력에 따라 챗봇의 응답을 출력하는 무한 루프를 실행합니다.
while True:
    input_sentence = input('You: ')
    if input_sentence.lower() == '종료':
        break
    response = chatbot.find_best_answer(input_sentence)
    print('Chatbot:', response)
