# -*- coding: utf-8 -*-
CH_I = r"""
<section class="chapter" id="const-nonhomo" style="display:none">
<div class="breadcrumb"></div>
<h2><span class="num">14</span>常系数非齐次：待定系数法</h2>
<p class="lead">非齐次方程 $L[x]=f(t)$ 只需要一个特解。当 $f$ 是"多项式乘指数"或"指数乘三角"时，特解的形状可以照抄 $f$ 再乘一个 $t^k$，剩下的只是算系数。这一章把"为什么能照抄"和"$k$ 从哪来"推清楚。对应课件 chapter4-2-2。</p>

<div class="callout callout-tip">
<div class="callout-title">生活直觉：照着输入的样子猜输出</div>敲一个频率，系统按同一频率振动。输入是 $e^{3t}$，输出也含 $e^{3t}$；输入是 $\cos 2t$，输出也是 $\cos 2t$ 与 $\sin 2t$ 的组合。待定系数法就是"按输入的频率猜输出形状，只把振幅留作未知数"。唯一例外是输入的频率正好撞上系统的固有频率（特征根），这时振幅会随时间线性增长，需要多乘一个 $t$。
</div>

<div class="callout callout-warn"><div class="callout-title">前置知识</div>第 11 章的莱布尼兹公式、欧拉公式、重根判别；第 13 章的特征方程与基本解组；第 12 章的非齐次通解结构。</div>

<h3>14.1 问题与思路</h3>
<p>要解</p>
<div class="formula">$$L[x]=\frac{d^nx}{dt^n}+a_1\frac{d^{n-1}x}{dt^{n-1}}+\cdots+a_nx=f(t) \tag{14.1}$$</div>
<p>由 12.7 节，通解 = 齐次通解 + 一个特解。齐次部分第 13 章已解决。现在只找特解。</p>
<p>思路：观察 $f$ 的形状，猜一个同形状的 $x$，代进去比较系数，把未知系数解出来。这个方法叫<strong>待定系数法</strong>，课件里也叫比较系数法。</p>

<h3>14.2 类型 I：$f(t)=P_m(t)e^{\lambda t}$</h3>
<p>其中 $P_m(t)=b_0t^m+b_1t^{m-1}+\cdots+b_m$ 是 $m$ 次多项式，$\lambda$ 是实常数（后面会推广到复数）。</p>
<p>先猜特解的形状。因为 $f$ 里有 $e^{\lambda t}$，而 $L$ 作用在 $e^{\lambda t}$ 上只提出 $F(\lambda)$，所以自然猜</p>
<div class="formula">$$\tilde x(t)=P(t)e^{\lambda t} \tag{14.2}$$</div>
<p>其中 $P(t)$ 是待定系数的多项式，次数先不定。</p>

<h4>推导：$L[P e^{\lambda t}]$ 展开成什么</h4>
<p>用莱布尼兹公式逐项算 $L[Pe^{\lambda t}]$。先看最高阶项：</p>
<div class="formula">$$\frac{d^n}{dt^n}(Pe^{\lambda t})=\sum_{k=0}^{n}C_n^kP^{(k)}\lambda^{n-k}e^{\lambda t}$$</div>
<p>低阶项同理，第 $n-j$ 阶导数给出 $\sum_{k=0}^{n-j}C_{n-j}^kP^{(k)}\lambda^{n-j-k}e^{\lambda t}$。把所有项按 $P^{(k)}$ 归并，$P^{(k)}$ 的系数是</p>
<div class="formula">$$c_k=\sum_{j=0}^{n-k}a_j\,C_{n-j}^{k}\,\lambda^{n-j-k},\qquad a_0=1$$</div>
<p>这个和式可以认出来：它等于 $\dfrac{1}{k!}F^{(k)}(\lambda)$。理由是 $F(\lambda)=\sum_{j=0}^{n}a_j\lambda^{n-j}$ 求 $k$ 阶导，每项 $\lambda^{n-j}$ 求 $k$ 次导得 $(n-j)(n-j-1)\cdots(n-j-k+1)\lambda^{n-j-k}$，前面的连乘等于 $k!\,C_{n-j}^{k}$。除以 $k!$ 正好是 $C_{n-j}^k$。</p>
<p>于是得到核心公式：</p>
<div class="formula">$$L[Pe^{\lambda t}]=e^{\lambda t}\left[P(t)F(\lambda)+P'(t)F'(\lambda)+\frac{P''(t)}{2!}F''(\lambda)+\cdots+\frac{P^{(n)}(t)}{n!}F^{(n)}(\lambda)\right] \tag{14.3}$$</div>

<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">用 $n=2$ 验证公式</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>设 $L[x]=x''+a_1x'+a_2x$，$F(\lambda)=\lambda^2+a_1\lambda+a_2$。逐项算 $L[Pe^{\lambda t}]$：</p>
<p>$x''=(P''+2\lambda P'+\lambda^2P)e^{\lambda t}$（莱布尼兹，$n=2$ 展开三项）；</p>
<p>$a_1x'=a_1(P'+\lambda P)e^{\lambda t}$；$a_2x=a_2Pe^{\lambda t}$。</p>
<p>合并，按 $P,P',P''$ 归并：</p>
<div class="formula">$$P(\lambda^2+a_1\lambda+a_2)+P'(2\lambda+a_1)+P''$$</div>
<p>而 $F(\lambda)=\lambda^2+a_1\lambda+a_2$，$F'(\lambda)=2\lambda+a_1$，$F''(\lambda)=2$，所以后两项是 $P'F'+P''\cdot F''/2!=P'F'+P''$。与 (14.3) 一致。</p>
</div></div>
</div>

<h4>三种情况决定 $P$ 的次数</h4>
<p>把 (14.3) 代进方程，两边除掉 $e^{\lambda t}$（非零），得</p>
<div class="formula">$$P F(\lambda)+P'F'(\lambda)+\frac{P''}{2!}F''(\lambda)+\cdots=P_m(t) \tag{14.4}$$</div>
<p>右边是 $m$ 次多项式。左边的次数由 $P$ 的次数和 $F$ 在 $\lambda$ 处的取值决定。</p>

<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">情形A</span><span class="derive-step-title">$\lambda$ 不是特征根：$F(\lambda)\neq0$</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>此时 $P F(\lambda)$ 这一项系数非零，左边次数等于 $P$ 的次数（后面 $P'$、$P''$ 次数更低，不会盖过它）。右边是 $m$ 次，所以 $P$ 取 $m$ 次即可：</p>
<div class="formula">$$\tilde x=P_m(t)e^{\lambda t} \tag{14.5}$$</div>
<p>待定 $m+1$ 个系数，代入比较同次幂，得到 $m+1$ 个方程，正好定下来。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">情形B</span><span class="derive-step-title">$\lambda$ 是 $k$ 重特征根</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>由重根判别（11.4 节）：</p>
<div class="formula">$$F(\lambda)=F'(\lambda)=\cdots=F^{(k-1)}(\lambda)=0,\qquad F^{(k)}(\lambda)\neq0$$</div>
<p>代进 (14.4)，前 $k$ 项（$P,P',\dots,P^{(k-1)}$）全消失，剩下的最低非零项是 $\dfrac{P^{(k)}}{k!}F^{(k)}(\lambda)$。左边次数 = $P$ 的次数减 $k$。要与右边的 $m$ 次相等，$P$ 必须取 $m+k$ 次：</p>
<div class="formula">$$\tilde x=P_{m+k}(t)e^{\lambda t}$$</div>
<p>再进一步：$P_{m+k}$ 里低于 $k$ 次的项在求 $k$ 阶导后消失，对结果没有贡献，可以任取。为方便全取零，于是 $P_{m+k}(t)=t^kP_m(t)$：</p>
<div class="formula">$$\tilde x=t^kP_m(t)e^{\lambda t} \tag{14.6}$$</div>
<p>$k$ 就是 $\lambda$ 作为特征根的重数（不是根时 $k=0$，回到情形 A）。</p>
</div></div>
</div>

<div class="callout callout-key"><div class="callout-title">结论（类型 I）</div>对 $f(t)=P_m(t)e^{\lambda t}$，特解取
<div class="formula">$$\tilde x=t^kP_m(t)e^{\lambda t}$$</div>
其中 $P_m$ 是与 $f$ 中同次的待定多项式，$k$ 是 $\lambda$ 作为特征根的重数（不是根则 $k=0$）。</div>

<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">$x''-3x'+2x=e^{3t}$</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>特征方程 $\lambda^2-3\lambda+2=(\lambda-1)(\lambda-2)=0$，根 $1,2$。$\lambda=3$ 不是根，$k=0$，$m=0$（$P_0$ 是常数）。</p>
<p>猜 $\tilde x=Ae^{3t}$。求导：$\tilde x'=3Ae^{3t}$，$\tilde x''=9Ae^{3t}$。代入：</p>
<div class="formula">$$9Ae^{3t}-9Ae^{3t}+2Ae^{3t}=2Ae^{3t}=e^{3t}$$</div>
<p>比较系数得 $2A=1$，$A=\dfrac12$。特解 $\tilde x=\dfrac12e^{3t}$。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">同一方程，右端换成 $e^{t}$</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>$\lambda=1$ 是单根，$k=1$，$m=0$。猜 $\tilde x=Ate^t$。</p>
<p>求导：$\tilde x'=A(t+1)e^t$，$\tilde x''=A(t+2)e^t$。代入左边：</p>
<div class="formula">$$A(t+2)e^t-3A(t+1)e^t+2Ate^t=A\left[(t+2)-3(t+1)+2t\right]e^t=A(-1)e^t$$</div>
<p>要等于 $e^t$，得 $A=-1$。特解 $\tilde x=-te^t$。</p>
<p>验算：$\tilde x''-3\tilde x'+2\tilde x=-[(t+2)-3(t+1)+2t]e^t=-(-1)e^t=e^t$ ✓。注意乘了 $t$ 之后，原来的"抵消"没有完全抵消，剩下常数 $-1$，这正是共振时能解出系数的原因。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">右端是 $t^2$ 时的次数判断</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>方程 $x''-3x'+2x=t^2$。这里 $\lambda=0$（$e^{0t}=1$），而 $0$ 不是特征根（根是 1、2），$k=0$，$m=2$。猜二次多项式：</p>
<div class="formula">$$\tilde x=at^2+bt+c$$</div>
<p>$\tilde x'=2at+b$，$\tilde x''=2a$。代入：</p>
<div class="formula">$$2a-3(2at+b)+2(at^2+bt+c)=2at^2+(2b-6a)t+(2a-3b+2c)=t^2$$</div>
<p>比较系数：$2a=1\Rightarrow a=1/2$；$2b-6a=0\Rightarrow b=3a=3/2$；$2a-3b+2c=0\Rightarrow c=(3b-2a)/2=(9/2-1)/2=7/4$。</p>
<p>特解 $\tilde x=\dfrac12t^2+\dfrac32t+\dfrac74$。</p>
</div></div>
</div>

<h3>14.3 类型 II：$f(t)=[A(t)\cos\beta t+B(t)\sin\beta t]e^{\alpha t}$</h3>
<p>其中 $A(t),B(t)$ 是实系数多项式，最高次数为 $m$；$\alpha,\beta$ 是实常数，$\beta\neq0$。</p>
<p>右端同时含 $\cos$ 和 $\sin$，直接猜 $P\cos\beta t+Q\sin\beta t$ 也能做，但推导会落到四个系数互相缠绕。更省事的办法是先用欧拉公式把它拆成两个复指数。</p>

<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">①</span><span class="derive-step-title">用欧拉公式拆开</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>由 (11.2)：$\cos\beta t=\dfrac{e^{i\beta t}+e^{-i\beta t}}{2}$，$\sin\beta t=\dfrac{e^{i\beta t}-e^{-i\beta t}}{2i}$。代入 $f$：</p>
<div class="formula">$$f=e^{\alpha t}\left[A(t)\frac{e^{i\beta t}+e^{-i\beta t}}{2}+B(t)\frac{e^{i\beta t}-e^{-i\beta t}}{2i}\right]$$</div>
<p>把含 $e^{i\beta t}$ 的项归到一起、含 $e^{-i\beta t}$ 的归到一起：</p>
<div class="formula">$$f=\left[\frac{A(t)}{2}+\frac{B(t)}{2i}\right]e^{(\alpha+i\beta)t}+\left[\frac{A(t)}{2}-\frac{B(t)}{2i}\right]e^{(\alpha-i\beta)t}$$</div>
<p>记 $C(t)=\dfrac{A(t)}{2}+\dfrac{B(t)}{2i}$，则第二项的系数正好是 $\overline{C(t)}$。于是</p>
<div class="formula">$$f=C(t)e^{(\alpha+i\beta)t}+\overline{C(t)}e^{(\alpha-i\beta)t}=f_1+\overline{f_1} \tag{14.7}$$</div>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">②</span><span class="derive-step-title">拆成两个方程，各找一个解</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>由叠加原理（更准确说，由"右端相加则解相加"的性质），先解</p>
<div class="formula">$$L[x]=f_1=C(t)e^{(\alpha+i\beta)t}$$</div>
<p>$f_1$ 属于类型 I，$\lambda=\alpha+i\beta$。设其作为特征根的重数为 $k$，则它有特解</p>
<div class="formula">$$x_1=t^kR_m(t)e^{(\alpha+i\beta)t}$$</div>
<p>其中 $R_m$ 是 $m$ 次复系数多项式。</p>
<p>对共轭方程 $L[x]=\overline{f_1}$，由于 $L$ 的系数是实数，取共轭后仍是解，所以 $\overline{x_1}$ 是它的特解。</p>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">③</span><span class="derive-step-title">两个特解相加，取实形式</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>原方程的特解是 $x_1+\overline{x_1}=2\operatorname{Re}(x_1)$：</p>
<div class="formula">$$x_1+\overline{x_1}=t^k\left[R_m(t)e^{(\alpha+i\beta)t}+\overline{R_m(t)}e^{(\alpha-i\beta)t}\right]$$</div>
<p>括号里是"一个复函数加它的共轭"，等于 $2\operatorname{Re}$。把 $R_m$ 写成 $R=P_1+iQ_1$（$P_1,Q_1$ 实系数），展开后实部形如 $P(t)\cos\beta t+Q(t)\sin\beta t$，其中 $P,Q$ 是 $m$ 次实系数多项式。</p>
<p>所以特解取</p>
<div class="formula">$$\tilde x=t^k\left[P(t)\cos\beta t+Q(t)\sin\beta t\right]e^{\alpha t} \tag{14.8}$$</div>
</div></div>
</div>

<div class="callout callout-key"><div class="callout-title">结论（类型 II）</div>对 $f(t)=[A(t)\cos\beta t+B(t)\sin\beta t]e^{\alpha t}$，特解取
<div class="formula">$$\tilde x=t^k\left[P(t)\cos\beta t+Q(t)\sin\beta t\right]e^{\alpha t}$$</div>
其中 $P,Q$ 是与 $A,B$ 同次（$m$ 次）的待定实系数多项式，$k$ 是 $\alpha+i\beta$ 作为特征根的重数（不是根则 $k=0$）。</div>

<div class="callout callout-tip"><div class="callout-title">口诀的来源</div>课件总结成两句："把 $f(t)$ 抄下来（最高次幂一致），前面乘 $t^k$，$k$ 是特征根重数。"抄下来指的是同频率、同次数；乘 $t^k$ 是因为共振——输入频率撞上固有频率时，原来的猜测会被 $L$ 作用成零，必须升一次幂才能留下非零项。类型 I 和类型 II 是同一条规则，只是频率写成 $\lambda$ 还是 $\alpha+i\beta$。</div>

<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">$x''+4x'+4x=\cos 2t$</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>特征方程 $\lambda^2+4\lambda+4=(\lambda+2)^2=0$，$\lambda=-2$ 是二重根。齐次通解 $x_h=(c_1+c_2t)e^{-2t}$。</p>
<p>右端 $\cos2t=e^{0t}\cos2t$，即 $\alpha=0,\beta=2$。$\alpha+i\beta=2i$ 不是特征根（根是 $-2$），$k=0$，$m=0$（$A,B$ 都是常数）。</p>
<p>猜 $\tilde x=A\cos2t+B\sin2t$。求导：</p>
<div class="formula">$$\tilde x'=-2A\sin2t+2B\cos2t,\qquad \tilde x''=-4A\cos2t-4B\sin2t$$</div>
<p>代入 $x''+4x'+4x$：</p>
<div class="formula">$$(-4A\cos2t-4B\sin2t)+4(-2A\sin2t+2B\cos2t)+4(A\cos2t+B\sin2t)$$</div>
<p>按 $\cos2t$、$\sin2t$ 归并。$\cos2t$ 的系数：$-4A+8B+4A=8B$。$\sin2t$ 的系数：$-4B-8A+4B=-8A$。所以</p>
<div class="formula">$$8B\cos2t-8A\sin2t=\cos2t$$</div>
<p>比较：$8B=1\Rightarrow B=1/8$；$-8A=0\Rightarrow A=0$。特解 $\tilde x=\dfrac18\sin2t$。</p>
<p>通解：</p>
<div class="formula">$$x=(c_1+c_2t)e^{-2t}+\frac18\sin2t$$</div>
</div></div>
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">共振情形：$x''+4x=\cos 2t$</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>特征方程 $\lambda^2+4=0$，根 $\pm2i$。右端频率 $\alpha+i\beta=2i$ 正好是单根，$k=1$。</p>
<p>猜 $\tilde x=t(A\cos2t+B\sin2t)$。求导：</p>
<div class="formula">$$\tilde x'=A\cos2t+B\sin2t+t(-2A\sin2t+2B\cos2t)$$</div>
<div class="formula">$$\tilde x''=(-2A\sin2t+2B\cos2t)+(-2A\sin2t+2B\cos2t)+t(-4A\cos2t-4B\sin2t)$$</div>
<p>整理 $\tilde x''=(-4A\sin2t+4B\cos2t)+t(-4A\cos2t-4B\sin2t)$。</p>
<p>代入 $\tilde x''+4\tilde x$：$t$ 的系数 $-4A+4A=0$、$-4B+4B=0$，$t$ 项全部抵消；剩下</p>
<div class="formula">$$-4A\sin2t+4B\cos2t=\cos2t$$</div>
<p>比较：$4B=1\Rightarrow B=1/4$；$-4A=0\Rightarrow A=0$。特解 $\tilde x=\dfrac14t\sin2t$。</p>
<p>这个解的振幅随 $t$ 线性增长，物理上叫共振。若不加 $t$，猜 $A\cos2t+B\sin2t$ 会被 $L$ 作用成零，永远凑不出右端。</p>
</div></div>
</div>

<h3>14.4 右端是多项之和：逐项拆开</h3>
<p>若 $f=f_1+f_2$，由线性性，分别找 $L[x_1]=f_1$、$L[x_2]=f_2$ 的特解，$x_1+x_2$ 就是 $L[x]=f$ 的特解（因为 $L[x_1+x_2]=f_1+f_2$）。</p>
<div class="derive-steps">
<div class="derive-step"><div class="derive-step-header"><span class="derive-step-num">例</span><span class="derive-step-title">$x''-x=e^t+\cos t$</span><span class="derive-step-arrow">▶</span></div><div class="derive-step-body">
<p>特征根 $\pm1$。右端两项分别处理。</p>
<p>第一项 $e^t$：$\lambda=1$ 是单根，$k=1$，$m=0$，猜 $Ate^t$。代入 $x''-x$：$(Ate^t)''=A(t+2)e^t$，减 $Ate^t$ 得 $2Ae^t$。要等于 $e^t$，$A=1/2$，特解 $\dfrac12te^t$。</p>
<p>第二项 $\cos t$：$\alpha+i\beta=i$ 不是根（根是 $\pm1$），$k=0$，猜 $B\cos t+C\sin t$。代入 $x''-x$：$(-B\cos t-C\sin t)-(B\cos t+C\sin t)=-2B\cos t-2C\sin t$。要等于 $\cos t$，$B=-1/2$，$C=0$，特解 $-\dfrac12\cos t$。</p>
<p>合起来，$x=c_1e^t+c_2e^{-t}+\dfrac12te^t-\dfrac12\cos t$。</p>
</div></div>
</div>

<h3>14.5 与常数变易法的分工</h3>
<table>
<colgroup><col style="width:22%"><col style="width:38%"><col style="width:40%"></colgroup>
<thead><tr><th>方法</th><th>适用</th><th>代价</th></tr></thead>
<tbody>
<tr><td>待定系数法</td><td>常系数方程，$f$ 是多项式、指数、三角及其乘积</td><td>只需求代数方程组；不适用其他 $f$</td></tr>
<tr><td>常数变易法</td><td>任意变系数方程，任意连续 $f$</td><td>要算积分，常常积不出来</td></tr>
</tbody>
</table>
<p>两者的共同前提是"已有齐次基本解组"。若齐次方程都解不出，两条路都走不通。</p>

<h3>14.6 本章小结与自测</h3>
<table>
<colgroup><col style="width:32%"><col style="width:34%"><col style="width:34%"></colgroup>
<thead><tr><th>右端 $f(t)$</th><th>特解形式</th><th>$k$ 的取法</th></tr></thead>
<tbody>
<tr><td>$P_m(t)e^{\lambda t}$</td><td>$t^kP_m(t)e^{\lambda t}$</td><td>$\lambda$ 的重数</td></tr>
<tr><td>$[A(t)\cos\beta t+B(t)\sin\beta t]e^{\alpha t}$</td><td>$t^k[P(t)\cos\beta t+Q(t)\sin\beta t]e^{\alpha t}$</td><td>$\alpha+i\beta$ 的重数</td></tr>
<tr><td>多项相加</td><td>各项分别找特解再相加</td><td>逐项判断</td></tr>
</tbody>
</table>

<div class="qa-item"><div class="qa-q">1. $x''-2x'+x=e^{t}$，特解该怎么猜？</div><div class="qa-a">特征方程 $\lambda^2-2\lambda+1=(\lambda-1)^2=0$，$\lambda=1$ 是二重根，$k=2$。猜 $\tilde x=At^2e^t$。验算：$\tilde x'=A(t^2+2t)e^t$，$\tilde x''=A(t^2+4t+2)e^t$，代入得 $A(t^2+4t+2)-2A(t^2+2t)+At^2=2Ae^t$，$A=1/2$。</div></div>
<div class="qa-item"><div class="qa-q">2. $x''+x=t\sin t$，为什么不能只猜 $At\sin t$？</div><div class="qa-a">右端是 $t\sin t$，属于类型 II（$A=0,B=t$，$m=1$，$\alpha=0,\beta=1$）。$\alpha+i\beta=i$ 是特征根（$\lambda^2+1=0$），$k=1$。所以特解应为 $t\cdot[(at+b)\cos t+(ct+d)\sin t]$，共四个待定系数，只猜一个不够。</div></div>
<div class="qa-item"><div class="qa-q">3. 为什么类型 II 要先拆成复指数，不能直接用三角形式猜？</div><div class="qa-a">能直接用三角形式，把 $\cos$、$\sin$ 当作两个独立基函数，代入后比较 $\cos$ 与 $\sin$ 的系数，同样能解。拆成复指数是为了复用类型 I 的结论（$t^k$ 与重数的关系），推导更短，也解释了"$k$ 为什么按 $\alpha+i\beta$ 算"。</div></div>
<div class="qa-item"><div class="qa-q">4. 若右端 $f(t)=1$，$\lambda$ 取多少？$k$ 怎么定？</div><div class="qa-a">$1=P_0(t)e^{0t}$，$\lambda=0$。$k$ 是 $0$ 作为特征根的重数：若 $a_n\neq0$（$0$ 不是根），$k=0$，猜常数；若 $a_n=0$ 但 $a_{n-1}\neq0$（$0$ 是单根），$k=1$，猜 $At$。</div></div>
<div class="qa-item"><div class="qa-q">5. 判断正误：待定系数法对变系数方程也适用。</div><div class="qa-a">错。公式 (14.3) 依赖 $L$ 的系数是常数，才能把 $L[Pe^{\lambda t}]$ 整理成"$P$ 的各阶导数 × $F$ 的各阶导数"。变系数时 $F(\lambda)$ 不存在，这套展开失效。变系数只能用常数变易法或降阶法。</div></div>

<div class="chapter-nav"></div>
</section>
"""
