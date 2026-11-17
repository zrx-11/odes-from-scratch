# -*- coding: utf-8 -*-
CH_J = r"""
<section class="chapter" id="reduction" style="display:none">
<div class="breadcrumb"></div>
<h2><span class="num">15</span>降阶与幂级数</h2>
<p class="lead">变系数的高阶方程没有通用解法。能做的只有一件事：找变换把阶数降下来。这一章讲三类可降阶的方程，以及解不出来时用幂级数硬展开的办法。对应课件 chapter4-3。</p>

<div class="callout callout-tip">
<div class="callout-title">生活直觉：少一个变量就少一阶</div>方程里没出现 $x$，说明 $x$ 本身不影响"导数怎么变"，可以把 $x'$ 当成新的未知函数，二阶就变一阶。方程里没出现 $t$，说明规律与时间无关，可以把 $x$ 当自变量、$x'$ 当未知函数，同样降一阶。已知一个解，相当于知道了一条参考轨道，把解写成"参考轨道 × 修正因子"，修正因子满足更低阶的方程。
</div>

<div class="callout callout-warn"><div class="callout-title">前置知识</div>第 12 章的齐次线性方程结构、朗斯基行列式；第 13 章的特征方程；第 3 章的变量分离法。</div>

<h3>15.1 一般高阶方程没有通用解法</h3>
<p>$n$ 阶方程一般写成</p>
<div class="formula">$$F\left(t,x,x',\dots,x^{(n)}\right)=0 \tag{15.1}$$</div>
<p>除了常系数线性方程（第 14、15 章）和少数特殊类型，没有统一的求解公式。实际做法是"降阶"：用变换把 $n$ 阶化成 $n-1$ 阶，再化到一阶，最后用第 2 至 6 章的方法解。降一阶就能解的情形有三类。</p>

<h3>15.2 类型一：方程不显含 $x$ 及其低阶导数</h3>
<p>更一般地，设方程只含 $x^{(k)}$ 及更高阶导数，不含 $x,x',\dots,x^{(k-1)}$：</p>
<div class="formula">$$F\left(t,x^{(k)},x^{(k+1)},\dots,x^{(n)}\right)=0,\qquad 1\le k\le n \tag{15.2}$$</div>
<p>令</p>
<div class="formula">$$x^{(k)}=y \tag{15.3}$$</div>
<p>则 $x^{(k+1)}=y'$，…，$x^{(n)}=y^{(n-k)}$。代入 (15.2)，得到关于 $y$ 的 $n-k$ 阶方程：</p>
<div class="formula">$$F\left(t,y,y',\dots,y^{(n-k)}\right)=0 \tag{15.4}$$</div>
<p>解出 $y=\varphi(t,c_1,\dots,c_{n-k})$ 后，再对 $x^{(k)}=y$ 积分 $k$ 次，得 $x$，其中又添 $k$ 个常数，共 $n$ 个。</p>

<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">$\dfrac{d^5x}{dt^5}-\dfrac{1}{t}\dfrac{d^4x}{dt^4}=0$</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>方程只含四阶、五阶导数，不含 $x$ 及低阶项，$k=4$。令 $x^{(4)}=y$，则 $x^{(5)}=y'$：</p>
<div class="formula">$$y'-\frac{1}{t}y=0$$</div>
<p>这是一阶线性齐次方程。分离变量：$\dfrac{dy}{y}=\dfrac{dt}{t}$，积分得 $\ln|y|=\ln|t|+C$，$y=ct$。</p>
<p>回代 $x^{(4)}=ct$，连续积分四次：</p>
<div class="formula">$$x^{(3)}=\frac{c}{2}t^2+c_1,\quad x''=\frac{c}{6}t^3+c_1t+c_2,\quad x'=\frac{c}{24}t^4+\frac{c_1}{2}t^2+c_2t+c_3$$</div>
<div class="formula">$$x=\frac{c}{120}t^5+\frac{c_1}{6}t^3+\frac{c_2}{2}t^2+c_3t+c_4$$</div>
<p>把常数重命名（$c/120\to c_1$ 等），写成</p>
<div class="formula">$$x=c_1t^5+c_2t^3+c_3t^2+c_4t+c_5$$</div>
<p>与课件一致。验算：$x^{(4)}=120c_1t$，$x^{(5)}=120c_1$，代入 $\dfrac{1}{t}x^{(4)}=120c_1$，相减为零 ✓。注意 $t=0$ 是奇点，解只在 $t\neq0$ 上成立。</p>
</div></div>
</div>

<h3>15.3 类型二：方程不显含自变量 $t$</h3>
<p>方程形如</p>
<div class="formula">$$F\left(x,x',\dots,x^{(n)}\right)=0 \tag{15.5}$$</div>
<p>没有 $t$ 出现。这时把 $x$ 当自变量、$x'$ 当未知函数：</p>
<div class="formula">$$x'=y,\qquad y=y(x) \tag{15.6}$$</div>
<p>关键是算高阶导数。$x''=\dfrac{dy}{dt}$，而 $\dfrac{dy}{dt}=\dfrac{dy}{dx}\dfrac{dx}{dt}=y\dfrac{dy}{dx}$：</p>
<div class="formula">$$x''=y\frac{dy}{dx}$$</div>
<p>再求一次：</p>
<div class="formula">$$x'''=\frac{d}{dt}\left(y\frac{dy}{dx}\right)=\frac{dx}{dt}\cdot\frac{d}{dx}\left(y\frac{dy}{dx}\right)=y\left[\left(\frac{dy}{dx}\right)^2+y\frac{d^2y}{dx^2}\right]$$</div>
<p>即</p>
<div class="formula">$$x'''=y\left(\frac{dy}{dx}\right)^2+y^2\frac{d^2y}{dx^2}$$</div>
<p>一般地，$x^{(k)}$ 可以只用 $y,\dfrac{dy}{dx},\dots,\dfrac{d^{k-1}y}{dx^{k-1}}$ 表示（数学归纳法可证：每次对 $t$ 求导等于"先对 $x$ 求导再乘 $y$"，只增加 $y$ 的一阶导的幂次与 $y$ 的高一阶导）。代入 (15.5) 得</p>
<div class="formula">$$G\left(x,y,\frac{dy}{dx},\dots,\frac{d^{n-1}y}{dx^{n-1}}\right)=0 \tag{15.7}$$</div>
<p>这是 $n-1$ 阶方程，比原来低一阶。</p>

<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">$xx''+(x')^2=0$</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>方程里没有 $t$，属类型二。令 $x'=y$，$x''=y\dfrac{dy}{dx}$，代入：</p>
<div class="formula">$$x\,y\frac{dy}{dx}+y^2=0$$</div>
<p>提公因子 $y$：$y\left(x\dfrac{dy}{dx}+y\right)=0$。</p>
<p>第一种可能 $y=0$，即 $x'=0$，$x=C$（常数解）。</p>
<p>第二种可能 $x\dfrac{dy}{dx}+y=0$。改写为 $\dfrac{dy}{y}=-\dfrac{dx}{x}$，积分：$\ln|y|=-\ln|x|+C$，$y=\dfrac{c}{x}$。</p>
<p>回代 $x'=y=\dfrac{c}{x}$，即 $x\,dx=c\,dt$。积分：</p>
<div class="formula">$$\frac{x^2}{2}=ct+c_1\quad\Longrightarrow\quad x^2=c_1t+c_2$$</div>
<p>（把 $2c$ 并入 $c_1$。）验算：$x^2=c_1t+c_2$ 两边求导得 $2xx'=c_1$，再求导 $2(x')^2+2xx''=0$，即 $xx''+(x')^2=0$ ✓。</p>
<p>所以通解为 $x^2=c_1t+c_2$，其中 $c_1\neq0$ 时是抛物线族，$c_1=0$ 时退化为常数解。</p>
</div></div>
</div>

<h3>15.4 类型三：已知 $k$ 个线性无关解，降 $k$ 阶</h3>
<p>齐次线性方程</p>
<div class="formula">$$x^{(n)}+a_1(t)x^{(n-1)}+\cdots+a_n(t)x=0 \tag{15.8}$$</div>
<p>若已知它的一个非零解 $x_1$，可以降一阶。做法是设</p>
<div class="formula">$$x=x_1(t)\int u(t)\,dt \tag{15.9}$$</div>
<p>也就是把解写成"已知解 × 待定因子"，$u$ 是待求函数。这个设定的好处是：$x_1$ 本身对应 $u=0$（积分是常数），新解由 $u$ 提供。</p>

<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">二阶情形：导出 $u$ 的一阶方程</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>取 $n=2$，方程 $x''+p(t)x'+q(t)x=0$。设 $x=x_1\int u\,dt$。先算导数：</p>
<div class="formula">$$x'=x_1'\int u\,dt+x_1u$$</div>
<div class="formula">$$x''=x_1''\int u\,dt+2x_1'u+x_1u'$$</div>
<p>（第二式：对第一项求导得多一项 $x_1'u$，对 $x_1u$ 求导得 $x_1'u+x_1u'$，合并 $x_1'u$ 得 $2x_1'u$。）</p>
<p>代入方程，按 $\int u\,dt$、$u$、$u'$ 归并：</p>
<div class="formula">$$\left[x_1''+px_1'+qx_1\right]\int u\,dt+\left[2x_1'+px_1\right]u+x_1u'=0$$</div>
<p>第一项方括号里是 $x_1$ 代入方程的结果，$x_1$ 是解，所以为零。剩下</p>
<div class="formula">$$x_1u'+\left(2x_1'+px_1\right)u=0 \tag{15.10}$$</div>
<p>这是关于 $u$ 的一阶线性方程，只含 $u'$ 与 $u$，阶数从 2 降到 1。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">解</span><span class="derive-step-title">分离变量求出 $u$，再求第二个解</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>把 (15.10) 除以 $x_1u$：</p>
<div class="formula">$$\frac{u'}{u}=-\left(\frac{2x_1'}{x_1}+p\right)$$</div>
<p>积分：$\ln|u|=-\ln x_1^2-\int p\,dt+C$。取指数：</p>
<div class="formula">$$u=C\frac{e^{-\int p\,dt}}{x_1^2} \tag{15.11}$$</div>
<p>再积分一次得修正因子，代回 (15.9)：</p>
<div class="formula">$$x_2=x_1(t)\int\frac{e^{-\int p(t)\,dt}}{x_1^2(t)}\,dt \tag{15.12}$$</div>
<p>这就是已知一个解时求第二个解的公式，叫刘维尔公式。</p>
</div></div>
</div>

<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">已知 $x_1=t$ 是 $t^2x''-2x=0$ 的解，求另一个</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>先把方程化成标准形（最高阶系数为 1）：$x''-\dfrac{2}{t^2}x=0$，于是 $p(t)=0$。</p>
<p>验算 $x_1=t$：$x_1''=0$，$-\dfrac{2}{t^2}\cdot t=-\dfrac{2}{t}\neq0$。这里算错了，$x_1=t$ 不满足。换一个：$x_1=t^2$，$x_1''=2$，$-\dfrac{2}{t^2}\cdot t^2=-2$，相加为零 ✓。所以 $x_1=t^2$。</p>
<p>代入 (15.12)，$p=0$，$e^{-\int p}=1$：</p>
<div class="formula">$$x_2=t^2\int\frac{1}{t^4}\,dt=t^2\left(-\frac{1}{3t^3}\right)=-\frac{1}{3t}$$</div>
<p>取 $x_2=1/t$（常数因子不影响）。验算：$x_2''=2/t^3$，$-\dfrac{2}{t^2}\cdot\dfrac1t=-\dfrac{2}{t^3}$，相加为零 ✓。</p>
<p>通解：$x=c_1t^2+\dfrac{c_2}{t}$。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">推广</span><span class="derive-step-title">已知 $k$ 个解的情况</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>设已知 $k$ 个线性无关解 $x_1,\dots,x_k$。依次做 $k$ 次同类变换，每次降一阶，最终得到一个 $n-k$ 阶的齐次线性方程。</p>
<p>二阶情形对应 $k=1$，降为 1 阶；三阶已知 2 个解，降为 1 阶。实际操作时，先把 $k$ 个解的信息用"伴随方程"或朗斯基行列式压缩，再解剩下的 $n-k$ 阶方程。</p>
<p>注意：变换后的方程仍是齐次的（不含自由项），因为每一步只是代换 $x=x_j\int u$，没有引入非齐次项。</p>
</div></div>
</div>

<h3>15.5 幂级数解法：解不出来就展开</h3>
<p>变系数方程在普通点附近，解可以写成幂级数。以</p>
<div class="formula">$$x''+x=0 \tag{15.13}$$</div>
<p>为例演示（这个方程本来能用特征方程解，选它只是为了看清步骤）。</p>

<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">①</span><span class="derive-step-title">设解为幂级数</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>在 $t=0$ 附近设</p>
<div class="formula">$$x(t)=\sum_{n=0}^{\infty}a_nt^n=a_0+a_1t+a_2t^2+\cdots$$</div>
<p>求导两次（逐项求导，收敛半径内合法）：</p>
<div class="formula">$$x''=\sum_{n=2}^{\infty}n(n-1)a_nt^{n-2}=2a_2+6a_3t+12a_4t^2+\cdots$$</div>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">②</span><span class="derive-step-title">代入，比较同次幂</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>$x''+x=0$：把两个级数按 $t^k$ 对齐。$x$ 的 $t^k$ 项系数是 $a_k$；$x''$ 的 $t^k$ 项来自 $n=k+2$，系数 $(k+2)(k+1)a_{k+2}$。于是</p>
<div class="formula">$$(k+2)(k+1)a_{k+2}+a_k=0,\qquad k=0,1,2,\dots$$</div>
<p>这是递推关系：</p>
<div class="formula">$$a_{k+2}=-\frac{a_k}{(k+2)(k+1)}$$</div>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">③</span><span class="derive-step-title">解递推，得到两组解</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>偶数项由 $a_0$ 决定：$a_2=-\dfrac{a_0}{2}$，$a_4=\dfrac{a_0}{24}$，$a_6=-\dfrac{a_0}{720}$，通项 $a_{2m}=\dfrac{(-1)^m}{(2m)!}a_0$。</p>
<p>奇数项由 $a_1$ 决定：$a_3=-\dfrac{a_1}{6}$，$a_5=\dfrac{a_1}{120}$，通项 $a_{2m+1}=\dfrac{(-1)^m}{(2m+1)!}a_1$。</p>
<p>于是</p>
<div class="formula">$$x=a_0\left(1-\frac{t^2}{2!}+\frac{t^4}{4!}-\cdots\right)+a_1\left(t-\frac{t^3}{3!}+\frac{t^5}{5!}-\cdots\right)$$</div>
<p>两个括号正是 $\cos t$ 与 $\sin t$ 的泰勒展开。所以 $x=a_0\cos t+a_1\sin t$，与第 13 章用特征方程得到的结果一致。</p>
</div></div>
</div>

<div class="callout callout-tip"><div class="callout-title">幂级数法的适用范围</div>在"普通点"（系数在该点解析）附近，$n$ 阶线性方程一定有 $n$ 个形如 $\sum a_kt^k$ 的解，收敛半径至少到最近的奇点。在"奇点"附近要用广义幂级数（Frobenius 方法），形式多一个 $t^r$ 因子。本课不展开，只要求知道：级数法是变系数方程的主要出路之一，代价是要算递推、讨论收敛。</div>

<h3>15.6 本章小结与自测</h3>
<table>
<colgroup><col style="width:26%"><col style="width:36%"><col style="width:38%"></colgroup>
<thead><tr><th>方程特征</th><th>变换</th><th>降阶结果</th></tr></thead>
<tbody>
<tr><td>不含 $x,x',\dots,x^{(k-1)}$</td><td>$y=x^{(k)}$</td><td>$n-k$ 阶</td></tr>
<tr><td>不含 $t$</td><td>$x'=y$，$x$ 作自变量</td><td>$n-1$ 阶</td></tr>
<tr><td>已知 $k$ 个无关解</td><td>$x=x_j\int u$ 逐次变换</td><td>$n-k$ 阶</td></tr>
</tbody>
</table>

<div class="qa-item"><div class="qa-q">1. $x''=f(x)$ 应该用哪类降阶？</div><div class="qa-a">方程不含 $t$，用类型二：令 $x'=y$，$x''=y\dfrac{dy}{dx}$，得 $y\dfrac{dy}{dx}=f(x)$，分离变量 $\int y\,dy=\int f(x)\,dx$，即 $\dfrac12(x')^2=F(x)+C$，再开方积分。这是能量守恒的形式。</div></div>
<div class="qa-item"><div class="qa-q">2. $y'''-2y''=0$ 用哪类降阶最快？</div><div class="qa-a">不含 $y$ 与 $y'$，$k=2$，令 $y''=u$，得 $u'-2u=0$，$u=ce^{2t}$，再积两次：$y=c_1e^{2t}+c_2t+c_3$。也可用特征方程 $(\lambda^3-2\lambda^2)=\lambda^2(\lambda-2)=0$，得同样结果。</div></div>
<div class="qa-item"><div class="qa-q">3. 已知 $x_1=\cos t$ 是 $x''+x=0$ 的解，用刘维尔公式求第二个解。</div><div class="qa-a">标准形 $p=0$，$e^{-\int p}=1$，代入 (15.12)：$x_2=\cos t\int\dfrac{1}{\cos^2t}\,dt=\cos t\cdot\tan t=\sin t$。得到 $\sin t$，与预期一致。</div></div>
<div class="qa-item"><div class="qa-q">4. 为什么类型二的变换要求 $x'=y$ 中的 $y$ 看成 $x$ 的函数，而不是 $t$ 的函数？</div><div class="qa-a">因为方程里没有 $t$，把 $x$ 当自变量后，$t$ 不再出现在方程中，$x$ 与 $y$ 是仅有的两个变量。若坚持 $y=y(t)$，就还得处理 $t$，降阶没有发生。变换的实质是换自变量。</div></div>
<div class="qa-item"><div class="qa-q">5. 幂级数解法中，为什么 $a_0$ 与 $a_1$ 可以任意取？</div><div class="qa-a">因为二阶方程的通解含两个任意常数。在 $t=0$ 处，$x(0)=a_0$、$x'(0)=a_1$，正好对应两个初值。递推关系把后面的系数全部由这两个定下来，符合"初值决定解"的唯一性定理。</div></div>

<div class="chapter-nav"></div>
</section>
"""

