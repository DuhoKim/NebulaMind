URL: https://arxiv.org/pdf/2210.07212

# Haptic Teleoperation goes Wireless: Evaluation and Benchmarking of a High-Performance Low-Power Wireless Control Technology

y y
Joseph Bolarinwa , Alex Smith , Adnan Aijaz, Aleksandar Stanoev,
<sup>y</sup>
Mahesh Soori<sup>y</sup>abandara, Manuel Giuliani

Bristol Robotics Laboratory, University of the West of England, Bristol, United Kingdom
<sup>y</sup>
Bristol Research and Innovation Laboratory, Toshiba Europe Ltd., Bristol, United Kingdom
firstname.lastname@brl.ac.uk; firstname.lastname@toshiba-bril.com

## Abstract

**—Communication delays and packet losses are com-**
**monly investigated issues in the area of robotic teleoperation.**
**This paper investigates application of a novel low-power wireless**
**control technology (GALLOP) in a haptic teleoperation scenario**
**developed to aid in nuclear decommissioning. The new wireless**
**control protocol, which is based on an off-the-shelf Bluetooth**
**chipset, is compared against standard implementations of wired**
**and wireless TCP/IP data transport. Results, through objective**
**and subjective data, show that GALLOP can be a reasonable**
**substitute for a wired TCP/IP connection, and performs better**
**than a standard wireless TCP/IP method based on Wi-Fi**
**connectivity.**

***Index Terms*****—automation, haptics, low-power, robotics, nu-**
**clear decommissioning, teleoperation, wireless control.**

## I. INTRODUCTION

Robot teleoperation, which involves the remote manipulation of robotic systems, continues to find application in
different fields of robotics including industrial robots [1],
mobile ground robots [2], [3], assistive robots [4], medical
and surgical robots [5] [6], robots for nuclear environments
[7], [8], and telepresence robots [9]. Depending on the
application, the leader and follower robots (that form the teleoperation system) may be situated in the same environment
(with physical obstruction between the teleoperator and the
arXiv:2210.07212v1  [cs.NI]  13 Oct 2022robot) [10]–[12], or thousands of miles away from each other
[13]. In robot teleoperation, the teleoperator sends position
and control commands and in turn receives visual and other
sensory feedback information from the remote end.

Applications that involve the teleoperation of a robot
within the same local environment as the operator [10] may
allow for wired connectivity between the teleoperated robot
and the operators’ control base. However, other applications
may require that the operator controls a robot many miles
away, or may encounter limitations to wired connectivity such
as limited cable length or cable disconnect. In such cases,
wireless robot teleoperation may be explored.

One of such applications where wireless robot teleoperation is currently being explored is in nuclear decommissioning, due to the health implications of exposure to nuclear radiations. However, the complexities of nuclear facilities and the

risk of cable disconnect create doubts on the sole use of wired
connectivity, hence the need to explore wireless robot teleoperation. Due to the real-time control-data communication
requirements of robot teleoperation, wireless communication
systems replacing the existing wired communication systems
should have similar or better performance, particularly in
terms of end-to-end delay/latency, jitter (latency variations),
and congestion.

To this end, the main objective of this paper is to report
the key differences in performance between wired and wireless communication protocols. We present our design and
implementation of the TCP/IP protocol for wired and wireless
robot teleoperation and an implementation of the GALLOP
wireless control protocol [14] for robot teleoperation - in
particular we aim to show that the novel GALLOP protocol
can be considered as a wireless alternative to a wired connection without loss of control quality. We compared how
long it takes to send and receive data between the leader and
follower robots, as well as the position and velocity errors
for all the protocols examined. We also report on a heuristic
evaluation of the wired and wireless robot teleoperation.
In the heuristic evaluation, we examined how responsive
the follower robot is to changes at the leader robot, the
smoothness of the control, and the safety of the control. For
clarity, wired TCP/IP and wireless TCP/IP (based on standard
Wi-Fi) are simply referred to as wired/wireless respectively
through the rest of this paper.

It is emphasized that low-power wireless technologies are
predominantly used for monitoring and non-critical applications. To the best of our knowledge, this is one of the first
works employing a low-power wireless control technology
(implemented on an off-the-shelf Bluetooth chipset) for haptic teleoperation in a real-world test bed.

## II. RELATED WORK

## A. Wireless Technologies for Teleoperation

Wireless communication technologies have evolved at an
unprecedented pace over the past three decades. Wireless technologies have also been used to transmit haptic information (kinesthetic and tactile) between leader robots and
follower robots. Bilateral haptic communication implies that
the interactions between the follower robot and the remote
environment reflect back to the operator, hence influencing
how the operator reacts. In order to enable real-time interactions as well as to provide system stability and transparency,
bilateral haptic feedback control loops for the leader and
follower robots impose a 1 kHz frequency update rate [15].
It is therefore vital to consider how network conditions might
affect haptic applications when choosing communication
protocols for teleoperation in order to provide high quality of
experience (QoE). Different protocols have been developed
with respect to the Internet protocol suite networking model
[16].

TCP and UDP protocols are the most commonly used
transport layer protocols for haptic communication to demonstrate physical interactions between human operators and
remote environments or for communication between physical
devices and virtual environments. Available protocols can
also be classified based on parameters like network delay,
jitter, packet loss, and rate of data transfer.

