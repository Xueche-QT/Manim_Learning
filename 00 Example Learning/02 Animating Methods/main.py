from manimlib import *

class AnimatingMethods(Scene):
    def construct(self):
        # Tex类用于渲染LaTex表达式，get_grid用于生成一个指定维度(10×10)，且高度为4的网格，网格中每个格子将包含 pi 符号
        grid = Tex(r"\pi").get_grid(10, 10, height = 4)
        self.add(grid)                                              # 添加到动画场景
        self.play(grid.animate.shift(LEFT))                         # 左移 1 个单位
        self.play(grid.animate.set_color(YELLOW))                   # 设置颜色为 黄色
        self.wait()
        # 对网格中的子对象应用[渐变颜色]效果
        self.play(grid.animate.set_submobject_colors_by_gradient(BLUE, GREEN))
        self.wait()
        # 改变对象的高度，将高度设置为 TAU - MED_SMALL_BUFF
        # TAU —— 圆的周长
        # MED_SMALL_BUFF —— 小的缓冲(间距)
        self.play(grid.animate.set_height(TAU - MED_SMALL_BUFF))
        self.wait()

        # apply_complex_function 复数函数[动画]
        # np.exp 为NumPy库中的指数函数
        # 若传入参数为 z，即为 e^z
        # run_time 设置动画持续时间
        self.play(grid.animate.apply_complex_function(np.exp), run_time = 5)
        self.wait()

        # 传递一个匿名函数(lambda 函数)，对各个点的坐标进行变换
        self.play(
            grid.animate.apply_function(
                lambda p: [
                    p[0] + 0.5 * math.sin(p[1]),        # X 坐标增加 0.5 * sin(y)
                    p[1] + 0.5 * math.sin(p[0]),        # Y 坐标增加 0.5 * sin(x)
                    p[2]                                # Z 坐标保持不变
                ]
            ),
            run_time = 5
        )
        self.wait()        
