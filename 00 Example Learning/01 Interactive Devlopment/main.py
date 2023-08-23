from manimlib import *                              # 导入manim类

# 创建一个 Scene 的子类 SqureToCircle，即渲染的场景
class SqureToCircle(Scene):
    def construct(self):                            # 编写 construct() 方法，决定如何创建画面中的物体，以及需要执行哪些操作
        circle = Circle()                           # 创建一个圆(Circle 类的实例)，命名为circle
        circle.set_fill(BLUE, opacity=0.5)          # 填充颜色——蓝色，填充透明度——0.5
        circle.set_stroke(BLUE_E, width=4)          # 线条颜色——深蓝色，线条宽度——4
        square = Square()                           # 创建一个正方体，命名为square

        self.play(ShowCreation(square))             # 通过 Scene 的 play() 方法播放动画。ShowCreation —— 创建物体[动画]
        self.wait()                                 # 停顿，默认为1s，也可以传入参数来表示停顿时间，例如 self.wait(3) 表示停顿 3s
        self.play(ReplacementTransform(square, circle))                             # 转换物体[动画]
        self.wait()
        self.play(circle.animate.stretch(4, dim = 0))                               # 在水平方向上拉伸到四倍
        self.play(Rotate(circle, TAU / 4))          # 旋转90°
        self.play(circle.animate.shift(2 * RIGHT), circle.animate.scale(0.25))      # 在向右移动2个单位的同时缩小为原来的1/4
        circle.insert_n_curves(10)                  # 给 circle 添加10段曲线(不播放动画)，方便后续的非线性变化
        self.play(circle.animate.apply_complex_function(lambda z: z**2))            # 给 circle 上的所有点施加 f(z)=z^2 的复变化

        text = Text("""
            Hello Manimgl!
        """)
        self.play(Write(text))

        # self.embed()                                # 启用交互
        # self.add(circle)                            # 将圆添加到画面上

# >manimgl main.py SqureToCircle -ow                保存动画
