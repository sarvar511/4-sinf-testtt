from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class TestApp(App):

    def build(self):

        self.oynacha = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=20
        )

        self.savollar = [
            ["5 + 5 = ?", "A) 8", "B) 10", "C) 12", "b"],
            ["10 - 4 = ?", "A) 6", "B) 5", "C) 7", "a"],
            ["3 × 4 = ?", "A) 7", "B) 10", "C) 12", "c"],
            ["20 + 10 = ?", "A) 30", "B) 25", "C) 40", "a"],
            ["15 - 7 = ?", "A) 6", "B) 8", "C) 9", "b"],
            ["6 × 3 = ?", "A) 18", "B) 16", "C) 20", "a"],
            ["24 ÷ 6 = ?", "A) 3", "B) 4", "C) 5", "b"],
            ["9 + 8 = ?", "A) 16", "B) 17", "C) 18", "b"],
            ["30 - 12 = ?", "A) 18", "B) 16", "C) 20", "a"],
            ["5 × 5 = ?", "A) 20", "B) 25", "C) 30", "b"]
        ]

        self.raqam = 0
        self.ball = 0

        self.sarlavha = Label(
            text="4-SINF TEST DASTURI",
            font_size=30
        )

        self.ism_oynasi = TextInput(
            hint_text="O'quvchining ismini kiriting",
            font_size=22,
            multiline=False
        )

        self.boshlash = Button(
            text="TESTNI BOSHLASH",
            font_size=24
        )

        self.natijalar = Button(
            text="NATIJALARNI KO'RISH",
            font_size=24
        )

        self.ochirish = Button(
            text="NATIJALARNI O'CHIRISH",
            font_size=24
        )

        self.boshlash.bind(
            on_press=self.testni_boshlash
        )

        self.natijalar.bind(
            on_press=self.natijalarni_korsatish
        )

        self.ochirish.bind(
            on_press=self.natijalarni_ochirish
        )

        self.bosh_sahifa()

        return self.oynacha

    def bosh_sahifa(self):

        self.oynacha.clear_widgets()

        self.oynacha.add_widget(self.sarlavha)
        self.oynacha.add_widget(self.ism_oynasi)
        self.oynacha.add_widget(self.boshlash)
        self.oynacha.add_widget(self.natijalar)
        self.oynacha.add_widget(self.ochirish)

    def testni_boshlash(self, tugma):

        self.ism = self.ism_oynasi.text

        if self.ism == "":
            self.ism = "O'quvchi"

        self.raqam = 0
        self.ball = 0

        self.oynacha.clear_widgets()

        self.savolni_korsatish()

    def savolni_korsatish(self):

        savol = self.savollar[self.raqam]

        matn = Label(
            text=str(self.raqam + 1)
            + "-SAVOL\n\n"
            + savol[0],
            font_size=30
        )

        a = Button(
            text=savol[1],
            font_size=24
        )

        b = Button(
            text=savol[2],
            font_size=24
        )

        c = Button(
            text=savol[3],
            font_size=24
        )

        a.bind(
            on_press=lambda x: self.javob("a")
        )

        b.bind(
            on_press=lambda x: self.javob("b")
        )

        c.bind(
            on_press=lambda x: self.javob("c")
        )

        self.oynacha.clear_widgets()

        self.oynacha.add_widget(matn)
        self.oynacha.add_widget(a)
        self.oynacha.add_widget(b)
        self.oynacha.add_widget(c)

    def javob(self, javob):

        togri_javob = self.savollar[self.raqam][4]

        if javob == togri_javob:
            self.ball += 1

        self.raqam += 1

        if self.raqam < len(self.savollar):
            self.savolni_korsatish()
        else:
            self.natijani_korsatish()

    def natijani_korsatish(self):

        self.oynacha.clear_widgets()

        if self.ball >= 9:
            baho = 5
        elif self.ball >= 7:
            baho = 4
        elif self.ball >= 5:
            baho = 3
        else:
            baho = 2

        fayl = open("natijalar.txt", "a")

        fayl.write(
            self.ism + " — "
            + str(self.ball)
            + "/10 — Baho: "
            + str(baho)
            + "\n"
        )

        fayl.close()

        natija = Label(
            text="TEST YAKUNLANDI!\n\n"
            + "O'quvchi: "
            + self.ism
            + "\n\nBall: "
            + str(self.ball)
            + " / 10"
            + "\n\nBaho: "
            + str(baho)
            + "\n\nNatija saqlandi!",
            font_size=28
        )

        qaytish = Button(
            text="BOSH SAHIFAGA",
            font_size=24
        )

        qaytish.bind(
            on_press=lambda x: self.bosh_sahifa()
        )

        self.oynacha.add_widget(natija)
        self.oynacha.add_widget(qaytish)

    def natijalarni_korsatish(self, tugma):

        self.oynacha.clear_widgets()

        try:

            fayl = open("natijalar.txt", "r")
            natijalar = fayl.readlines()
            fayl.close()

            if len(natijalar) == 0:

                matn = "Hozircha natijalar yo'q."

            else:

                matn = "O'QUVCHILAR NATIJALARI\n\n"

                for i, natija in enumerate(natijalar):

                    matn += (
                        str(i + 1)
                        + ". "
                        + natija
                    )

        except FileNotFoundError:

            matn = "Hozircha natijalar yo'q."

        natija_oynasi = Label(
            text=matn,
            font_size=24
        )

        qaytish = Button(
            text="ORTGA",
            font_size=24
        )

        qaytish.bind(
            on_press=lambda x: self.bosh_sahifa()
        )

        self.oynacha.add_widget(natija_oynasi)
        self.oynacha.add_widget(qaytish)

    def natijalarni_ochirish(self, tugma):

        fayl = open("natijalar.txt", "w")
        fayl.close()

        self.oynacha.clear_widgets()

        matn = Label(
            text="BARCHA NATIJALAR O'CHIRILDI!",
            font_size=28
        )

        qaytish = Button(
            text="BOSH SAHIFAGA",
            font_size=24
        )

        qaytish.bind(
            on_press=lambda x: self.bosh_sahifa()
        )

        self.oynacha.add_widget(matn)
        self.oynacha.add_widget(qaytish)


TestApp().run()