Application layer protocols for haptic communication enable aggregation and multiplexing of audio, video and haptic
data streams. This is important because quality of experience
requirements demand synchronized transmission of video and
audio data, with real-time haptic interaction between the user
and the remote environment. Some examples of application
protocols include Session Initiation Protocol (SIP) [17], Real-
Time Protocol (RTP) for distributed interactive media(RTP/I)
[18], and Application Layer Protocol for Haptic Networking
(ALPHAN) [19]. For application in telesurgery, [20] present
an application layer protocol, referred to as the Interoperable
telesurgery Protocol (ITP). However, communication using
this protocol was not bilateral as it was used to transmit only
video data. The Haptics over Internet Protocol (HoIP) uses
UDP and a multiplexing algorithm which enables packetization audio/haptic or video/haptic data [21].

Recently, fifth-generation (5G) mobile/cellular technology
has received significant attention for haptic teleoperation due
to native support for ultra-reliable low-latency communication (uRLLC). The requirements and design challenges for
haptic communication over 5G have been identified in [22],
[23], and [24]. Wireless resource allocation enhancements
for meeting the requirements of haptic communication over
5G have been investigated in [25] and [26]. Although 5G
is promising for haptic teleoperation, guaranteed latency
and timeliness for packet delivery is not possible without
scheduling enhancements. Besides, real-world trials of haptic
teleoperation over 5G are in infancy.

## B. Stability Control Architectures for Teleoperation

Long distance communication introduces varying amount
of latency which makes certain applications of teleoperation difficult and/or impossible due to instability. There are
however stability control architectures and methods that are
employed to minimise the impact of latency on the stability of

applications like teleoperation. The introduction of adaptive
control subsystems also has advantages and disadvantages,
and the choice of which control scheme to employ depends
on applications. Comparison of different control schemes
was carried out by [27]. Classifying bilateral control of
teleoperation systems can be based on the choice of either
compensating for communication delays, estimation of the
operator and environment model, handling of internal and
external disturbances of the subsystems, or a combination of
the highlighted tasks.

Wave variable control, time-domain passivity approach,
and model-mediated tele-operation are some of the key
available control schemes that address stability and communication challenges for networked teleoperation systems.
Using algorithms created to ensure stability and transparency
between leader and follower devices when time delay is
introduced, [28], [29] conceptualised the wave-variable control method. It builds on the work of [30] which combines
scattering transformation, network theory and passive control.
The time-domain passivity control (TDPC) [31] monitors the
energy flowing to and from the leader side, follower side, or
both in real time by using a passivity observer (PO) placed in
series or parallel to the communication channel. In the TDPC,
a passivity controller (PC) retains the system’s passivity
through the use of adjustable damping elements. In order
to ensure system stability and transparency in the presence
of arbitrary communication delay, the model-mediated teleoperation approach (MMTA) was proposed [32]. Instead of
directly sending back haptic (force) signals, parameters of the
object model (which approximates the remote environment)
are estimated and transmitted back to the master in real-time
as the slave interacts with the remote environment.

## III. OVERVIEW OF GALLOP TECHNOLOGY

This work employs a high-performance wireless control
technology, i.e., GALLOP, as a wire-replacement technology
for haptic teleoperation. GALLOP has been designed for
wireless closed-loop control or feedback control in singlehop as well as multi-hop scenarios. GALLOP is capable
of handling control loops with ultra-fast dynamics on the
order of milliseconds (ms). GALLOP implements a controlaware bi-directional schedule that handles cyclic exchange
of control information with very low latency and zero jitter.
GALLOP also implements various techniques for achieving
very high reliability in harsh wireless environment. GALLOP
is agnostic to the Physical (PHY) layer design; hence it
can be implemented on different wireless chipsets including
those of Bluetooth and Wi-Fi. Further technical details about
GALLOP are available in [33] and [14]. In our work,
GALLOP provides wireless connectivity for bi-directional
haptic data exchange between the leader and the follower
robot. We realize this communication based on a Bluetooth
5.0 wireless chipset.

## IV. TELEOPERATION SETUP

In this section, we describe the hardware and software
setup for the three scenarios explored in this study. The

---

Fig. 1: Setup for leader and follower robots.

study was carried out at the Nuclear Robotics test bed of the
Bristol Robotics Laboratory, Bristol. The teleoperation setup
comprises of two sets of robotic manipulators. The first is the
leader robot, at the operator end, where commands are issued.
The second robot is the follower, designed to replicate the
movements of the leader robot, hence the reference “leaderfollower”. Fig. 1 shows the leader robot and follower robot
setup with an operator demonstrating the process. The robot
used on both end is the Franka Emika Panda robot arm [34].
Computations on and communication between the leader and
follower robots is carried out using an Nvidia Jetson Xavier
board [35] connected to the controller of each arm. Based on
the real time control loop requirement for efficient teleoperation, Ubuntu operating system with real-time kernel was
installed on the Jetson boards. Programs written to implement
data transfer and processing were written in C++ and run on
the Jetson boards connected to each robot controller.

Fig. 2: Control loop for leader and follower robots.

The control loop for the leader and follower robots is
shown in Fig. 2. As the leader robot is moved, joint angles
and velocities of the leader robot are sent to the follower
robot (which replicates the leader robot’s movements) at the
remote end. Simultaneously, external torques on the follower
robot are sent back to the leader robot moved by the operator.
The command torque for the leader side is defined as:

$$
\tau_{d}^{L}(t)=K\tau_{e x t}^{F}(t),\;\;\;K<1
$$

(1)

