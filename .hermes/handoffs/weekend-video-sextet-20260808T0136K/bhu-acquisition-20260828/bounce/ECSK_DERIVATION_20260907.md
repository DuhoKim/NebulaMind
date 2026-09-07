# ECSK action → spin-fluid effective stress-energy

Independent derivation for Tori, 2026-09-07. Units are $c=1$, with $\hbar$ retained. The matter model is an ideal, minimally coupled Weyssenhoff fluid with conserved particle number and advected spin magnitude per particle. Unpolarised averaging is performed **after** eliminating torsion. No result from either excluded local derivation is used.

## 1. Action, indices, and conventions

Use signature $(-+++)$, $u^\mu u_\mu=-1$, and

\[
\kappa=8\pi G>0,\qquad
\nabla_\mu v^\rho=\partial_\mu v^\rho+\Gamma^\rho{}_{\mu\nu}v^\nu.
\]

The first lower connection index is the derivative index. The connection is metric compatible, but need not be symmetric. Define

\[
\begin{split}
R^\rho{}_{\sigma\mu\nu}
&=\partial_\mu\Gamma^\rho{}_{\nu\sigma}
-\partial_\nu\Gamma^\rho{}_{\mu\sigma}
+\Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma}
-\Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma},\\
R_{\sigma\nu}&=R^\rho{}_{\sigma\rho\nu},\qquad R=g^{\sigma\nu}R_{\sigma\nu},\\
T^\rho{}_{\mu\nu}&=2\Gamma^\rho{}_{[\mu\nu]},\qquad
T_\mu=T^\lambda{}_{\mu\lambda},\\
\Gamma^\rho{}_{\mu\nu}&=\bar\Gamma^\rho{}_{\mu\nu}+K^\rho{}_{\mu\nu}.
\end{split}
\]

Bars mean Levi-Civita quantities. Antisymmetrisation and symmetrisation include $1/2$. With all indices lowered, metric compatibility gives $K_{a c b}=-K_{b c a}$. To make the independent antisymmetric pair visible, write

\[
A_{abc}:=K_{a c b}=-A_{bac},\qquad V_b=g^{ac}A_{abc}=-T_b.
\]

Latin indices here are generic spacetime indices, or orthonormal components when evaluating contractions at a point; they have the same tensor ordering throughout.

Start with the ECSK action

\[
S[g,A,\psi]=\int d^4x\sqrt{-g}\left[\frac{R(\Gamma)}{2\kappa}
+L_m(g,\psi,\nabla\psi)\right].
\]

The spin definition and Hilbert stress convention are

\[
\delta_A S_m=\frac12\int d^4x\sqrt{-g}\,\tau^{abc}\delta A_{abc},
\quad\tau^{abc}=-\tau^{bac},\qquad
T_{\mu\nu}=-\frac{2}{\sqrt{-g}}\frac{\delta S_m}{\delta g^{\mu\nu}}.
\]

Thus in the spinless limit $\bar G_{\mu\nu}=\kappa T_{\mu\nu}$. For the first-order spin matter used here, minimal coupling is linear in the spin connection:

\[
L_m=L_m^{(0)}+\tfrac12\tau^{abc}A_{abc}.
\]

This assumption is a specification of the matter action, not a statement that every conceivable spin-carrying Lagrangian is linear in contortion.

One realisation of the fluid matter action is the material-frame form

\[
L_m=-\epsilon(n)+\frac12s_{ab}\Omega^{ab}+L_{\rm constraints},\qquad
\Omega^{ab}=u^\mu(D_\mu\Lambda^a{}_A)\Lambda^{bA}.
\]

Here $\Lambda^a{}_A$ is an orthonormal material frame, $\Lambda^a{}_0=u^a$, and $s^{ab}=n\Lambda^a{}_A\Lambda^b{}_B\sigma^{AB}$, with $\sigma^{0A}=0$. The constraints impose particle conservation, frame orthonormality, and advection of the material spin. Equivalently they can be solved using a conserved particle-current density and material-frame variables before metric variation. Entropy and spin magnitude per particle are held fixed in that variation. Since $\delta\Omega^{ab}=u^c\delta A^{ab}{}_c$, this action has

