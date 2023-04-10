from utilites import amount_of_sentences
from utilites import amount_of_non_declarative_sentences
from utilites import sentences_length
from utilites import words_length
from utilites import get_top_k_ngrams

if __name__ == '__main__':

    answer = int(input("Что вы хотите сделать?\n1)Ввести текст из консоли\n2)Прочитать из файла\n"))

    if answer == 1:
        text = input("Введите текст: ")
    elif answer == 2:
        with open("text.txt", "r") as file:
            text = file.read()
            print(text)

    print("Количество предложений: ", amount_of_sentences(text))
    print("Количество недекларативных предложений: ", amount_of_non_declarative_sentences(text))

    if amount_of_sentences(text) != 0:
        print("Cредняя длина предложения в символах : ", sentences_length(text))
        print("Cредняя длина слова в тексте в символах: ", words_length(text))

        answer = input("Вы хотите ввести N и K(топ-K наиболее повторяющихся N-грамм в тексте; по умолчанию K=10, N=4) Y/N: ")

        n = 4
        k = 10

        if answer.lower() == "y":
            k = int(input("Введите К: "))
            n = int(input("Введите N: "))

        print(f"Tоп-{k} наиболее повторяющихся {n}-грамм в тексте: ", get_top_k_ngrams(text, k, n))