7
where<sup>dL</sup>*2* R is the desired torque for the leader arm,
F 7
*K 2* R is a scaling factor and<sub>ext</sub>2 R is the measured
external torques being applied at the follower side. For the
follower robot control

$$
\tau_{d}^{L}\;\in\;\mathbb{R}^{7}
$$

$$
\tau_{e x t}^{F}\in\mathbb{R}^{7}
$$

$$
K\in\mathbb{R}
$$

$$
\tau_{d}^{F}(t)=P\left(q^{F}\left(t\right)-q^{L}\left(t\right)\right)-D\left(\dot{q}^{F}\left(t\right)-\dot{q}^{L}\left(t\right)\right)
$$

(2)

where<sup>dF</sup>*2* R⁷ is the desired follower-side torque, *P* and
F L
*D* are diagonal gain matrices, *q;q 2* R⁷ are follower and
F L
leader joint angles respectively, and *q*_*; q*_ *2* R⁷ are follower
and leader joint velocities. Data transfer is therefore limited to
a single 7-double vector in Eq. (1) and two 7-double vectors
in Eq. (2). The control loop for each robot runs at 1kHz,
with the communication loop running in a separate thread at
20Hz. In Fig. 3a, the physical wired connection between the

$$
\tau_{d}^{F}\in\mathbb{R}^{7}
$$

$$
q^{F},q^{L}\in\mathbb{R}^{7}
$$

$$
\dot{q}^{F},\dot{q}^{L}\in\mathbb{R}^{7}
$$

(a)

<sup>Human</sup> 
**TCP/IP wireless connection**
input
Follower

(b)

<sup>Human</sup> **GALLOP wireless connection**
input
Leader Follower

(c)

Fig. 3: Robot teleoperation setup (a) wired, (b) wireless, and
(c) GALLOP-based.

leader robot and follower robot is shown. Whilst the leader
and follower Jetson boards were physically connected using
a LAN cable (wired connection), programs for running the
TCP/IP communication protocol on either side were run on
the Jetson Xavier boards.

As shown in Fig. 3b, the only difference between the wired
connection and the wireless connection is that the physical
wired LAN connection was replaced with a network router
for wireless communication between the leader and follower
robots.

In Fig. 3c, we introduce the GALLOP protocol to allow
wireless communication of haptic data between the leader and follower robots. The GALLOP files were uploaded onto
NORDIC nRF52840 boards [36], connected to the Jetson
boards responsible for processing data transmission to and
from each robot.

## V. EVALUATION

A heuristic evaluation of the three communication protocols of interest was carried out. Heuristic evaluations are
often employed in the field of human-computer-interface
(HCI) as part of the design cycle as a usability inspection
method. Heuristic evaluations require that experts use their
practical skills in combination with theoretical knowledge of
standards and guidelines [37]. During the evaluations, experts
carry out tasks against previously determined usability principles referred to as heuristics that when violated make the
system more difficult to use [38]. Heuristic evaluations have
previously been carried out on smartphone applications in
supporting elderly [39], virtual reality systems [38], design
and development of a statistics serious game [40], and mobile
applications [41].

In the study reported in this paper, five robotics experts
(mean years of robot experience = 10.8 years) carried out
heuristic evaluations of the three communication protocols
(wired, wireless, GALLOP) as they carried out a task of
sorting six objects into three containers (two objects per
container). During the heuristic evaluation, the leader and
follower robots were placed in the same room, so the experts
were able to see the movements of the follower robot in
real time. For each experiment run, the objects to be sorted
were placed randomly in front of the follower robot. The
expert participants moved the leader robot by hand and used
a keypad button to open/close the robot’s gripper. The experts
carried out three repetitions of the task for each of the
communication protocols in a randomised order.

For each task scenario, we measured the send and receive
times of packets sent from the leader robot and follower
robot. Position and velocity errors were also measured for
each communication scenario explored. At the end of each
task, the expert participants completed a heuristic questionnaire, which consisted of three 5-point Likert scales rating
the responsive, feeling of safety, and feeling of smoothness
of the robot control.

## VI. RESULTS

To compare the performance of the different communication methods objectively, we calculate errors from position
and velocity in time for each experimental run, then calculate
error indexes and _ from the root-mean-square (RMS) of
errors.
e(t) = q (t) q (t)

$$
e(t)=q_{l}(t)-q_{f}(t)
$$

(3)

Where *e*(*t*) *2* R⁷ denotes joint position error at time (*t*),
*q*<sub>l</sub>(*t*) *2* R⁷ is leader manipulator joint angles and *q*<sub>f</sub>(*t*) *2* R⁷
is follower manipulator joint angles. Similarly, for velocity
7
error *e*_(*t*) *2* R :

$$
q_{l}(t)\in\mathbb{R}^{7}
$$

$$
e(t)\in\mathbb{R}^{7}
$$

$$
q_{f}(t)\in\mathbb{R}^{7}
$$

$$
\dot{\boldsymbol{e}}(t)\in\mathbb{R}^{7}
$$

$$
\dot{e}(t)=\dot{q}_{l}(t)-\dot{q}_{f}(t)
$$

(4)

where *q*_<sub>l</sub>(*t*) *2* R⁷ is leader manipulator joint velocities and
*q*<sub>f</sub>(*t*) *2* R⁷ is follower manipulator joint velocities. From
these error values we can generate Root Mean Square (RMS)
values for each joint 1 *i* 7 as
v