\[
\tau^{abc}=s^{ab}u^c,\qquad s^{ab}u_b=0.
\]

The second equation is the Frenkel condition. The zero-contortion action includes the rotational term and its spin transport; it is not obtained by deleting the spin degrees of freedom.

## 2. Vary and solve the connection equation

Expanding the curvature definition gives

\[
R=\bar R+g^{\sigma\nu}\left(
\bar\nabla_\rho K^\rho{}_{\nu\sigma}
-\bar\nabla_\nu K^\rho{}_{\rho\sigma}
+K^\rho{}_{\rho\lambda}K^\lambda{}_{\nu\sigma}
-K^\rho{}_{\nu\lambda}K^\lambda{}_{\rho\sigma}\right).
\]

The contractions are $K^\rho{}_{\rho\lambda}=-T_\lambda$ and $g^{\nu\sigma}K^\lambda{}_{\nu\sigma}=T^\lambda$. Consequently

\[
R=\bar R+2\bar\nabla_\mu T^\mu+Q(A),\qquad
Q=-V_aV^a-A_{abc}A^{bca}.
\]

The divergence contributes only a boundary integral. Fixing boundary variations, or taking compactly supported variations, removes it from the bulk equation. All remaining connection dependence is

\[
L_{\rm aux}=\frac{1}{2\kappa}(-V^2-A_{abc}A^{bca})
+\frac12\tau^{abc}A_{abc}.
\]

In particular, there are **no derivatives of $A$** in this bulk Lagrangian. To vary it, use $\delta V_b=g^{ac}\delta A_{abc}$ and the antisymmetry of $\delta A_{abc}$. Then

\[
\begin{split}
\delta(-V^2)&=(g^{bc}V^a-g^{ac}V^b)\delta A_{abc},\\
\delta(-A_{abc}A^{bca})&=-(A^{bca}+A^{cab})\delta A_{abc}.
\end{split}
\]

Stationarity therefore requires

\[
A_{bca}+A_{cab}-g_{bc}V_a+g_{ac}V_b=\kappa\tau_{abc}.\tag{1}
\]

Since $T_{cab}=-(A_{bca}+A_{cab})$ and $V_a=-T_a$, the same equation is

\[
T^c{}_{ab}+\delta^c_aT_b-\delta^c_bT_a=-\kappa\tau_{ab}{}^c.\tag{2}
\]

Put $c=b$ and sum in four dimensions. Writing $t_a:=\tau_{ab}{}^b$, the left side is $T_a+T_a-4T_a=-2T_a$, so

\[
T_a=\frac\kappa2t_a,\qquad
\boxed{T^c{}_{ab}=-\kappa\tau_{ab}{}^c
-\frac\kappa2\delta^c_a t_b+\frac\kappa2\delta^c_b t_a.}\tag{3}
\]

For completeness, add the two cyclic permutations of (1) and subtract (1). This isolates $2A_{abc}$. Substituting $V=-\kappa t/2$ gives

\[
\boxed{A^*_{abc}=\frac\kappa2\left(
\tau_{bca}+\tau_{cab}-\tau_{abc}-g_{ac}t_b+g_{bc}t_a\right).}\tag{4}
\]

This is the explicit algebraic solution. The accompanying script verifies all 24 independent variations with a general symbolic $\tau_{abc}$, including its trace, and finds rank 24 for the quadratic connection Hessian. Thus no connection mode remains undetermined in this metric-compatible problem.

## 3. Substitute back and vary the reduced action

Because (Q) is homogeneous of degree two, contracting the stationary equation with $A^*$ gives

\[
\frac{Q(A^*)}{\kappa}+\frac12\tau^{abc}A^*_{abc}=0.
\]

It follows that the **sum of the gravitational and matter connection terms** is

\[
L_{\rm contact}=\frac{Q(A^*)}{2\kappa}+\frac12\tau^{abc}A^*_{abc}
=\frac14\tau^{abc}A^*_{abc}.
\]

Define $I=\tau_{abc}\tau^{abc}$ and $J=\tau_{abc}\tau^{bca}$. The two cyclic contractions in (4) are equal after relabelling dummy indices. Also $g^{ac}\tau_{abc}=-t_b$ and $g^{bc}\tau_{abc}=t_a$. Therefore

