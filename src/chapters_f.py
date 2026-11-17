# -*- coding: utf-8 -*-
CH_F = r"""
<section class="chapter" id="foundation2" style="display:none">
<div class="breadcrumb"></div>
<h2><span class="num">11</span>数学地基 II：复数与线性代数</h2>
<p class="lead">第四章开始处理二阶以上的方程。课件默认你会复数、行列式、线性无关这几样工具，实际上大多数人数过复数的加减乘除之后就断了。这一章把这四样从初中能懂的地方重新铺一遍，第 12 章起直接用。对应课件 chapter4-1 之前需要的准备知识。</p>

<div class="callout callout-tip">
<div class="callout-title">生活直觉：为什么高阶方程需要这些新工具</div>
二阶方程 $x''+x=0$ 的解里有 $\cos t$ 和 $\sin t$。想把它写成指数形式，就必须让 $\sqrt{-1}$ 合法，这就是复数。想判断 $\cos t$ 和 $\sin t$ 是不是"两个独立的解"，需要一个能一次判完的工具，这就是行列式。想说明"任意解都能写成这两个解的线性组合"，需要线性无关的概念。三样东西缺一不可。
</div>

<div class="callout callout-warn"><div class="callout-title">前置知识</div>第 1 章的导数与积分；第 2 章的线性组合概念（第二章解的结构用过 $c_1y_1+c_2y_2$）；初中一元二次方程与因式分解。</div>

<h3>11.1 这一章要补的四样东西</h3>
<table>
<colgroup><col style="width:26%"><col style="width:38%"><col style="width:36%"></colgroup>
<thead><tr><th>工具</th><th>解决什么问题</th><th>用在哪一章</th></tr></thead>
<tbody>
<tr><td>复数与欧拉公式</td><td>让 $e^{\lambda t}$ 在 $\lambda$ 为负数平方根时也有意义</td><td>14.5 复根情形、15.3 类型 II</td></tr>
<tr><td>多项式根与重数</td><td>判断特征根是单根、二重根还是三重根</td><td>14.7 重根情形</td></tr>
<tr><td>行列式</td><td>一次判断几个函数是否线性无关</td><td>13.5 朗斯基行列式</td></tr>
<tr><td>莱布尼兹公式</td><td>把 $(P(t)e^{\lambda t})^{(n)}$ 展开成有限项</td><td>15.2 待定系数法推导</td></tr>
</tbody>
</table>

<h3>11.2 复数：从"负数不能开平方"开始</h3>
<p>初中学到 $\sqrt{-1}$ 无意义，因为任何实数的平方都 $\ge 0$。到了二阶方程 $x''+x=0$，按 14 章的方法要解 $\lambda^2+1=0$，也就是 $\lambda^2=-1$。若坚持"无意义"，这类方程就解不下去。于是数学家造了一个数，规定它的平方等于 $-1$。</p>

<div class="callout callout-key"><div class="callout-title">定义 12.1（虚数单位）</div>记 $i$ 是一个满足 $i^2=-1$ 的符号。任何形如 $z=a+bi$ 的表达式叫<strong>复数</strong>，$a$ 叫实部（记 $\operatorname{Re}z$），$b$ 叫虚部（记 $\operatorname{Im}z$），$a,b$ 都是实数。
</div>

<p>这个定义没有"构造"出 $i$，只是承认一个新符号并按实数运算律使用它。所有运算规则都由 $i^2=-1$ 这一条推出来。</p>

<h4>加减乘</h4>
<p>加减法逐项对应：$(a+bi)\pm(c+di)=(a\pm c)+(b\pm d)i$。</p>
<p>乘法按多项式展开，再把 $i^2$ 换成 $-1$：</p>
<div class="formula">$$(a+bi)(c+di)=ac+adi+bci+bdi^2=(ac-bd)+(ad+bc)i$$</div>

<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">算 $(2+i)(3-2i)$</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>按分配律四项相乘：</p>
<div class="formula">$$(2+i)(3-2i)=6-4i+3i-2i^2$$</div>
<p>把 $i^2=-1$ 代入最后一项：$-2i^2=-2(-1)=2$。合并：</p>
<div class="formula">$$6+2+(-4i+3i)=8-i$$</div>
<p>验证：实部 $2\cdot3-1\cdot(-2)=8$，虚部 $2\cdot(-2)+1\cdot3=-1$。</p>
</div></div>
</div>

<h4>除法：用共轭把分母变成实数</h4>
<p>分母 $c+di$ 里有 $i$，不能直接除。办法是上下同乘 $c-di$，因为</p>
<div class="formula">$$(c+di)(c-di)=c^2-(di)^2=c^2-d^2i^2=c^2+d^2$$</div>
<p>$i^2=-1$ 让最后一步变成加法，分母成了实数 $c^2+d^2$。$c-di$ 叫 $c+di$ 的<strong>共轭复数</strong>，记 $\bar z$。</p>
<div class="formula">$$\frac{a+bi}{c+di}=\frac{(a+bi)(c-di)}{c^2+d^2}=\frac{ac+bd}{c^2+d^2}+\frac{bc-ad}{c^2+d^2}i$$</div>

<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">算 $\dfrac{1+i}{2-i}$</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>分母 $2-i$ 的共轭是 $2+i$，分母平方 $2^2+(-1)^2=5$：</p>
<div class="formula">$$\frac{(1+i)(2+i)}{5}=\frac{2+i+2i+i^2}{5}=\frac{2+3i-1}{5}=\frac{1}{5}+\frac{3}{5}i$$</div>
<p>验算：$(1/5+3i/5)(2-i)=(2/5+6/5)+(3/5-1/5)i=(8/5)+(2/5)i$，不是 $1+i$。重算分子：$(1+i)(2+i)=2+i+2i+i^2=2+3i-1=1+3i$，除以 5 得 $1/5+3i/5$。回代检验应为原式 $1+i$：</p>
<div class="formula">$$\left(\frac15+\frac35 i\right)(2-i)=\frac25+\frac65 i-\frac15 i-\frac35 i^2=\frac25+\frac35+i\left(\frac65-\frac15\right)=1+i$$</div>
<p>对上了。注意 $-\frac35 i^2=+\frac35$，这一步容易漏。</p>
</div></div>
</div>

<h4>几何表示：复数就是平面上的点</h4>
<p>把 $a+bi$ 对应到平面点 $(a,b)$：实部当横坐标，虚部当纵坐标。这样加法就是向量相加，$i$ 的作用是"逆时针转 90 度"：$(a,b)$ 乘以 $i$ 得 $(-b,a)$，正好转 90°。</p>
<p>点 $(a,b)$ 到原点的距离叫<strong>模</strong>：$|z|=\sqrt{a^2+b^2}$。方向角 $\theta$ 满足 $\cos\theta=a/|z|$，$\sin\theta=b/|z|$。于是</p>
<div class="formula">$$z=|z|(\cos\theta+i\sin\theta)$$</div>
<p>这一步把复数拆成"长度 × 方向"，是下一节欧拉公式的入口。</p>

<h3>11.3 欧拉公式：把 $e^{i\theta}$ 定义成 $\cos\theta+i\sin\theta$</h3>
<p>第 1 章讲过 $e^x$ 的性质：$(e^x)'=e^x$，$e^0=1$。现在想问：$e^{i\theta}$ 应该是什么？</p>
<p>有两种走法。一种是泰勒级数硬算，需要先讲级数收敛，成本太高。另一种是从"旋转"出发直接定义，再用两条性质验证它和实指数函数是同一套规则。这里走第二种。</p>

<div class="callout callout-key"><div class="callout-title">定义 12.2（欧拉公式）</div>对任意实数 $\theta$，规定
<div class="formula">$$e^{i\theta}=\cos\theta+i\sin\theta \tag{11.1}$$</div>
这相当于说：$e^{i\theta}$ 是单位圆上转过 $\theta$ 角的那个点。</div>

<p>为什么这个定义合理？检查两条性质。</p>

<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">验一</span><span class="derive-step-title">乘法对应角度相加</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>按定义展开 $e^{i\alpha}e^{i\beta}$：</p>
<div class="formula">$$(\cos\alpha+i\sin\alpha)(\cos\beta+i\sin\beta)$$</div>
<p>乘开，四项：$\cos\alpha\cos\beta+i\cos\alpha\sin\beta+i\sin\alpha\cos\beta+i^2\sin\alpha\sin\beta$。用 $i^2=-1$ 合并实部：</p>
<div class="formula">$$(\cos\alpha\cos\beta-\sin\alpha\sin\beta)+i(\cos\alpha\sin\beta+\sin\alpha\cos\beta)$$</div>
<p>括号里两个式子正好是余弦、正弦的和角公式（初中/高中三角）：</p>
<div class="formula">$$\cos(\alpha+\beta)+i\sin(\alpha+\beta)=e^{i(\alpha+\beta)}$$</div>
<p>于是 $e^{i\alpha}e^{i\beta}=e^{i(\alpha+\beta)}$，与实指数 $e^ae^b=e^{a+b}$ 完全一致。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">验二</span><span class="derive-step-title">对 $\theta$ 求导等于 $i$ 倍自身</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>把 $\cos\theta+i\sin\theta$ 对 $\theta$ 求导（$i$ 当常数）：</p>
<div class="formula">$$\frac{d}{d\theta}(\cos\theta+i\sin\theta)=-\sin\theta+i\cos\theta$$</div>
<p>另一方面，把 $i(\cos\theta+i\sin\theta)$ 乘开：</p>
<div class="formula">$$i\cos\theta+i^2\sin\theta=i\cos\theta-\sin\theta$$</div>
<p>两式相同。所以</p>
<div class="formula">$$\frac{d}{d\theta}e^{i\theta}=i\,e^{i\theta}$$</div>
<p>这与 $(e^{\lambda t})'=\lambda e^{\lambda t}$ 的形状一致，只是 $\lambda$ 换成了 $i$。第 13 章正是要用这个性质：把 $e^{\lambda t}$ 代进微分方程，导数只会提出一个 $\lambda$ 因子。</p>
</div></div>
</div>

<h4>反过来用：把 $\cos$、$\sin$ 写成指数</h4>
<p>由 $e^{i\theta}=\cos\theta+i\sin\theta$ 和 $e^{-i\theta}=\cos\theta-i\sin\theta$（把 $\theta$ 换成 $-\theta$，$\cos$ 偶、$\sin$ 奇），两式相加、相减：</p>
<div class="formula">$$\cos\theta=\frac{e^{i\theta}+e^{-i\theta}}{2},\qquad \sin\theta=\frac{e^{i\theta}-e^{-i\theta}}{2i} \tag{11.2}$$</div>
<p>把右边展开可以验证回来：相加得 $2\cos\theta$，相减得 $2i\sin\theta$。这两条在第 14.3 节把 $[A\cos\beta t+B\sin\beta t]e^{\alpha t}$ 拆成复指数时要用。</p>

<div class="callout callout-tip"><div class="callout-title">数值感受</div>取 $\theta=\pi$：$e^{i\pi}=\cos\pi+i\sin\pi=-1$。这就是欧拉恒等式 $e^{i\pi}+1=0$。取 $\theta=\pi/2$：$e^{i\pi/2}=\cos(\pi/2)+i\sin(\pi/2)=i$，与"$i$ 是转 90°"的几何解释对得上。</div>

<h3>11.4 多项式的根与重数</h3>
<p>第 13 章要解 $n$ 次方程 $\lambda^n+a_1\lambda^{n-1}+\cdots+a_n=0$。这类方程有几个根、根会不会重复，直接决定基本解组怎么写。</p>

<div class="callout callout-key"><div class="callout-title">代数基本定理</div>任何 $n$ 次多项式（$n\ge1$，最高次系数不为 0）在复数范围内至少有一个根；把它一个一个分解下去，恰好有 $n$ 个根，按重数计。</div>

<p>"按重数计"的意思是：方程 $(x-1)^3(x+2)=0$ 表面只有两个不同的根 $1$ 和 $-2$，但 $1$ 出现了三次，所以算三个根，总数 $3+1=4$，与次数 4 相符。</p>

<div class="callout callout-key"><div class="callout-title">定义 12.3（重根）</div>若多项式 $F(\lambda)$ 能写成
<div class="formula">$$F(\lambda)=(\lambda-\lambda_1)^k G(\lambda),\qquad G(\lambda_1)\neq0$$</div>
则称 $\lambda_1$ 是 $F$ 的 <strong>$k$ 重根</strong>。$k=1$ 叫单根。</div>

<p>重数有一个等价的判别法，用导数：</p>
<div class="formula">$$\lambda_1 \text{ 是 } k \text{ 重根} \iff F(\lambda_1)=F'(\lambda_1)=\cdots=F^{(k-1)}(\lambda_1)=0,\quad F^{(k)}(\lambda_1)\neq0$$</div>

<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">为什么重根能用导数判定</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>设 $F(\lambda)=(\lambda-\lambda_1)^kG(\lambda)$，$G(\lambda_1)\neq0$。用莱布尼兹公式（11.7 节）求 $j$ 阶导数，$0\le j\le k-1$：</p>
<div class="formula">$$F^{(j)}(\lambda)=\sum_{m=0}^{j}C_j^m\left[(\lambda-\lambda_1)^k\right]^{(m)}G^{(j-m)}(\lambda)$$</div>
<p>当 $m\le j\le k-1$ 时，$(\lambda-\lambda_1)^k$ 的 $m$ 阶导数是 $k(k-1)\cdots(k-m+1)(\lambda-\lambda_1)^{k-m}$，仍含因子 $(\lambda-\lambda_1)$，在 $\lambda=\lambda_1$ 处为 0。所以每一项都带 $(\lambda-\lambda_1)$，$F^{(j)}(\lambda_1)=0$。</p>
<p>再看 $j=k$ 阶：求导 $k$ 次时，只有把 $(\lambda-\lambda_1)^k$ 完全求导完的那一项不含 $(\lambda-\lambda_1)$，它是 $k!\,G(\lambda)$，在 $\lambda_1$ 处等于 $k!G(\lambda_1)\neq0$。其余项仍含因子，为 0。故 $F^{(k)}(\lambda_1)\neq0$。</p>
<p>反过来，若前 $k-1$ 阶导都为 0 而 $k$ 阶不为 0，把 $F$ 在 $\lambda_1$ 处展开（泰勒），最低非零项是 $k$ 次项，即 $F=(\lambda-\lambda_1)^k\cdot(\text{常数}+\cdots)$，正是 $k$ 重根。</p>
</div></div>
</div>

<p>这个判别法在第 14.2 节会用到：待定系数法要判断 $\lambda$ 是几重特征根，$k$ 就等于"前几个导数等于 0"的个数。</p>

<h4>实系数多项式的复根成对出现</h4>
<p>如果 $F$ 的系数全是实数，$\lambda_0=\alpha+i\beta$ 是根，那么它的共轭 $\bar\lambda_0=\alpha-i\beta$ 也是根。理由：对 $F(\lambda_0)=0$ 两边取共轭，利用"实数的共轭是自己"和"共轭的运算等于运算的共轭"，得到 $F(\bar\lambda_0)=\overline{F(\lambda_0)}=0$。</p>
<p>所以实系数方程的根只有两种：实数根，或者成对的共轭复根。第 13 章处理复根时正是按"一对"处理，得到两个实值解 $\cos$ 与 $\sin$。</p>

<h3>11.5 行列式：一次判断"是否独立"</h3>
<p>解二元一次方程组时用过消元法。行列式是把消元的结果写成一个数，这个数是否为 0 直接说明方程组有没有唯一解。</p>

<div class="callout callout-key"><div class="callout-title">定义 12.4（二阶行列式）</div>
<div class="formula">$$\begin{vmatrix}a&b\\c&d\end{vmatrix}=ad-bc$$</div>
口诀"主对角线相乘减副对角线相乘"。</div>

<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">行列式为什么能判断方程组有没有唯一解</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>看方程组</p>
<div class="formula">$$\begin{cases}ax+by=e\\ cx+dy=f\end{cases}$$</div>
<p>第一式乘 $d$、第二式乘 $b$ 相减，消掉 $y$：</p>
<div class="formula">$$(ad-bc)x=ed-bf$$</div>
<p>同理消 $x$ 得 $(ad-bc)y=af-ce$。只要 $ad-bc\neq0$，两个未知数都被唯一确定：</p>
<div class="formula">$$x=\frac{ed-bf}{ad-bc},\qquad y=\frac{af-ce}{ad-bc}$$</div>
<p>若 $ad-bc=0$，两式左边为 0，右边若不为 0 则无解，若为 0 则有无穷多解。所以 $ad-bc$ 就是"系数矩阵是否可逆"的判据。</p>
</div></div>
</div>

<h4>三阶行列式</h4>
<p>按第一行展开，每一项配一个"余子式"（划掉该行该列后的二阶行列式），符号按 $+,-,+$ 交替：</p>
<div class="formula">$$\begin{vmatrix}a_1&a_2&a_3\\ b_1&b_2&b_3\\ c_1&c_2&c_3\end{vmatrix}=a_1\begin{vmatrix}b_2&b_3\\ c_2&c_3\end{vmatrix}-a_2\begin{vmatrix}b_1&b_3\\ c_1&c_3\end{vmatrix}+a_3\begin{vmatrix}b_1&b_2\\ c_1&c_2\end{vmatrix}$$</div>

<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">算一个三阶行列式</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<div class="formula">$$\begin{vmatrix}1&2&3\\ 0&1&4\\ 5&6&0\end{vmatrix}=1\begin{vmatrix}1&4\\6&0\end{vmatrix}-2\begin{vmatrix}0&4\\5&0\end{vmatrix}+3\begin{vmatrix}0&1\\5&6\end{vmatrix}$$</div>
<p>逐项算：$1(1\cdot0-4\cdot6)=1(0-24)=-24$；$-2(0\cdot0-4\cdot5)=-2(-20)=40$；$3(0\cdot6-1\cdot5)=3(-5)=-15$。相加：</p>
<div class="formula">$$-24+40-15=1$$</div>
</div></div>
</div>

<h4>最关键的一条性质：两列相同或成比例，行列式为 0</h4>
<p>以二阶为例：若第二列是第一列的 $k$ 倍，即 $b=ka$、$d=kc$，则 $ad-bc=a(kc)-(ka)c=0$。三阶同理，因为可以拆成"两列成比例的矩阵"的行列式，展开后每项都互相抵消。</p>
<p>这条性质正是 12.5 节朗斯基行列式判据的来源：把 $n$ 个函数排成矩阵，如果它们线性相关（某一列能由其他列线性组合出来），行列式就是 0。</p>

<h4>范德蒙行列式（第 13 章要用）</h4>
<p>形如</p>
<div class="formula">$$V=\begin{vmatrix}1&1&\cdots&1\\ \lambda_1&\lambda_2&\cdots&\lambda_n\\ \vdots&\vdots&&\vdots\\ \lambda_1^{n-1}&\lambda_2^{n-1}&\cdots&\lambda_n^{n-1}\end{vmatrix}$$</div>
<p>的行列式叫范德蒙行列式。它的值等于所有"后减前"的乘积：</p>
<div class="formula">$$V=\prod_{1\le i&lt;j\le n}(\lambda_j-\lambda_i)$$</div>
<p>所以只要 $\lambda_1,\dots,\lambda_n$ 两两不同，$V\neq0$。第 13.5 节要证的"$e^{\lambda_1t},\dots,e^{\lambda_nt}$ 线性无关"，其朗斯基行列式正好是"$e^{(\sum\lambda_i)t}$ 乘一个范德蒙行列式"，靠这条性质收尾。</p>

<h3>11.6 线性相关与线性无关（函数版）</h3>
<p>第 2 章已经用过这个说法：$y_1$、$y_2$ 线性无关，才能写通解 $c_1y_1+c_2y_2$。现在把它定义清楚。</p>

<div class="callout callout-key"><div class="callout-title">定义 12.5（线性相关）</div>区间 $[a,b]$ 上的 $k$ 个函数 $x_1(t),\dots,x_k(t)$，如果存在<strong>不全为零</strong>的常数 $c_1,\dots,c_k$，使得
<div class="formula">$$c_1x_1(t)+c_2x_2(t)+\cdots+c_kx_k(t)\equiv0,\qquad \forall t\in[a,b]$$</div>
就称它们<strong>线性相关</strong>；否则称<strong>线性无关</strong>。</div>

<p>两个词的区别在"是否存在一组非零系数能把它们抵消成恒零"。</p>

<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">例1</span><span class="derive-step-title">$\cos^2 t$ 与 $\sin^2 t-1$ 相关</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>取 $c_1=1,\ c_2=1$：</p>
<div class="formula">$$\cos^2t+(\sin^2t-1)=\cos^2t+\sin^2t-1=1-1=0$$</div>
<p>恒等于 0，系数不全为零，所以线性相关。几何上：第二个函数就是第一个函数的 $-1$ 倍（$\sin^2t-1=-\cos^2t$）。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">例2</span><span class="derive-step-title">$1,t,t^2$ 无关</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>设 $c_0+c_1t+c_2t^2\equiv0$。取 $t=0$ 得 $c_0=0$；剩下 $c_1t+c_2t^2\equiv0$，取 $t=1$ 得 $c_1+c_2=0$，取 $t=2$ 得 $2c_1+4c_2=0$，联立解得 $c_1=c_2=0$。所以只能全零，线性无关。</p>
<p>一般地 $1,t,t^2,\dots,t^n$ 在任何区间上都线性无关。理由同上：一个 $n$ 次多项式若恒等于 0，所有系数必须为 0。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">例3</span><span class="derive-step-title">$\cos t$ 与 $\sin t$ 无关</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>设 $c_1\cos t+c_2\sin t\equiv0$。取 $t=0$：$c_1=0$。取 $t=\pi/2$：$c_2=0$。所以只能全零。无关。</p>
<p>直观说法：两条曲线形状不同，没有任何一条是另一条的常数倍。</p>
</div></div>
</div>

<div class="callout callout-tip"><div class="callout-title">判定顺序</div>先看"是否一个是另一个的常数倍"（一眼能看出的相关），不行再用"取特殊点解方程组"，再不行才上朗斯基行列式。前两种够用于二三个函数，朗斯基是为 $n$ 个函数准备的一次性判据。</div>

<h3>11.7 莱布尼兹公式：高阶导数的乘法法则</h3>
<p>一阶导数的乘积法则是 $(fg)'=f'g+fg'$。求二阶导数要把这个法则再用一次：</p>
<div class="formula">$$(fg)''=(f'g+fg')'=f''g+2f'g'+fg''$$</div>
<p>系数 $1,2,1$。三阶：(1,3,3,1)。这与二项式展开 $(a+b)^n$ 的系数完全相同，原因是每次求导都要对 $f$ 或 $g$ 各"作用"一次，选 $k$ 次作用于 $f$ 的方案数就是 $C_n^k$。</p>

<div class="callout callout-key"><div class="callout-title">定理 12.1（莱布尼兹公式）</div>
<div class="formula">$$(fg)^{(n)}=\sum_{k=0}^{n}C_n^k\,f^{(k)}g^{(n-k)} \tag{11.3}$$</div>
其中 $C_n^k=\dfrac{n!}{k!(n-k)!}$ 是组合数，$f^{(0)}$ 表示 $f$ 本身。</div>

<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">对 $n$ 归纳证明</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>$n=1$ 时 $(fg)'=f'g+fg'=C_1^0f^{(0)}g^{(1)}+C_1^1f^{(1)}g^{(0)}$，成立。</p>
<p>设 $n$ 时成立，对 $n+1$ 求导：</p>
<div class="formula">$$(fg)^{(n+1)}=\sum_{k=0}^{n}C_n^k\left[f^{(k+1)}g^{(n-k)}+f^{(k)}g^{(n-k+1)}\right]$$</div>
<p>把第一个和式中的 $k$ 换成 $k-1$（即把 $f^{(k+1)}$ 改写成 $f^{(k)}$，指标从 $k=1$ 到 $n+1$），与第二个和式合并同类项 $f^{(k)}g^{(n+1-k)}$：</p>
<div class="formula">$$\sum_{k=0}^{n+1}\left(C_n^{k-1}+C_n^k\right)f^{(k)}g^{(n+1-k)}$$</div>
<p>用组合数的帕斯卡公式 $C_n^{k-1}+C_n^k=C_{n+1}^k$（从 $n$ 个里选 $k$ 个 = 不选第 $n+1$ 个选 $k$ 个 + 选第 $n+1$ 个再从前 $n$ 个选 $k-1$ 个），得到 $n+1$ 阶的公式。归纳完成。</p>
</div></div>
</div>

<p>第 14 章要算 $\left(P(t)e^{\lambda t}\right)^{(n)}$。取 $f=P$、$g=e^{\lambda t}$，$g$ 的任意阶导数都是 $\lambda^{n-k}e^{\lambda t}$，公式立刻给出</p>
<div class="formula">$$\left(Pe^{\lambda t}\right)^{(n)}=e^{\lambda t}\sum_{k=0}^{n}C_n^k P^{(k)}\lambda^{n-k}$$</div>
<p>这正是待定系数法能"逐项比较系数"的技术前提。</p>

<h3>11.8 本章小结</h3>
<table>
<colgroup><col style="width:30%"><col style="width:70%"></colgroup>
<thead><tr><th>工具</th><th>要记住的结论</th></tr></thead>
<tbody>
<tr><td>复数</td><td>$i^2=-1$，$(a+bi)(c+di)=(ac-bd)+(ad+bc)i$，除法乘共轭</td></tr>
<tr><td>欧拉公式</td><td>$e^{i\theta}=\cos\theta+i\sin\theta$，$e^{i\alpha}e^{i\beta}=e^{i(\alpha+\beta)}$，求导提出 $i$</td></tr>
<tr><td>多项式</td><td>$n$ 次方程恰有 $n$ 个根（计重数）；$k$ 重根 ⇔ 前 $k-1$ 阶导为 0、第 $k$ 阶不为 0</td></tr>
<tr><td>行列式</td><td>$2\times2$ 是 $ad-bc$；两列成比例则为 0；范德蒙行列式 = $\prod(\lambda_j-\lambda_i)$</td></tr>
<tr><td>线性无关</td><td>不存在不全为零的系数使线性组合恒为 0</td></tr>
<tr><td>莱布尼兹</td><td>$(fg)^{(n)}=\sum C_n^k f^{(k)}g^{(n-k)}$</td></tr>
</tbody>
</table>

<h3>11.9 自测</h3>
<div class="qa-item"><div class="qa-q">1. 计算 $(3-2i)(1+4i)$，并写出它的模。</div><div class="qa-a">乘开：$3+12i-2i-8i^2=3+10i+8=11+10i$。模 $\sqrt{121+100}=\sqrt{221}\approx14.87$。</div></div>
<div class="qa-item"><div class="qa-q">2. 用欧拉公式把 $\sin 2t$ 写成指数形式，并说明系数为什么是 $1/(2i)$。</div><div class="qa-a">$\sin2t=\dfrac{e^{i2t}-e^{-i2t}}{2i}$。因为 $e^{i2t}=\cos2t+i\sin2t$，$e^{-i2t}=\cos2t-i\sin2t$，相减剩 $2i\sin2t$，所以除以 $2i$ 才回到 $\sin2t$。</div></div>
<div class="qa-item"><div class="qa-q">3. 判断 $x_1=1$、$x_2=t$、$x_3=t^2$ 是否线性无关；若把 $x_3$ 换成 $2t^2-3$ 呢？</div><div class="qa-a">$1,t,t^2$ 无关（多项式恒零则系数全零）。换成 $2t^2-3$ 后，$x_3=2x_1+2x_2^2$ 不是 $x_1,x_2$ 的线性组合，但 $x_3-2x_2^2+3x_1=0$ 用到了 $x_2^2$ 这个不属于函数组的东西，不能这样写。正确判断：设 $c_1+c_2t+c_3(2t^2-3)\equiv0$，按 $t$ 的幂次比较：$t^2$ 项系数 $2c_3=0$，常数项 $c_1-3c_3=0$，$t$ 项 $c_2=0$，故全零，仍线性无关。</div></div>
<div class="qa-item"><div class="qa-q">4. 用莱布尼兹公式展开 $(t^2e^{3t})'''$。</div><div class="qa-a">$f=t^2$，$f'=2t$，$f''=2$，$f'''=0$。$g^{(k)}=3^ke^{3t}$。代入：$f g'''+3f'g''+3f''g'=t^2\cdot27e^{3t}+3\cdot2t\cdot9e^{3t}+3\cdot2\cdot3e^{3t}=e^{3t}(27t^2+54t+18)$。</div></div>
<div class="qa-item"><div class="qa-q">5. 范德蒙行列式 $\begin{vmatrix}1&1&1\\1&2&3\\1&4&9\end{vmatrix}$ 等于多少？</div><div class="qa-a">按公式 $\prod_{i&lt;j}(\lambda_j-\lambda_i)=(2-1)(3-1)(3-2)=1\cdot2\cdot1=2$。</div></div>

<div class="chapter-nav"></div>
</section>
"""
