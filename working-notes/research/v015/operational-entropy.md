# Fixed Observational Entropy and Measurement Access

This is the original kinematic two-qubit illustration, not the finite-time
Bell minimum. The supplied embeddings are not selected by dynamics.
Use computational order $(00,01,10,11)$, $\Phi^\pm=(00\pm11)/\sqrt2$,
$U=(\Phi^+,\Phi^-,01,10)$, $W\in\{I,U\}$, and
$\rho_p=(1-p)|\Phi^+\rangle\langle\Phi^+|+pI_4/4$, $0\le p\le1$.
Thus $U^\dagger\rho_pU=(1-p)|00\rangle\langle00|+pI_4/4$.

## Fixed Protocol and Exact Entropies

For a POVM $C=\{E_i\}$, define
$S_C(\tau)=-\sum_i\pi_i\log_2(\pi_i/V_i)$,
$\pi_i=\operatorname{Tr}(\tau E_i)$ and $V_i=\operatorname{Tr}E_i$,
using the ordinary global trace and zero-probability terms equal to zero.
This established definition, not a new cosmological $S_{\rm eff}$, follows
[Buscemi et al., Definition 1](https://arxiv.org/html/2209.03803v2#S3).
Choose one Pauli axis uniformly, measure its sign, and retain both labels:

$$
E^{W,\eta}_{a,s}=\frac16W[(I_2+s\eta\sigma_a)\otimes I_2]W^\dagger,
\quad a=X,Y,Z,\quad s=\pm1,\quad0\le\eta\le1.
$$

These are alternatives, not serial measurements. Each effect has volume
$2/3$ and eigenvalues $(1\pm\eta)/6$, each twice; their sum is $I_4$.
For arbitrary $\tau$, write $\tau_A^W=(I+\mathbf r\cdot\boldsymbol\sigma)/2$
and $f(x)=h_2((1+x)/2)$, where $h_2(z)=-z\log_2z-(1-z)\log_2(1-z)$.
Then $\pi_{a,s}=(1+s\eta r_a)/6$, and directly

$$
S_{\rm main}^W(\tau)=1+\frac13\sum_a f(\eta r_a),\qquad
S_a^W(\tau)=1+f(\eta r_a)
$$

for the main and single-axis POVMs. The random-axis Shannon term
$\log_2 3$ cancels its volume term; the inaccessible factor contributes
one bit, not a subtraction. Put $q=1-p$, $x=\eta q$.
Old/new Bloch vectors are $0$ and $(0,0,q)$, so

$$
S_{\rm main}^{I}=2,\quad S_{\rm main}^{U}=\frac53+\frac13f(x),\quad
\Delta S=\frac{1-f(x)}3,\quad
(S_X^U,S_Y^U,S_Z^U)=(2,2,1+f(x)).
$$

The global spectrum is $(1-3p/4,p/4,p/4,p/4)$ and its entropy is
$h_2(3p/4)+(3p/4)\log_2 3$ in both embeddings. Reduced entropies are
$1$ and $f(q)=h_2(p/2)$; for $p>0$ these are not entanglement measures.
At $(p,\eta)=(0,1)$ the main entropies are $2,5/3$, a $1/3$-bit contrast,
while reduced entropies are $1,0$ and global entropy is zero.
The contrast is positive exactly for $p<1,\eta>0$ in this stipulated
white-noise/unsharpness family and tends to zero at its boundary.
No arbitrary-noise robustness or finite-sample detectability is established.

Forgetting the axis but retaining sign gives $1+f(\eta\sum_ar_a/3)$:
old $2$, new $1+f(x/3)$. Forgetting the sign or all outcomes gives $2$.
Generally $S_C=2-D_{\rm cl}(\boldsymbol\pi\Vert\mathbf V/4)$; classical
postprocessing sends both distributions through the same stochastic map.
The log-sum inequality therefore proves $S_{\rm coarse}\ge S_{\rm refined}$,
consistent with [Buscemi et al., section 6](https://arxiv.org/html/2209.03803v2#S6).
Simultaneously conjugating state and effects preserves probabilities and
volumes; the old/new comparison instead keeps the state fixed.

The Petz coarse state $\rho_{\rm P}=\sum_i\pi_i E_i/V_i$ obeys
$S(\tau)\le S_C(\tau)\le S(\rho_{\rm P})\le2$ by relative-entropy data
processing, but its entropy need not equal $S_C$ for a general POVM.
For this main measurement,

$$
\rho_{\rm P}^W=W\left[\frac{I+\eta^2\mathbf r\cdot\boldsymbol\sigma/3}{2}
\otimes\frac{I_2}{2}\right]W^\dagger,\qquad
S(\rho_{\rm P}^W)=1+f(\eta^2|\mathbf r|/3).
$$

The ideal new value is $1+h_2(2/3)\simeq1.918296$, not $5/3$.
For a single axis it is $1+f(\eta^2r_a)$.
The algebra completion $W(\tau_A^W\otimes I_2/2)W^\dagger$ instead has
entropy $1+f(|\mathbf r|)$, the maximum-entropy extension of that marginal.
Thus $S(\tau)\le1+S(\tau_A^W)\le S_C^W(\tau)\le2$.
Neither recovered nor completion entropy defines the actual instrument output.
For $\eta>0$ the effects span the same algebra and determine its marginal,
yet changing $\eta$ changes $S_C$. A rotated Pauli frame gives
$1+\frac13\sum_a f(xn_a)$, $\sum_an_a^2=1$; equal weights do not give
general rotation invariance. The result is protocol-relative, not algebra-only.

## All-Input Local Realization

Direct conjugation gives

$$
X'=(X\otimes I+Z\otimes X)/\sqrt2,\quad
Y'=(I\otimes Y+Y\otimes Z)/\sqrt2,\quad Z'=Z\otimes Z.
$$

With $P^M_r=(I+rM)/2$, set $Q_b=(X+bZ)/\sqrt2$ and
$R_a=(Y+aZ)/\sqrt2$; both square to $I$. Fine-record Kraus operators are

$$
K^X_{b,s}=P^{Q_b}_s\otimes P^X_b,\qquad
K^Y_{a,s}=P^Y_a\otimes P^{R_a}_s,\qquad
K^Z_{a,s}=P^Z_a\otimes P^Z_{as}.
$$

For X measure B first and communicate $b$ to A; for Y measure A first
and communicate $a$ to B; for Z measure both and report their sign product.
These are complete product-projector branches. Using
$\sum_rP^M_r=I$ and $\sum_r rP^M_r=M$ gives, for every $j,s$,

$$
\sum_r(K^j_{r,s})^\dagger K^j_{r,s}
=\frac{I_4+sO'_j}{2}=F'_{j,s},\qquad \sum_sF'_{j,s}=I_4.
$$

This operator equality proves the probabilities for every input density
matrix, including entangled inputs. Independent uniform axis choice gives
Kraus operators $K^j_{r,s}/\sqrt3$ and the required effects $F'_{j,s}/3$.
State-independent sign flips $T_\eta(s|t)=(1+\eta st)/2$ give Kraus operators
$\sqrt{T_\eta(s|t)}K^j_{r,t}$ and
$F'_{j,s}(\eta)=(I_4+s\eta O'_j)/2$ for every $0\le\eta\le1$.
No inter-qubit gate, quantum communication between the original subsystems,
or extra shared entangled ancilla is
needed for these statistics; both local systems, adaptive measurements,
classical messages and records are required by this construction.

An A-only procedure with independent local auxiliaries and no B messages has
effects $H_i\otimes I_B$, hence depends only on the A marginal.
$|00\rangle$ and $|01\rangle$ share that marginal but require conditional
positive-parity probabilities $(1+\eta)/2$ and $(1-\eta)/2$.
This rules out A-only access for every $\eta>0$; $|00\rangle,|10\rangle$
similarly rule out B-only access. At $\eta=0$, fair classical outcomes need
no input access. No minimum communication, energy, duration or gate count
is proved; tensor labels alone do not imply spatial separation.

## Statistics Do Not Determine an Instrument

The ideal sharp parity operation is $\mathcal L_s(\tau)=\Pi_s\tau\Pi_s$,
$\Pi_s=(I+sZZ)/2$. The local instrument instead is
$\mathcal I_s(\tau)=\sum_aK^Z_{a,s}\tau K^Z_{a,s}$ and loses cross terms.
On $|++\rangle$ both give parity probabilities $1/2$, but their normalized
positive outputs are $|\Phi^+\rangle\langle\Phi^+|$ and
$(|00\rangle\langle00|+|11\rangle\langle11|)/2$; negative outputs are
$|\Psi^+\rangle\langle\Psi^+|$ and the analogous $01,10$ mixture.
Every fully refined LOCC branch has product Kraus form. On a product input,
each branch is product and any grouping/postselection is separable, also
with independent local auxiliaries or separable shared ancillas. Limits
remain separable. Thus unassisted LOCC cannot implement this ideal
entangling instrument on the original A,B outputs, although it implements
its POVM. These resource definitions follow
[Chitambar et al., sections 2.1-2.3](https://arxiv.org/html/1210.4583v2#S2).
Joint control suffices: apply $U^\dagger$, a local Pauli Luders measurement,
then $U$. This sufficient construction is not a resource lower bound.

Keeping the helper record gives twelve rank-one effects of volume $1/3$.
For the ideal Bell input their entropy is approximately
$1.400584$ bits, versus $5/3$ after
merging to $(j,s)$. This is a different refined report, not a retuned main
protocol. Ignoring records does not erase physical memory or restore coherence.
Neither reported entropy is a postmeasurement entropy, heat-removal budget,
thermodynamic reset or transition. Tomographic statistics do not establish
arbitrary coherent control of the new subsystem.

The [entropy](observational_entropy_checks.py) and
[access](measurement_access_checks.py) scripts check fixed matrices and grids;
all-input/all-sharpness statements rely on the analytic identities above.
See [README](README.md) for dependencies and internal AI-review limits.
Physical access changes, algebra selection and a cosmological entropy remain
unprovided. These finite examples neither prove nor refute ICC in general.
