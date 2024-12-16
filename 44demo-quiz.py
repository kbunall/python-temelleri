# Question

class Question:
    def __init__(self,text,choices,answer):
        self.text=text
        self.choices=choices
        self.answer=answer  # soru seçenekler ve cevap şeklinde yazılır.
    def checkAnswer(self,answer):
        return self.answer==answer # dışarıdan alınan cevapla bizim cevabımız eşleşiyormu kontrol edilir.


# Quiz

class Quiz:
    def __init__(self,questions):
        self.questions=questions # Dışarıdan soruları buraya aktarıyoruz
        self.score=0 
        self.questionIndex=0 # kaçıncı soruyu alıcağımızı belirliyoruz.
    def getQuestion(self):
        return self.questions[self.questionIndex] # soruları çalıştırmak için bir fonksiyon
    def displayQuestion(self):
        question=self.getQuestion() # burada az önce yaptığımız fonksiyonu questiona atıyoruz ve bu fonksiyonda devam ediyoruz.
        print(f'soru{self.questionIndex+1}:{question.text}')

        for q in question.choices: # seneçekleri bir for döngüsü ile ekrana yazdırıyoruz. Zaten soruları yazdırmıştık.
            print('-',q)
        answer=input('cevap: ')
        self.guess(answer)
        self.loadQuestion()
    def guess(self,answer):
        question=self.getQuestion()

        if question.checkAnswer(answer): # burada if koşulu ile doğru mu diye kontrol ediyoruz.
            self.score += 1 # eğer doğru ise 1 score ekleniyor eğer yanlış ise direk çıkış yapıyor.
        self.questionIndex += 1 # ve döngüden sonra index numarasını bir artırarak diğer soruya geçiyoruz.

    def loadQuestion(self):
        if len(self.questions)==self.questionIndex: # burada soru bitti mi diye yine index kontrol edip bitiriyoruz.
            self.showScore() # kontrol edildikten sonra scoru ekrana yazdırıyoruz.
        else:
            self.displayProgress() # eğer bitmediyse devam ediiliyor diğer fonksiyonları kullanarak.
            self.displayQuestion()
    
    def showScore(self):
        print('score: ', self.score)

    def displayProgress(self):
        totalQuestion=len(self.questions)
        questionNumber=self.questionIndex+1
        if questionNumber > totalQuestion:
            print('Quiz bitti.')
        else:
            print(f'Question{questionNumber} of {totalQuestion}'.center(100,'*'))



q1=Question('en iyi programlama dili hangisidir?',['C#','python','Javascript','java'],'python')
q2=Question('en popüler programlama dili hangisidir?',['python','Javascript','C#','java'],'python')
q3=Question('en çok kazandıran programlama dili hangisidir?',['C#','Javascript','java','python'],'python')

questions=[q1,q2,q3]

quiz=Quiz(questions)
quiz.loadQuestion()