\[
\boxed{L_{\rm contact}=\frac\kappa8F,\qquad F=2J-I+2t_at^a.}\tag{5}
\]

The reduced action is

\[
S_{\rm eff}=\int\sqrt{-g}\left(\frac{\bar R}{2\kappa}+L_m^{(0)}+\frac\kappa8F\right)d^4x.
\]

There is no extra term from varying $A^*(g,\psi)$: its coefficient is the already-satisfied connection Euler–Lagrange equation.

### Explicit general quadratic stress, with the matter variables specified

Let $T^{(0)}_{\mu\nu}:=-2(-g)^{-1/2}\delta S_m^{(0)}/\delta g^{\mu\nu}$. For clarity about what is held fixed, introduce

\[
\chi_{abc|\mu\nu}:=\left.\frac{\partial\tau_{abc}}{\partial g^{\mu\nu}}\right|_{\text{independent matter variables}}.
\]

This is the algebraic metric response of the spin current, not a new dynamical field. Define the following explicit contractions (all displayed free-index pairs are symmetrised where indicated):

\[
\begin{split}
I_{\mu\nu}&=2\tau_{(\mu|bc|}\tau_{\nu)}{}^{bc}
+\tau_{ab\mu}\tau^{ab}{}_{\nu},\\
J_{\mu\nu}&=\left[
\tau_{\mu bc}\tau^{bc}{}_{\nu}
+\tau_{a\mu c}\tau_{\nu}{}^{ca}
+\tau_{ab\mu}\tau^b{}_{\nu}{}^a\right]_{(\mu\nu)},\\
D_{\mu\nu}&=2J_{\mu\nu}-I_{\mu\nu}
+2t_\mu t_\nu+4t^a\tau_{a(\mu\nu)}.
\end{split}
\]

These follow simply by differentiating each inverse metric in $I,J,t^2$, holding the lower components $\tau_{abc}$ fixed for this part. Thus $D_{\mu\nu}=(\partial F/\partial g^{\mu\nu})_\tau$. Varying the spin factors themselves gives $\delta_\tau L_{\rm contact}=\tfrac12 A^{*abc}\delta\tau_{abc}$. Combining both parts and the volume-element variation prints the general effective tensor explicitly:

\[
\boxed{\bar G_{\mu\nu}=\kappa T^{\rm eff}_{\mu\nu},\qquad
T^{\rm eff}_{\mu\nu}=T^{(0)}_{\mu\nu}
+\frac\kappa8g_{\mu\nu}F-\frac\kappa4D_{\mu\nu}
-A^{*abc}\chi_{abc|\mu\nu}.}\tag{6}
\]

Equation (4) makes the last term explicit once the matter action fixes its spin response. If the independent variables really are lower-component spin tensors, $\chi=0$. **That choice is not the conserved-current fluid variation.** Spin alone does not specify the metric response of arbitrary matter; silently setting it to zero can change the purported pressure. For the specified fluid we can evaluate the entire response without this auxiliary notation, as follows.

### Evaluate the full quadratic tensor for the fluid action

Use $\tau_{abc}=s_{ab}u_c$, the Frenkel condition, and define

\[
s^2:=\tfrac12s_{ab}s^{ab}\geq0.
\]

Then every trace or cyclic product contains a vanishing contraction with $u$:

\[
t_a=s_{ab}u^b=0,\qquad
I=(s_{ab}s^{ab})(u_cu^c)=-2s^2,\qquad
J=s_{ab}u_c s^{bc}u^a=0.
\]

In particular, (3)–(5) reduce to

\[
T^c{}_{ab}=-\kappa s_{ab}u^c,\qquad
A^*_{abc}=\frac\kappa2(s_{bc}u_a+s_{ca}u_b-s_{ab}u_c),\qquad
L_s=\frac\kappa4s^2.\tag{7}
\]

One can also check the substitution term by term:

\[
Q(A^*)=-\frac{\kappa^2}{2}s^2,\quad
\frac12\tau A^*=\frac\kappa2s^2,\quad
\frac{Q}{2\kappa}+\frac12\tau A^*=-\frac\kappa4s^2+\frac\kappa2s^2=\frac\kappa4s^2.
\]

