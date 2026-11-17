# -*- coding: utf-8 -*-
CH_H = r"""
<section class="chapter" id="const-homo" style="display:none">
<div class="breadcrumb"></div>
<h2><span class="num">13</span>常系数齐次：特征方程</h2>
<p class="lead">系数全是常数时，解齐次方程变成解一个代数方程。这一章把"猜 $e^{\lambda t}$"的动机、特征方程怎么来、单根/复根/重根三种情形怎么处理，从头推一遍。对应课件 chapter4-2-1。</p>

<div class="callout callout-tip">
<div class="callout-title">生活直觉：找"求导后还是自己"的函数</div>$e^{\lambda t}$ 有个特别之处：求导一次只乘上 $\lambda$，求导 $n$ 次只乘上 $\lambda^n$，函数形状不变。把这样的函数塞进微分方程，所有导数项都变成"同一个 $e^{\lambda t}$ 乘一个数"，方程退化成"这个数等于零"。微分问题于是变成解多项式方程。
</div>

<div class="callout callout-warn"><div class="callout-title">前置知识</div>第 11 章的复数、欧拉公式、重根判别、范德蒙行列式；第 12 章的基本解组与通解结构。</div>

<h3>13.1 方程的形状</h3>
<p>常系数齐次线性方程：</p>
<div class="formula">$$L[x]\equiv\frac{d^nx}{dt^n}+a_1\frac{d^{n-1}x}{dt^{n-1}}+\cdots+a_{n-1}\frac{dx}{dt}+a_nx=0 \tag{13.1}$$</div>
<p>$a_1,\dots,a_n$ 全是常数，不随 $t$ 变。由第 12 章，只要求出 $n$ 个线性无关的解，通解就是它们的线性组合。任务很明确：找基本解组。</p>

<h3>13.2 从一阶情形得到启发</h3>
<p>一阶常系数齐次方程 $\dfrac{dx}{dt}+ax=0$ 的解是 $x=ce^{-at}$。写成指数形式就是 $e^{\lambda t}$，其中 $\lambda=-a$。这提示高阶方程的解可能也是指数函数。</p>
<p>试令</p>
<div class="formula">$$x=e^{\lambda t} \tag{13.2}$$</div>
<p>$\lambda$ 是待定常数，允许是复数（第 11 章已备好）。</p>

<h3>13.3 代入：$L[e^{\lambda t}]=F(\lambda)e^{\lambda t}$</h3>
<p>把 $x=e^{\lambda t}$ 逐项代进 $L$。先算第 $k$ 阶导数：</p>
<div class="formula">$$\frac{d^k}{dt^k}e^{\lambda t}=\lambda^k e^{\lambda t},\qquad k=0,1,\dots,n$$</div>
<p>理由：每求导一次提出一个 $\lambda$，求 $k$ 次提出 $\lambda^k$；$k=0$ 就是函数本身。代入 (13.1)，每一项都带 $e^{\lambda t}$，可以提出来：</p>
<div class="formula">$$L[e^{\lambda t}]=\left(\lambda^n+a_1\lambda^{n-1}+\cdots+a_{n-1}\lambda+a_n\right)e^{\lambda t} \tag{13.3}$$</div>
<p>括号里是一个 $n$ 次多项式，记作</p>
<div class="formula">$$F(\lambda)=\lambda^n+a_1\lambda^{n-1}+\cdots+a_{n-1}\lambda+a_n \tag{13.4}$$</div>
<p>于是</p>
<div class="formula">$$L[e^{\lambda t}]=F(\lambda)e^{\lambda t}$$</div>
<p>$e^{\lambda t}$ 永远不为零（指数函数恒正，复指数模为 $e^{\alpha t}$ 也不为零），所以 $L[e^{\lambda t}]=0$ 等价于 $F(\lambda)=0$。</p>

<div class="callout callout-key"><div class="callout-title">定理 14.1（特征方程）</div>$x=e^{\lambda t}$ 是方程 (13.1) 的解，当且仅当
<div class="formula">$$F(\lambda)\equiv\lambda^n+a_1\lambda^{n-1}+\cdots+a_n=0 \tag{13.5}$$</div>
成立。方程 (13.5) 叫<strong>特征方程</strong>，它的根叫<strong>特征根</strong>，$F$ 叫<strong>特征多项式</strong>。</div>

<p>这套方法叫欧拉待定指数函数法，也叫特征值法。下面按特征根的三种情况分别讨论。</p>

<h3>13.4 情形一：$n$ 个互不相同的单根</h3>
<p>若特征方程有 $n$ 个彼此不同的根 $\lambda_1,\lambda_2,\dots,\lambda_n$，对应有 $n$ 个解：</p>
<div class="formula">$$e^{\lambda_1t},\ e^{\lambda_2t},\ \dots,\ e^{\lambda_nt} \tag{13.6}$$</div>
<p>要证明它们构成基本解组，只需证线性无关，即朗斯基行列式不为零。</p>

<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">推</span><span class="derive-step-title">算这组解的朗斯基行列式</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>按定义排矩阵。第 $j$ 列是 $e^{\lambda_jt}$ 及其各阶导数：</p>
<div class="formula">$$W(t)=\begin{vmatrix}e^{\lambda_1t}&e^{\lambda_2t}&\cdots&e^{\lambda_nt}\\ \lambda_1e^{\lambda_1t}&\lambda_2e^{\lambda_2t}&\cdots&\lambda_ne^{\lambda_nt}\\ \vdots&\vdots&&\vdots\\ \lambda_1^{n-1}e^{\lambda_1t}&\lambda_2^{n-1}e^{\lambda_2t}&\cdots&\lambda_n^{n-1}e^{\lambda_nt}\end{vmatrix}$$</div>
<p>每一列都提出一个公因子 $e^{\lambda_jt}$。从第 $j$ 列提一个，总共提出 $e^{(\lambda_1+\cdots+\lambda_n)t}$：</p>
<div class="formula">$$W(t)=e^{(\lambda_1+\cdots+\lambda_n)t}\begin{vmatrix}1&1&\cdots&1\\ \lambda_1&\lambda_2&\cdots&\lambda_n\\ \vdots&\vdots&&\vdots\\ \lambda_1^{n-1}&\lambda_2^{n-1}&\cdots&\lambda_n^{n-1}\end{vmatrix}$$</div>
<p>剩下的正是范德蒙行列式（11.5 节）。它的值等于 $\prod_{1\le i&lt;j\le n}(\lambda_j-\lambda_i)$。</p>
<p>因为 $\lambda_i$ 两两不同，每个因子都不为零，乘积不为零；$e^{(\sum\lambda_i)t}$ 也不为零。所以 $W(t)\neq0$，解组线性无关。</p>
</div></div>
</div>

<p>于是通解为</p>
<div class="formula">$$x=c_1e^{\lambda_1t}+c_2e^{\lambda_2t}+\cdots+c_ne^{\lambda_nt}$$</div>

<h3>13.5 情形二：一对共轭复根</h3>
<p>实系数方程若有复根，必成对出现（11.4 节）。设 $\lambda=\alpha+i\beta$ 是特征根（$\beta\neq0$），则 $\bar\lambda=\alpha-i\beta$ 也是。对应两个复值解：</p>
<div class="formula">$$e^{(\alpha+i\beta)t}=e^{\alpha t}(\cos\beta t+i\sin\beta t),\qquad e^{(\alpha-i\beta)t}=e^{\alpha t}(\cos\beta t-i\sin\beta t)$$</div>
<p>这里用了欧拉公式 $e^{i\theta}=\cos\theta+i\sin\theta$，以及 $e^{\alpha t+i\beta t}=e^{\alpha t}e^{i\beta t}$（指数相加性质，11.3 节验过）。</p>

<div class="callout callout-key"><div class="callout-title">命题 14.1（复值解的实部虚部仍是解）</div>若方程系数 $a_i$ 都是实函数，$z(t)=\varphi(t)+i\psi(t)$ 是齐次方程的解，则实部 $\varphi$、虚部 $\psi$、共轭 $\bar z$ 也都是解。</div>

<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">证</span><span class="derive-step-title">把 $L$ 作用在实部虚部上</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>$L$ 的系数是实函数，对复值函数按实部虚部分别作用：</p>
<div class="formula">$$L[\varphi+i\psi]=L[\varphi]+iL[\psi]$$</div>
<p>（因为求导、乘实系数都保持实部虚部分开。）已知左边 $=0$，即 $L[\varphi]+iL[\psi]=0$。一个复数为零当且仅当实部虚部都为零，所以 $L[\varphi]=0$、$L[\psi]=0$。$\bar z$ 同理（或由 $\bar z=\varphi-i\psi$ 直接得）。</p>
</div></div>
</div>

<p>取实部虚部，得到两个实值解：</p>
<div class="formula">$$e^{\alpha t}\cos\beta t,\qquad e^{\alpha t}\sin\beta t \tag{13.7}$$</div>
<p>这两个解线性无关（比值是 $\cot\beta t$，不是常数；$\beta\neq0$）。它们对应一对共轭复根，占两个基本解的名额。</p>

<div class="callout callout-tip"><div class="callout-title">为什么不是直接留 $e^{\alpha t}\cos\beta t+i e^{\alpha t}\sin\beta t$</div>复值解也是解，但实际问题的初始条件通常是实数（位置、速度、浓度都是实数）。若通解含复数系数，最后还要取实部，不如一开始就用实值解。用实值解写通解，$c_1,c_2$ 可以取实数。</div>

<h3>13.6 情形三：重根</h3>
<p>重根的情形要分两步看：先看最简单的"零是重根"，再看一般的重根。</p>

<h4>第一步：$\lambda=0$ 是 $k$ 重根</h4>
<p>若 $0$ 是特征方程的 $k$ 重根，由 11.4 节的重根定义，$F(\lambda)$ 含因子 $\lambda^k$：</p>
<div class="formula">$$F(\lambda)=\lambda^k\left(\lambda^{n-k}+b_1\lambda^{n-k-1}+\cdots+b_{n-k}\right)$$</div>
<p>展开对比系数可以发现：$a_n=a_{n-1}=\cdots=a_{n-k+1}=0$，也就是说方程 (13.1) 里 $x,x',\dots,x^{(k-1)}$ 的系数全为零，方程变成</p>
<div class="formula">$$\frac{d^nx}{dt^n}+a_1\frac{d^{n-1}x}{dt^{n-1}}+\cdots+a_{n-k}\frac{d^kx}{dt^k}=0$$</div>
<p>这个方程里最低阶导数是 $k$ 阶。直接看：任何不超过 $k-1$ 次的多项式，求 $k$ 阶导数都得零。所以</p>
<div class="formula">$$1,\ t,\ t^2,\ \dots,\ t^{k-1}$$</div>
<p>都是解。它们线性无关（多项式次数不同，11.6 节例 2）。这 $k$ 个解对应 $k$ 重零根。</p>

<h4>第二步：一般重根 $\lambda_1\neq0$，重数 $k$</h4>
<p>思路是"把重根移到原点"。做变量替换：</p>
<div class="formula">$$x(t)=y(t)e^{\lambda_1t} \tag{13.8}$$</div>
<p>也就是把解的指数因子先剥掉，看剩下的 $y$ 满足什么方程。</p>

<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">①</span><span class="derive-step-title">算 $x^{(m)}$ 与 $y$ 的关系</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>用莱布尼兹公式（11.7 节），取 $f=y$、$g=e^{\lambda_1t}$。$g$ 的 $j$ 阶导数是 $\lambda_1^je^{\lambda_1t}$：</p>
<div class="formula">$$x^{(m)}=\sum_{j=0}^{m}C_m^j\,y^{(m-j)}\,\lambda_1^{j}e^{\lambda_1t}=e^{\lambda_1t}\sum_{j=0}^{m}C_m^j\lambda_1^j y^{(m-j)}$$</div>
<p>换指标 $i=m-j$，写成</p>
<div class="formula">$$x^{(m)}=e^{\lambda_1t}\left[y^{(m)}+m\lambda_1y^{(m-1)}+\frac{m(m-1)}{2}\lambda_1^2y^{(m-2)}+\cdots+\lambda_1^my\right]$$</div>
<p>这就是课件上那串系数 $1,m,\frac{m(m-1)}{2!},\dots$ 的来源，正是二项式系数。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">②</span><span class="derive-step-title">代入原方程，得到 $y$ 的新方程</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>把上面每个 $x^{(m)}$ 乘 $e^{\lambda_1t}$ 提出公因子，剩下一个关于 $y$ 的算子：</p>
<div class="formula">$$L[ye^{\lambda_1t}]=\left(\frac{d^ny}{dt^n}+b_1\frac{d^{n-1}y}{dt^{n-1}}+\cdots+b_ny\right)e^{\lambda_1t}\equiv L_1[y]\,e^{\lambda_1t}$$</div>
<p>其中 $b_1,\dots,b_n$ 仍是常数（由 $a_i$ 与 $\lambda_1$ 组合而成）。于是 $L[x]=0$ 等价于</p>
<div class="formula">$$L_1[y]\equiv\frac{d^ny}{dt^n}+b_1\frac{d^{n-1}y}{dt^{n-1}}+\cdots+b_ny=0 \tag{13.9}$$</div>
</div></div>
</div>

<p>关键一步：$L_1$ 的特征多项式 $G(\mu)$ 与原来的 $F(\lambda)$ 有什么关系？</p>

<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">③</span><span class="derive-step-title">取 $y=e^{\mu t}$，两边对比</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>由式 (13.9) 的定义，把 $y=e^{\mu t}$ 代入左边：</p>
<div class="formula">$$L[\,e^{\mu t}e^{\lambda_1t}\,]=L_1[e^{\mu t}]\,e^{\lambda_1t}$$</div>
<p>左边是 $L[e^{(\mu+\lambda_1)t}]$，由 13.3 节等于 $F(\mu+\lambda_1)e^{(\mu+\lambda_1)t}$；右边是 $G(\mu)e^{\mu t}\cdot e^{\lambda_1t}=G(\mu)e^{(\mu+\lambda_1)t}$。两边同除 $e^{(\mu+\lambda_1)t}$：</p>
<div class="formula">$$F(\mu+\lambda_1)=G(\mu) \tag{13.10}$$</div>
<p>这说明 $G$ 就是 $F$ 平移到原点。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">④</span><span class="derive-step-title">重数不变，$y$ 的方程有零重根</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>$\lambda_1$ 是 $F$ 的 $k$ 重根，即 $F(\lambda)=(\lambda-\lambda_1)^kH(\lambda)$。把 $\lambda=\mu+\lambda_1$ 代入：</p>
<div class="formula">$$G(\mu)=F(\mu+\lambda_1)=\mu^kH(\mu+\lambda_1)$$</div>
<p>所以 $0$ 是 $G$ 的 $k$ 重根，即 $L_1[y]=0$ 有 $k$ 个解 $1,t,\dots,t^{k-1}$（由第一步的结论）。</p>
<p>回到 $x=ye^{\lambda_1t}$，得到原方程的 $k$ 个解：</p>
<div class="formula">$$e^{\lambda_1t},\ te^{\lambda_1t},\ t^2e^{\lambda_1t},\ \dots,\ t^{k-1}e^{\lambda_1t} \tag{13.11}$$</div>
<p>它们线性无关：若 $\sum_{j=0}^{k-1}c_jt^je^{\lambda_1t}\equiv0$，除掉非零因子 $e^{\lambda_1t}$，得 $\sum c_jt^j\equiv0$，多项式恒零则系数全零。</p>
</div></div>
</div>

<h3>13.7 复重根</h3>
<p>若 $\lambda=\alpha+i\beta$ 是 $k$ 重特征根，则 $\bar\lambda=\alpha-i\beta$ 也是 $k$ 重（共轭配对）。由 (13.11)，对应 $2k$ 个复值解：</p>
<div class="formula">$$t^je^{(\alpha+i\beta)t},\qquad t^je^{(\alpha-i\beta)t},\qquad j=0,1,\dots,k-1$$</div>
<p>展开成三角形式：</p>
<div class="formula">$$t^je^{\alpha t}(\cos\beta t+i\sin\beta t),\qquad t^je^{\alpha t}(\cos\beta t-i\sin\beta t)$$</div>
<p>取实部、虚部（命题 14.1），得 $2k$ 个实值解：</p>
<div class="formula">$$e^{\alpha t}\cos\beta t,\ te^{\alpha t}\cos\beta t,\ \dots,\ t^{k-1}e^{\alpha t}\cos\beta t$$</div>
<div class="formula">$$e^{\alpha t}\sin\beta t,\ te^{\alpha t}\sin\beta t,\ \dots,\ t^{k-1}e^{\alpha t}\sin\beta t \tag{13.12}$$</div>
<p>这 $2k$ 个解正好补齐 $k$ 重共轭复根占的名额。</p>

<div class="callout callout-key"><div class="callout-title">汇总：基本解组怎么拼</div>
设特征根按重数分组：$\lambda_1$（重数 $k_1$）、…、$\lambda_m$（重数 $k_m$），$\sum k_j=n$，两两不同。则基本解组为
<ul>
<li>每个实根 $\lambda_j$：$e^{\lambda_jt},te^{\lambda_jt},\dots,t^{k_j-1}e^{\lambda_jt}$</li>
<li>每对共轭复根 $\alpha\pm i\beta$（重数 $k$）：$t^le^{\alpha t}\cos\beta t$ 与 $t^le^{\alpha t}\sin\beta t$，$l=0,\dots,k-1$</li>
</ul>
总数 $n$ 个，全部线性无关。
</div>

<h3>13.8 四个例题</h3>

<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">例1</span><span class="derive-step-title">$\dfrac{d^4x}{dt^4}-x=0$</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>特征方程 $\lambda^4-1=0$。分解：$(\lambda^2-1)(\lambda^2+1)=(\lambda-1)(\lambda+1)(\lambda-i)(\lambda+i)=0$。四个单根：$1,-1,i,-i$。</p>
<p>实根 $1,-1$ 给 $e^t,e^{-t}$；复根 $\pm i$（$\alpha=0,\beta=1$）给 $\cos t,\sin t$。</p>
<div class="formula">$$x=c_1e^t+c_2e^{-t}+c_3\cos t+c_4\sin t$$</div>
</div></div>

<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">例2</span><span class="derive-step-title">$\dfrac{d^3x}{dt^3}+x=0$</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>特征方程 $\lambda^3+1=0$。用立方和分解：$\lambda^3+1=(\lambda+1)(\lambda^2-\lambda+1)=0$。</p>
<p>第一个根 $\lambda_1=-1$。二次因子求根：</p>
<div class="formula">$$\lambda=\frac{1\pm\sqrt{1-4}}{2}=\frac{1\pm i\sqrt3}{2}=\frac12\pm i\frac{\sqrt3}{2}$$</div>
<p>于是 $\alpha=1/2$，$\beta=\sqrt3/2$，三个单根。</p>
<div class="formula">$$x=c_1e^{-t}+e^{t/2}\left(c_2\cos\frac{\sqrt3}{2}t+c_3\sin\frac{\sqrt3}{2}t\right)$$</div>
</div></div>

<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">例3</span><span class="derive-step-title">$\dfrac{d^3x}{dt^3}-3\dfrac{d^2x}{dt^2}+3\dfrac{dx}{dt}-x=0$</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>特征方程 $\lambda^3-3\lambda^2+3\lambda-1=0$。注意到系数 $1,-3,3,-1$ 正是 $(a-b)^3$ 的展开，所以</p>
<div class="formula">$$(\lambda-1)^3=0$$</div>
<p>$\lambda=1$ 是三重根。按 (13.11)，基本解组 $e^t,te^t,t^2e^t$：</p>
<div class="formula">$$x=(c_1+c_2t+c_3t^2)e^t$$</div>
<p>验算：令 $x=(c_1+c_2t+c_3t^2)e^t$，可以把 $c_1+c_2t+c_3t^2$ 看成 $y$，则 $x=ye^t$，而 $y$ 满足 $y'''=0$（因为 $(D-1)^3$ 作用在 $ye^t$ 上等于 $y'''e^t$），$y'''=0$ 的解正是二次多项式。</p>
</div></div>

<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">例4</span><span class="derive-step-title">$\dfrac{d^4x}{dt^4}+2\dfrac{d^2x}{dt^2}+x=0$</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>特征方程 $\lambda^4+2\lambda^2+1=0$。令 $u=\lambda^2$，得 $u^2+2u+1=(u+1)^2=0$，所以</p>
<div class="formula">$$(\lambda^2+1)^2=0$$</div>
<p>$\lambda=\pm i$ 各是二重根（因为 $(\lambda-i)^2(\lambda+i)^2$）。</p>
<p>由 (13.12)，$\alpha=0,\beta=1,k=2$，四个实值解：</p>
<div class="formula">$$\cos t,\ t\cos t,\ \sin t,\ t\sin t$$</div>
<div class="formula">$$x=(c_1+c_2t)\cos t+(c_3+c_4t)\sin t$$</div>
<p>验算思路：$(D^2+1)^2x=0$。令 $u=(D^2+1)x$，则 $(D^2+1)u=0$，$u=A\cos t+B\sin t$；再解 $(D^2+1)x=u$，共振情形会产生 $t\cos t,t\sin t$ 项，正是上式。</p>
</div></div>
</div>

<h3>13.9 本章小结与判别流程</h3>
<table>
<colgroup><col style="width:26%"><col style="width:34%"><col style="width:40%"></colgroup>
<thead><tr><th>特征根</th><th>对应解</th><th>个数</th></tr></thead>
<tbody>
<tr><td>单实根 $\lambda$</td><td>$e^{\lambda t}$</td><td>1</td></tr>
<tr><td>单复根 $\alpha\pm i\beta$</td><td>$e^{\alpha t}\cos\beta t$、$e^{\alpha t}\sin\beta t$</td><td>2</td></tr>
<tr><td>$k$ 重实根 $\lambda$</td><td>$e^{\lambda t},te^{\lambda t},\dots,t^{k-1}e^{\lambda t}$</td><td>$k$</td></tr>
<tr><td>$k$ 重复根 $\alpha\pm i\beta$</td><td>$t^le^{\alpha t}\cos\beta t$、$t^le^{\alpha t}\sin\beta t$（$l=0..k-1$）</td><td>$2k$</td></tr>
</tbody>
</table>

<p>操作顺序：写特征方程 → 求全部根（含重数）→ 按上表拼解 → 数够 $n$ 个 → 写通解。</p>

<h3>13.10 自测</h3>
<div class="qa-item"><div class="qa-q">1. 方程 $x''-4x'+4x=0$ 的特征根是什么？通解？</div><div class="qa-a">$\lambda^2-4\lambda+4=(\lambda-2)^2=0$，$\lambda=2$ 是二重根。通解 $x=(c_1+c_2t)e^{2t}$。</div></div>
<div class="qa-item"><div class="qa-q">2. 为什么 $x''+x=0$ 不能写成 $x=c_1e^{it}+c_2e^{-it}$ 就结束？</div><div class="qa-a">可以，但 $c_1,c_2$ 会是复数。实际问题的初始条件通常是实数，需要实值通解。用欧拉公式把 $e^{\pm it}$ 拆开，取实部虚部得到 $\cos t,\sin t$，$c_1,c_2$ 就能取实数，物理意义也更清楚。</div></div>
<div class="qa-item"><div class="qa-q">3. 特征方程有 $\lambda=0$ 的三重根，会给出哪三个解？对方程的形状有什么要求？</div><div class="qa-a">给出 $1,t,t^2$。要求方程中 $x,x',x''$ 的系数都为零，即方程最低阶导数是三阶：$x'''+\cdots=0$。</div></div>
<div class="qa-item"><div class="qa-q">4. 方程 $x'''+x''=0$ 的通解是什么？</div><div class="qa-a">特征方程 $\lambda^3+\lambda^2=\lambda^2(\lambda+1)=0$。$\lambda=0$ 是二重根，给 $1,t$；$\lambda=-1$ 单根给 $e^{-t}$。通解 $x=c_1+c_2t+c_3e^{-t}$。验算：$x'''= -c_3e^{-t}$，$x''=c_3e^{-t}$，相加为零 ✓。</div></div>
<div class="qa-item"><div class="qa-q">5. 若已知 $x'''-3x''+3x'-x=0$ 的一个解是 $e^t$，能否直接断言 $(c_1+c_2t+c_3t^2)e^t$ 是通解？</div><div class="qa-a">不能只凭一个解断言。需要验证 $1$ 是特征方程的三重根（$\lambda^3-3\lambda^2+3\lambda-1=(\lambda-1)^3$），这时才能按重根表写出三个解 $e^t,te^t,t^2e^t$ 并确认它们无关。</div></div>

<div class="chapter-nav"></div>
</section>
"""