$$
\dot{q}_{l}(t)\in\mathbb{R}^{7}
$$

$$
q_{f}(t)\;\in\;\mathbb{R}^{7}
$$

$$
1\leq i\leq7
$$

$$
\begin{aligned}{r{s s_{i}}}&{{}=\sqrt{\frac{1}{T}\sum_{t=0}^{T}|e{_i}(t)|^{2}},}\\ {\dot{{r}s s_{i}}}&{{}=\sqrt{\frac{1}{T}\sum_{t=0}^{T}|\dot{e}_{i}(t)|^{2}}}\\ \end{aligned}
$$

(5)

where *rms* and *rms* _ *2* R⁷. These values at this point can be
used to generate an error score for each experimental run by
summing the RMS over all joints which will be represented
by the variables and _ for RMS of position and velocity
error respectively:

$$
r{\dot{m}}s\in\mathbb{R}^{7}
$$

$$
\begin{array}{l} \epsilon = \sum_ {i = 1} ^ {n} r m s _ {i}, \\ \dot {\epsilon} = \sum_ {i = 1} ^ {n} r \dot {m} s _ {i} \\ \end{array}
$$

(6)

Fig. 4: Distributions of for the three communication methods.

Fig. 5: Distributions of _ for the three communication methods.

---

(a)
[Image: Im0]

(b)

Fig. 6: Leader-side data transmit times (a) and receive times
(b), for the three communication methods. Follower-side distributions were found to be similar, so are not presented here
for brevity.

Fig. 7: Scores for perceived ”smoothness”.

Fig. 8: Scores for perceived ”responsiveness”.

Fig. 9: Scores for perceived safety.

All data were tested for normal distribution using
Kolmogorov-Smirnov test [42], which returned negative results for all. Therefore, non-parametric tests are required. A
Friedman test was carried out to determine if statistically
significant differences appear between GALLOP, wired and
wireless conditions, followed by Wilcoxon Sign-Rank Tests
(with a Bonferroni correction p < 0: 017) to determine
differences between conditions.

For the position error shown in Fig. 4 there was a

TABLE I: Statistics for *Tsend*

$$
T_{s e n d}
$$

|  | GALLOP |  | wired |  | wireless Lead |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | Lead | Follow | Lead | Follow | Lead | Follow |
| N | 35,478 | 35,635 | 30,359 | 60,464 | 27,636 | 55,040 |
| Mean(ms) | 49.1 | 49.1 | 0.116 | 0.126 | 0.178 | 0.217 |
| $\sigma$ | 1.61 | 1.51 | 0.127 | 0.093 | 0.176 | 0.153 |
| Range(ms) | 54.2 | 63.3 | 5.59 | 3.45 | 5.36 | 8.91 |
| IQR(ms) | 0.451 | 0.541 | 0.039 | 0.046 | 0.049 | 0.061 |

TABLE II: Statistics for *Trecv*

$$
T_{r e c v}
$$

|  | GALLOP |  | wired |  | wireless Lead |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | Lead | Follow | Lead | Follow | Lead | Follow |
| N | 35,478 | 35,635 | 30,359 | 60,464 | 27,636 | 55,040 |
| Mean(ms) | 0.688 | 0.786 | 1.26 | 0.994 | 12.9 | 12.7 |
| $\sigma$ | 1.03 | 0.622 | 2.37 | 1.88 | 51.7 | 52.8 |
| Range(ms) | 50.1 | 35.1 | 52.5 | 51.6 | 1268 | 1545 |
| IQR(ms) | 0.317 | 0.376 | 0.646 | 0.224 | 2.67 | 2.39 |

$$
\sigma
$$ statistically significant difference between communication
2
methods, = 14*:* 9, *p* = 0*:* 001. Post-hoc analysis shows
no significant difference between the wired and wireless
conditions (*Z* = 0*:* 454, *p* = 0*:* 65), however there was a
statistically significant reduction in between GALLOP and
wired (*Z* = 3*:* 18, *p* = 0*:* 001) and GALLOP and wireless
(*Z* = 2*:* 76, *p* = 0*:* 006).

$$
\chi^{2}\,=\,14.9,\,p\,=\,0.001
$$