CH_K = r"""
<section class="chapter" id="case-drone" style="display:none">
<div class="breadcrumb"></div>
<h2><span class="num">16</span>应用案例：无人机走廊拥堵</h2>
<p class="lead">把前面所有工具用到一道真实场景题上：城市低空无人机物流走廊里，一个关键航段的密度怎么随时间变化，拥堵会不会自己消散。题目给的是一个一阶线性方程，但要求做解析解、三种数值方法、误差阶验证，正好把第 4 章和第 10 章串起来。对应课件 3.4 应用实操案例。</p>

<div class="callout callout-tip">
<div class="callout-title">生活直觉：浴缸里一边进水一边漏水</div>密度 $\rho$ 像一个水位：订单到达是"进水"（两个高峰，正弦波形），航段通行能力是"漏水"（漏得越快水位越低，漏速与水位成正比）。水位最终稳在哪个高度，取决于进水与漏水什么时候打平。这道题就是给这个浴缸算水位曲线。
</div>

<div class="callout callout-warn"><div class="callout-title">前置知识</div>第 4 章的一阶线性方程与积分因子；第 8 章的延拓（全局存在）；第 10 章的 Euler、改进 Euler、RK4 与误差阶。</div>

<h3>16.1 题目背景</h3>
<p>某超大城市在核心城区规划一条无人机物流走廊，走廊内设若干起降点，无人机沿固定航路往返。订单量增长后出现"空中拥堵"：局部航段密度升高，后续无人机减速、悬停，拥堵沿航路向上游传播。</p>
<p>运营方要回答：当订单到达率出现双高峰周期波动（午间、傍晚）时，某关键航段的密度如何演化？拥堵是消散还是累积？不同数值方案能否以足够精度刻画这一过程？</p>

<h3>16.2 建模：为什么是一阶线性方程</h3>
<p>设 $\rho(t)$ 为该航段在时刻 $t$ 的无人机密度（架/公里），$t$ 为归一化时间（分钟），考察 $t\in[0,2]$。</p>
<p>密度的变化率 = 流入率 − 流出率。题目给出：</p>
<ul>
<li>流出（拥堵消散）与密度成正比：$-a\rho(t)$，$a&gt;0$ 是平均消散强度；</li>
<li>流入是双高峰周期波动：$A_1\sin(\omega_1t)+A_2\sin(\omega_2t)$。</li>
</ul>
<p>于是</p>
<div class="formula">$$\rho'(t)=-a\rho(t)+A_1\sin(\omega_1t)+A_2\sin(\omega_2t),\qquad t\in[0,2] \tag{16.1}$$</div>
<p>初值 $\rho(0)=\rho_0$。基准实例取 $a=2$、$A_1=1$、$\omega_1=1$、$A_2=0.6$、$\omega_2=3$、$\rho_0=1$：</p>
<div class="formula">$$\begin{cases}\rho'(t)=-2\rho(t)+\sin t+0.6\sin 3t,\\ \rho(0)=1\end{cases}\qquad t\in[0,2] \tag{16.2}$$</div>

<h3>16.3 任务一：存在唯一性与延拓</h3>
<p>右端 $f(t,\rho)=-2\rho+\sin t+0.6\sin 3t$ 在带状区域 $[0,2]\times\mathbb{R}$ 上连续，且关于 $\rho$ 满足 Lipschitz 条件：</p>
<div class="formula">$$|f(t,\rho_1)-f(t,\rho_2)|=|-2(\rho_1-\rho_2)|=2|\rho_1-\rho_2|$$</div>
<p>Lipschitz 常数 $L=2$。由第 7 章的存在唯一性定理，初值问题在 $t=0$ 附近有唯一解；由第 8 章的延拓定理，因为 $f$ 在整个 $\mathbb{R}$ 上对 $\rho$ 满足 Lipschitz 且不爆破，解可以延拓到整个区间 $[0,2]$（事实上可延拓到 $[0,\infty)$）。</p>
<p>结论：解存在、唯一、可延拓到整个考察区间。数值方法有明确的对象。</p>

<h3>16.4 解析解</h3>
<p>方程是一阶线性非齐次，用第 4 章的积分因子法。标准形 $\rho'+2\rho=\sin t+0.6\sin3t$，积分因子</p>
<div class="formula">$$\mu(t)=e^{\int2\,dt}=e^{2t}$$</div>
<p>两边乘 $\mu$，左边凑成 $(\rho e^{2t})'$：</p>
<div class="formula">$$\left(\rho e^{2t}\right)'=e^{2t}\left(\sin t+0.6\sin3t\right)$$</div>
<p>从 $0$ 积到 $t$，用初值 $\rho(0)=1$：</p>
<div class="formula">$$\rho(t)e^{2t}-1=\int_0^t e^{2s}\sin s\,ds+0.6\int_0^t e^{2s}\sin3s\,ds \tag{16.3}$$</div>

<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">①</span><span class="derive-step-title">算 $\int e^{2s}\sin s\,ds$</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>用分部积分两次（或查公式 $\int e^{as}\sin bs\,ds=\dfrac{e^{as}(a\sin bs-b\cos bs)}{a^2+b^2}$）。这里 $a=2,b=1$：</p>
<div class="formula">$$\int e^{2s}\sin s\,ds=\frac{e^{2s}(2\sin s-\cos s)}{2^2+1^2}=\frac{e^{2s}(2\sin s-\cos s)}{5}$$</div>
<p>验算：对右边求导，$e^{2s}$ 项提出 2，得 $\frac{2e^{2s}(2\sin s-\cos s)+e^{2s}(2\cos s+\sin s)}{5}=\frac{e^{2s}(4\sin s-2\cos s+2\cos s+\sin s)}{5}=e^{2s}\sin s$ ✓。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">②</span><span class="derive-step-title">算 $\int e^{2s}\sin3s\,ds$</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>同公式，$a=2,b=3$：</p>
<div class="formula">$$\int e^{2s}\sin3s\,ds=\frac{e^{2s}(2\sin3s-3\cos3s)}{4+9}=\frac{e^{2s}(2\sin3s-3\cos3s)}{13}$$</div>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">③</span><span class="derive-step-title">代入上下限，整理</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>把两个积分从 0 到 $t$ 相减。$s=0$ 时：$\sin0=0,\cos0=1$，第一式给 $-1/5$，第二式给 $-3/13$。</p>
<div class="formula">$$\rho e^{2t}=1+\frac{1}{5}\left[e^{2t}(2\sin t-\cos t)+1\right]+\frac{0.6}{13}\left[e^{2t}(2\sin3t-3\cos3t)+3\right]$$</div>
<p>两边除以 $e^{2t}$，逐项整理，与 $t$ 无关的常数项合并到 $e^{-2t}$ 的系数：</p>
<div class="formula">$$\rho(t)=\frac{87}{65}e^{-2t}+\frac{2}{5}\sin t-\frac{1}{5}\cos t+\frac{6}{65}\sin3t-\frac{9}{65}\cos3t \tag{16.4}$$</div>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">验</span><span class="derive-step-title">用初值检查</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>代 $t=0$：$e^0=1$，$\sin0=0$，$\cos0=1$，$\sin0=0$，$\cos0=1$：</p>
<div class="formula">$$\rho(0)=\frac{87}{65}-\frac15-\frac{9}{65}=\frac{87-13-9}{65}=\frac{65}{65}=1$$</div>
<p>与 $\rho(0)=1$ 相符。再代 $t=2$（数值）：$\rho(2)\approx0.31272426$，后面表格的基准值就用这个。</p>
</div></div>
</div>

<div class="callout callout-tip"><div class="callout-title">解的形态</div>四项里只有 $\frac{87}{65}e^{-2t}$ 随时间衰减（约 $1.3385e^{-2t}$），其余是频率 1 与频率 3 的振荡。$t$ 稍大后，指数项消失，密度按 $\frac25\sin t-\frac15\cos t+\frac6{65}\sin3t-\frac9{65}\cos3t$ 周期振荡。前两项合成振幅 $\sqrt{(2/5)^2+(1/5)^2}=\sqrt{5}/5\approx0.447$、相位滞后 $\arctan(1/2)$ 的振荡；后两项振幅 $\sqrt{(6/65)^2+(9/65)^2}=\sqrt{117}/65\approx0.166$。所以长期来看密度在 $[-0.61,0.61]$ 附近摆动，不会无限累积。</div>

<h3>16.5 任务二：三种数值方法</h3>
<p>取步长 $h=0.2$，节点 $t_n=nh$（$n=0,\dots,10$），记 $\rho_n\approx\rho(t_n)$。右端 $f(t,\rho)=-2\rho+\sin t+0.6\sin3t$。</p>

<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">Euler</span><span class="derive-step-title">显式 Euler</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<div class="formula">$$\rho_{n+1}=\rho_n+h f(t_n,\rho_n)$$</div>
<p>一阶精度。每步只算一次 $f$。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">Heun</span><span class="derive-step-title">改进 Euler（预估-校正）</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>先用 Euler 走一步作预估，再用两端斜率的平均作校正：</p>
<div class="formula">$$\bar\rho_{n+1}=\rho_n+hf(t_n,\rho_n),\qquad \rho_{n+1}=\rho_n+\frac{h}{2}\left[f(t_n,\rho_n)+f(t_{n+1},\bar\rho_{n+1})\right]$$</div>
<p>二阶精度。每步算两次 $f$。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">RK4</span><span class="derive-step-title">经典四阶 Runge-Kutta</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<div class="formula">$$\begin{aligned}k_1&=f(t_n,\rho_n)\\ k_2&=f\left(t_n+\tfrac h2,\rho_n+\tfrac h2k_1\right)\\ k_3&=f\left(t_n+\tfrac h2,\rho_n+\tfrac h2k_2\right)\\ k_4&=f\left(t_n+h,\rho_n+hk_3\right)\\ \rho_{n+1}&=\rho_n+\frac h6\left(k_1+2k_2+2k_3+k_4\right)\end{aligned}$$</div>
<p>四阶精度。每步算四次 $f$，用加权平均代替"两端平均"。</p>
</div></div>
</div>

<h3>16.6 数值结果（$h=0.2$）</h3>
<p>下表是实际计算结果，基准为解析解 (16.4)。前四列是四种方案在节点上的值，后三列是绝对误差。</p>
<table>
<colgroup><col style="width:9%"><col style="width:16%"><col style="width:14%"><col style="width:14%"><col style="width:14%"><col style="width:11%"><col style="width:11%"><col style="width:11%"></colgroup>
<thead><tr><th>$t$</th><th>解析解</th><th>Euler</th><th>Heun</th><th>RK4</th><th>Euler 误差</th><th>Heun 误差</th><th>RK4 误差</th></tr></thead>
<tbody>
<tr><td>0.0</td><td>1.000000</td><td>1.000000</td><td>1.000000</td><td>1.000000</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>0.2</td><td>0.718496</td><td>0.600000</td><td>0.733745</td><td>0.718616</td><td>1.18e-1</td><td>1.52e-2</td><td>1.20e-4</td></tr>
<tr><td>0.4</td><td>0.608826</td><td>0.467491</td><td>0.626058</td><td>0.608974</td><td>1.41e-1</td><td>1.72e-2</td><td>1.48e-4</td></tr>
<tr><td>0.6</td><td>0.585279</td><td>0.470223</td><td>0.597533</td><td>0.585404</td><td>1.15e-1</td><td>1.23e-2</td><td>1.25e-4</td></tr>
<tr><td>0.8</td><td>0.582283</td><td>0.511924</td><td>0.587523</td><td>0.582367</td><td>7.04e-2</td><td>5.24e-3</td><td>8.40e-5</td></tr>
<tr><td>1.0</td><td>0.559771</td><td>0.531681</td><td>0.559488</td><td>0.559818</td><td>2.81e-2</td><td>2.83e-4</td><td>4.70e-5</td></tr>
<tr><td>1.2</td><td>0.505085</td><td>0.504237</td><td>0.502673</td><td>0.505109</td><td>8.48e-4</td><td>2.41e-3</td><td>2.40e-5</td></tr>
<tr><td>1.4</td><td>0.429008</td><td>0.435848</td><td>0.428060</td><td>0.429026</td><td>6.84e-3</td><td>9.48e-4</td><td>1.80e-5</td></tr>
<tr><td>1.6</td><td>0.356159</td><td>0.354010</td><td>0.359018</td><td>0.356185</td><td>2.15e-3</td><td>2.86e-3</td><td>2.60e-5</td></tr>
<tr><td>1.8</td><td>0.312339</td><td>0.292781</td><td>0.319264</td><td>0.312376</td><td>1.96e-2</td><td>6.93e-3</td><td>3.70e-5</td></tr>
<tr><td>2.0</td><td>0.312724</td><td>0.277706</td><td>0.321876</td><td>0.312768</td><td>3.50e-2</td><td>9.15e-3</td><td>4.36e-5</td></tr>
</tbody>
</table>

<div class="callout callout-tip"><div class="callout-title">读表要点</div>Euler 的误差不是单调增长，在 $t=1.0\sim1.4$ 附近误差很小，因为这一段解的斜率较平，折线走得准。Heun 在 $t=1.2$ 处反而比 Euler 差，原因是该点 Euler 恰好"蒙对"，不代表方法更好。看总体，看终点，不看单点。</div>

<h3>16.7 任务三：误差阶的数值验证</h3>
<p>取 $h=0.2$ 与 $h=0.1$，算终点 $t=2$ 的绝对误差，看误差缩小多少倍。</p>
<table>
<colgroup><col style="width:22%"><col style="width:24%"><col style="width:24%"><col style="width:30%"></colgroup>
<thead><tr><th>方法</th><th>$h=0.2$ 误差</th><th>$h=0.1$ 误差</th><th>缩小倍数</th></tr></thead>
<tbody>
<tr><td>Euler（1 阶）</td><td>$3.50\times10^{-2}$</td><td>$1.70\times10^{-2}$</td><td>约 2.05（理论 2）</td></tr>
<tr><td>Heun（2 阶）</td><td>$9.15\times10^{-3}$</td><td>$2.09\times10^{-3}$</td><td>约 4.38（理论 4）</td></tr>
<tr><td>RK4（4 阶）</td><td>$4.36\times10^{-5}$</td><td>$2.48\times10^{-6}$</td><td>约 17.6（理论 16）</td></tr>
</tbody>
</table>
<p>缩小倍数的理论值：$p$ 阶方法的误差与 $h^p$ 同阶，$h$ 减半则误差变 $2^p$ 分之一。实测与理论基本吻合；Heun 的 4.38 略高于 4，RK4 的 17.6 略高于 16，因为 $h=0.2$ 还不算渐近区，高阶项有贡献。把 $h$ 再减半会更接近理论值。</p>

<h4>误差要求 $10^{-4}$ 时各方法需要多大步长</h4>
<p>用 $h=0.001$ 的实测数据反推常数：Euler 误差 $1.67\times10^{-4}$（$h=10^{-3}$），近似 $e\approx0.167h$；Heun 误差 $1.91\times10^{-7}$，近似 $e\approx0.191h^2$；RK4 在 $h=0.01$ 时 $2.26\times10^{-10}$，$e\approx0.0226h^4$。</p>
<table>
<colgroup><col style="width:18%"><col style="width:26%"><col style="width:26%"><col style="width:30%"></colgroup>
<thead><tr><th>方法</th><th>误差模型</th><th>解 $e=10^{-4}$ 的 $h$</th><th>区间 $[0,2]$ 所需步数</th></tr></thead>
<tbody>
<tr><td>Euler</td><td>$0.167h$</td><td>$h\approx6.0\times10^{-4}$</td><td>约 3300 步</td></tr>
<tr><td>Heun</td><td>$0.191h^2$</td><td>$h\approx2.3\times10^{-2}$</td><td>约 87 步</td></tr>
<tr><td>RK4</td><td>$0.0226h^4$</td><td>$h\approx0.25$</td><td>约 8 步</td></tr>
</tbody>
</table>
<p>按函数求值次数算（Euler 每步 1 次、Heun 2 次、RK4 4 次）：Euler 约 3300 次，Heun 约 174 次，RK4 约 32 次。精度相同的前提下，RK4 的计算量比 Euler 少两个数量级。这就是高精度方法的价值：单步贵，但总账便宜。</p>

<h3>16.8 结论与工程含义</h3>
<ul>
<li><strong>拥堵会消散。</strong>解析解中指数项 $1.3385e^{-2t}$ 在 $t\approx1$ 后基本消失，剩下的振荡振幅约 0.61，密度不会持续累积。原因：消散强度 $a=2$ 大于流入的有效增长，系统是稳定的。</li>
<li><strong>双高峰造成短时波动。</strong>频率 3 的分量（振幅 0.166）对应较快的短周期波动，频率 1 的分量（振幅 0.447）对应午间与傍晚的大起伏。</li>
<li><strong>容量设计要看峰值。</strong>长期峰值约 0.61（相对初始 1.0 已下降），若走廊设计容量低于这个峰值就会在高峰时段拥堵。</li>
<li><strong>数值方案选 RK4。</strong>工程上要求 $10^{-4}$ 精度时，RK4 用 8 步就够，Euler 需要 3300 步，实时调度场景不可能接受。</li>
</ul>

<h3>16.9 思考题</h3>
<div class="qa-item"><div class="qa-q">1. 若把消散强度 $a$ 从 2 改成 0.5，解的长期行为会怎么变？</div><div class="qa-a">$\rho'=-0.5\rho+\sin t+0.6\sin3t$，指数项衰减变慢（$e^{-0.5t}$），达到稳态需要更长时间。稳态解的振幅会更大，因为分母 $a^2+\omega^2$ 变小：频率 1 的振幅 $\frac{1}{\sqrt{0.25+1}}\approx0.894$，频率 3 的振幅 $\frac{0.6}{\sqrt{0.25+9}}\approx0.198$。总体峰值接近 1.09，可能超过初始密度，说明通行能力不足时拥堵会累积。</div></div>
<div class="qa-item"><div class="qa-q">2. 为什么 Euler 法在 $t=1.0\sim1.4$ 段误差特别小？</div><div class="qa-a">这一段解曲线接近拐点、斜率变化慢，折线近似贴着曲线走；加上误差在前后段有正有负，恰好抵消。这是"巧合"，不能当作方法精度的证据。判断精度要看整体误差包络与阶数验证。</div></div>
<div class="qa-item"><div class="qa-q">3. 用 $h=0.2$ 的 Euler 数据算 $\rho_1$，与解析解差多少？为什么第一步就差这么多？</div><div class="qa-a">$\rho_1=1+0.2f(0,1)=1+0.2(-2+0+0)=0.6$；解析解 $\rho(0.2)=0.718496$，差 0.1185。第一步误差大是因为初值处斜率 $-2$ 很陡，Euler 用左端斜率外推，低估了密度（真实解在区间内斜率变缓）。这也是为什么改进 Euler 要"再走一步校正"。</div></div>
<div class="qa-item"><div class="qa-q">4. 若要求 $10^{-6}$ 精度，三种方法各需多少步？</div><div class="qa-a">按同一误差模型：Euler $h=10^{-6}/0.167\approx6\times10^{-6}$，约 33 万步；Heun $h=\sqrt{10^{-6}/0.191}\approx2.3\times10^{-3}$，约 870 步；RK4 $h=(10^{-6}/0.0226)^{1/4}\approx0.081$，约 25 步。阶数越高，提高精度的代价增长越慢。</div></div>
<div class="qa-item"><div class="qa-q">5. 这个模型为什么没有用高阶方程？现实中的拥堵传播是否需要高阶模型？</div><div class="qa-a">题目把"某一段"的密度演化简化为零维（只看时间、不看空间），流出与密度成正比，所以是一阶。若要描述拥堵沿航路向上游传播，需要引入空间维度（偏微分方程，如交通流 LWR 模型）或把多个航段串联成方程组，阶数会升高。这是后续课程的内容。</div></div>

<div class="chapter-nav"></div>
</section>
"""
