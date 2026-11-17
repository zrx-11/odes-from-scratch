# -*- coding: utf-8 -*-
CH_G = r"""
<section class="chapter" id="higher-theory" style="display:none">
<div class="breadcrumb"></div>
<h2><span class="num">12</span>n 阶线性方程：解的结构</h2>
<p class="lead">这一章不讲怎么解，只讲"解长什么样"。核心结论只有一句：$n$ 阶齐次线性方程的解构成一个 $n$ 维空间，找到 $n$ 个线性无关的解，所有解就都是它们的线性组合。非齐次方程再加一个特解。对应课件 chapter4-1。</p>

<div class="callout callout-tip">
<div class="callout-title">生活直觉：解空间像一张 n 维的布</div>二阶齐次方程的解由两个"方向"张成，任意解都是这两个方向的组合，就像平面上的任意向量都能写成两个基向量的组合。三阶方程由三个方向张成，是三维空间。$n$ 阶就是 $n$ 维。所谓"基本解组"，就是这组基。
</div>

<div class="callout callout-warn"><div class="callout-title">前置知识</div>第 11 章的线性无关、行列式；第 2 章的叠加原理（二阶版）；第 4 章的常数变易法（一阶版）；第 7 章的存在唯一性定理。</div>

<h3>12.1 n 阶线性方程与算子 L</h3>
<p>课件里的方程写成这样：</p>
<div class="formula">$$\frac{d^nx}{dt^n}+a_1(t)\frac{d^{n-1}x}{dt^{n-1}}+\cdots+a_{n-1}(t)\frac{dx}{dt}+a_n(t)x=f(t) \tag{12.1}$$</div>
<p>"线性"指的是未知函数 $x$ 及其各阶导数都只以一次方出现，没有 $x^2$、$x\cdot x'$、$\sin x$ 这类项。系数 $a_i(t)$ 只依赖 $t$，可以随 $t$ 变，这一点与第 13 章的"常系数"不同。</p>
<p>为书写方便，定义一个符号 $L$，它表示"把 $x$ 按这套系数求导再相加"这一整套操作：</p>
<div class="formula">$$L[x]=\frac{d^n x}{dt^n}+a_1(t)\frac{d^{n-1}x}{dt^{n-1}}+\cdots+a_n(t)x \tag{12.2}$$</div>
<p>于是方程 (12.1) 简写为 $L[x]=f(t)$，对应齐次方程 (12.3) 简写为 $L[x]=0$。</p>
<div class="formula">$$\frac{d^nx}{dt^n}+a_1(t)\frac{d^{n-1}x}{dt^{n-1}}+\cdots+a_n(t)x=0 \tag{12.3}$$</div>
<p>$L$ 叫<strong>线性算子</strong>。它把函数变成函数，就像一台机器：丢进 $x$，出来 $L[x]$。</p>

<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">核</span><span class="derive-step-title">$L$ 的线性性：$L[c_1x_1+c_2x_2]=c_1L[x_1]+c_2L[x_2]$</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>给 $L$ 喂一个组合 $c_1x_1+c_2x_2$，逐项算。先看最高阶项：</p>
<div class="formula">$$\frac{d^n}{dt^n}(c_1x_1+c_2x_2)=c_1x_1^{(n)}+c_2x_2^{(n)}$$</div>
<p>理由：求导是线性的，$(u+v)'=u'+v'$，$(cu)'=cu'$，反复用 $n$ 次即得。</p>
<p>再看低阶项，例如 $a_n(t)(c_1x_1+c_2x_2)=c_1a_nx_1+c_2a_nx_2$，只是乘开。</p>
<p>把所有项加起来，按 $c_1$、$c_2$ 分组：</p>
<div class="formula">$$L[c_1x_1+c_2x_2]=c_1\left[x_1^{(n)}+a_1x_1^{(n-1)}+\cdots+a_nx_1\right]+c_2\left[x_2^{(n)}+\cdots+a_nx_2\right]=c_1L[x_1]+c_2L[x_2]$$</div>
<p>这就是线性性。它是后面所有结论的根源：叠加原理、通解结构、待定系数法的拆分，全靠这一条。</p>
</div></div>
</div>

<h3>12.2 初值问题需要 n 个条件</h3>
<p>一阶方程给一个初值 $x(t_0)=x_0$ 就够。$n$ 阶方程要给 $n$ 个：</p>
<div class="formula">$$x(t_0)=x_0,\quad x'(t_0)=x_0^{(1)},\quad \dots,\quad x^{(n-1)}(t_0)=x_0^{(n-1)} \tag{12.4}$$</div>
<p>为什么是 $n$ 个？因为每积一次分就多一个任意常数，积 $n$ 次得 $n$ 个，要全部定下来就得 $n$ 个条件。第 2 章二阶方程用两个条件（位置 + 速度），道理相同。</p>

<div class="callout callout-key"><div class="callout-title">定理 13.1（存在唯一性）</div>若 $a_1(t),\dots,a_n(t)$ 与 $f(t)$ 在区间 $[a,b]$ 上连续，$t_0\in[a,b]$，则初值问题 (12.1)+(12.4) 在 $[a,b]$ 上有且只有一个解。</div>

<p>证明思路与第 7 章的一阶情形相同：把 $n$ 阶方程化成一阶方程组（令 $y_1=x,y_2=x',\dots,y_n=x^{(n-1)}$），对向量用 Picard 逐步逼近。本章不重复证明，只把它当工具：唯一性在 12.5 节证"$W\neq0$"时要用到。</p>

<h3>12.3 叠加原理</h3>
<div class="callout callout-key"><div class="callout-title">定理 13.2（叠加原理）</div>若 $x_1,\dots,x_k$ 都是齐次方程 $L[x]=0$ 的解，则任意线性组合 $c_1x_1+\cdots+c_kx_k$ 也是解。</div>

<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">证</span><span class="derive-step-title">用 $L$ 的线性性一行写完</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>设 $L[x_i]=0$（$i=1,\dots,k$）。由线性性，</p>
<div class="formula">$$L\left[\sum_{i=1}^{k}c_ix_i\right]=\sum_{i=1}^{k}c_iL[x_i]=\sum_{i=1}^{k}c_i\cdot0=0$$</div>
<p>所以组合也是解。证完。</p>
<p>注意：叠加原理对<strong>齐次</strong>方程成立，对非齐次不成立。$L[x]=f$ 的两个解相加，$L[x_1+x_2]=2f\neq f$，不再是解。非齐次只能"齐次解 + 特解"（12.7 节）。</p>
</div></div>
</div>

<h3>12.4 为什么需要"线性无关"</h3>
<p>叠加原理只保证"组合还是解"，没保证"组合能表示所有解"。举个反面例子：二阶方程 $x''-x=0$ 有两个解 $e^t$ 和 $2e^t$，它们能组合出 $c_1e^t+c_2(2e^t)=(c_1+2c_2)e^t$，本质上只是一个方向的解，漏掉了 $e^{-t}$。</p>
<p>问题在于这两个解线性相关。要用两个"独立方向"才能张成整个解空间。于是需要判断：给定一组解，它们独立吗？</p>

<h3>12.5 朗斯基行列式与三个定理</h3>
<p>把 $n$ 个函数和它们的各阶导数排成一个 $n\times n$ 矩阵，取行列式：</p>
<div class="formula">$$W(t)=\begin{vmatrix}x_1(t)&x_2(t)&\cdots&x_n(t)\\ x_1'(t)&x_2'(t)&\cdots&x_n'(t)\\ \vdots&\vdots&&\vdots\\ x_1^{(n-1)}(t)&x_2^{(n-1)}(t)&\cdots&x_n^{(n-1)}(t)\end{vmatrix} \tag{12.5}$$</div>
<p>叫<strong>朗斯基行列式</strong>（Wronskian）。它的作用是把"$n$ 个函数是否线性无关"化成一个数是否为零。</p>

<div class="callout callout-key"><div class="callout-title">定理 13.3</div>若 $x_1,\dots,x_n$ 在 $[a,b]$ 上线性相关，则 $W(t)\equiv0$ 于 $[a,b]$。</div>

<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">证</span><span class="derive-step-title">相关意味着某一列是其他列的线性组合</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>相关：存在不全为零的 $c_1,\dots,c_n$ 使</p>
<div class="formula">$$c_1x_1(t)+\cdots+c_nx_n(t)\equiv0$$</div>
<p>对 $t$ 求导 $j$ 次（$j=0,1,\dots,n-1$）：</p>
<div class="formula">$$c_1x_1^{(j)}(t)+\cdots+c_nx_n^{(j)}(t)\equiv0$$</div>
<p>这 $n$ 个恒等式说明：矩阵的每一行都与系数向量 $(c_1,\dots,c_n)$ 正交。等价地，矩阵的列向量线性相关（存在非零系数使列的线性组合为零向量）。线性相关的列向量组成的矩阵行列式为 0，所以 $W(t)=0$ 对每个 $t$ 成立。</p>
</div></div>
</div>

<p>逆定理一般<strong>不成立</strong>：$W\equiv0$ 推不出相关。课件给的例子是两个分段函数：</p>
<div class="formula">$$x_1(t)=\begin{cases}t^2,&-1\le t&lt;0\\0,&0\le t\le1\end{cases},\qquad x_2(t)=\begin{cases}0,&-1\le t&lt;0\\t^2,&0\le t\le1\end{cases}$$</div>

<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">这两个函数 $W\equiv0$ 但线性无关</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>先算 $W=x_1x_2'-x_1'x_2$。在 $t&lt;0$ 时 $x_2=0$，$x_2'=0$，$W=0$；在 $t&gt;0$ 时 $x_1=0$，$x_1'=0$，$W=0$；在 $t=0$ 处两侧极限都是 0。所以 $W\equiv0$。</p>
<p>再证无关。设 $c_1x_1+c_2x_2\equiv0$。在 $t=-1/2$（$t&lt;0$ 段）：$c_1\cdot(1/4)+c_2\cdot0=0$，得 $c_1=0$。在 $t=1/2$：$c_1\cdot0+c_2\cdot(1/4)=0$，得 $c_2=0$。故只能全零，线性无关。</p>
<p>结论：$W\equiv0$ 只是相关的<strong>必要</strong>条件，不是充分条件。原因在于这两个函数在 $t=0$ 处不可导（$x_1$ 左导数 $0$、右导数 $0$，其实可导；但二阶导在 0 处跳变），它们不是同一个线性方程的解。</p>
</div></div>
</div>

<p>但对"同一个齐次线性方程的解"，逆命题成立，这就是定理 13.4。</p>

<div class="callout callout-key"><div class="callout-title">定理 13.4</div>若 $x_1,\dots,x_n$ 是方程 (12.3) 的 $n$ 个解，且在 $[a,b]$ 上线性无关，则 $W(t)$ 在 $[a,b]$ 上处处不为零。</div>

<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">证</span><span class="derive-step-title">反证：某点 $W=0$ 会逼出一组非零系数使解恒为零</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>假设存在 $t_0\in[a,b]$ 使 $W(t_0)=0$。把 $W(t_0)$ 看作以 $c_1,\dots,c_n$ 为未知量的齐次线性方程组的系数行列式：</p>
<div class="formula">$$\begin{cases}c_1x_1(t_0)+\cdots+c_nx_n(t_0)=0\\ c_1x_1'(t_0)+\cdots+c_nx_n'(t_0)=0\\ \qquad\vdots\\ c_1x_1^{(n-1)}(t_0)+\cdots+c_nx_n^{(n-1)}(t_0)=0\end{cases}$$</div>
<p>系数行列式 $W(t_0)=0$，方程组有非零解 $(c_1,\dots,c_n)$。</p>
<p>令 $\varphi(t)=c_1x_1(t)+\cdots+c_nx_n(t)$。它是齐次方程的解（叠加原理），且由上面的方程组，$\varphi(t_0)=\varphi'(t_0)=\cdots=\varphi^{(n-1)}(t_0)=0$。</p>
<p>另一方面，恒零函数 $0$ 也是解，且它在 $t_0$ 的各阶初值同样是 0。由存在唯一性定理（初值相同则解相同），$\varphi(t)\equiv0$。</p>
<p>这意味着 $c_1x_1+\cdots+c_nx_n\equiv0$ 且系数不全为零，即 $x_1,\dots,x_n$ 线性相关，与假设矛盾。故 $W(t_0)\neq0$。</p>
</div></div>
</div>

<div class="callout callout-key"><div class="callout-title">推论 13.1</div>齐次线性方程的 $n$ 个解组成的朗斯基行列式，要么恒等于零（解组相关），要么处处不为零（解组无关）。不存在"某些点为 0、另一些点不为 0"的情形。</div>

<p>（更精确的结论是刘维尔公式：$W(t)=W(t_0)\exp\left(-\int_{t_0}^{t}a_1(s)\,ds\right)$，指数函数恒不为零，所以 $W$ 的零点性质完全由 $W(t_0)$ 决定。）</p>

<h3>12.6 基本解组与通解结构</h3>
<div class="callout callout-key"><div class="callout-title">定理 13.5</div>$n$ 阶齐次线性方程 (12.3) 一定存在 $n$ 个线性无关的解。</div>

<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">构</span><span class="derive-step-title">用 $n$ 组标准初值造出 $n$ 个解</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>取定 $t_0$。对 $j=1,\dots,n$，令 $x_j$ 是满足下面初值的解：</p>
<div class="formula">$$x_j^{(i)}(t_0)=\begin{cases}1,&i=j-1\\0,&i\neq j-1\end{cases},\qquad i=0,1,\dots,n-1$$</div>
<p>也就是说，第 $j$ 个解的初值向量是"第 $j$ 个位置为 1、其余为 0"。由存在唯一性，这 $n$ 个解都存在。</p>
<p>在 $t_0$ 处算朗斯基行列式，矩阵正好是单位矩阵（对角线上 1，其余 0），$W(t_0)=1\neq0$。由定理 13.4，这 $n$ 个解线性无关。</p>
<p>这组解叫<strong>标准基本解组</strong>。</p>
</div></div>
</div>

<div class="callout callout-key"><div class="callout-title">定义 13.1（基本解组）</div>齐次方程 (12.3) 的任意 $n$ 个线性无关的解，称为它的一个<strong>基本解组</strong>。</div>

<div class="callout callout-key"><div class="callout-title">定理 13.6（通解结构）</div>若 $x_1,\dots,x_n$ 是 (12.3) 的基本解组，则
<div class="formula">$$x=c_1x_1(t)+c_2x_2(t)+\cdots+c_nx_n(t) \tag{12.6}$$</div>
是 (12.3) 的通解，即它包含了 (12.3) 的所有解，其中 $c_1,\dots,c_n$ 为任意常数。</div>

<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">证</span><span class="derive-step-title">任给一个解，反解出 $c_i$</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>设 $x^*(t)$ 是 (12.3) 的任一解。要证存在常数 $c_1,\dots,c_n$ 使 $x^*=\sum c_ix_i$。</p>
<p>把 $x^*$ 与 $\sum c_ix_i$ 在 $t_0$ 处比较。要求它们相等，需要 $n$ 个等式：</p>
<div class="formula">$$\sum_{i=1}^{n}c_ix_i^{(j)}(t_0)=x^{*(j)}(t_0),\qquad j=0,1,\dots,n-1$$</div>
<p>这是关于 $c_1,\dots,c_n$ 的 $n$ 元线性方程组，系数行列式正是 $W(t_0)$。基本解组线性无关，$W(t_0)\neq0$，由克拉默法则（或矩阵可逆），方程组有唯一解 $c_1,\dots,c_n$。</p>
<p>取这组 $c_i$，令 $\varphi=\sum c_ix_i$。$\varphi$ 与 $x^*$ 都是解，且在 $t_0$ 处的 $n$ 个初值完全相同。由唯一性，$\varphi\equiv x^*$。</p>
<p>所以任一解都能写成 (12.6) 的形式。证完。</p>
</div></div>
</div>

<div class="callout callout-key"><div class="callout-title">推论 13.2（解空间的维数）</div>齐次方程 (12.3) 的所有解构成一个 $n$ 维线性空间。理由：基本解组是 $n$ 个基，任一解是它们的线性组合；线性无关解的个数最多为 $n$（$n+1$ 个解必相关，因为 $n$ 维空间里放不下 $n+1$ 个无关向量）。</div>

<p>用线性代数的说法：$L$ 的零空间（kernel）维数等于方程的阶数 $n$。</p>

<h3>12.7 非齐次方程的解的结构</h3>
<p>看非齐次方程 $L[x]=f(t)$ 和它对应的齐次方程 $L[x]=0$。</p>

<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">性质1</span><span class="derive-step-title">齐次解 + 非齐次解 = 非齐次解</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>设 $L[\bar x]=f$，$L[x]=0$。由线性性：</p>
<div class="formula">$$L[\bar x+x]=L[\bar x]+L[x]=f+0=f$$</div>
<p>所以 $\bar x+x$ 还是非齐次方程的解。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">性质2</span><span class="derive-step-title">两个非齐次解之差是齐次解</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>设 $L[\bar x_1]=f$，$L[\bar x_2]=f$：</p>
<div class="formula">$$L[\bar x_1-\bar x_2]=L[\bar x_1]-L[\bar x_2]=f-f=0$$</div>
<p>差是齐次方程的解。</p>
</div></div>
</div>

<div class="callout callout-key"><div class="callout-title">定理 13.7（非齐次通解）</div>设 $x_1,\dots,x_n$ 是齐次方程的基本解组，$\bar x$ 是非齐次方程的某一个解（叫特解），则非齐次方程的通解为
<div class="formula">$$x=c_1x_1+\cdots+c_nx_n+\bar x \tag{12.7}$$</div>
</div>

<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">证</span><span class="derive-step-title">用性质 2 把任意解归到齐次情形</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>设 $x^*$ 是任一非齐次解。由性质 2，$x^*-\bar x$ 是齐次解。由定理 13.6，$x^*-\bar x=\sum c_ix_i$。移项即得 $x^*=\sum c_ix_i+\bar x$。证完。</p>
<p>所以解非齐次方程的全部工作，归结为两件：解齐次方程求基本解组；找<strong>一个</strong>特解。</p>
</div></div>
</div>

<h3>12.8 常数变易法（n 阶版）</h3>
<p>找特解有两条路：待定系数法（只适用于常系数 + 特定形式的 $f$，第 14 章）和常数变易法（适用于一般情形，但要做积分）。这里推常数变易法。</p>
<p>第 4 章的一阶情形是把 $x=ce^{-\int P}$ 里的常数 $c$ 换成函数 $c(t)$。$n$ 阶同理：把 $x=\sum c_ix_i$ 的 $n$ 个常数全换成函数 $c_i(t)$：</p>
<div class="formula">$$x=c_1(t)x_1(t)+c_2(t)x_2(t)+\cdots+c_n(t)x_n(t) \tag{12.8}$$</div>

<p>现在 $n$ 个未知函数，却只有一个方程 $L[x]=f$，条件不够。所以要人为补 $n-1$ 个限制条件。课件的做法是：每次求导后，令"含 $c_i'$ 的那一堆"等于零。</p>

<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">①</span><span class="derive-step-title">第一次求导，加第 1 个条件</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>对 (12.8) 求导，按乘积法则，每项分成"$c_i$ 乘 $x_i'$"和"$c_i'$ 乘 $x_i$"两部分：</p>
<div class="formula">$$x'=\sum_{i=1}^{n}c_i(t)x_i'(t)+\sum_{i=1}^{n}c_i'(t)x_i(t)$$</div>
<p>令第二个和为零：</p>
<div class="formula">$$\sum_{i=1}^{n}c_i'(t)x_i(t)=0 \tag{12.9}$$</div>
<p>于是 $x'=\sum c_ix_i'$，形式上与"常数情形"一样。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">②</span><span class="derive-step-title">第二次求导，加第 2 个条件</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>对 $x'=\sum c_ix_i'$ 求导：</p>
<div class="formula">$$x''=\sum c_ix_i''+\sum c_i'x_i'$$</div>
<p>令 $\sum c_i'x_i'=0$，得 $x''=\sum c_ix_i''$。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">③</span><span class="derive-step-title">一直做到第 $n-1$ 次</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>第 $k$ 次求导加条件 $\sum c_i'x_i^{(k-1)}=0$，得到 $x^{(k)}=\sum c_ix_i^{(k)}$。做到 $k=n-1$：</p>
<div class="formula">$$\sum_{i=1}^{n}c_i'(t)x_i^{(n-2)}(t)=0,\qquad x^{(n-1)}=\sum_{i=1}^{n}c_i x_i^{(n-1)}$$</div>
<p>此时共加了 $n-1$ 个条件。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">④</span><span class="derive-step-title">第 $n$ 次求导，代回原方程</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>对 $x^{(n-1)}=\sum c_ix_i^{(n-1)}$ 求导，这次<strong>不</strong>再加条件：</p>
<div class="formula">$$x^{(n)}=\sum c_ix_i^{(n)}+\sum c_i'x_i^{(n-1)}$$</div>
<p>把 $x,x',\dots,x^{(n)}$ 的表达式代进 $L[x]=f$。先看 $x^{(n)}$ 那项的贡献：$\sum c_ix_i^{(n)}$ 与其余项 $\sum c_ix_i^{(n-1)},\dots$ 合起来，正好是 $\sum c_iL[x_i]$。因为 $x_i$ 是齐次解，$L[x_i]=0$，这部分全为 0。剩下只有 $\sum c_i'x_i^{(n-1)}$：</p>
<div class="formula">$$\sum_{i=1}^{n}c_i'(t)x_i^{(n-1)}(t)=f(t) \tag{12.10}$$</div>
</div></div>
</div>

<p>把 (12.9)、第 2 到第 $n-1$ 个条件、以及 (12.10) 放在一起，得到一个 $n$ 元线性方程组：</p>
<div class="formula">$$\begin{cases}x_1c_1'+x_2c_2'+\cdots+x_nc_n'=0\\ x_1'c_1'+x_2'c_2'+\cdots+x_n'c_n'=0\\ \qquad\vdots\\ x_1^{(n-2)}c_1'+\cdots+x_n^{(n-2)}c_n'=0\\ x_1^{(n-1)}c_1'+\cdots+x_n^{(n-1)}c_n'=f(t)\end{cases} \tag{12.11}$$</div>
<p>这个方程组的系数行列式正是 $W(t)$。基本解组线性无关，$W(t)\neq0$，所以方程组有唯一解：</p>
<div class="formula">$$c_i'(t)=\varphi_i(t),\qquad i=1,\dots,n$$</div>
<p>积分一次：</p>
<div class="formula">$$c_i(t)=\int\varphi_i(t)\,dt+\gamma_i \tag{12.12}$$</div>
<p>代回 (12.8)：</p>
<div class="formula">$$x=\sum_{i=1}^{n}\gamma_i x_i(t)+\sum_{i=1}^{n}x_i(t)\int\varphi_i(t)\,dt \tag{12.13}$$</div>
<p>第一项是齐次通解，第二项是一个特解，合起来就是非齐次方程的通解。</p>

<div class="callout callout-tip"><div class="callout-title">为什么可以随便加条件</div>原本 $n$ 个未知函数 $c_i(t)$ 只受一个方程约束，解不唯一。每加一个条件就减少一个自由度。加到 $n-1$ 个条件时，还剩 1 个自由度，正好由方程 $L[x]=f$ 定下来。加上去的条件只要"能让后面的推导干净"就行，课件选"让多余项为零"，因为这能让 $x^{(k)}$ 保持 $\sum c_ix_i^{(k)}$ 的简单形状。</div>

<h3>12.9 例题一：$x''+x=\dfrac{1}{\cos t}$</h3>
<p>已知对应齐次方程 $x''+x=0$ 的基本解组是 $\cos t$、$\sin t$。求通解。</p>

<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">①</span><span class="derive-step-title">写出变易形式与两个条件方程</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>令 $x=c_1(t)\cos t+c_2(t)\sin t$。按 (12.11)，$n=2$ 只有两个方程：</p>
<div class="formula">$$\begin{cases}\cos t\,c_1'+\sin t\,c_2'=0\\ -\sin t\,c_1'+\cos t\,c_2'=\dfrac{1}{\cos t}\end{cases}$$</div>
<p>第二个方程的系数是 $x_i'$：$(\cos t)'=-\sin t$，$(\sin t)'=\cos t$。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">②</span><span class="derive-step-title">解二元方程组</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>系数行列式</p>
<div class="formula">$$W=\cos t\cdot\cos t-\sin t\cdot(-\sin t)=\cos^2t+\sin^2t=1$$</div>
<p>用克拉默法则。$c_1'$ 的分子是把第一列换成右端项：</p>
<div class="formula">$$c_1'=\frac{1}{W}\begin{vmatrix}0&\sin t\\ \frac{1}{\cos t}&\cos t\end{vmatrix}=0\cdot\cos t-\sin t\cdot\frac{1}{\cos t}=-\frac{\sin t}{\cos t}$$</div>
<p>$c_2'$ 的分子是把第二列换掉：</p>
<div class="formula">$$c_2'=\frac{1}{W}\begin{vmatrix}\cos t&0\\ -\sin t&\frac{1}{\cos t}\end{vmatrix}=\cos t\cdot\frac{1}{\cos t}-0=1$$</div>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">③</span><span class="derive-step-title">积分</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>$c_1=\int(-\tan t)\,dt=\ln|\cos t|+\gamma_1$（因为 $(\ln|\cos t|)'=-\tan t$）。</p>
<p>$c_2=\int1\,dt=t+\gamma_2$。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">④</span><span class="derive-step-title">代回，写通解</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<div class="formula">$$x=(\ln|\cos t|+\gamma_1)\cos t+(t+\gamma_2)\sin t$$</div>
<p>展开整理：</p>
<div class="formula">$$x=\gamma_1\cos t+\gamma_2\sin t+\cos t\ln|\cos t|+t\sin t$$</div>
<p>最后两项是特解。验算：令 $x_p=\cos t\ln|\cos t|+t\sin t$，求两次导代进 $x''+x$，可逐项抵消，剩下 $1/\cos t$。</p>
</div></div>
</div>

<h3>12.10 例题二：$tx''-x'=t^2\ (t\neq0)$</h3>
<p>这个例子先要自己找齐次方程的基本解组。</p>

<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">①</span><span class="derive-step-title">解齐次方程 $tx''-x'=0$</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>改写为 $\dfrac{x''}{x'}=\dfrac{1}{t}$。两边对 $t$ 积分：</p>
<div class="formula">$$\ln|x'|=\ln|t|+C\ \Longrightarrow\ x'=At$$</div>
<p>再积一次：$x=\dfrac{A}{2}t^2+B$。取 $A/2$ 作任意常数，得基本解组：</p>
<div class="formula">$$x_1=1,\qquad x_2=t^2$$</div>
<p>验算：$x_1'=0,x_1''=0$，$t\cdot0-0=0$ ✓；$x_2'=2t,x_2''=2$，$t\cdot2-2t=0$ ✓。朗斯基 $W=1\cdot2t-0\cdot t^2=2t\neq0$（$t\neq0$）。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">②</span><span class="derive-step-title">把方程化成标准形</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>常数变易法的标准形要求最高阶系数为 1。两边除以 $t$：</p>
<div class="formula">$$x''-\frac{1}{t}x'=t$$</div>
<p>此时 $f(t)=t$，$a_1(t)=-1/t$。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">③</span><span class="derive-step-title">列条件方程</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>令 $x=c_1(t)\cdot1+c_2(t)\cdot t^2$。由 (12.11)：</p>
<div class="formula">$$\begin{cases}c_1'\cdot1+c_2'\,t^2=0\\ c_1'\cdot0+c_2'\cdot2t=t\end{cases}$$</div>
<p>第二式直接给 $c_2'=\dfrac{1}{2}$，于是 $c_1'=-t^2c_2'=-\dfrac{t^2}{2}$。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">④</span><span class="derive-step-title">积分并代回</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<div class="formula">$$c_1=-\frac{t^3}{6}+\gamma_1,\qquad c_2=\frac{t}{2}+\gamma_2$$</div>
<p>代回：</p>
<div class="formula">$$x=\gamma_1+\gamma_2t^2-\frac{t^3}{6}+\frac{t}{2}\cdot t^2=\gamma_1+\gamma_2t^2+\frac{t^3}{3}$$</div>
<p>验算：$x'=2\gamma_2t+t^2$，$x''=2\gamma_2+2t$，</p>
<div class="formula">$$tx''-x'=t(2\gamma_2+2t)-(2\gamma_2t+t^2)=2\gamma_2t+2t^2-2\gamma_2t-t^2=t^2$$</div>
<p>正确。</p>
</div></div>
</div>

<div class="callout callout-tip"><div class="callout-title">两个例子的共同点</div>都要先有齐次基本解组，再写两个条件方程，再解二元一次方程组。区别只在第一步：例一的齐次解是现成的，例二要先解一次齐次方程。解齐次方程时注意"缺 $x$ 项"（只有 $x''$ 和 $x'$）可以令 $p=x'$ 降阶，这正是第 15 章的内容。</div>

<h3>12.11 本章小结</h3>
<table>
<colgroup><col style="width:34%"><col style="width:66%"></colgroup>
<thead><tr><th>结论</th><th>内容</th></tr></thead>
<tbody>
<tr><td>叠加原理</td><td>齐次解的任意线性组合仍是齐次解（靠 $L$ 的线性性）</td></tr>
<tr><td>朗斯基行列式</td><td>相关 ⇒ $W\equiv0$；对解而言，无关 ⇔ $W\neq0$</td></tr>
<tr><td>基本解组</td><td>$n$ 个线性无关的解；一定存在（标准初值构造）</td></tr>
<tr><td>齐次通解</td><td>$x=c_1x_1+\cdots+c_nx_n$，包含所有解；解空间 $n$ 维</td></tr>
<tr><td>非齐次通解</td><td>齐次通解 + 一个特解</td></tr>
<tr><td>常数变易法</td><td>令 $x=\sum c_i(t)x_i$，逐次求导加 $n-1$ 个零条件，最后解 $W$ 为系数的方程组</td></tr>
</tbody>
</table>

<h3>12.12 自测</h3>
<div class="qa-item"><div class="qa-q">1. 为什么二阶齐次方程不可能有三个线性无关的解？</div><div class="qa-a">因为它的解空间是 2 维（推论 13.2）。三个向量在 2 维空间里必线性相关。具体说，若 $x_1,x_2,x_3$ 都是解，把三者在 $t_0$ 处的初值排成 $2\times3$ 矩阵，列数大于行数，列向量必相关，即存在非零 $(c_1,c_2,c_3)$ 使三者初值的线性组合为零，由唯一性得恒零，故相关。</div></div>
<div class="qa-item"><div class="qa-q">2. $x_1=e^t$、$x_2=e^{2t}$ 的朗斯基行列式是多少？它们能构成 $x''-3x'+2x=0$ 的基本解组吗？</div><div class="qa-a">$W=e^t\cdot2e^{2t}-e^t\cdot e^{2t}=2e^{3t}-e^{3t}=e^{3t}\neq0$，线性无关。验算方程：$x_1''-3x_1'+2x_1=e^t-3e^t+2e^t=0$ ✓，$x_2''-3x_2'+2x_2=4e^{2t}-6e^{2t}+2e^{2t}=0$ ✓。两个无关解正好凑成二阶方程的基本解组，通解 $x=c_1e^t+c_2e^{2t}$。</div></div>
<div class="qa-item"><div class="qa-q">3. 用常数变易法解 $x''-x=1$，已知齐次基本解组 $e^t,e^{-t}$。</div><div class="qa-a">列方程：$e^tc_1'+e^{-t}c_2'=0$；$e^tc_1'-e^{-t}c_2'=1$。两式相加得 $2e^tc_1'=1$，$c_1'=e^{-t}/2$；相减得 $2e^{-t}c_2'=-1$，$c_2'=-e^{t}/2$。积分：$c_1=-e^{-t}/2+\gamma_1$，$c_2=-e^{t}/2+\gamma_2$。代回：$x=\gamma_1e^t+\gamma_2e^{-t}-1/2-1/2=\gamma_1e^t+\gamma_2e^{-t}-1$。验算 $x''-x=0-(-1)=1$ ✓。</div></div>
<div class="qa-item"><div class="qa-q">4. 若已知非齐次方程的两个特解 $\bar x_1=t$、$\bar x_2=t+e^t$，能直接写出什么？</div><div class="qa-a">由性质 2，$\bar x_2-\bar x_1=e^t$ 是对应齐次方程的解。但只知道一个齐次解，不足以写出通解（还缺一个无关的）。需要再找一个齐次解，或用降阶法（第 15 章）构造第二个。</div></div>
<div class="qa-item"><div class="qa-q">5. 常数变易法加的 $n-1$ 个条件，如果不按"令多余项为零"来加，还能得到正确结果吗？</div><div class="qa-a">能。那些条件的唯一作用是让 $c_1',\dots,c_n'$ 的方程组非奇异、可解。选"多余项为零"只是让中间表达式最简洁（$x^{(k)}$ 保持 $\sum c_ix_i^{(k)}$ 的形状）。换别的条件，最后解出的 $c_i(t)$ 会不同，但代回后得到的通解等价。</div></div>

<div class="chapter-nav"></div>
</section>
"""