Now perform the fluid metric variation, rather than reading an energy density directly from this positive Lagrangian term. Hold the conserved particle-current **density** $\mathcal N^\mu=\sqrt{-g}\,nu^\mu$ and material spin per particle fixed. Its norm defines

\[
n^2=\frac{-g_{\alpha\beta}\mathcal N^\alpha\mathcal N^\beta}{-g}.
\]

Using $\delta g_{\alpha\beta}=-g_{\alpha\mu}g_{\beta\nu}\delta g^{\mu\nu}$ and $\delta\ln(-g)=-g_{\mu\nu}\delta g^{\mu\nu}$, differentiation gives

\[
\delta n^2=n^2(u_\mu u_\nu+g_{\mu\nu})\delta g^{\mu\nu},\qquad
\delta n=\frac n2h_{\mu\nu}\delta g^{\mu\nu},\quad h_{\mu\nu}=g_{\mu\nu}+u_\mu u_\nu.
\]

Frame orthonormality gives $s^2=n^2\sigma^2$, where $\sigma^2=\tfrac12\sigma_{AB}\sigma^{AB}$ is held fixed. Hence

\[
\delta s^2=2s^2\frac{\delta n}{n}=s^2h_{\mu\nu}\delta g^{\mu\nu}.
\]

Finally $\delta\sqrt{-g}=-\tfrac12\sqrt{-g}g_{\mu\nu}\delta g^{\mu\nu}$. The complete contact variation is

\[
\delta S_s=\int\sqrt{-g}\left[-\frac\kappa8s^2g_{\mu\nu}
+\frac\kappa4s^2h_{\mu\nu}\right]\delta g^{\mu\nu}d^4x.
\]

Thus the unaveraged quadratic correction and the effective Einstein equation are

\[
\boxed{T^{(s)}_{\mu\nu}=-\frac\kappa4s^2(2u_\mu u_\nu+g_{\mu\nu}),\qquad
\bar G_{\mu\nu}=\kappa\left[T^{(0)}_{\mu\nu}-\frac\kappa4s^2(2u_\mu u_\nu+g_{\mu\nu})\right].}\tag{8}
\]

This is the evaluated fluid version of (6), with its metric spin response included. $T^{(0)}$ is the complete torsion-free fluid stress, including the rotational/transport part; no assertion that a polarised, inhomogeneous spinning fluid is an ordinary perfect fluid is needed.

## 4. Unpolarised homogeneous average; density and pressure

Let $S_2:=\langle s^2\rangle$. Isotropy and the Frenkel condition imply

\[
\langle s_{\mu\nu}\rangle=0,\qquad
\langle s_{\mu\nu}s_{\alpha\beta}\rangle
=\frac{S_2}{3}(h_{\mu\alpha}h_{\nu\beta}-h_{\mu\beta}h_{\nu\alpha}).
\]

The coefficient follows by contracting both pairs: the projector has rank three, so the right side contracts to $S_2(9-3)/3=2S_2$, as required by the definition. It also gives $\langle s_{\mu\lambda}s_\nu{}^\lambda\rangle=2S_2h_{\mu\nu}/3$. In the ideal homogeneous ensemble, gradients and velocities do not correlate with a preferred spin orientation. The terms linear in spin from the zero-contortion rotational action consequently average to zero, leaving $\langle T^{(0)}_{\mu\nu}\rangle=(\epsilon+p)u_\mu u_\nu+pg_{\mu\nu}$. The quadratic term survives. Equation (8) becomes

\[
\boxed{\langle T^{\rm eff}_{\mu\nu}\rangle
=\left(\epsilon+p-\frac\kappa2S_2\right)u_\mu u_\nu
+\left(p-\frac\kappa4S_2\right)g_{\mu\nu}.}\tag{9}
\]

Use the invariant definitions $\epsilon_s=u^\mu u^\nu T^{(s)}_{\mu\nu}$ and $p_s=\tfrac13h^{\mu\nu}T^{(s)}_{\mu\nu}$. Since $u^\mu u^\nu(2u_\mu u_\nu+g_{\mu\nu})=2-1=1$, whereas $h^{\mu\nu}u_\nu=0$ and $h^{\mu\nu}g_{\mu\nu}=3$,