$$
(Z\,=\,-0.454
$$

Examining the velocity errors _ shown in Fig. 5, the
2
Friedman test showed no significant difference ( = <sup>2</sup>,
*p* = 0*:* 368).

$$
(\chi^{2}\,=\,2.
$$

For all results from the data transmission send/receive
times, shown in Fig. 6, a statistically significant result is
reported between all conditions (full results are shown in
Tables III and IV).

TABLE III: Significance results for *Tsend*and *Trecv*, Leader
side.

$$
T_{s e n d}
$$

$$
T_{r e c v}
$$

|  | GALLOP/ wired Send |  | wired/ wireless Send |  | GALLOP/ wireless Send |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | Send | Receive | Send | Receive | Send | Receive |
| Z | -150.8 | -104.5 | -112.4 | -142.7 | -143.9 | -143.9 |
| p | &lt;0.001 | &lt;0.001 | &lt;0.001 | &lt;0.001 | &lt;0.001 | &lt;0.001 |

TABLE IV: Significance results for *Tsend*and *Trecv*, follower
side.

$$
T_{s e n d}
$$

$$
T_{r e c v}.
$$

|  | GALLOP/ wired Send |  | wired/ wireless Send |  | GALLOP/ wireless Send |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | Send | Receive | Send | Receive | Send | Receive |
| Z | -163.4 | -65.9 | -170.5 | -201.9 | -163.4 | -163.3 |
| p | &lt;0.001 | &lt;0.001 | &lt;0.001 | &lt;0.001 | &lt;0.001 | &lt;0.001 |

Examining the results of the heuristics, for “smoothness”
from Fig. 7, there was no significance between GALLOP and
wired conditions (*Z* = 0*:* 791, *p* = 0*:* 429) but significance
was found between wired/wireless (*Z* = 3*:* 024, *p* = 0*:* 002)
and GALLOP/wireless (*Z* = 2*:* 83, *p* = 0*:* 005).

$$
(Z=-0.791
$$

For “responsiveness” results shown in Fig. 8 results were
similar: GALLOP/wired non-significant (*Z* = 0*:* 816, *p* =
0*:* 414), wired/wireless and GALLOP/wireless both significant (*Z* = 2*:* 973, *p* = 0*:* 003, *Z* = 3*:* 115, *p* = 0*:* 002
respectively).

$$
p\,=\,0.002
$$

Finally, this was also reflected in safety scores from
Fig. 9, with GALLOP/wired showing no significant difference (*Z* = 1*:* 414, *p* = 0*:* 157), but wired/wireless and
GALLOP/wireless both significantly different (*Z* = 3*:* 217,
*p* = 0*:* 001, *Z* = 3*:* 017, *p* = 0*:* 003 respectively).

$$
(Z\,=\,-1.414,\,p\,=\,0.157)
$$

## VII. DISCUSSION

Analysis of the position error results shown in Fig. 4
shows that GALLOP produced a statistically significant reduction in error overall, with errors for wired and wireless
communication very similar, and no significant differences
in velocity errors shown in Fig. 5. However, the heuristics
scores from Figs. 7 to 9 show that participants perceived very
little difference between GALLOP and wired communication
methods, but perceived a statistically significant difference in
the wireless condition.

By examining the transmission times shown in Fig. 6 and
Tables I to IV we can see that, in particular, the range of

transmission delay for wireless communication when receiving can be very high, up to more than a second. Despite a
mean value of *T*<sub>recv</sub>from Table II being reasonably low at
12.7ms, the occasional long delay can have a large affect on
teleoperation performance - something that has been studied
for many years [43]–[46]. In particular, performance drops
significantly when delays exceeding 400ms are experienced
[47], [48]. This accounts for the absence of a drop in
performance from the mean *T*<sub>send</sub>for GALLOP of 50ms,
where the perceived delay is small enough to be compensated
for by the human central nervous system.

$$
T_{r e c v}
$$

$$
T_{s e n d}
$$

## VIII. CONCLUDING REMARKS

Haptic teleoperation is an important application for various
industries. This paper conducted real-world evaluation of
wireless and wired technologies for haptic teleoperation. One
of its key objectives was to provide a robust, responsive,
and reliable wireless communication method for control
commands and haptic feedback in a teleoperation system.
Specifically with relation to the nuclear industry, safety and
stability are particularly important for the predicted use cases.

Our results, based on objective and subjective evaluation,
reveal that the use of low-power wireless control technology, based on an off-the-shelf Bluetooth 5.0 chipset, i.e.,
GALLOP, does not impact the performance of teleoperation
system. It is comparable to a standard TCP/IP wired connection, and superior to a wireless TCP/IP connection with a
Wi-Fi router performing data transport.It can be concluded
that GALLOP wireless interface is a suitable low-power (and
low-cost) cable replacement solution for haptic teleoperation.

What has been omitted from this work is investigation into
other control-based techniques such as the use of wave variables [49]–[52], where the usual network transport of torques
and velocities (which have a *multiplicative* dependence on
the power-input) are transformed to wave variables (in a
form where the dependence is *additive*), reducing the effect
of time delays on the stability and control of the system.
Another method known as model-mediated control [32], [53],
[54], where the remote environment is sensed, modeled, then
transported and rendered at the local controller, can also be
used to improve stability in the face of time delay. Both of
these methods are well documented, and could be applied
using the GALLOP transport protocol, which we have plans
for in the future.

There are a number of future work directions for this work.
We haven’t conducted comparison against UDP which is
promising for teleoperation due to (usually) lower delay and
jitter. Using UDP does, however, suffers more from dropped
packets. As our aims was to compare methods with similar
packet loss probability, we opted to compared against TCP/IP.
Future work will compare the performance of GALLOP
against UDP/IP. Other areas of future work include: (a)
incorporation of stability control architectures in wireless
teleoperation, (b) multi-hop wireless communication based
on GALLOP, and (c) the use of machine learning techniques
for recovering lost packets.

---

We have not compared against the user datagram protocol
(UDP), which is often used for teleoperation systems due
to (usually) lower delay and jitter [28]. Using UDP does,
however, suffer more from dropped packets due to how it is
implemented - we wanted to compare methods with similar
packet-loss chance, so opted to compare against TCP/IP
protocol. Future experiments will be carried out to compare
GALLOP against UDP.

There are many future plans for this work - we have only
touched on the many configurations we would like to experiment with. For example, the GALLOP system can work
in a daisy-chain network, which would extend the wireless
range but introduce more complexities to the data transport.
In addition, there are plans to employ an edge-intelligence
system to reduce effective packet loss through the use of
machine learning techniques directly in the communication
layer.

## no. 15, pp. 11 860–11 876, 2021. ACKNOWLEDGMENT

This work was supported by UK Engineering and Physical
Sciences Research Council (EPSRC No. EP/R02572X/1) for
the National Centre for Nuclear Robotics (NCNR).

## ACKNOWLEDGMENT

## REFERENCES

[1]C. Gonzalez, J. E. Solanes, A. Mu ´ noz, L. Gracia, V. Girb ˜ es-Juan, and ´
J. Tornero, “Advanced teleoperation and control system for industrial
robots based on augmented virtuality and haptic feedback,” *Journal of*
*Manufacturing Systems*, vol. 59, pp. 283–298, apr 2021.
[2]S. Opiyo, J. Zhou, E. Mwangi, W. Kai, and I. Sunusi, “A Review on
Teleoperation of Mobile Ground Robots: Architecture and Situation
Awareness,” *International Journal of Control, Automation and Systems*,
vol. 19, no. 3, pp. 1384–1407, mar 2021.
[3]T. Kot and P. Novak, ´ “Application of virtual reality in
teleoperation of the military mobile robotic system TAROS:,”
*https://doi.org/10.1177/1729881417751545*, vol. 15, no. 1, jan
2018. [Online]. Available: https://journals.sagepub.com/doi/10.1177/
1729881417751545
[4]J. Bolarinwa, I. Eimontaite, S. Dogramadzi, T. Mitchell, and P. Caleb-
Solly, “The use of different feedback modalities and verbal collaboration in tele-robotic assistance,” *IEEE International Symposium on*
*Robotic and Sensors Environments, ROSE 2019 - Proceedings*, jun
2019.
[5]N. Feizi, M. Tavakoli, R. V. Patel, and S. F. Atashzar, “Robotics and
AI for Teleoperation, Tele-Assessment, and Tele-Training for Surgery
in the Era of COVID-19: Existing Challenges, and Future Vision,”
*Frontiers in Robotics and AI*, vol. 8, apr 2021. [Online]. Available: /pmc/articles/PMC8079974//pmc/articles/PMC8079974/?report=
abstracthttps://www.ncbi.nlm.nih.gov/pmc/articles/PMC8079974/
[6]G. Yang, H. Lv, Z. Zhang, L. Yang, J. Deng, S. You, J. Du,
and H. Yang, “Keep Healthcare Workers Safe: Application of
Teleoperated Robot in Isolation Ward for COVID-19 Prevention
and Control,” *Chinese Journal of Mechanical Engineering 2020*
*33:1*, vol. 33, no. 1, pp. 1–4, jun 2020. [Online]. Available:
https://cjme.springeropen.com/articles/10.1186/s10033-020-00464-0
[7]K. Qian, A. Song, J. Bao, and H. Zhang, “Small Teleoperated
Robot for Nuclear Radiation and Chemical Leak Detection:,”
*https://doi.org/10.5772/50720*, vol. 9, jan 2012. [Online]. Available:
https://journals.sagepub.com/doi/full/10.5772/50720
[8]J. Aleotti, G. Micconi, S. Caselli, G. Benassi, N. Zambelli,
M. Bettelli, and A. Zappettini, “Detection of Nuclear Sources by UAV
Teleoperation Using a Visuo-Haptic Augmented Reality Interface,”
*Sensors 2017, Vol. 17, Page 2234*, vol. 17, no. 10, p. 2234, sep
2017. [Online]. Available: https://www.mdpi.com/1424-8220/17/10/
2234/htmhttps://www.mdpi.com/1424-8220/17/10/2234
[9]M. Niemela,¨ L. van Aerschot, A. Tammela, I. Aaltonen, and
H. Lammi, “Towards Ethical Guidelines of Using Telepresence
Robots in Residential Care,” *International Journal of Social Robotics*
*2019 13:3*, vol. 13, no. 3, pp. 431–439, feb 2019. [Online]. Available:
https://link.springer.com/article/10.1007/s12369-019-00529-8

[10]G. Dogangil, B. L. Davies, and F. R. y. Baena, “A review
of medical robotics for minimally invasive soft tissue surgery:,”
*http://dx.doi.org/10.1243/09544119JEIM591*, vol. 224, no. 5, pp.
653–679, jul 2009. [Online]. Available: https://journals.sagepub.com/
doi/abs/10.1243/09544119jeim591
[11]J. Arata, H. Takahashi, S. Yasunaka, K. Onda, K. Tanaka, N. Sugita,
K. Tanoue, K. Konishi, S. Ieiri, Y. Fujino, Y. Ueda, H. Fujimoto,
M. Mitsuishi, and M. Hashizume, “Impact of network time-delay and
force feedback on tele-surgery,” *International Journal of Computer*
*Assisted Radiology and Surgery*, vol. 3, no. 3-4, pp. 371–378, 2008.
[12]N. Zemiti, T. Ortmaier, and G. Morel, “A new robot for force control in
minimally invasive surgery,” *2004 IEEE/RSJ International Conference*
*on Intelligent Robots and Systems (IROS)*, vol. 4, pp. 3643–3648, 2004.
[13]S. Avgousti, E. G. Christoforou, A. S. Panayides, S. Voskarides,
C. Novales,systems: L. Nouaille, C. status S. Pattichis, and P.trends,” Vieyres, “Medical
telerobotic current and future *BioMedical*
*Engineering OnLine 2016 15:1*, vol. 15, no. 1, pp. 1–44,
aug 2016. [Online]. Available: https://biomedical-engineering-online.
biomedcentral.com/articles/10.1186/s12938-016-0217-7
[14]A. Aijaz and A. Stanoev, “Closing the Loop: A High-Performance
Connectivity Solution for Realizing Wireless Closed-Loop Control in
Industrial IoT Applications,” *IEEE Internet of Things Journal*, vol. 8,
no. 15, pp. 11 860–11 876, 2021.
[15]M. Oparin and M. Eid, “Analysis of High-Rate Wireless Links for Tele-
Haptics Applications,” *2017 International Conference on Computer*
*and Applications, ICCA 2017*, pp. 169–173, oct 2017.
[16]G. Kokkonis, K. E. Psannis, M. Roumeliotis, S. Kontogiannis, and
Y. Ishibashi, “Evaluating transport and application layer protocols for
haptic applications,” *Proceedings - 2012 IEEE Symposium on Haptic*
*Audio-Visual Environments and Games, HAVE 2012*, pp. 66–71, 2012.
[17]H. H. King, B. Hannaford, J. Kammerl, and E. Steinbach, “Establishing
multimodal telepresence sessions using the session initiation protocol
(SIP) and advanced haptic codecs,” *2010 IEEE Haptics Symposium,*
*HAPTICS 2010*, pp. 321–325, 2010.
[18]M. Mauve, V. Hilt, C. Kuhmunch, and W. Effelsberg, “RTP/I - Toward ¨
a common application level protocol for distributed interactive media,”
*IEEE Transactions on Multimedia*, vol. 3, no. 1, pp. 152–161, mar
2001.
[19]H. A. Osman, M. Eid, R. Iglesias, and A. El Saddik, “ALPHAN:
Application Layer Protocol for Haptic Networking,” *HAVE 2007-*
*The 6th IEEE International Workshop on Haptic, Audio and Visual*
*Environments and Games, Proceedings*, pp. 96–101, 2007.
[20]H. H. King, K. Tadano, R. Donlin, D. Friedman, M. J. H. Lum, V. Asch,
C. Wang, K. Kawashima, and B. Hannaford, “Preliminary protocol
for interoperable telesurgery,” in *2009 International Conference on*
*Advanced Robotics*, 2009, pp. 1–6.
[21]V. Gokhale, O. Dabeer, and S. Chaudhuri, “Hoip: Haptics over internet
protocol,” in *2013 IEEE International Symposium on Haptic Audio*
*Visual Environments and Games (HAVE)*, 2013, pp. 45–50.
[22]A. Aijaz, M. Dohler, A. H. Aghvami, V. Friderikos, and M. Frodigh,
“Realizing the Tactile Internet: Haptic Communications over Next
Generation 5G Cellular Networks,” *IEEE Wireless Communications*,
vol. 24, no. 2, pp. 82–89, 2017.
[23]M. Simsek, A. Aijaz, M. Dohler, J. Sachs, and G. Fettweis, “5G-
Enabled Tactile Internet,” *IEEE Journal on Selected Areas in Commu-*
*nications*, vol. 34, no. 3, pp. 460–473, 2016.
[24]A. Aijaz and M. Sooriyabandara, “The Tactile Internet for Industries:
A Review,” *Proceedings of the IEEE*, vol. 107, no. 2, pp. 414–435,
2019.
[25]A. Aijaz, “Toward Human-in-the-Loop Mobile Networks: A Radio
Resource Allocation Perspective on Haptic Communications,” *IEEE*
*Transactions on Wireless Communications*, vol. 17, no. 7, pp. 4493–
4508, 2018.
[26]——, “Hap SliceR: A Radio Resource Slicing Framework for
5G Networks With Haptic Communications,” *IEEE Systems Journal*,
vol. 12, no. 3, pp. 2285–2296, 2018.
[27]P. Arcara and C. Melchiorri, “Control schemes for teleoperation with
time delay: A comparative study,” *Robotics and Autonomous Systems*,
vol. 38, no. 1, pp. 49–64, jan 2002.
[28]G. Niemeyer and J. J. E. Slotine, “Stable Adaptive Teleoperation,”
*IEEE Journal of Oceanic Engineering*, vol. 16, no. 1, pp. 152–162,
1991.
[29]——, “Towards force-reflecting teleoperation over the Internet,” *Pro-*
*ceedings - IEEE International Conference on Robotics and Automation*,
vol. 3, pp. 1909–1915, 1998.

---

[30]R. J. Anderson and M. W. Spong, “Bilateral control of teleoperators
with time delay,” *Proceedings of the IEEE Conference on Decision*
*and Control*, pp. 167–173, dec 1988.
[31]J. H. Ryu, J. Artigas, and C. Preusche, “A passive bilateral control
scheme for a teleoperator with time-varying communication delay,”
*Mechatronics*, vol. 20, no. 7, pp. 812–823, oct 2010.
[32]A. Achhammer, C. Weber, A. Peer, and M. Buss, “Improvement
of model-mediated teleoperation using a new hybrid environment
estimation technique,” in *2010 IEEE International Conference on*
*Robotics and Automation*. IEEE, 2010, pp. 5358–5363.
[33]A. Aijaz, A. Stanoev, and U. Raza, “GALLOP: Toward High-
Performance Connectivity for Closing Control Loops over Multi-Hop
Wireless Networks,” in *ACM International Conference on Real-Time*
*Networks and Systems (RTNS)*. New York, NY, USA: Association
for Computing Machinery, 2019, p. 176–186. [Online]. Available:
https://doi.org/10.1145/3356401.3356413
[34]Franka Emika, “The Robot System,” 2021. [Online]. Available:
https://www.franka.de/robot-system
[35]Nvidia, “Jetson AGX Xavier Developer Kit,”
2021. [Online]. Available: https://developer.nvidia.com/embedded/
jetson-agx-xavier-developer-kit
[36]Nordic Semiconductors, “nRF52840,” 2021. [Online]. Available:
https://www.nordicsemi.com/Products/nRF52840
[37]A. Yeratziotis and P. Zaphiris, “A Heuristic Evaluation for Deaf Web User Experience (HE4DWUX),”
*https://doi.org/10.1080/10447318.2017.1339940*, vol. 34, no. 3, pp.
195–217, mar 2017. [Online]. Available: https://www.tandfonline.
com/doi/abs/10.1080/10447318.2017.1339940
[38]R. Murtza, S. Monroe, and R. J. Youmans, “Heuristic Evaluation for
Virtual Reality Systems:,” *https://doi.org/10.1177/1541931213602000*,
vol. 2017-October, pp. 2067–2071, oct 2017. [Online]. Available:
https://journals.sagepub.com/doi/abs/10.1177/1541931213602000
[39]H. M. Salman, W. F. Wan Ahmad, and S. Sulaiman, “Heuristic
Evaluation of the Smartphone Applications in Supporting Elderly,”
*Advances in Intelligent Systems and Computing*, vol. 843, pp.
781–790, jun 2018. [Online]. Available: https://link.springer.com/
chapter/10.1007/978-3-319-99007-1-72
[40]L. Bunt, V. Leendertz, and n. A. Seugnet Blignaut, “A heuristic
evaluation of the design and development of a statistics serious game,”
*Proceedings of the 16th World Conference on Mobile and Contextual*
*Learning*, vol. 10, 2017.
[41]G. Joyce, M. Lilley, T. Barker, and A. Jefferies, “Heuristic Evaluation
for Mobile Applications: Extending a Map of the Literature,”
*Advances in Intelligent Systems and Computing*, vol. 794, pp.
15–26, jul 2018. [Online]. Available: https://link.springer.com/chapter/
10.1007/978-3-319-94947-5-2
[50]S. Munir and W. J. Book, “Internet based teleoperation using wave
variables with prediction,” in *2001 IEEE/ASME International Con-*

[42]Y. Dodge, *Kolmogorov–Smirnov Test*. New York, NY: Springer New
York, 2008, pp. 283–287. [Online]. Available: https://doi.org/10.1007/
978-0-387-32833-1-214
[43]T. B. Sheridan and W. R. Ferrell, “Remote manipulative control
with transmission delay,” *IEEE Transactions on Human Factors in*
*Electronics*, no. 1, pp. 25–29, 1963.
[44]R. J. Anderson and M. W. Spong, “Bilateral control of teleoperators
with time delay,” in *Proceedings of the 1988 IEEE International*
*Conference on Systems, Man, and Cybernetics*, vol. 1. IEEE, 1988,
pp. 131–138.
[45]Y.-C. Liu and N. Chopra, “Control of semi-autonomous teleoperation
system with time delays,” *Automatica*, vol. 49, no. 6, pp. 1553–1565,
2013.
[46]R. Daniel and P. R. McAree, “Fundamental limits of performance for
force reflecting teleoperation,” *The International Journal of Robotics*
*Research*, vol. 17, no. 8, pp. 811–830, 1998.
[47]W. R. Ferrell, “Remote manipulation with transmission delay,” *IEEE*
*Transactions on Human Factors in Electronics*, vol. HFE-6, no. 1, pp.
24–32, 1965.
[48]S. Xu, M. Perez, K. Yang, C. Perrenot, J. Felblinger, and J. Hubert,
“Determination of the latency effects on surgical performance and
the acceptable latency levels in telesurgery using the dv-trainer®
simulator,” *Surgical endoscopy*, vol. 28, no. 9, pp. 2569–2576, 2014.
[49]G. D. Niemeyer, “Using wave variables in time delayed force reflecting
teleoperation,” Ph.D. dissertation, Massachusetts Institute of Technology, 1996.
*ference on Advanced Intelligent Mechatronics. Proceedings (Cat. No.*
*01TH8556)*, vol. 1. IEEE, 2001, pp. 43–50.
[51]A. Aziminejad, M. Tavakoli, R. V. Patel, and M. Moallem, “Transparent time-delayed bilateral teleoperation using wave variables,” *IEEE*
*Transactions on control systems technology*, vol. 16, no. 3, pp. 548–
555, 2008.
[52]C. Yang, X. Wang, Z. Li, Y. Li, and C.-Y. Su, “Teleoperation control
based on combination of wave variable and neural networks,” *IEEE*
*Transactions on Systems, Man, and Cybernetics: Systems*, vol. 47,
no. 8, pp. 2125–2136, 2016.
[53]B. Willaert, H. Van Brussel, and G. Niemeyer, “Stability of modelmediated teleoperation: Discussion and experiments,” in *International*
*conference on human haptic sensing and touch enabled computer*
*applications*. Springer, 2012, pp. 625–636.
[54]L. S. Pecly, M. L. Souza, and K. Hashtrudi-Zaad, “Model-reference
model-mediated control for time-delayed teleoperation systems,” in
*2018 IEEE Haptics Symposium (HAPTICS)*. IEEE, 2018, pp. 72–
77.
