from manimlib import *

class TextExample(Scene):
    def construct(self):
        text = Text("Here is a text", font = "Consolas", font_size = 90)
        difference = Text(
            """
            The most important difference between Text and TexText is that \n
            you can change the font more easily, but can't use the LaTex grammar
            """,
            font = "Arial", font_size = 24,
            # t2c 是一个有 文本-颜色 键值组成的质点
            t2c = {"Text": BLUE, "TexText": BLUE, "LaTex": ORANGE}
        )
        # 创建 VGroup 对象，将text和difference垂直排列，之间的间距由 buff 参数控制
        VGroup(text, difference).arrange(DOWN, buff = 1)
        self.play(Write(text))
        # 使用 FadeIn 将difference对象逐渐淡入画面中，从画面上方(UP方向)进入
        self.play(FadeIn(difference, UP))
        self.wait(3)

        fonts = Text(
            "And you can also set the font according to difference words",
            font = "Arial",
            t2f = {"font": "Consolas", "words": "Consolas"},
            t2c = {"font": BLUE, "words": GREEN}
        )
        fonts.set_width(FRAME_WIDTH - 1)
        slant = Text(
            "And the same as slant and weight",
            font = "Consolas",
            t2s = {"slant": ITALIC},
            t2w = {"weight": BOLD},
            t2c = {"slant": ORANGE, "weight": RED}
        )
        VGroup(fonts, slant).arrange(DOWN, buff = 0.8)
        self.play(FadeOut(text), FadeOut(difference, shift = DOWN))
        self.play(Write(fonts))
        self.wait()
        self.play(Write(slant))
        self.wait()