\[
\boxed{\epsilon_s=-\frac\kappa4S_2,\qquad p_s=-\frac\kappa4S_2,\qquad w_s=\frac{p_s}{\epsilon_s}=1.}\tag{10}
\]

This ratio is defined for nonzero spin variance. At zero variance both corrections vanish and their ratio is undefined.

For advected spin per particle, $S_2=Cn^2$, $C=\langle\sigma^2\rangle>0$ constant. A commonly used spin-1/2 fluid closure is $C=\hbar^2/8$. With this closure,

\[
\boxed{\epsilon_s=p_s=-\frac{\kappa\hbar^2}{32}n^2.}\tag{11}
\]

The numerical closure $C=\hbar^2/8$ is an additional microscopic averaging prescription, **not** something that follows from the gravitational action or from isotropy alone. An unpolarised state specifies a zero first moment; it does not uniquely specify a local spin-density correlator, its coarse graining, or a quantum four-fermion expectation value. Equations (8)–(10) are derived without assigning $C$. Adopting a different positive, constant normalisation changes (11)'s coefficient, but not (10) or $w_s$. No identification of a microscopic Dirac axial current with a Weyssenhoff convective current is assumed.

An independent pressure derivation is obtained directly from the reduced fluid energy function. Since $L_s=+\kappa Cn^2/4$ adds to $L=-\epsilon(n)$,

\[
\epsilon_s(n)=-\kappa Cn^2/4,\qquad
p_s=n\frac{d\epsilon_s}{dn}-\epsilon_s
=-\frac\kappa2Cn^2+\frac\kappa4Cn^2=-\frac\kappa4Cn^2.
\]

The pressure identity itself follows from $E_s=V\epsilon_s(N/V)$ at fixed particle number: $-\partial E_s/\partial V=n\epsilon_s'-\epsilon_s$. It is therefore another variation, not an imposed equation of state.

## 5. Continuity check and the opposite-sign trial

For $ds^2=-dt^2+a(t)^2d\boldsymbol x^2$, conserved particle number gives

\[
0=\bar\nabla_\mu(nu^\mu)=\frac1{a^3}\frac{d(a^3n)}{dt},\quad
\dot n=-3Hn,\quad n=n_0(a_0/a)^3.
\]

Write $A_s=\kappa C/4>0$. The derived pair is $\epsilon_s=p_s=-A_sn^2$. Direct substitution yields

\[
\dot\epsilon_s=-2A_sn\dot n=+6HA_sn^2=-6H\epsilon_s,
\]

\[
\boxed{\dot\epsilon_s+3H(\epsilon_s+p_s)
=6HA_sn^2+3H(-2A_sn^2)=0.}\tag{12}
\]

Thus the spin contribution is separately conserved under the stated homogeneous, fixed-$C$, conserved-number assumptions. It scales as $a^{-6}$. The total Bianchi identity also then implies the usual continuity equation for the remaining fluid sector. Separate conservation has been checked here, rather than inferred from total conservation alone.

For comparison, try $p_s=-\epsilon_s=+A_sn^2$ while retaining the same $\epsilon_s(n)$ and particle conservation. The residual becomes

\[
\dot\epsilon_s+3H(\epsilon_s-\epsilon_s)
=6HA_sn^2=-6H\epsilon_s\ne0
\]

in a nonstatic universe with nonzero spin variance. That trial would require an energy-transfer source $Q_s=6HA_sn^2$ and an opposite source in another sector. Such a transfer is absent from this ideal fluid model. More generally, allowing $\dot n+3Hn=\Psi$ or a time-dependent $C$ changes the residual of the equal-pressure pair to

\[
-\frac\kappa4n^2\dot C-\frac\kappa2Cn\Psi.
\]

These are additional physical assumptions, not alternative index conventions.

As an additional action-level check, introduce a lapse $\mathcal L$ and a fixed comoving particle number $N$. Per unit comoving volume,

\[
L_{s,\rm mini}=\mathcal L a^3\frac{\kappa C}{4}(N/a^3)^2
=\frac{\mathcal L\kappa CN^2}{4a^3}.
\]

