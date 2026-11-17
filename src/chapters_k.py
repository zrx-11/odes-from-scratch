# -*- coding: utf-8 -*-
CH_SUMMARY = r"""
<section class="chapter" id="summary" style="display:none">
<div class="breadcrumb"></div>
<h2><span class="num">17</span>知识图谱与自测</h2>
<p class="lead">把 0 到 17 章串成一条链：每个工具解决什么问题、它依赖谁、后面被谁用。最后给一张公式速查表和十道跨章自测题。</p>

<h3>17.1 整门课的依赖树</h3>
<p>从下往上读。下面一层没打通，上面一层就会卡住。</p>

<div class="callout callout-key"><div class="callout-title">根系（常识与初中数学）</div>
数、四则运算、比较大小、函数（一个输入对应一个输出）、坐标系、直线方程、距离、面积、比例。
</div>

<div class="callout callout-key"><div class="callout-title">第一层：变化率（第 1 章）</div>
函数、导数（瞬时变化率）、微分 $dy=y'dx$、不定积分（反导数）、定积分（面积）、微积分基本定理（两者互逆）、链式法则、偏导数、全微分、二阶导数、绝对值、上确界、极限与一致收敛、变上限积分求导。
</div>

<div class="callout callout-key"><div class="callout-title">第二层：微分方程的基本语言（第 2 章）</div>
阶、线性/非线性、通解与特解、初值问题、方向场、积分曲线。
</div>

<div class="callout callout-key"><div class="callout-title">第三层：一阶方程的五种解法（第 3—6 章）</div>
变量分离（$\int\frac{dy}{\varphi(y)}=\int f(x)dx$）→ 一阶线性 + 常数变易（$y=e^{-\int P}\left[\int Qe^{\int P}+C\right]$）→ 恰当方程 + 积分因子（$\frac{\partial M}{\partial y}=\frac{\partial N}{\partial x}$，$\mu$ 的两种求法）→ 隐式方程与参数表示（$y=f(x,y')$、$x=f(y,y')$、$y=f(x,y')$ 三种）。
</div>

<div class="callout callout-key"><div class="callout-title">第四层：理论保证（第 7—9 章）</div>
Picard 逐步逼近、Lipschitz 条件、存在唯一性定理、解的延拓、Gronwall 不等式、初值依赖性、奇解与包络。
</div>

<div class="callout callout-key"><div class="callout-title">第五层：数值解（第 10 章）</div>
离散化、Euler、改进 Euler、RK4、局部截断误差、整体误差阶、稳定性。
</div>

<div class="callout callout-key"><div class="callout-title">第六层：高阶线性方程的工具（第 11 章）</div>
复数与欧拉公式、多项式重根、行列式与范德蒙、线性无关、莱布尼兹公式。这一层是第 13—15 章的地基。
</div>

<div class="callout callout-key"><div class="callout-title">第七层：高阶线性方程的结构（第 12 章）</div>
算子 $L$、叠加原理、朗斯基行列式、基本解组、通解结构（齐次 $n$ 维、非齐次加特解）、$n$ 阶常数变易法。
</div>

<div class="callout callout-key"><div class="callout-title">第八层：常系数方程的解法（第 14—15 章）</div>
特征方程 $F(\lambda)=0$、单根/复根/重根三种情形、待定系数法两种类型（$P_m e^{\lambda t}$ 与 $[A\cos+B\sin]e^{\alpha t}$）。
</div>

<div class="callout callout-key"><div class="callout-title">第九层：变系数与不可解情形（第 15 章）</div>
三类降阶（缺 $x$、缺 $t$、已知解）、刘维尔公式、幂级数解法。
</div>

<div class="callout callout-key"><div class="callout-title">主干：应用（第 16 章）</div>
从"密度变化 = 流入 − 流出"建模到一阶线性方程，解析解、三种数值方案、误差阶验证、工程结论。
</div>

<h3>17.2 各章之间的关键衔接</h3>
<table>
<colgroup><col style="width:26%"><col style="width:37%"><col style="width:37%"></colgroup>
<thead><tr><th>从</th><th>靠什么接上</th><th>接到哪</th></tr></thead>
<tbody>
<tr><td>第 1 章导数</td><td>$dy=y'dx$ 让 $y'=\frac{dy}{dx}$ 可以当分数拆</td><td>第 3 章分离变量</td></tr>
<tr><td>第 4 章一阶常数变易</td><td>"把常数换成函数"这一手</td><td>第 12.8 节 $n$ 阶常数变易</td></tr>
<tr><td>第 7 章唯一性</td><td>"初值相同则解相同"</td><td>第 12.5 节 $W\neq0$ 的证明</td></tr>
<tr><td>第 11 章欧拉公式</td><td>$e^{i\theta}=\cos+i\sin$</td><td>第 13.5 节复根 → 实值解</td></tr>
<tr><td>第 11 章范德蒙</td><td>$\prod(\lambda_j-\lambda_i)\neq0$</td><td>第 13.4 节单根解组无关</td></tr>
<tr><td>第 11 章重根判别</td><td>$F=F'=\cdots=0$</td><td>第 14.2 节 $k$ 决定乘几个 $t$</td></tr>
<tr><td>第 11 章莱布尼兹</td><td>$(Pe^{\lambda t})^{(n)}$ 展开</td><td>第 14.2 节核心公式 (14.3)</td></tr>
<tr><td>第 13 章齐次通解</td><td>齐次部分</td><td>第 14 章非齐次 = 齐次 + 特解</td></tr>
<tr><td>第 10 章误差阶</td><td>$O(h^p)$</td><td>第 16 章三种方法的比较</td></tr>
</tbody>
</table>

<h3>17.3 公式速查</h3>

<h4>一阶方程</h4>
<table>
<colgroup><col style="width:26%"><col style="width:44%"><col style="width:30%"></colgroup>
<thead><tr><th>类型</th><th>解法</th><th>注意</th></tr></thead>
<tbody>
<tr><td>可分离 $y'=f(x)\varphi(y)$</td><td>$\int\frac{dy}{\varphi(y)}=\int f(x)dx+C$</td><td>$\varphi(y)=0$ 的常数解可能漏掉</td></tr>
<tr><td>一阶线性 $y'+P(x)y=Q(x)$</td><td>$y=e^{-\int P}\left[\int Qe^{\int P}dx+C\right]$</td><td>积分因子 $e^{\int P}$</td></tr>
<tr><td>恰当 $Mdx+Ndy=0$</td><td>$\frac{\partial M}{\partial y}=\frac{\partial N}{\partial x}$，求 $u$ 使 $du=Mdx+Ndy$</td><td>不恰当时找积分因子 $\mu$</td></tr>
<tr><td>齐次 $y'=\varphi(y/x)$</td><td>令 $u=y/x$，化为可分离</td><td>$x\neq0$</td></tr>
<tr><td>伯努利 $y'+Py=Qy^n$</td><td>令 $z=y^{1-n}$</td><td>$n\neq0,1$</td></tr>
</tbody>
</table>

<h4>高阶线性</h4>
<table>
<colgroup><col style="width:26%"><col style="width:44%"><col style="width:30%"></colgroup>
<thead><tr><th>情形</th><th>结论</th><th>备注</th></tr></thead>
<tbody>
<tr><td>齐次通解</td><td>$x=c_1x_1+\cdots+c_nx_n$</td><td>$x_i$ 是基本解组</td></tr>
<tr><td>非齐次通解</td><td>$x=x_h+\tilde x$</td><td>$\tilde x$ 是任一特解</td></tr>
<tr><td>常数变易</td><td>$x=\sum\gamma_ix_i+\sum x_i\int\varphi_i dt$</td><td>解 $W$ 为系数的方程组</td></tr>
<tr><td>特征方程</td><td>$F(\lambda)=\lambda^n+a_1\lambda^{n-1}+\cdots+a_n=0$</td><td>$e^{\lambda t}$ 是解 ⇔ 根</td></tr>
<tr><td>单根</td><td>$e^{\lambda_jt}$</td><td>范德蒙保证无关</td></tr>
<tr><td>共轭复根 $\alpha\pm i\beta$</td><td>$e^{\alpha t}\cos\beta t$、$e^{\alpha t}\sin\beta t$</td><td>取实部虚部</td></tr>
<tr><td>$k$ 重实根</td><td>$e^{\lambda t},te^{\lambda t},\dots,t^{k-1}e^{\lambda t}$</td><td>变量替换证明</td></tr>
<tr><td>$k$ 重复根</td><td>$t^le^{\alpha t}\cos\beta t$、$t^le^{\alpha t}\sin\beta t$</td><td>$l=0,\dots,k-1$</td></tr>
<tr><td>待定系数 I</td><td>$\tilde x=t^kP_m(t)e^{\lambda t}$</td><td>$k$ 为 $\lambda$ 的重数</td></tr>
<tr><td>待定系数 II</td><td>$\tilde x=t^k[P\cos\beta t+Q\sin\beta t]e^{\alpha t}$</td><td>$k$ 为 $\alpha+i\beta$ 的重数</td></tr>
<tr><td>刘维尔公式</td><td>$x_2=x_1\int\frac{e^{-\int p}}{x_1^2}dt$</td><td>已知一个解求第二个</td></tr>
</tbody>
</table>

<h4>数值方法</h4>
<table>
<colgroup><col style="width:22%"><col style="width:52%"><col style="width:26%"></colgroup>
<thead><tr><th>方法</th><th>公式</th><th>阶</th></tr></thead>
<tbody>
<tr><td>Euler</td><td>$y_{n+1}=y_n+hf(t_n,y_n)$</td><td>1</td></tr>
<tr><td>改进 Euler</td><td>$y_{n+1}=y_n+\frac h2[f(t_n,y_n)+f(t_{n+1},y_n+hf_n)]$</td><td>2</td></tr>
<tr><td>RK4</td><td>$y_{n+1}=y_n+\frac h6(k_1+2k_2+2k_3+k_4)$</td><td>4</td></tr>
</tbody>
</table>

<h3>17.4 跨章自测（十题）</h3>
<div class="qa-item"><div class="qa-q">1. 判断 $y'=\dfrac{y}{x}+\tan\dfrac{y}{x}$ 的类型并求解。</div><div class="qa-a">齐次方程（右端只含 $y/x$）。令 $u=y/x$，$y=xu$，$y'=u+xu'$，代入得 $u+xu'=u+\tan u$，即 $xu'=\tan u$。分离：$\cot u\,du=\frac{dx}{x}$，积分 $\ln|\sin u|=\ln|x|+C$，$\sin u=Cx$。回代 $u=y/x$：$\sin(y/x)=Cx$。</div></div>
<div class="qa-item"><div class="qa-q">2. $y'=3y^{2/3}$ 在 $y(0)=0$ 处解唯一吗？</div><div class="qa-a">不唯一。$f(y)=3y^{2/3}$ 在 $y=0$ 处不满足 Lipschitz（$\partial f/\partial y=2y^{-1/3}\to\infty$）。$y=0$ 是一个解；$y=t^3$ 也是解（$y'=3t^2$，$3y^{2/3}=3t^2$，且 $y(0)=0$）。所以过 $(0,0)$ 至少有两个解，唯一性失效。</div></div>
<div class="qa-item"><div class="qa-q">3. 求 $x'''-6x''+11x'-6x=0$ 的通解。</div><div class="qa-a">特征方程 $\lambda^3-6\lambda^2+11\lambda-6=0$。试 $\lambda=1$：$1-6+11-6=0$ ✓。分解 $(λ-1)(λ^2-5λ+6)=(λ-1)(λ-2)(λ-3)$。三个单根，通解 $x=c_1e^t+c_2e^{2t}+c_3e^{3t}$。</div></div>
<div class="qa-item"><div class="qa-q">4. 求 $x''+2x'+5x=0$ 的通解，并说明振荡是否会衰减。</div><div class="qa-a">$\lambda^2+2\lambda+5=0$，$\lambda=-1\pm2i$（$\alpha=-1,\beta=2$）。通解 $x=e^{-t}(c_1\cos2t+c_2\sin2t)$。$e^{-t}$ 衰减，所以振荡会衰减，最终趋于 0。</div></div>
<div class="qa-item"><div class="qa-q">5. $x''+4x'+4x=te^{-2t}$，特解怎么猜？</div><div class="qa-a">特征根 $\lambda=-2$ 是二重根，右端 $P_1(t)e^{-2t}$，$m=1$、$k=2$。猜 $\tilde x=t^2(at+b)e^{-2t}$，展开为 $(at^3+bt^2)e^{-2t}$。</div></div>
<div class="qa-item"><div class="qa-q">6. 已知 $x_1=e^t$ 是 $x''-2x'+x=0$ 的解，求第二个解。</div><div class="qa-a">标准形 $p=-2$，$e^{-\int p}=e^{2t}$。代入刘维尔公式：$x_2=e^t\int\frac{e^{2t}}{e^{2t}}dt=e^t\int1\,dt=te^t$。正是二重根对应的第二个解。</div></div>
<div class="qa-item"><div class="qa-q">7. 用 Taylor 展开说明 Euler 法的局部误差为什么是 $O(h^2)$。</div><div class="qa-a">真解 $y(t_{n+1})=y(t_n)+hy'(t_n)+\frac{h^2}{2}y''(\xi)$。Euler 用 $hf(t_n,y_n)=hy'(t_n)$ 代替前两项，差的正是 $\frac{h^2}{2}y''(\xi)$，量级 $h^2$。</div></div>
<div class="qa-item"><div class="qa-q">8. 若 $h$ 减半，RK4 的终点误差大约变成原来的几分之一？</div><div class="qa-a">$2^4=16$ 分之一。实测 17.6 分之一，略高于理论值，因为 $h=0.2$ 时还有高阶项未完全进入渐近区。</div></div>
<div class="qa-item"><div class="qa-q">9. 为什么非齐次方程的通解一定要加一个特解，而不是加任意一个非齐次解？</div><div class="qa-a">"加任意一个非齐次解"和"加特解"是同一件事：任何非齐次解都可以当特解。定理 13.7 的证明里，任给非齐次解 $x^*$，$x^*-\bar x$ 是齐次解，所以 $x^*$ 也能写成 $\sum c_ix_i+\bar x$。区别只在于选哪个 $\bar x$ 写起来简单。</div></div>
<div class="qa-item"><div class="qa-q">10. 无人机走廊案例里，若把 $a$ 改成 0 会怎样？</div><div class="qa-a">$a=0$ 时方程变成 $\rho'=\sin t+0.6\sin3t$，直接积分 $\rho=1-\cos t+0.2(1-\cos3t)$。密度在 $[0,2.4]$ 之间周期振荡，没有消散机制，初始的 1 不会被"漏掉"，拥堵只增不减。建模上说明 $a&gt;0$ 是系统稳定的必要条件。</div></div>

<h3>17.5 学习路径建议</h3>
<div class="callout callout-tip"><div class="callout-title">三轮法</div>
<strong>第一轮</strong>（打通链条）：第 1 章 → 第 2 章 → 第 3、4 章 → 第 7 章。目标：能判断类型、能解分离变量与一阶线性、知道解为什么存在。<br>
<strong>第二轮</strong>（补齐技巧）：第 5、6 章 → 第 10 章。目标：会积分因子、会参数表示、会三种数值方法。<br>
<strong>第三轮</strong>（高阶）：第 11 章 → 第 12 章 → 第 14、15 章 → 第 15 章。目标：能独立推出特征方程的三种情形、能猜对特解形式。<br>
<strong>收尾</strong>：第 17、18 章。用一道综合题检验全链。
</div>

<div class="callout callout-tip"><div class="callout-title">每章过关标准</div>不看答案能复述这一章的三个核心结论；能独立做对章末自测的 4 道题；能说出这一章的方法"什么时候不能用"。三条都做到再进下一章。</div>

<h3>17.6 下一步学什么</h3>
<p>本课覆盖到一阶方程、高阶线性方程、数值解。往后四个方向：</p>
<ul>
<li><strong>线性微分方程组</strong>（课件第五章）：$X'=A(t)X+F(t)$，基解矩阵、矩阵指数 $e^{At}$、特征值与 Jordan 形。前置是线性代数（矩阵、特征值、对角化）。</li>
<li><strong>稳定性理论</strong>：平衡点、相平面、Lyapunov 函数、极限环。前置是多元微积分与拓扑初步。</li>
<li><strong>偏微分方程</strong>：热方程、波动方程、拉普拉斯方程。前置是多元微积分、傅里叶级数。</li>
<li><strong>数值进阶</strong>：刚性方程、隐式方法（Backward Euler、BDF）、自适应步长、稳定性区域。</li>
</ul>

<div class="chapter-nav"></div>
</section>
"""