The stress definition gives

\[
\epsilon_s=-\frac1{a^3}\frac{\partial L_{s,\rm mini}}{\partial\mathcal L}
=-\frac{\kappa CN^2}{4a^6},\qquad
p_s=\frac1{3\mathcal L a^2}\frac{\partial L_{s,\rm mini}}{\partial a}
=-\frac{\kappa CN^2}{4a^6}.
\]

This obtains pressure without invoking the continuity equation.

## 6. Verdict, then published-convention check

The derivation gives the effective pressure correction the SAME sign as the effective density correction.

This supports the published **negative stiff-spin Weyssenhoff convention**, with both corrections negative and $w_s=1$. As checks only: Bréchet, Hobson and Lasenby, *Weyssenhoff fluid dynamics in general relativity using a 1+3 covariant approach*, equations (24)–(25), give equal negative spin-squared shifts (their spin normalisation differs); Hashemi, Jalalzadeh and Ziaie, *Collapse and dispersal of a homogeneous spin fluid in Einstein–Cartan theory*, section 2, equation (9), give the explicit $ -\kappa S^2/4$ shifts in signature (+---). The latter's equation (15) also records the $\hbar^2/8$ averaging prescription. [Bréchet–Hobson–Lasenby (2007)](https://arxiv.org/pdf/0706.2367), [Hashemi–Jalalzadeh–Ziaie (2015)](https://link.springer.com/article/10.1140/epjc/s10052-015-3276-1).

These references check the derived result; neither supplies any algebraic step above. Neither Poplawski paper is used to decide the sign.

## 7. What convention changes can and cannot flip

- Reversing the definition of $R^\rho{}_{\sigma\mu\nu}$ requires reversing the Einstein–Hilbert prefactor to represent the same attractive-gravity theory. Doing both preserves (10). Reversing only the prefactor of the quadratic connection action changes the solution and contact Lagrangian sign, and flips **both** corrections; it is a changed action, not a consistent convention translation.
- Reversing the definition of spin or the sign of its linear coupling reverses (3)–(4) but leaves the quadratic contact result invariant. Defining torsion as $\Gamma_{[\mu\nu]}$ instead of $2\Gamma_{[\mu\nu]}$ changes the displayed Cartan coefficient by two, not the physical pressure sign.
- In signature (+---), the perfect-fluid decomposition is $T_{\mu\nu}=(\epsilon+p)u_\mu u_\nu-pg_{\mu\nu}$, with the correspondingly consistent action/stress convention. The coefficient of $g_{\mu\nu}$ then looks different; the invariant measured pressure and density corrections still obey (10). Reading that coefficient as (+p) would create a false sign disagreement. Likewise $T^0{}_0=-\epsilon$ in the signature used here; it is not $+\epsilon$.
- Holding $s^2$ artificially metric independent in (7) would give $T^{(s)}_{\mu\nu}=L_sg_{\mu\nu}$, hence $\epsilon_s=-L_s$, $p_s=+L_s$. This is precisely the missing-density-variation error for the stated fluid: it drops $\delta s^2=s^2h_{\mu\nu}\delta g^{\mu\nu}$. A truly constant scalar vacuum term is a different matter model and would not scale as $n^2\propto a^{-6}$.

No consistent signature, curvature, spin-sign, or torsion-normalisation convention turns the relative sign in this fixed physical model from equal to opposite.

## 8. Reproduction

From `bounce/`, run `/usr/bin/python3 ecsk_derive.py`. It uses the installed SymPy, disables bytecode caching before importing it, performs no file writes, and prints the results to standard output. It verifies the general connection variation and solution, the eliminated quadratic action, its fluid specialisation, both fluid-stress projections, the lapse/scale-factor variations, and both continuity residuals. The completed run returned exit status 0 and printed:

```text
Algebraic contortion Hessian rank: 24 / 24
eps_s = -C*kappa*n**2/4
p_s   = -C*kappa*n**2/4
w = 1
For the conventional closure C = hbar^2/8:
eps_s = -hbar**2*kappa*n**2/32
p_s   = -hbar**2*kappa*n**2/32
Continuity residual = 0
Opposite-pressure trial residual = 3*C*H*kappa*n**2/2
```
